{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/index.css')}}">
<title>Mastermind</title>
{% endblock %}
{% block body %}
<main>
    <form action="/" method="POST">
        <input type="submit" value="Start New Game">
        <input type="hidden" value="StartGame" name="Msg">
    </form>
</main>
{% endblock %}