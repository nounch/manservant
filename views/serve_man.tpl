<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  <head>
    <title>Manservant</title>
  </head>


<body>

<div id="header">
<div id="headerContent">
<div id="logo"><a href="/manservant">Manservant</a></div>
<div id="topRight">
<form method="POST" action="/manservant">
  <input type="text" name="program" class="textbox"/>
  <input type="submit" name="submit" value="Go" class="button"/>
</form>
</div>
</div>
</div>

<div id="mainContent">



%if program_name == None and manpage == None:
<h1>No manpage</h1>
<a href="/help">Show me how.</a>
%end

%if manpage:
<div id="manpage">
{{!manpage}}
</div>
%end

</div>
</body>

<link rel="stylesheet" href="/static/main.css" type="text/css" media="screen" />

</html>
