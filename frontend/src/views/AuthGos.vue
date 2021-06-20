<template>
  <div class="container">
    <h1>
      <div class="image"><img src="../assets/GosUslugi.svg" alt="GosUslugi"></div>
      Единая система <br>
      идентификации и аутентификации
    </h1>

    <form @submit.prevent="logIn" class="reg-form">
      <h1>Вход</h1>
      <input placeholder="СНИЛС, email" class="gosUslugi" type="text" v-model="login" required>
      <input placeholder="Пароль" class="gosUslugi" type="password" v-model="password" required>
      <button type="submit" class="gosUslugi blue">Войти</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default defineComponent({
  setup() {
    const login = ref('');
    const password = ref('');
    const loginAPI = "/api/jwt/create/"
    const router = useRouter()

    const logIn = () => {
      axios.post(
        loginAPI,
        {
          'email': login.value,
          'password': password.value
        },
        {
          headers: {
            'Content-Type': 'application/json',
          }
        }
      ).then(response => {
        localStorage.setItem('JWTRefresh', response.data.refresh)
        localStorage.setItem('JWTAccess', response.data.access)
        router.push('/hw');
      }).catch(error => {
        alert(error.response.data.detail)
      })
    }

    return {
      login,
      password,
      logIn
    }
  },
})
</script>


<style lang="scss" scoped>
.container {
  min-height: 100vh;
  display: flex;
  flex-flow: column;
  align-items: center;
  justify-content: center;
  text-align: center;

  & > h1 {
    font-weight: normal;
  }
}
</style>