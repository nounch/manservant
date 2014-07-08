<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <title>Tasks</title>
  </head>

<body>

%include header subtitle="Tasks"

<div id="mainContent">

    <form class="inputForm" method="POST" action="/tasks/success">
      <div class="formRow">
      </div>

	<div class="formRow">
	  <label for="tsskInputField">Task</label>
	  <input id="taskInputField" type="text" name="task"/>
	</div>
	<div class="formRow">
	  <label for="tsskTextInputField">Descr.</label>
	  <textarea name="description" id="taskTextInputField" rows="1" cols="50" tabindex=""></textarea>
	</div>
	<div class="formRow">
	  <label for="tsskInputField">Status</label>
	  <select name="status">
	    <option value="0">Not done</option>
	    <option value="1">Done</option>
	  </select>
	</div>
	<div class="formRow" id="goButton">
	  <input class="submit" type="submit" value="Go"/>
	</div>

    </form>

%if tasks:
%tasks.reverse()

%for task in tasks:
<div id="task">
%if task[2] == 1:
    <div class="done statusIndicator">
      &#x2713
    </div>
%else:
    <div class="notDone statusIndicator">
      &#x2717
    </div>
%end
      <div id="taskLinkHolder" class="">
	<a id="taskLink" href="/tasks/edit/{{task[0]}}">{{task[3]}}
	  <div id="taskID">{{task[0]}}</div>
	</a>
      </div>
</div>
%end
%else:
    <p>No tasks defined.</p>
%end

</div>

</body>


<link rel="stylesheet" href="/static/tasks.css" type="text/css" media="screen" />

</html>
