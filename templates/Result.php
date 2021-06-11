{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/Result.css')}}">
{% if result == TRUE %}
<title>MM | You won!</title>
{% else %}
<title>MM | You lost...</title>
{% endif %}
{% endblock %}
{% block body %}
<h3><u>Result</u></h3>
<main>
    {% if result == TRUE %}
    <span style="border-color: green;"></span>
    <p class="CelText">You won,<br>good job!</p>
    {% else %}
    <span style="border-color: red;"></span>
    <p class="CelText">You lost,<br>better luck next time...</p>
    {% endif %}
    <form action="/" method="POST">
        <input type="submit" value="Return to start screen" id="ReturnButton">
        <input type="hidden" name="Msg" value="return">
    </form>
</main>
{% endblock %}