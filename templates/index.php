{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css')}}">
<title>Mastermind</title>
{% endblock %}
{% block body %}
<main>
    <form action="/" method="POST" id="StartForm">
        <input type="submit" value="Start New Game" id="StartButton">
        <input type="hidden" value="StartGame" name="Msg">
    </form>
</main>
{% endblock %}