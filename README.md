![Banner](banner.png)

## О проекте
**Моё давление** - это сервис, который позволяет удобно отслеживать артериальное давление, мгновенно делиться данными с лечащим врачом и получать своевременные корректировки в лечении.

Работает как PWA (Progressive Web Application), что позволяет использовать его как в браузере (удобно для врача), так и с телефона как обычное приложение (удобно для пациента).

## Демо

Скоро здесь будет демка...

## Локальный запуск

### По вопросам
- Бэк: [@dipuzyrev](https://t.me/dipuzyrev)
- Фронт: [@SeamMiner](https://t.me/SeamMiner)

```bash
git clone https://github.com/dipuzyrev/mbp

# Start API
cd backend
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
python manage.py runserver

# Start frontend
cd ../frontend
yarn && yarn serve
```

...to be continued

## Технологический стэк

- [Django](https://www.djangoproject.com/) - свободный фреймворк для веб-приложений на языке Python
- [DRF](https://www.django-rest-framework.org/) -  библиотека, которая работает со стандартными моделями Django для создания гибкого API
- [Vue 3](https://v3.ru.vuejs.org/) - прогрессивный JavaScript-фреймворк для создания фронтенда веб-приложения
- [Vuex](https://vuex.vuejs.org/ru/) - официальный менеджер состояний для VueJS
- [Router](https://router.vuejs.org/ru/) - официальный маршрутизатор для VueJS
- [TypeScript](https://www.typescriptlang.org/) - типизированный JavaScript, позволяющий отлавливать ошибки до запуска кода

