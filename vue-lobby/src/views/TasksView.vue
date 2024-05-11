<template>
    <div class="usersdiv">
      <h1>Tasks</h1>
      <ul>
        <li v-for="user in users" :key="user.id">{{ user }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import { userSessionStore  } from '@/stores/counter';

    export default {
        data() {
            return {
            users: [],
            };
        },
        methods: {
        async getTasks() {
            try {
            const token = userSessionStore().token
            const response = await fetch('http://127.0.0.1:8000/api/tasks/',{
              headers: {
                'Authorization': `token ${token}`
              }
            });
            if (!response.ok) {
                throw new Error('Failed to fetch data');
            }
            const data = await response.json();
            console.log(data);
            this.users = data;
            } catch (error) {
            console.error('Error fetching data:', error);
            }
        },
        },
        mounted() {
        this.getTasks();
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
  