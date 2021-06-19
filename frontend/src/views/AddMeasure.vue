<template>
  <div class="container">
    <nav>
      <img class="goBack" @click="$router.push('/patient')" src="../assets/Chevron.svg" alt="Go back"/>
      <div class="title">
        <h3>Ввод измерений</h3>
      </div>
    </nav>

    <form @submit.prevent="addMeasure">
      <h1>Введите замеры, разделяя цифры пробелом</h1>

      <h4>Верхнее / нижнее / пульс</h4>

      <input v-mask="'### ## ##'" placeholder="120 80 70" type="text" v-model="params" required/>

      <div class="special">
        <button class="option" disabled>
          <img src="../assets/Camera.svg" alt="Camera">
        </button>
        <button class="option" disabled>
          <img src="../assets/Micro.svg" alt="Mircrophone">
        </button>
      </div>

      <textarea placeholder="Комментарий (опционально)" name="comment" id="1" cols="30" rows="10" v-model="comment"></textarea>
    </form>

    <div class="addMeasure">
      <button @click="addMeasure">Добавить замер</button>
    </div>
  </div>

  
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import {mask} from 'vue-the-mask'

export default defineComponent({
  directives: {mask},
  setup() {
    const api = '/api/add_measurement/'
    const router = useRouter()
    const params = ref('')
    const comment = ref('')

    const addMeasure = () => {
      const upper = params.value.split(" ")[0]
      const bottom = params.value.split(" ")[1]
      const pulse = params.value.split(" ")[2]
      axios.post(
        api, 
        {
          "upper": upper,
          "bottom": bottom,
          "pulse": pulse,
          "comment": comment.value
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
      addMeasure,
      params,
      comment
    }
  },
})
</script>

<style lang="scss" scoped>
nav {
  display: flex;
  align-items: center;
  position: relative;

  & > * + * {
    margin-left: 20px;
  }

  & > .goBack {
    position: absolute;
    left: 18px;
  }

  & > .title {
    width: 100%;
    text-align: center;
  }
}

.addMeasure {
  // position: fixed;
  // bottom: 0;
  width: 100%;
  max-width: 640px;
  background: #FFFFFF;
  box-shadow: inset 0px 1px 0px #E2E2EB;
  padding: 14px 14px 17px 14px;
  margin: 0 auto;
}

.special {
  display: flex;
  margin-bottom: 16px;
  
  & > * + * {
    margin-left: 18px;
  }
}

.goBback {
  cursor: pointer;
}
</style>