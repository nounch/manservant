<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <title>Edit Task</title>
  </head>

<body>

%include header subtitle="Tasks"


<div id="mainContent">

<div id="backLink">
  <a id="backLink" href="/tasks">back</a>
</div>

<form id="taskEditForm" method="POST" action="/tasks/update">
  <h1>Task No. {{id}}</h1>
  <div class="formLine">
    <label for="task">Task</label>
    <input type="text" name="task" value="{{task}}" />
  </div>
  <div class="formLine">
    <label for="description">Descr.</label>
    <textarea name="description" rows="3", cols="50">{{description}}</textarea>
  </div>
  <div class="formLine">
    <label for="status">Status</label>
    <select type="select" name="status" value="{{status}}">
%if status == 1:
      <option value="1">Done</option>
      <option value="0">Not done</option>
%else:
      <option value="0">Not done</option>
      <option value="1">Done</option>
%end
    </select><br />
  </div>
  <div class="submitButton">
    <input type="submit" name="submit" value="Ok" />
    <input type="hidden" name="id" value="{{id}}" /><br />
  </div>
</form>


</div>


</body>

<link rel="stylesheet" href="/static/tasks.css" type="text/css" media="screen" />
<link rel="stylesheet" href="/static/edit_task.css" type="text/css" media="screen" />

</html>
