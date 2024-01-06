import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],

  server: {
    proxy: {
      '/trio_marino': 'http://127.0.0.1:5000',
      '/duo_marino': 'http://127.0.0.1:5000',
      '/fritos' : 'http://127.0.0.1:5000',
      '/platos_solos' : 'http://127.0.0.1:5000',
      '/sopas' : 'http://127.0.0.1:5000',
      '/pedido' : 'http://127.0.0.1:5000',
      '/items_pedido' : 'http://127.0.0.1:5000',
    }
  }
})
