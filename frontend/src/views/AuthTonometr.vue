<template>
  <div class="container">
    <div class="title">
      <h1>
        <div class="image">
          <img height="88" width="88" src="../assets/Tonometr.png" alt="">
        </div>
        Последний шаг — ваш тонометр
      </h1>
      <h3>
        Точная модель устройства позволит вашему лечащему врачу точнее интерпретировать результаты
      </h3>
    </div>
    

    <form @submit.prevent="$router.push('/patient')" class="reg-form">
      <input placeholder="Изготовитель и модель" type="text" required>
      <button type="submit">Продолжить</button>
    </form>
  </div>
</template>

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