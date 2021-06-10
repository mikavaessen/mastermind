{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/login.css')}}">
<title>MM | Login</title>
{% endblock %}
{% block body %}
<main>
    <h3><U>Game Settings</U></h3>
    <form action="/" method="POST" id="UserSelect">
        <h2>Nickname</h2>
        <div class="FormDiv">
            <select name="user", id="users">
                {% for name in names %}
                <option value="{{name}}">{{name}}</option>
                {% endfor %}
            </select>
            <input type="text" placeholder="New Nickname" id="NewNameField" name="NewNameField">
            <input type="submit" name="Add Nickname" id="AddNick" value="Add">
            <input type="hidden" name="Msg" value="AddName">
        </div>
    </form>
    <form action="/" method="POST" id="Difficulty">
        <h2>Difficulty</h2>
        <div class="FormDiv">
            <div id="HmDiv">
                <input type="checkbox" class="item" name="hardmode">
                <label for="hardmode">Hard Mode</label>
            </div>
            <div id="ClDiv">
                <input type="number" class="item" name="colours" step="1" min="6" max="10" value="6">
                <label for="colours">Colours<br>(6-10)</label>
            </div>
            <div id="TryDiv">
                <input type="number" class="item" name="'tries" step="1" min="4" max="10" value="4">
                <label for="tries">Tries<br>(4-10)</label>
            </div>
        </div>
        <input type="submit" name="Start" value="Start Game" id="StartGame">
        <input type="hidden" name="Msg" value="StartGame">
    </form>
</main>
{% endblock %}