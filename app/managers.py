import sqlite3


from app.models import Actor
class ActorManager:
    def __init__(self, db_name, table_name):
        self.db = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create(self, first_name, last_name):
        self.cursor.execute("INSERT INTO ActorManager (first_name, last_name) VALUES(?, ?)",
                            (first_name, last_name))
        self.conn.commit()

    def all(self):
        self.cursor.execute("SELECT * FROM ActorManager")
        self.rows = self.cursor.fetchall()
        actors = []
        for row in self.rows:
            actors.append(Actor(*row))
        return actors

    def update(self, id, first_name, last_name):
        self.cursor.execute("UPDATE ActorManager SET first_name = ?, last_name = ? WHERE id = ?", (first_name, last_name, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM ActorManager WHERE id = ?", (id,))
        self.conn.commit()
