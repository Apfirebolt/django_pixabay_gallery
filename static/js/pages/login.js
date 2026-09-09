import { createApp, ref, computed } from 'vue';

const app = createApp({
  delimiters: ['[[', ']]'],
  setup() {
    const form = ref({
      username: '',
      password: '',
      rememberMe: false
    });

    const touched = ref({
      username: false,
      password: false
    });

    const errors = computed(() => {
      const errs = { username: '', password: '' };

      // Username Validation
      const trimmedUser = form.value.username.trim();
      if (!trimmedUser) {
        errs.username = 'Username or email is required.';
      } else if (trimmedUser.length < 3) {
        errs.username = 'Username must be at least 3 characters.';
      }

      // Password Validation
      if (!form.value.password) {
        errs.password = 'Password is required.';
      } else if (form.value.password.length < 6) {
        errs.password = 'Password must be at least 6 characters.';
      }

      return errs;
    });

    const isValid = computed(() => {
      return !errors.value.username && !errors.value.password;
    });

    const handleBlur = (field) => {
      touched.value[field] = true;
    };

    const handleSubmit = (event) => {
      // Mark all fields as touched on submit
      touched.value.username = true;
      touched.value.password = true;

      // If valid, submit the form via native DOM method so Django gets standard POST
      if (isValid.value) {
        event.target.submit();
      }
    };

    return {
      form,
      touched,
      errors,
      isValid,
      handleBlur,
      handleSubmit
    };
  }
});

app.mount('#app');