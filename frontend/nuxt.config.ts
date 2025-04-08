// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },

  modules: [
    '@nuxt/content',
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/scripts',
    '@nuxt/test-utils',
    '@nuxt/ui'
  ],

  // Vite-Konfiguration hinzufügen, um host.docker.internal zu erlauben
  vite: {
    server: {
      hmr: {
        protocol: 'ws', // Wichtig für Docker-Umgebungen
        host: 'localhost', // HMR sollte weiterhin über localhost laufen
      },
      // Erlaube Anfragen von host.docker.internal (für Puppeteer im Docker-Container)
      // und localhost (für den normalen Browserzugriff)
      allowedHosts: ['host.docker.internal', 'localhost'] 
    }
  }
})
