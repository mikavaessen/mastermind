{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/Game.css')}}">
<title>MM | Home</title>
{% endblock %}
{% block body %}
<main>
    <h3><u>Game window</u></h3>
    <div id="gameWindow">
        <div id="Board">
            {% if inserts == NULL %}
            <div id="col0">
                {% for in range(0, tries) %}
                <span class="empty" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="col1">
                {% for in range(0, tries) %}
                <span class="empty" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="col2">
                {% for in range(0, tries) %}
                <span class="empty" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="col3">
                {% for in range(0, tries) %}
                <span class="empty" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="colFb">

            </div>
            {% for i in range(0, tries) %}
            <span class="empty" id="row{{i}} col0"></span>
            <span class="empty" id="row{{i}} col1"></span>
            <span class="empty" id="row{{i}} col2"></span>
            <span class="empty" id="row{{i}} col3"></span>
        </div>
    </div>
    <div id="controls">

    </div>
    {% for i in range(0, tries) %}

        <!--
            Veld van 4x10 met per rij 4 plekken voor feedback pins
        -->
</main>
{% endblock %}