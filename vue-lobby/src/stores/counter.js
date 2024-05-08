import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})

export const userSessionStore = defineStore({
  id: "session",
  state: () => ({
    token: "",
    user_id: "", // Changed to 'user_id' to match the case used in the actions
  }),
  actions: {
    setSession(token, user_id) { // Use regular function here
      this.token = token;
      this.user_id = user_id;
    },
    clearSession() {
      this.token = "";
      this.user_id = "";
      localStorage.removeItem('token');
      localStorage.removeItem('user_id');
    }
  },
});
