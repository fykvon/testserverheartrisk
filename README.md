#Web-API по ТЗ. 

###Фреймворк FastApi. Хранение данных в json.
####Часть проекта защищена соглашением о неразглашении

* Установите все зависимости для запуска проекта
  
```html
    pip install -r requirements.txt
```


1. Parsing.py (parsing data from "rambler" and "ru-meteo")

  *Для обработки данных полученной html используется Beautiful Soup

2. Count.py (main module. In this module hidded intellectual property. Сalculate  heart risk dependence from humidity, pressure, temperature etc.)

  *Используется для расчёта и передачи данных на фронтэнд

3. main.py (Common start FastApi module)

```html
    uvicorn main:app --reload
```
