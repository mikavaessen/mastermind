{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/statistics.css')}}">
<title>MM | Statistics</title>
{% endblock %}
{% block body %}
<main>
    <h3><u>Statistics</u></h3>
    <aside id="PlayerList">
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
    </aside>
    <div id="PlayerInfo">
        <p id="PlayerName">Player: {{name}}</p>
        {% for game in games %}
        <div class="Game">
            <p class="GameName">Game {{game.playTime}}</p>
            <p class="GameResult">Result {{game.result}}</p>
            <p class="GameGuesses">Guesses {{game.guesses}}</p>
        <br>
        {% endfor %}
    </div>
    <form action="/" method="POST" id="ExitForm">
        <input type="submit" value="Back" id="ExitButton">
        <input type="hidden" name="Msg" value="return">
    </form>
</main>
{% endblock %}