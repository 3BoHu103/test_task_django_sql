# Тестовое Django
(Django==3.2.9, Python==3.10.4)
## Запуск:

- Клонировать репозиторий
- Активировать виртуальное окружение
- Установить зависимости
- Создать миграции
- Запустить сервер Django
- По адресу localhost:8000 находится сервис
- Пример с деплоем можно посмотреть на моём сайте-портфолио ratkevich.online

В тестовом задании использовалась библиотека django-bootstrap5 для более-менее красивого вида интерфейса приложения.

# Тестовое SQL
## Запуск:

Для работы с запросами в БД я использовал docker compose и sqladminer:

- Файл stack.yml отвечает за adminer
- Собрать образ и запустить контейнер: docker-compose -f stack.yml up -d --build
- В браузере перейти по адресу localhost:8080
- Импортировать дамп БД
- Сделать запросы
##  Запрос для пунка 1:
```sh
SELECT client_number,
SUM(outcome = 'win' and value = coefficient) AS Побед,
SUM(outcome = 'win' and value != coefficient) AS Поражений
FROM bid
INNER JOIN event_value
ON bid.play_id = event_value.play_id
GROUP BY client_number;
```
## Запрос для пункта 2:
```sh
SELECT ent.game, count(*) AS games_count
FROM (SELECT CONCAT(LEAST(away_team, home_team), '-', GREATEST(away_team, home_team)) AS game FROM event_entity) AS ent
GROUP BY game ASC
ORDER BY games_count ASC
```
Полные результаты запросов хранятся в папке sql: sql_1.csv и sql_2.csv - соответственно.
Там же находится и yml файл.

PS Есть различия в резульатах, может так было задумано? :)