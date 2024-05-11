<script>
// Import the MenuComponent
import MenuComponent from '../components/MenuComponent.vue';

export default {
  name: 'UserHome',
  components: {
    MenuComponent, // Register the MenuComponent as a local component
  },
  // Other component options...
}
</script>

<template>
    <!-- Contenedor del menú con posición fija -->
    <div class="menu-container">
      <MenuComponent/>
    </div>
  </template>
  
  <style scoped>

  </style>
  