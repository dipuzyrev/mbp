<template>
  <div class="container">
    <h1>
      <div class="image"><img src="../assets/GosUslugi.svg" alt="GosUslugi"></div>
      Единая система <br>
      идентификации и аутентификации
    </h1>

    <form @submit.prevent="$router.push('/HW')" class="reg-form">
      <h1>Вход</h1>
      <input placeholder="СНИЛС, email" class="gosUslugi" type="text" required>
      <input placeholder="Пароль" class="gosUslugi" type="password" required>
      <button type="submit" class="gosUslugi blue">Войти</button>
    </form>
  </div>
</template>

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