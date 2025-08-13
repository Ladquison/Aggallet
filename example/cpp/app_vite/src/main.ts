import { WasmWrapper } from './WasmWrapper.ts';
import { FUNCTION_ID } from './types/WasmCallbackId';

class Sample {
    private wasm = new WasmWrapper();
    private onoff = false;
    private value = 0.0;

    public start() {
        this.wasm.load().then(() => {
            this.wasm.addCallback(FUNCTION_ID.RESPOND_PARAMETERS, this.callback.bind(this));
            setInterval(() => { this.update(); }, 60);
            setInterval(() => { this.sendParamters(); }, 100);
            setTimeout(() => {
                this.wasm.removeCallback(FUNCTION_ID.RESPOND_PARAMETERS);
            }, 10000)
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

let sample = new Sample();
sample.start();