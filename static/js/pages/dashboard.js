import { createApp } from 'https://cdn.jsdelivr.net/npm/vue@3/dist/vue.esm-browser.js';
import AppHeader from '../components/AppHeader.js';

const app = createApp({
  delimiters: ['[[', ']]'], // Prevent Django collision
  components: {
    AppHeader
  },
  setup() {
    return {};
  }
});

// Mount to root DOM element
app.mount('#app');