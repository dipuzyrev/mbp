<template>
  <div class="container">
    <div class="wrapper">
      <h1>Добрый день, Дмитрий</h1>

      <div class="surface white treatment">
        <div class="title">
          <img height="32" width="32" src="../assets/Treatment.png" alt="Treatment">
          <h3>Назначенное <br> лечение</h3>
        </div>
        <h4>{{ treatment }}</h4>
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
        <h3>{{ tonometer }}</h3>

        <h4>Уже другой? <span class="link" @click="$router.push('/tonometr')">Обновить</span></h4>
      </div>

      <button class="danger" @click="logout">Выйти</button>
      <div class="addMeasure">
        <button @click="addMeasurement">Добавить замер</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import Chart from 'chart.js/auto'

type pacient = {
  treatment: string,
  measurements?: measure[],
  tonometr: string
}

type measure = {
  upper: number,
  bottom: number,
  pulse: number,
  commnet?: string,
  date: string
}

export default defineComponent({
    setup() {
      const router = useRouter();
      const pacient = '/api/patient_profile/'
      const treatment = ref('')
      const measurement = ref([])
      const tonometer = ref('')

  const data = ref({
    labels: [] as string[],
    datasets: [
      {
        label: 'Верхнее давление',
        data: [] as number[],
        borderColor: '#FF5151',
        backgroundColor: '#FF5151',
        fill: false,
      },
      {
        label: 'Нижнее давление',
        data: [] as number[],
        borderColor: '#08B408',
        backgroundColor: '#08B408',
        fill: false,
      },
      {
        label: 'Пульс',
        data: [] as number[],
        borderColor: '#0082FF',
        backgroundColor: '#0082FF',
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
        lineTension: 0,
      },
    });

    axios.get(
      pacient,
      {
        headers: {
          Authorization: 'Bearer ' + localStorage.getItem('JWTAccess'),
          'X-Requested-With': 'XMLHttpRequest',
        }
      }
    ).then(response => {
      treatment.value = response.data.treatment
      measurement.value = response.data.measurements
      tonometer.value = response.data.tonometer

      measurement.value.forEach((m: measure)=> {
        data.value.labels.push((new Date(m.date)).toLocaleDateString('ru-RU'))
        data.value.datasets[0].data.push(m.upper)
        // data.value.datasets[0].borderColor.push((m.upper > 140 || m.upper < 100) ? '#FF5151': '#08B408')
        // data.value.datasets[0].borderColor.push('#FF5151')
        // data.value.datasets[0].backgroundColor.push((m.upper > 140 || m.upper < 100) ? '#FF5151' : '#08B408')
        // data.value.datasets[0].backgroundColor.push('#FF5151')
        
        data.value.datasets[1].data.push(m.bottom)
        // data.value.datasets[1].borderColor.push((m.bottom > 100 || m.bottom < 70) ? '#FF5151': '#08B408')
        // data.value.datasets[1].backgroundColor.push((m.upper > 100 || m.upper < 80) ? '#FF5151' : '#08B408')

        data.value.datasets[2].data.push(m.pulse)
        // data.value.datasets[2].borderColor.push((m.upper > 140 || m.upper < 100) ? '#FF5151': '#08B408')
        // data.value.datasets[2].backgroundColor.push((m.upper > 140 || m.upper < 100) ? '#FF5151' : '#08B408')

      })

      const ctx = document.getElementById('graph');
      new Chart(ctx, config.value)
    })

    const logout = () => {
      localStorage.removeItem('JWTRefresh')
      localStorage.removeItem('JWTAccess')
      router.push('/')
    }

    const addMeasurement = () => {
      router.push('/add')
    }

    return {
      logout,
      addMeasurement,
      treatment,
      tonometer
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
  left: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  background: #FFFFFF;
  box-shadow: inset 0px 1px 0px #E2E2EB;
  padding: 14px 14px 17px 14px;

  & > * {
    max-width: 640px;
    margin-bottom: 0;
  }
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