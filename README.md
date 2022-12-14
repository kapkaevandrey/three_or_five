# Three_or_five

![parser_workflow](https://github.com/kapkaevandrey/three_or_five/actions/workflows/test_style_workflow.yml/badge.svg)

### _Описание проекта_
> ***Аристотель***
>>Математика... выявляет порядок, симметрию и определенность 
>, а это – важнейшие виды прекрасного.
>>
Сервис в котором можно проверить делимость вводимого числа на 3 и на 5

Пример развёрнутого сервиса https://div-five-or-three.herokuapp.com/

### _Технологии_
 - __[Python 3.10.1](https://docs.python.org/3/)__
 - __[Flask 2.2.1](https://flask.palletsprojects.com/en/2.2.x/)__
 - __[WTForms 3.0.1](https://wtforms.readthedocs.io/en/3.0.x/)__

## _Как запустить проект_:
________________________________________

Клонировать репозиторий и перейти в него в командной строке:

```bash
https://github.com/kapkaevandrey/three_or_five.git
```

```bash
cd three_or_five
```

### _Стандартное виртуальное окружение (pip)_:
Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
python3 pip install -r requirements.txt
```

### _C использованием [Poetry](https://python-poetry.org/docs/)_
Установите Poetry следуя официальной инструкции и затем выполните
```bash
poetry init
```

Заполните файл .env, предварительно создав его в главной директории проекта. Для примера в директории проекта есть файл ```example.env```

Пример заполнения
```
FLASK_APP=app                                   <----название приложения
SECRET_KEY=MyLittlePOny                         <----секретный ключ
FLASK_DEBUG=on                                  <----включить в режиме DEBUG
```

Запустите приложение
```shell
flask run
```

### _Описание работы сервиса и пользовательские роли_:
__________________________________________
Сервис позволяет проверить делиться ли вводимое число на 5 (хотя это и так легко проверить) или на 3.
- Если число делится на 3, то на сайте появится надпись ***FOO***,
- Если на 5 ***BAR***, 
- если же введённое число делится и на 3 и на 5 ***FOOBAR***
- если не делится не на 3 ни на 5, то появится 🌿***Зак Галифианакис***🌿
_______________________________________________________


### Автор проекта:
#### Андрей ***Lucky*** Капкаев
>*Улыбайтесь - это всех раздражает :relaxed:.*


