<template>
  <div class="container">
    <h1>
      Укажите пожалуйста ваш рост и вес
    </h1>

    <form @submit.prevent="$router.push('/tonometr')" class="reg-form">
      <input placeholder="Рост" type="text" required>
      <input placeholder="Вес"  type="text" required>
      <button type="submit">Войти</button>
    </form>

    <img class="image" src="../assets/Blue.png" alt="Beautiful blue table">
  </div>
</template>

<style lang="scss" scoped>
h1 {
  text-align: center;
  margin-top: 80px;
}
</style>