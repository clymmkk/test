import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:6000',
      '/admin': 'http://127.0.0.1:6001',
      '/upload': 'http://127.0.0.1:6002',
      '/service': 'http://127.0.0.1:6000',
      '/api-v2': 'http://127.0.0.1:6000'
    }
  }
})
