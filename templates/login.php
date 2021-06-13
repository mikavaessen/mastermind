{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/login.css')}}">
<title>MM | Login</title>
{% endblock %}
{% block body %}
<h3><U>Game Settings</U></h3>
<main>
    <form action="/" method="POST" id="Difficulty">
        <div class="FormDiv">
            <div id="HmDiv">
                <label for="difficultySelect">Difficulty</label>
                <select name="difficulty" id="difficultySelect" class="item">
                    <option value="Easy">Easy</option>
                    <option value="Hard">Hard</option>
                </select>
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