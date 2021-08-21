# Django back 

## getting started
для начала установите [python 3.9.6](https://www.python.org/downloads/)

```bash
cd Нужный каталог
git clone https://github.com/squad-of-programmers/letsgo_back_django.git

# затем создайте и актив. py virtual environment след. командами
python -m venv venv
# активация на windows:
.\venv\Scripts\activate.bat
# установите зависимости:
pip install -r requirements.txt
# осталось подключить базу данных и включить сервер django
```

здесь будет инструкция по подключению бд...
```
python manage.py migrate # по умолчанию создась db.sqlite3
```


```bash
cd letsgo # из корня проекта
python manage.py runserver # включение сервера 
```
`Ctrl+C` - остановка сервера


## api

api is [here](https://github.com/squad-of-programmers/letsgo_todo#questions)