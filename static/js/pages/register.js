import { createApp, ref, computed } from 'vue';

const app = createApp({
  delimiters: ['[[', ']]'],
  setup() {
    const form = ref({
      username: '',
      email: '',
      password: '',
      confirmPassword: ''
    });

    const touched = ref({
      username: false,
      email: false,
      password: false,
      confirmPassword: false
    });

    const errors = computed(() => {
      const errs = { username: '', email: '', password: '', confirmPassword: '' };

      // Username
      const trimmedUser = form.value.username.trim();
      if (!trimmedUser) {
        errs.username = 'Username is required.';
      } else if (trimmedUser.length < 3) {
        errs.username = 'Username must be at least 3 characters.';
      }

      // Email
      if (form.value.email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(form.value.email.trim())) {
          errs.email = 'Please enter a valid email address.';
        }
      }

      // Password
      if (!form.value.password) {
        errs.password = 'Password is required.';
      } else if (form.value.password.length < 8) {
        errs.password = 'Password must be at least 8 characters.';
      }

      // Confirm Password
      if (form.value.confirmPassword && form.value.password !== form.value.confirmPassword) {
        errs.confirmPassword = 'Passwords do not match.';
      }

      return errs;
    });

    const isValid = computed(() => {
      return !errors.value.username && !errors.value.email && !errors.value.password && !errors.value.confirmPassword;
    });

    // Reads the field's name attribute dynamically from the event
    const handleBlur = (event) => {
      const fieldName = event.target.name;
      if (fieldName === 'password1' || fieldName === 'password') {
        touched.value.password = true;
      } else if (fieldName === 'password2' || fieldName === 'confirm_password') {
        touched.value.confirmPassword = true;
      } else if (fieldName in touched.value) {
        touched.value[fieldName] = true;
      }
    };

    const handleSubmit = (event) => {
      Object.keys(touched.value).forEach((key) => {
        touched.value[key] = true;
      });

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