<template>
  <div class="container">
    <nav>
      <img @click="$router.push('/patient')" src="../assets/Chevron.svg" alt="Go back">
      <div class="title">
        <h3>Ввод измерений</h3>
      </div>
    </nav>

    <form>
      <h1>Введите замеры, разделяя цифры пробелом</h1>

      <h4>Верхнее / нижнее / пульс</h4>

      <input placeholder="120 80 70" type="text" required>

      <textarea placeholder="Комментарий (опционально)" name="comment" id="1" cols="30" rows="10"></textarea>
    </form>

    <div class="addMeasure">
      <button @click="$router.push('/patient')">Добавить замер</button>
    </div>
  </div>

  
</template>

<style lang="scss" scoped>
nav {
  display: flex;
  align-items: center;

  & > * + * {
    margin-left: 20px;
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
</style>