import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Auth from '../views/Auth.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/gos',
    name: 'AuthGos',
    component: () => import(/* webpackChunkName: "auth" */ '../views/AuthGos.vue')
  },
  {
    path: '/HW',
    name: 'AuthHW',
    component: () => import(/* webpackChunkName: "auth" */ '../views/AuthHW.vue')
  },
  {
    path: '/tonometr',
    name: 'AuthTonometr',
    component: () => import(/* webpackChunkName: "auth" */ '../views/AuthTonometr.vue')
  },
  {
    path: '/patient',
    name: 'Patient',
    component: () => import(/* webpackChunkName: "patient" */ '../views/Patient.vue')
  },
  {
    path: '/add',
    name: 'AddMesaure',
    component: () => import(/* webpackChunkName: "patient" */ '../views/AddMeasure.vue')
  },
  {
    path: '/doctor',
    name: 'Doctor',
    component: () => import (/* webpackChunkName: "doctor" */ '../views/Doctor.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
