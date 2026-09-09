import { ref, onMounted, onBeforeUnmount } from 'https://cdn.jsdelivr.net/npm/vue@3/dist/vue.esm-browser.js';

export default {
  name: 'AppHeader',
  props: {
    userEmail: {
      type: String,
      default: ''
    },
    logoUrl: {
      type: String,
      default: ''
    }
  },
  setup(props) {
    const isDropdownOpen = ref(false);
    const isMobileMenuOpen = ref(false);
    const flyoutRef = ref(null);

    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value;
    };

    const closeAll = () => {
      isDropdownOpen.value = false;
      isMobileMenuOpen.value = false;
    };

    const handleClickOutside = (event) => {
      if (flyoutRef.value && !flyoutRef.value.contains(event.target)) {
        isDropdownOpen.value = false;
      }
    };

    onMounted(() => {
      document.addEventListener('click', handleClickOutside);
    });

    onBeforeUnmount(() => {
      document.removeEventListener('click', handleClickOutside);
    });

    return {
      isDropdownOpen,
      isMobileMenuOpen,
      flyoutRef,
      toggleDropdown,
      closeAll
    };
  },
  template: `
    <header class="relative bg-white" @keydown.escape="closeAll">
      <div class="flex justify-between items-center max-w-7xl mx-auto px-4 py-6 sm:px-6 md:justify-start md:space-x-10 lg:px-8">
        <div class="flex justify-start lg:w-0 lg:flex-1">
          <a href="/">
            <span class="sr-only">Workflow</span>
            <img class="h-8 w-auto sm:h-10" :src="logoUrl" alt="Logo">
          </a>
        </div>

        <div class="-mr-2 -my-2 md:hidden">
          <button type="button" @click="isMobileMenuOpen = true" class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100">
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>

        <nav class="hidden md:flex space-x-10">
          <div class="relative" ref="flyoutRef">
            <button type="button" @click="toggleDropdown" class="group bg-white rounded-md inline-flex items-center text-base font-medium hover:text-gray-900">
              <span>Solutions</span>
              <svg :class="[isDropdownOpen ? 'rotate-180' : '', 'ml-2 h-5 w-5 transform transition-transform duration-200']" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>

            <transition
              enter-active-class="transition ease-out duration-200"
              enter-from-class="opacity-0 translate-y-1"
              enter-to-class="opacity-100 translate-y-0"
              leave-active-class="transition ease-in duration-150"
              leave-from-class="opacity-100 translate-y-0"
              leave-to-class="opacity-0 translate-y-1">
              <div v-if="isDropdownOpen" class="absolute z-20 left-1/2 -translate-x-1/2 mt-3 px-2 w-screen max-w-xs sm:px-0">
                <div class="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 overflow-hidden bg-white p-4 space-y-3">
                  <a href="#" class="block p-2 hover:bg-gray-50 rounded">Analytics</a>
                  <a href="#" class="block p-2 hover:bg-gray-50 rounded">Engagement</a>
                </div>
              </div>
            </transition>
          </div>
          <a href="#" class="text-base font-medium text-gray-500 hover:text-gray-900">Pricing</a>
        </nav>

        <div class="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
          <span v-if="userEmail" class="text-sm text-gray-600 mr-4">[[ userEmail ]]</span>
        </div>
      </div>
    </header>
  `
};