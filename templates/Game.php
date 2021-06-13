{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/Game.css')}}">
<link rel="stylesheet" href="{{ url_for('static', filename='css/colrow.css')}}">
<title>MM | Game</title>
{% endblock %}
{% block body %}
<h3><u>Game window</u></h3>
<main>
    <div id="gameWindow">
        <div id="Board">
            {% if inserts == 'no' %}
            <div id="col0" class="col">
                {% for i in range(0, tries) %}
                <span class="Empty row" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="col1" class="col">
                {% for i in range(0, tries) %}
                <span class="Empty row" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="col2" class="col">
                {% for i in range(0, tries) %}
                <span class="Empty row" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="col3" class="col">
                {% for i in range(0, tries) %}
                <span class="Empty row" id="row{{i}}"></span>
                {% endfor %}
            </div>
            <div id="colFb" class="col">
                {% for i in range(0, tries) %}
                    <div class="FbBox" id="row{{i}}">
                        {% for j in range(0, 4) %}
                        <span class="Empty" id="FbPin{{j}}"></span>
                        {% endfor %}
                    </div>
                {% endfor %}
            </div>
        {% else %}
        <p>Oops...</p>
        {% endif %}
        </div>
    </div>
    <form action="/" method="POST" id="controls">
        <select name="colour0" id="colour0" class="colourSelect">
            {% for col in colours %}
            <option value="{{col}}">{{col}}</option>
            {% endfor %}
        </select>
        <select name="colour1" id="colour1" class="colourSelect">
            {% for col in colours %}
            <option value="{{col}}">{{col}}</option>
            {% endfor %}
        </select>
        <select name="colour2" id="colour2" class="colourSelect">
            {% for col in colours %}
            <option value="{{col}}">{{col}}</option>
            {% endfor %}
        </select>
        <select name="colour3" id="colour3" class="colourSelect">
            {% for col in colours %}
            <option value="{{col}}">{{col}}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Make guess" id="GuessButton">
        <input type="hidden" name="Msg" value="CheckResult">
    </form>
    <form action="/" method="POST" id="StopForm">
        <input type="submit" value="Give up" id="StopButton">
        <input type="hidden" name="Msg" value="quit">
    </form>
</main>
{% endblock %}