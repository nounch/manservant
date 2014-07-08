import os
from subprocess import Popen, PIPE

import sqlite3

from bottle import Bottle, route, run, template, debug
from bottle import request, static_file, redirect


app = Bottle()
db = 'test.db'

@app.route('/static/<filepath:path>')
def static(filepath):
  """Serves all static files in the specified directory."""
  return static_file(filepath, root=os.getcwd() + '/static/files/')

@app.route('/')
@app.route('/manservant')
def index():
  return template('serve_man', program_name=None, manpage=None)

@app.route('/', method='POST')
@app.route('/manservant', method='POST')
def manpage(program_name='', manpage=''):
  program_name = request.forms.get('program')
  path = ''
  manpage = ''
  output = 'There is no manpage for: <b>' + program_name + "</b>"

  if program_name != '':
    # manpage = check_output(['man2html',
    #                         check_output(['man', '-w',
    #                                       str(program_name)])])
    path = Popen(["man", "-w", str(program_name)],
                 stdout=PIPE).communicate()[0]

    # FIXME: Deprecated + dangerous! 'Use subprocess' instead.
    if path != '':
      output = os.popen("man2html %s" % path)

    for line in output:
      manpage += line


    return template('serve_man', program_name=program_name,
                    manpage=manpage)

@app.route('/help')
def help():
  return template('help')

@app.route('/tasks')
def tasks():
  conn = sqlite3.connect(db)
  c = conn.cursor()

  c.execute("SELECT id, task FROM tasks WHERE status LIKE '0';")
  tasks = c.fetchall()

  c.close()

  return template('tasks', tasks=tasks)

@app.route('/tasks/edit/<no:int>') # , method='GET')
def edit_task_no(no):
  id = str(no)

  conn = sqlite3.connect(db)
  c = conn.cursor()

  tuples = c.execute('SELECT task, description, status FROM tasks WHERE id=?',
                     (id,))
  tasks = tuples.fetchall()
  task = tasks[0][0]
  description = tasks[0][1]
  status = tasks[0][2]

  conn.commit()
  c.close()

  return template(
    'edit_task', id=id, task=task, status=status, description=description)

@app.route('/tasks/setstatus', method='POST')
def set_status():
  # Get ALL query parameters
  status = str(request.POST.getall('status'))
  description = request.POST.getall('description')

  conn = sqlite3.connect(db)
  c = conn.cursor()

  if status == 0:
    # c.execute("INSERT INTO tasks (description, status) VALUES (?, ?, ?)",
    #           (description, status))
    # c.execute("UPDATE tasks SET description=?, status=? WHERE name=?",
    #           ())
    pass
  else:
    # c.execute("INSERT INTO tasks (task) VALUES (?)", ('1'))
    pass

  conn.commit()
  c.close()

  redirect('/tasks')

@app.route('/tasks/success<:re:.*>', method="POST")
def tasks_submit_success():
  task = str(request.POST.get('task'))
  description = request.POST.get('description')
  status = int(request.POST.get('status'))

  tasks = []

  conn = sqlite3.connect(db)
  c = conn.cursor()

  if task != None and status != None and task.strip() != '':
    c.execute(
      'INSERT INTO tasks (task, description, status) VALUES (?, ?, ?)',
      (task, description, status))

    conn.commit()
    c.close()

    redirect('/tasks')

@app.route('/tasks/update', method='POST')
def tasks_update():
  task = request.POST.get('task')
  description = request.POST.get('description')
  status = request.POST.get('status')
  id = request.POST.get('id')

  conn = sqlite3.connect(db)
  c = conn.cursor()

  c.execute(
    'UPDATE tasks SET task=?, description=?, status=? WHERE id=?',
    (task, description, status, id))

  conn.commit()
  c.close()

  redirect('/tasks')

@app.route('/tasks', method='GET')
def tasks_submit():
  task = str(request.GET.get('task'))
  tasks = []

  conn = sqlite3.connect(db)
  c = conn.cursor()

  c.execute("SELECT id, description, status, task  FROM tasks WHERE status LIKE '0' OR '1';")
  tasks = c.fetchall()

  conn.commit()
  c.close()

  return template('tasks', tasks=tasks)



# Debugging

run(app, host='localhost', port=4321)
debug(reloader=True)
