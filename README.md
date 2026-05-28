        # postgresql — Схемы, таблицы, типы и constraint-ы

        Homework-шаблон для урока **l2_schemas_tables_types** (Схемы, таблицы, типы и constraint-ы) на платформе Vibe Learn.

        ## Что делать

        Дано: голая БД и спека приложения «book club». Тебе нужны таблицы users, books, reviews,
с FK, CHECK на rating in 1..5, UNIQUE (user_id, book_id) и timestamptz. Реализуй
миграции через Alembic (или raw SQL), напиши smoke-тесты, что constraint-ы реально
отшивают плохие данные (rating=6, duplicate review, FK без родителя). Тесты в template
запустят миграцию и попробуют сломать схему — должны получить ошибку, а не пройти.

## Контекст (из transfer-задачи урока)

Ты делаешь маркетплейс. Тебе спустили на ревью DDL от джуна:

```sql
CREATE TABLE listings (
  id varchar(255),
  seller_id varchar(255),
  title varchar(255),
  price real,
  currency char(3),
  created_at timestamp,
  status varchar(50),
  tags text,
  location varchar(255)
);
```

## Recap из урока

- **Схема ≠ DDL.** В PG schema — это namespace для таблиц/функций; нужна для изоляции компонентов, multi-tenancy и GRANT.
- **Типы важны.** `text` вместо `varchar(255)`, `timestamptz` вместо `timestamp`, `numeric` или `bigint в копейках` вместо `money`/`float` для денег, `jsonb` вместо `text` для JSON.
- **Constraint-ы — это валидация, которую невозможно обойти.** NOT NULL, FK, CHECK, UNIQUE стоят микросекунды и закрывают целые классы багов.
- **FOREIGN KEY → не создаёт индекс на referencing-стороне автоматически.** На `orders.user_id` индекс ставишь сам, иначе DELETE из users будет full scan.
- **ON DELETE — выбирай явно.** RESTRICT (по умолчанию — нельзя удалить родителя), CASCADE (удалить детей), SET NULL/DEFAULT — каждое имеет смысл, угадывать опасно.

        ## Как работать

        1. Платформа Vibe Learn создаёт копию этого репо в твоём GitHub-аккаунте по клику «Начать домашку» на странице урока (через GitHub `/generate`, codecrafters-pattern).
        2. Склонируй копию локально, реализуй TODO в `main.py`, прогони тесты, запушь.
        3. CI (`.github/workflows/ci.yml`) ставит зависимости и запускает `pytest` на каждый push. Платформа слушает результат через webhook от GitHub Actions и обновляет статус домашки на странице урока.

        ## Локальное окружение

        - Python 3.12+
        - Docker + docker-compose — `docker compose up -d` поднимает single-node PostgreSQL 16 на `localhost:5432` с healthcheck. DSN: `postgresql://postgres:postgres@localhost:5432/postgres`. Переопределяется через env `DATABASE_URL`.

        ## Запуск

        ```bash
        # Поднять локальный PostgreSQL
        docker compose up -d

        # Установить зависимости
        pip install -r requirements.txt

        # Прогнать тесты (интеграционный включается через PG_INTEGRATION=1)
        pytest
        PG_INTEGRATION=1 pytest

        # Запустить main (печатает marker; замени stub на реализацию)
        python main.py
        ```

        ## Заметка автора

        Это baseline-шаблон, сгенерированный платформой. Бизнес-сущность задачи (что конкретно реализовать в `main.py`, какие тесты сделать строгими) расширяется по ходу итераций — параллельно с углублением теории урока.
