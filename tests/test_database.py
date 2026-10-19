import sqlite3

import pytest

from app import database


def test_connection_is_closed_after_success(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    monkeypatch.setattr(database, "DATABASE_PATH", db_path)

    with database.get_connection() as connection:
        connection.execute("CREATE TABLE example (id INTEGER)")

    with pytest.raises(sqlite3.ProgrammingError, match="closed"):
        connection.execute("SELECT 1")


def test_connection_is_closed_after_exception(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    monkeypatch.setattr(database, "DATABASE_PATH", db_path)

    with pytest.raises(RuntimeError, match="test failure"), database.get_connection() as connection:
        connection.execute("CREATE TABLE example (id INTEGER)")
        raise RuntimeError("test failure")

    with pytest.raises(sqlite3.ProgrammingError, match="closed"):
        connection.execute("SELECT 1")


def test_exception_rolls_back_transaction(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"
    monkeypatch.setattr(database, "DATABASE_PATH", db_path)

    with database.get_connection() as connection:
        connection.execute("CREATE TABLE example (value TEXT NOT NULL)")

    with pytest.raises(RuntimeError, match="test failure"), database.get_connection() as connection:
        connection.execute(
            "INSERT INTO example (value) VALUES (?)",
            ("not committed",),
        )
        raise RuntimeError("test failure")

    with database.get_connection() as connection:
        row_count = connection.execute(
            "SELECT COUNT(*) FROM example"
        ).fetchone()[0]

    assert row_count == 0