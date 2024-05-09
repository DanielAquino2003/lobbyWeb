import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/TasksView',
      name: 'TasksView',

      component : () => import('../views/TasksView.vue')
    },
    {path:'/login', name:'Login', component: () => import('../views/LoginView.vue')},
    {path:'/TaskDeporteView', name:'TaskDeporteView', component: () => import('../views/TaskDeporteView.vue')},
    {path:'/TaskEstudioView', name:'TaskEstudioView', component: () => import('../views/TaskEstudioView.vue')},
    {path:'/SubjectView', name:'SubjectView', component: () => import('../views/SubjectView.vue')},
    {path:'/EjercicioView', name:'EjercicioView', component: () => import('../views/EjercicioView.vue')},
    {path:'/SerieView', name:'SeriesView', component: () => import('../views/SerieView.vue')},

  ]
})

export default router
