"""Homework scaffold — postgresql lesson `l2_schemas_tables_types` (Vibe Learn).

Задача: book-club схема (users/books/reviews) с FK, CHECK rating 1..5, UNIQUE — миграция + smoke.

Реализуй функции ниже — сигнатуры и тестовая поверхность фиксированы;
CI (.github/workflows/ci.yml) ставит зависимости и гоняет `pytest`.
Подробности и критерии приёмки — в README.md.

Драйвер: psycopg (v3). DSN берётся из env DATABASE_URL.
"""

import os

import psycopg


def database_url() -> str:
    """DSN PostgreSQL из env. Дефолт совпадает с docker-compose.yml."""
    return os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/postgres",
    )


def connect() -> "psycopg.Connection":
    """Открыть соединение psycopg из DATABASE_URL."""
    return psycopg.connect(database_url())


# ----- TODO #1: apply_migration -----
def apply_migration(conn) -> None:
    """выполнить DDL: users, books, reviews с FK, CHECK (rating BETWEEN 1 AND 5), UNIQUE(user_id, book_id), timestamptz"""
    raise NotImplementedError("apply_migration: реализуй меня")


# ----- TODO #2: insert_review -----
def insert_review(conn, user_id: int, book_id: int, rating: int) -> int:
    """вставить отзыв и вернуть id; пусть БД сама отшивает плохие данные через constraint-ы"""
    raise NotImplementedError("insert_review: реализуй меня")



def main() -> None:
    """Точка входа: подключиться и напомнить, что реализовать.

    Замени тело на демонстрацию реализованных функций.
    """
    print("Vibe Learn — postgresql lesson scaffold up")
    print(f"DATABASE_URL: {database_url()}")
    print("Реализуй TODO-функции, затем `pytest`. README.md содержит задачу.")


if __name__ == "__main__":
    main()
