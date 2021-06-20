<template>
  <div class="container">
    <h1>
      Укажите пожалуйста ваш рост и вес
    </h1>

    <form @submit.prevent="updateHW" class="reg-form">
      <input placeholder="Рост" type="text" v-model="height" required>
      <input placeholder="Вес"  type="text" v-model="weight" required>
      <button type="submit">Войти</button>
    </form>

    <img class="image" src="../assets/Blue.png" alt="Beautiful blue table">
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default defineComponent({
  setup() {
    const api = '/api/update_height_weight/'
    const router = useRouter()
    const height = ref('')
    const weight = ref('')

    const updateHW = () => {
      axios.post(
        api, 
        {
          'height': height.value,
          'weight': weight.value
        },
        {
          headers: {
            Authorization: 'Bearer ' + localStorage.getItem('JWTAccess'),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
          }
        }
      ).then(response => {
        router.push('/tonometr')
      }).catch(error => {
        alert(error.response.data.detail)
      })
    }

    return {
      updateHW,
      height,
      weight
    }
  },
})
</script>

<style lang="scss" scoped>
h1 {
  text-align: center;
  margin-top: 80px;
}
</style>