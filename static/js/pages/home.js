import { createApp, ref, computed, onMounted } from 'vue';

const app = createApp({
  delimiters: ['[[', ']]'],
  setup() {
    const isAuthenticated = ref(false);
    const user = ref(null);

    onMounted(() => {
      console.log('Mounted home.js');  
      const dataElement = document.getElementById('django-user-data');
      console.log('Data element:', dataElement);
      if (dataElement) {
        try {
          const data = JSON.parse(dataElement.textContent);
          if (data && data.is_authenticated) {
            user.value = data;
            isAuthenticated.value = true;
          }
          console.log('User session data:', isAuthenticated.value);
        } catch (err) {
          console.error('Failed to parse user session data:', err);
        }
      }
    });

    console.log('isAuthenticated:', isAuthenticated.value);

    return {
      isAuthenticated,
      user,
    };
  }
});

app.mount('#app');