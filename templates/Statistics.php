{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/statistics.css')}}">
<title>MM | Statistics</title>
{% endblock %}
{% set gameName = 2 %}
{% set gameResult = 4 %} 
{% set gameTries = 3 %}
{% set gameMode = 5 %}
{% block body %}
<h3><u>Statistics</u></h3>
<main>
    <aside id="PlayerList">
        {% if data == 'no' %}
        <p id="NoDataAside">No games present in database</p>
        {% else %}
        <form action="/" method="POST" id="PlayerListForm">
            <h4>Players</h4>   
            <div id="PlayerListEntries">
            {% for player in players %}
            {% if player == name %}
                <input type="submit" name="name" value="{{player}}" class="PlayerSelectedButton">
                <br>
            {% else %}
                <input type="submit" name="name" value="{{player}}" class="PlayerButton">
                <br>
            {% endif %}
            {% endfor %}
            </div>
            <input type="hidden" name="Msg" value="statsFilter">
        </form>
        {% endif %}
    </aside>
    <div id="PlayerInfo">
        {% if data == 'no' %}
        <p id="NoDataMain">No games present in database</p>
        {% else %}
        <p id="PlayerName">Player: {{name}}</p>
        {% for game in data %}
        <div class="Game">
            <p class="GameName">Game:<br>{{game[gameName]}}</p>
            <p class="GameResult">Result: {{game[gameResult]}}</p>
            <p class="GameGuesses">Guesses: {{game[gameTries]}}</p>
            <p class="GameDifficulty">Difficulty: {{game[gameMode]}}</p>
        <br>
        </div>
        {% endfor %}
        {% endif %}
    </div>
    <form action="/" method="POST" id="ExitForm">
        <input type="submit" value="Back" id="ExitButton">
        <input type="hidden" name="Msg" value="return">
    </form>
</main>
{% endblock %}