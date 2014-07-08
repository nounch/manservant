%try:
%    subtitle
% except NameError:
%    subtitle = ''
%end

<div id="header">
<div id="headerContent">
<div id="logo"><a href="/manservant">Manservant</a></div>
<div id="subtitle">{{subtitle}}</div>
<div id="topRight">
<form method="POST" action="/manservant">
  <input type="text" name="program" class="textbox"/>
  <input type="submit" name="submit" value="Go" class="button"/>
</form>
</div>
</div>
</div>

<link rel="stylesheet" href="/static/header.css" type="text/css" media="screen" />
