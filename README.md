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



#### важные опции (дебаг мод, секретный ключ)
Скопируйте exmaple-файл с переменными среды
```bash
cp .env.example .env
```
теперь зайдите в созданный файл и вставьте значение ключа, полученное от администрации
или же сгенерируйте новый ключ следующей командой
```bash
python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> print(get_random_secret_key())
>>> exit()
```

а этой командой можно быстро добавить ключ в .env
```bash
# для начала переместитесь в корневой каталог проекта(там где лежат 'venv', 'requirements.txt')
# затем:
dotenv set DEBUG True
dotenv set SECRET_KEY "your_secret_key" 
# заместо SECRET_KEY можно ставить и другие переменные что есть в .env.example
```

Дальше настройте бд


#### postgresql...
```bash
python manage.py migrate # по умолчанию создась db.sqlite3
```

#### запуск
```bash
cd letsgo # из корня проекта
python manage.py runserver # включение сервера 
```
`Ctrl+C` - остановка сервера


## api

api is [here](https://github.com/squad-of-programmers/letsgo_todo#questions)