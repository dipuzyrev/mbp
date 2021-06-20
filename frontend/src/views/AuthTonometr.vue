<template>
  <div class="container">
    <div class="title">
      <h1>
        <div class="image">
          <img height="88" width="88" src="../assets/Tonometr.png" alt="">
        </div>
        Последний шаг — ваш тонометр
      </h1>
      <h4>
        Точная модель устройства позволит вашему лечащему врачу точнее интерпретировать результаты
      </h4>
    </div>
    

    <form @submit.prevent="updateTon" class="reg-form">
      <input placeholder="Изготовитель и модель" type="text" v-model="tonometr" required>
      <button type="submit">Продолжить</button>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export default defineComponent({
  setup() {
    const api = '/api/update_tonometer/'
    const router = useRouter()
    const tonometr = ref('')

    const updateTon = () => {
      axios.post(
        api, 
        {
          'name': tonometr.value
        },
        {
          headers: {
            Authorization: 'Bearer ' + localStorage.getItem('JWTAccess'),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
          }
        }
      ).then(response => {
        router.push('/patient')
      }).catch(error => {
        alert(error.response.data.detail)
      })
    }

    return {
      updateTon,
      tonometr
    }
  },
})
</script>


<style lang="scss" scoped>
.container {
  justify-content: center;
}

.title {
  text-align: center;
  margin-top: 80px;
}

.reg-form {
  margin-top: 80px;
}
</style>