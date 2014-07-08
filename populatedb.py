import random
import sqlite3


def populate_db(db, file):
  con = sqlite3.connect(db)

  with open(file) as infile:
    for line in infile:
      if line.strip() != '':
        con.execute(
          """INSERT INTO tasks (task, description, status)
                           VALUES (?, ?, ?)""",
          (buffer(line), buffer(line + line), random.choice(['1', '0'])))

        con.commit()

if __name__ == '__main__':
  db = 'test.db'
  input_file = 'sentences.txt'

  populate_db(db, input_file)
