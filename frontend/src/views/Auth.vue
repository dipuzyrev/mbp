<template>
  <div class="container">
      <div class="title">
        <div class="image">
          <img src="../assets/Logo.svg" alt="">
        </div>
        <h1>Авторизация</h1>
        <h4>Легко. Без паролей и логинов</h4>
      </div>
      <div class="auth">
        <h4>войти через</h4>
        <button @click="$router.push('/gos')" class="gosUslugi">
          <img src="../assets/GosUslugi.svg" alt="Госуслуги">
        </button>
      </div>
    <img class="image" src="../assets/Yellow.png" alt="Beautiful yellow stairs" style="align-self: flex-start">
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    console.log("hi");
  },
})
</script>


<style lang="scss" scoped>
.title, .auth {
  text-align: center;
}

.title {
  margin-top: 80px;
}
</style>