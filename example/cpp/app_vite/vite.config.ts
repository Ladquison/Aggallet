import path from 'path';

export default {
  resolve: {
    alias: {
      'wasm': path.resolve(__dirname, 'src/wasm'),
      'types': path.resolve(__dirname, 'src/types'),
    }
  }
}
