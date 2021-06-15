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
    {% if result == 'TRUE' %}
    <span style="border-color: green;"></span>
    <p class="CelText">You won,<br>good job!</p>
    {% else %}
    <span style="border-color: red;"></span>
    <p class="CelText">You lost,<br>better luck next time...</p>
    {% endif %}
    <form action="/" method="POST">
        <input type="text"  placeholder="Enter a nickname" name="nickName" id="nameField">
        <input type="submit" value="Submit result" id="ReturnButton">
        {% if result == 'TRUE' %}
        <input type="hidden" name="result" value="Win">
        {% else %}
        <input type="hidden" name="result" value="Loss">
        {% endif %}
        <input type="hidden" name="Msg" value="returnEndGame">
    </form>
</main>
{% endblock %}