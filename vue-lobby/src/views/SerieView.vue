<template>
    <div class="usersdiv">
      <h1>Series</h1>
      <ul>
        <li v-for="serie in series" :key="serie.id">{{ serie }}</li>
      </ul>
    </div>
  </template>
  
  <script>

    export default {
        data() {
            return {
            series: [],
            };
        },
        methods: {
        async getseries() {
            try {
            const response = await fetch('http://127.0.0.1:8000/api/series/');
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            const data = await response.json();
            console.log(data);
            this.series = data;
            } catch (error) {
            console.error('Error fetching data:', error);
            }
        },
        },
        mounted() {
        this.getseries();
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
  