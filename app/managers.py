import sqlite3
from app.models import Actor


class ActorManager:
    def __init__(self, db_name, table_name):
        self.db = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name, last_name):
        sql = f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)"
        self.cursor.execute(sql, (first_name, last_name))
        self.conn.commit()

    def all(self):
        a = f"SELECT * FROM {self.table_name}"
        self.cursor.execute(a)
        self.rows = self.cursor.fetchall()
        actors = []
        for row in self.rows:
            actors.append(Actor(*row))
        return actors

    def update(self, pk, new_first_name, new_last_name):
        u = f"UPDATE {self.table_name} SET first_name=?, last_name=? WHERE id=?"
        self.cursor.execute(u, (new_first_name, new_last_name, pk))
        self.conn.commit()

    def delete(self, id):
        d = f"DELETE FROM {self.table_name} WHERE id=?"
        self.cursor.execute(d, (id,))
        self.conn.commit()
