import sqlite3


con = sqlite3.connect('test.db')
con.execute(
    """CREATE TABLE tasks (
                 id INTEGER PRIMARY KEY
                 , task char(100) NOT NULL
                 , description char(5000) NOT NULL
                 , status bool NOT NULL
               )""")

con.execute(
    """INSERT INTO tasks (task, description, status)
           VALUES (
               'Read A-byte-of-python to get a good introduction into Python'
               , 'This is a description'
               , 0
        )""")
con.execute(
    """INSERT INTO tasks (task, description, status)
           VALUES (
               'Do nothing'
               , 'Teally nothing'
               , 1
        )""")
con.execute(
    """INSERT INTO tasks (task, description, status)
           VALUES (
               'This is nonsense.'
               , 'Really, it is nonsense.'
               ,  0
        )""")
con.execute(
    """INSERT INTO tasks (task, description, status)
           VALUES (
               'Foo'
               , 'Bar'
               , 0
        )""")
con.commit()
