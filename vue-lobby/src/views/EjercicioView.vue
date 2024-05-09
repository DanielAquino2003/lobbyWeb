<template>
    <div class="ejerciciosdiv">
      <h1>Tasks</h1>
      <ul>
        <li v-for="ejercicio in ejercicios" :key="ejercicio.id">{{ ejercicio }}</li>
      </ul>
    </div>
  </template>
  
  <script>

    export default {
        data() {
            return {
            ejercicios: [],
            };
        },
        methods: {
        async getejercicios() {
            try {
            const response = await fetch('http://127.0.0.1:8000/api/ejercicios/');
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            const data = await response.json();
            console.log(data);
            this.ejercicios = data;
            } catch (error) {
            console.error('Error fetching data:', error);
            }
        },
        },
        mounted() {
        this.getejercicios();
        }
    };
  </script>
  
  
  <style scoped>
  header {
    line-height: 1.5;
  }
  
  .logo {
    display: block;
    margin: 0 auto 2rem;
  }
  
  .vehiculosdiv {
    margin-top: 2rem;
  }
  
  .talleresdiv {
    margin-top: 2rem;
    margin-left: 2rem;
  }
  
  .reparacionesdiv {
    margin-top: 2rem;
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
  }
  </style>
  