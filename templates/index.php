{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css')}}">
<title>MM | Home</title>
{% endblock %}
{% block body %}
<main>
    <form action="/" method="POST" id="StartForm">
        <input type="submit" value="Start New Game" id="StartButton" name="submit">
        <input type="submit" value="Statistics" id="Stats" name="submit">
    </form>
</main>
{% endblock %}