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
    component: () => import(/* webpackChunkName: "auth" */ '../views/AuthHW.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/tonometr',
    name: 'AuthTonometr',
    component: () => import(/* webpackChunkName: "auth" */ '../views/AuthTonometr.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/patient',
    name: 'Patient',
    component: () => import(/* webpackChunkName: "patient" */ '../views/Patient.vue'),
    meta: {
      requiresAuth: true
    },
  },
  {
    path: '/add',
    name: 'AddMesaure',
    component: () => import(/* webpackChunkName: "patient" */ '../views/AddMeasure.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/doctor',
    name: 'Doctor',
    component: () => import (/* webpackChunkName: "doctor" */ '../views/Doctor.vue'),
    meta: {
      requiresAuth: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(x => x.meta.requiresAuth);
  if (requiresAuth && !localStorage.getItem('JWTAccess')) {
    next('/');
  } else {
    next();
  }
});

export default router
