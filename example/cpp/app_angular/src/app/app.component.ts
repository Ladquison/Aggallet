import { Component } from '@angular/core';
import { WasmWrapper } from 'WasmWrapper';
import { FUNCTION_ID } from 'types/WasmCallbackId';

@Component({
  selector: 'app-root',
  template: ''
})
export class AppComponent {
  private wasm = new WasmWrapper();
  private onoff = false;
  private value = 0.0;

  constructor() {
    this.wasm.load().then(() => {
      this.wasm.addCallback(FUNCTION_ID.RESPOND_PARAMETERS, this.callback.bind(this));
      setInterval(() => { this.update(); }, 60);
      setInterval(() => { this.sendParamters(); }, 100);
      setTimeout(() => {
        this.wasm.removeCallback(FUNCTION_ID.RESPOND_PARAMETERS);
      }, 10000);
    });
  }

  private callback(onoff: boolean, value: number, time: string) {
    console.log(`onoff = ${onoff}, value = ${value}, time = ${time}`);
  }

  private update() {
    this.wasm.update(60);
  }

  private sendParamters() {
    this.onoff = !this.onoff;
    this.value += 0.015;
    const now = new Date();
    this.wasm.setParameters(!this.onoff, this.value, now.toISOString());
  }
}
