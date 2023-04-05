### Установка MongoDB в Docker
```bash
docker pull mongo
ocker container run -d --name mongodb-hw mongodb:latest
docker exec -it mongodb-hw bash
```

 - Допустим мы добавили данные в бд командой

```bash
python3 data_parser.py
```
 ---

Допустим мы ищем цветок Iris-setosa с самым маленькой длиной чашелистика
[ответ](queries/query_1.py)

Исключим все записи с цветком Iris-versicolor
[ответ](queries/query_2.py)

Мы узнали, что есть ошибка в данных исправим длиной чашелистика для всех Iris-virginica на +1
[ответ](queries/query_3.py)

Создадим индексы для ускорения запросов
[ответ](queries/make_indexes_1.py)

Сравним замеры needTime
| Without index | With index |
| ------------- | ---------- |
| 152           | 0          |

Сильное ускорение, экономия в одну операцию.