<script setup>
import { RouterLink, RouterView, useRoute } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import LoginButton from './components/LoginButton.vue'
import SingUpButton from './components/SingUpButton.vue'
import { userSessionStore } from "@/stores/counter";

const isRegistered = userSessionStore().isRegistered;
console.log(isRegistered);
const isAuthenticated = userSessionStore().isAuthenticated;
console.log(isAuthenticated);

</script>

<template>
  <header v-if="useRoute().path && useRoute().path === '/'">
    <img class="logo" src="@/assets/correct.png" alt="Logo Lobby" width="125" height="125">
    <div class="wrapper">
      <HelloWorld msg="Welcome to Lobby!" />
      <nav>
        <RouterLink to="/">Begining</RouterLink>
        <RouterLink to="/TasksView">TasksView</RouterLink>
        <RouterLink to="/TaskDeporteView">TaskDeporteView</RouterLink>
        <RouterLink to="/TaskEstudioView">TaskEstudioView</RouterLink>
        <RouterLink to="/SubjectView">SubjectView</RouterLink>
        <RouterLink to="/EjercicioView">EjercicioView</RouterLink>
        <RouterLink to="/SerieView">SerieView</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
  <div v-if="!userSessionStore().isAuthenticated && (useRoute().path && useRoute().path === '/')" class="button-container"><LoginButton class="LoginButtonComponent"/></div>
  <div v-if="!userSessionStore().isAuthenticated && (!userSessionStore().isRegistered && !userSessionStore().isAuthenticated) && (useRoute().path && useRoute().path === '/')" class="button-container2"><SingUpButton class="SingUpButtonComponent"/></div>

</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}


@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }

  .button-container {
    position: absolute;
    top: 10px;
    right: 10px;
  }

  .button-container2 {
    position: absolute;
    top: 10px;
    right: 150px
  }

  @media (max-width: 1023px) {

    

  }

}
</style>
