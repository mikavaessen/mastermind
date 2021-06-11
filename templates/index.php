{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css')}}">
<title>MM | Home</title>
{% endblock %}
{% block body %}
<h3><u>Welcome!</u></h3>
<main>
    <form action="/" method="POST">
        <input type="submit" value="Start New Game" id="StartButton">
        <input type="hidden" name="Msg" value="login">
    </form>
    <form action="/" method="POST">
        <input type="submit" value="Statistics" id="StatButton">
        <input type="hidden" name="Msg" value="stats">
    </form>
</main>
{% endblock %}