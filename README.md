# Сервер:

В директории server/
```sh
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Сервер запустится на localhost:8000

# Клиент

В директории client/pics/
```sh
npm install
npm run dev
```
Клиент запустится на localhost:5173
