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

Допустим мы ищем цветок Iris-setosa с самым маленькой длиной чашелистика
[ответ](queries/query_1.py)

Исключим
