<template>
	<div class="container">
		<form @submit.prevent="getPatient" class="title">
			<h2>Карточка пациента</h2>
			<input type="search" name="snils" id="snils" v-model="snils" placeholder="Поиск по СНИЛС">
		</form>

    <div v-show="!fname && isNotFound" class="surface white notFound">
      <img src="../assets/Heart.svg" alt="Beautiful heart">
      <h3>Такой пациент не найден</h3>
      <h4>Попробуйте проверить правильность написания СНИЛС</h4>
    </div>

			<div v-show="fname && !isNotFound" class="surface white">
				<div class="title">
					<h3>{{  `${fname} ${lname}` }}</h3>
					<a :href="`tel:${phone}`">{{ phone }}</a>
				</div>

				<div class="surface info">
					<h4>Общие сведения</h4>
					<ul>
						<li>Пол: <strong>{{ gender }}</strong></li>
						<li>Возраст: <strong>{{ age }}</strong></li>
						<li>Вес: <strong>{{ weight }}</strong></li>
						<li>Рост: <strong>{{ height }}</strong></li>
						<li>СНИЛС: <strong>{{ snils }}</strong></li>
						<li>Тонометр: <strong>{{ tonometer }}</strong></li>
						<li>Начало лечения: <strong>{{ (new Date(treatment_start)).toLocaleDateString('ru-RU') }}</strong></li>
					</ul>
				</div>

				<div class="graph">
					<form class="selector">
						<select name="time" id="time" v-model="graphType">
							<option value="all">Все метрики</option>
							<option value="systolic">Верхнее</option>
							<option value="diastolic">Нижнее</option>
							<option value="pulse">Пульс</option>
						</select>

            <div class="datePicker">
              <div class="fdate">
                <label for="#fdate">c</label>
                <input type="date" id="fdate" v-model="startDate">
              </div>
              <div class="fdate">
                <label for="#ldate">по</label>
                <input type="date" id="ldate" v-model="endDate">
              </div>
              <button>За все время</button>
            </div>
					</form>
					<canvas id="graph"></canvas>
				</div>

				<form @submit.prevent="addTreatment" class="treatment">
					<h3>Лечение</h3>
					<textarea name="treatement" cols="30" rows="10" placeholder="Лечениие" v-model="treatmentCurrent"></textarea>
					<button type="submit">Скорректировать лечение</button>
				</form>

				<form @submit.prevent="addNote" class="notes">
					<div class="title">
						<h3>Заметки</h3>
						<h4>Не видны пациенту</h4>
					</div>

					<textarea name="notes" cols="30" rows="10" v-model="notes"></textarea>

					<button type="submit">Обновить</button>
				</form>

				<div class="treatementChrono">
					<h3>Хронология</h3>

          <div class="treatement_note" v-for="t in treatment" :key="t.date">
          <h4>{{ `Запись от ${(new Date(t.date).toLocaleDateString('ru-RU'))}` }}</h4>
            <textarea name="note" disabled id="" cols="30" rows="10" :value="t.comment || ''">
            </textarea>
          </div>
				</div>

				<div class="measurement">
					<h3>Показатели за выбранный период</h3>
					<table>
						<thead>
							<tr>
								<td>Дата и значения</td>
								<td>Давление</td>
								<td>Пульс</td>
							</tr>
						</thead>
						<tbody>
							<tr>
								<td>Минимальное</td>
								<td>132/97</td>
								<td>80</td>
							</tr>
							<tr>
								<td>Максимальное</td>
								<td>132/97</td>
								<td>80</td>
							</tr>
							<tr class="divider">
								<td>Среднее</td>
								<td>132/97</td>
								<td>80</td>
							</tr>
							<tr class="table" v-for="m in measurements" :key="m.date">
								<td>{{ (new Date(m.date)).toLocaleDateString() }}</td>
								<td>{{`${m.upper}/${m.bottom}`}}</td>
								<td>{{ m.pulse }}</td>
								<td v-if="m.comment">{{ m.comment }}</td>
							</tr>
						</tbody>
					</table>
				</div>
					
			</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref, watchEffect, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Chart from 'chart.js/auto'
import axios from 'axios';

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

    const route = useRoute();
    const router = useRouter();
    const apiPatient = '/api/patient_by_snils/'
    const apiTreatment = '/api/add_treatment/'
    const apiNote = '/api/add_note/'
    const snils = ref('')
    
    const fname = ref('')
    const lname = ref('')
    const age = ref('')
    const gender = ref('')
    const height = ref('')
    const weight = ref('')
    const phone = ref('')
    const treatment_start = ref('')
    const treatment = ref([])
    const measurements = ref([])
    const tonometer = ref('')
    const notes = ref('')
    const graphType = ref('all')
    const startDate = ref('')
    const endDate = ref('')
    const treatmentCurrent = ref('')
    const isNotFound = ref(0)
    

    const dataset = ref([
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
    ])

    const data = ref({
    labels: [] as string[],
    datasets: graphType.value == 'all' ? dataset.value :
    graphType.value == 'systolic' ? [dataset.value[0]] :
    graphType.value == 'diastolic' ? [dataset.value[1]]:
    [dataset.value[2]]
  })

  watchEffect(() => {
    data.value.datasets = graphType.value == 'all' ? dataset.value :
    graphType.value == 'systolic' ? [dataset.value[0]] :
    graphType.value == 'diastolic' ? [dataset.value[1]]:
    [dataset.value[2]]
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
        lineTension: .35,
      },
    });

    // watchEffect(graphType => {
    //   const ctx = document.getElementById('graph')
    //   new Chart(ctx, config.value)
    // })


      
      let chart: any;

      onMounted(() => {
        const ctx = document.getElementById('graph')
        chart = new Chart(ctx, config.value)
      })

      watch(config.value, () => {
        chart.update()
      })

    const getPatient = async () => {
      console.log(route.params.sault);
      
      await axios.post(
        apiPatient,
        {
          "snils": snils.value,
          "sault": route.params.sault,
        }
      ).then(response => {
        isNotFound.value = 0
        fname.value = response.data.first_name
        lname.value = response.data.last_name
        age.value = response.data.age
        phone.value = response.data.phone
        gender.value = response.data.gender
        height.value = response.data.height
        weight.value = response.data.weight
        treatment_start.value = response.data.treatment_start
        treatment.value = response.data.treatment
        measurements.value = response.data.measurements
        tonometer.value = response.data.tonometer
        notes.value = response.data.notes

        let labels = [] as string[];
        let upper = [] as number[];
        let bottom = [] as number[];
        let pulse = [] as number[];

        measurements.value.forEach((m: measure) => {
          labels.push((new Date(m.date)).toLocaleDateString())
          upper.push(m.upper)        
          bottom.push(m.bottom)
          pulse.push(m.pulse)
        })

        data.value.labels = labels;
        dataset.value[0].data = upper;
        dataset.value[1].data = bottom;
        dataset.value[2].data = pulse;
      }).catch(error => {
        isNotFound.value = 1
      })
    }

    const addTreatment = () => {
      axios.post(
        apiTreatment,
        {
          "comment": treatmentCurrent.value,
          "snils": snils.value,
          "sault": route.params.sault,
        }
      ).catch(e => alert(e))
      getPatient();
    }

    const addNote = () => {
      axios.post(
        apiNote,
        {
          "text": notes.value,
          "snils": snils.value,
          "sault": route.params.sault,
        }
      ).catch(e => alert(e))
      getPatient();
    }

    return {
      snils,
      getPatient,
      fname,
      lname,
      age,
      gender,
      height,
      weight,
      treatment_start,
      treatment,
      measurements,
      tonometer,
      notes,
      graphType,
      startDate,
      endDate,
      phone,
      treatmentCurrent,
      addNote,
      addTreatment,
      dataset,
      isNotFound
    }
  },
})
</script>


<style lang="scss" scoped>
.container {
  max-width: 100%;
  display: flex;
  flex-flow: column;
  align-items: center;
  padding-top: 50px;
  justify-content: flex-start;

  & > * {
    max-width: 920px;
  }

  & > .title {
    display: grid;
    grid: auto / 1fr auto;
    gap: 10px;
    align-items: center;
    margin-bottom: 24px;

    & > * {
      margin: 0;
    }

    & > input {
      padding: 14px 10px 15px;
    }
  }

  & > .surface {
    display: grid;
    grid: "title title" max-content
          "info info" max-content
          "graph graph" max-content
          "notes measurement" max-content
          "treatment measurement" max-content
          "treatementChrono measurement" max-content
          / 1fr 1fr
    ;
    place-items: flex-start;
    gap: 24px;

    & > * {
      margin: 0;
    }

    & > .title {
      grid-area: title;
      display: flex;
      width: 100%;
      align-items: center;
      justify-content: space-between;

      & > * {
        margin: 0;
      }
    }

    & > .info {
      grid-area: info;
      display: block;

      & > h4 {
        text-transform: uppercase;
        font-size: 14px;
        margin-top: 0;
      }

      & > ul {
        display: grid;
        list-style-type: none;
        grid: max-content / repeat(3, 1fr);
        gap: 8px;
        margin: 0;
        padding: 0;
        font-size: 15px;
        color: #646978;
      }
      
    }

    & > .graph {
      grid-area: graph;
      width: 100%;

      & > .selector {
        display: flex;
        width: 100%;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;

        & > .datePicker {
          display: grid;
          grid: min-content / repeat(3, 120px);
          gap: 12px;
          align-content: center;

          & > * {
            display: flex;

            & > input {
              padding: 4px 9px 5px;
              font-size: 13px;
              margin-bottom: 0;
            }

            & > label {
              margin-right: 6px;
            }

          }

          & > button {
            font-size: 13px;
            padding: 4px 9px 5px;
          }
        }

        & > select {
          width: auto;
          margin-bottom: 0;
          padding: 4px 9px 5px;
        }
      }
    }

    & > .notes {
      grid-area: notes;
      
      & > .title {
        display: flex;
        width: 100%;
        align-items: center;
        justify-content: space-between;

        & > h4 {
          color: #646978;
          font-size: 14px;
        }
      }
    }

    & > .treatment {
      grid-area: treatment;
    }

    & > .treatementChrono {
      grid-area: treatementChrono;
    }

    & > .measurement {
      grid-area: measurement;
      width: 100%;

      & > table {
        width: 100%;

        & > thead, tbody {
          font-size: 15px;
          line-height: 1.4;

          & > tr {
            &.divider > td {
              border-bottom: 1px solid #ECEEF2;
            }

            & > td {
            padding: 12px 0;
            }
          }
        }

        thead > tr > td {
          border-bottom: 1px solid #ECEEF2;
        }
      }
    }
  }

  & > .notFound {
    display: block;
    text-align: center;
    padding: 56px 10px;

    & > h3 {
      margin: 40px 0 16px;
    }
  }
}
</style>