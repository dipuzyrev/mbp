<template>
	<div class="container">
		<div class="title">
			<h2>Карточка пациента</h2>
			<input type="search" name="snils" id="snils" placeholder="Поиск по СНИЛС">
		</div>

			<div class="surface white">
				<div class="title">
					<h3>Алексей Смирнов</h3>
					<a href="tel:1">+7 (960) 148-44-31</a>
				</div>

				<div class="surface info">
					<h4>Общие сведения</h4>
					<ul>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
						<li>Возраст: <strong>22 года</strong></li>
					</ul>
				</div>

				<div class="graph">
					<div class="selector">
						<select name="time" id="time">
							<option value="1">Все метрики</option>
							<option value="2">Верхнее</option>
							<option value="3">Нижнее</option>
							<option value="4">Пульс</option>
						</select>

            <div class="datePicker">
              <div class="fdate">
                <label for="#fdate">c</label>
                <input type="text" id="fdate">
              </div>
              <div class="fdate">
                <label for="#ldate">по</label>
                <input type="text" id="ldate">
              </div>
              <button>За все время</button>
            </div>
					</div>
					<canvas id="graph"></canvas>
				</div>

				<div class="treatment">
					<h3>Лечение</h3>
					<textarea name="treatement" cols="30" rows="10" placeholder="Лечениие"></textarea>
					<button>Скорректировать лечение</button>
				</div>

				<div class="notes">
					<div class="title">
						<h3>Заметки</h3>
						<h4>Не видны пациенту</h4>
					</div>

					<textarea name="notes" cols="30" rows="10"></textarea>

					<button>Обновить</button>
				</div>

				<div class="treatementChrono">
					<h3>Хронология</h3>

					<div class="treatement_note">
						<h4>Запись от 19.06.2021</h4>
						<textarea name="note" disabled id="" cols="30" rows="10">
							Lorem ipsum dolor sit amet consectetur adipisicing elit.
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
							<tr>
								<td>19.06.2021 • 1:12</td>
								<td>132/97</td>
								<td>80</td>
								<td>comment</td>
							</tr>
						</tbody>
					</table>
				</div>
					
			</div>
	</div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import Chart from 'chart.js/auto'

export default defineComponent({
  setup() {

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

    onMounted(() => {
      const ctx = document.getElementById('graph');
      new Chart(ctx, config.value)
    })
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
}
</style>