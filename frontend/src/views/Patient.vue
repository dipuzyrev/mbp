<template>
  <div class="container">
    <div class="wrapper">
      <h1>Добрый день, Дмитрий</h1>

      <div class="surface white treatment">
        <div class="title">
          <img height="32" width="32" src="../assets/Treatment.png" alt="Treatment">
          <h3>Назначенное <br> лечение</h3>
        </div>
        <h4>Препарат, текст текста для текста и тому подобное, ну вы поняли Это тоже не забудьте принять или уже ничего не примете: препарат фарат, текст текста для текста и тому подобное...</h4>
      </div>

      <div class="surface white">
        <div class="title">
          <img height="32" width="32" src="../assets/Graph.png" alt="Graph">
          <h3>Измерения</h3>
        </div>

        <canvas id="graph"></canvas>

        <ul>
          <li
            v-for="m in measurements"
            :key="m.date"
          >
            {{ m.upper }} / {{ m.bottom }} &nbsp; {{ m.pulse }} &nbsp; {{ m.date.seconds }}
          </li>
        </ul>
      </div>

      <div class="surface white tips">
        <div class="title">
          <img height="32" width="32" src="../assets/Tips.png" alt="Tips">
          <h3>Как правильно замерять давление?</h3>
        </div>
        <h4>
          Подготовка:
          <ol>
            <li>Выберите спокойную обстановку.</li>
            <li>После еды должно пройти 2 часа.</li>
            <li>Нельзя употреблять кофе или курить за 30 минут до измерения.</li>
            <li>Избегайте активности перед измерением.</li>
            <li>При необходимости очистить мочевой пузырь и кишечник.</li>
            <li>Сидите спокойно в течение 5 минут перед измерением артериального давления.</li>
            <li>Если возможно, не проводите измерения, если испытываете дискомфорт или стресс.</li>
            <li>Снимите плотно облегающие предметы одежды с плеча. Чтобы избежать сдавливания, рукава не должны свертываться - они не мешают манжете, если они сложены.</li>
        </ol>
  Во время измерения:
        <ol>
          <li>Не разговаривайте.</li>
          <li>Сядьте на стул со спинкой.</li>
          <li>Положите манжету артериального давления на середину руки (2-3 см выше локтя).</li>
          <li>Положите руку на уровне сердца.</li>
          <li>Не скрещивайте ноги.</li>
          <li>Поставьте ноги на пол.</li>
        </ol>
        </h4>
      </div>

      <div class="surface white">
        <h4>Вы используете тонометр</h4>
        <h3>B.Well PRO-33 (М-L)</h3>

        <h4>Уже другой? <span class="link">Обновить</span></h4>
      </div>

      <button class="danger" @click="logout">Выйти</button>
      <div class="addMeasure">
        <button @click="addMeasurement">Добавить замер</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import Chart from 'chart.js/auto'

export default defineComponent({
    setup() {
      const router = useRouter();

      const measurements = ref([
        {
          'upper': 120,
          'bottom': 80,
          'pulse': 77,
          'date': new Date(),
        }
      ])

        const data = ref({
      labels: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
      datasets: [
        {
          label: 'Замер Давления',
          data: [0, 0, 1, 2, 79, 82, 27, 14],
          borderColor: ['#08B408', '#FF5151' ],
          backgroundColor: ['#08B408', '#FF5151' ],
          fill: false,
        }
      ]
    })

    const config = ref({
      type: 'line',
      data: data.value,
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
                padding: 25
              }
            }
          ]
        },
        interaction: {
          intersect: false,
        },
        lineTension: 1,
      },
    });

    const logout = () => {
      router.push('/')
    }

    const addMeasurement = () => {
      router.push('/add')
    }

    onMounted(() => {
      const ctx = document.getElementById('graph');
      new Chart(ctx, config.value)
    })

    return {
      measurements,
      logout,
      addMeasurement
    }
  },
})
</script>


<style lang="scss" scoped>
.wrapper {
  padding-bottom: 100px;
}

.description > * {
  margin: 4px 0;
}

.surface.white {
  background: #FFFFFF;
  border: 1px solid #F3F3F7;
  box-sizing: border-box;
  border-radius: 16px;
  flex-flow: column;
  align-items: flex-start;

  & > * + * {
    margin-left: 0;
  }

  & > .title {
    display: flex;
    align-items: center;

    & > * + * {
      margin-left: 20px;
    }
  }

  &.treatment > * + * {
    padding-left: 52px;
  }

}

.addMeasure {
  position: fixed;
  bottom: 0;
  width: 100%;
  max-width: 640px;
  background: #FFFFFF;
  box-shadow: inset 0px 1px 0px #E2E2EB;
  padding: 14px 14px 17px 14px;
  margin: 0 auto;
}

button {
  margin-bottom: 16px;
}

.link {
  color: #0082FF;
  text-decoration: underline;
  transition: all .15s ease-in-out;
  cursor: pointer;

  &:hover {
    color: #1e90ff;
  }
}
</style>