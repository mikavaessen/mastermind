{% extends 'base.php' %}

{% block head %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/login.css')}}">
<title>MM | Login</title>
{% endblock %}
{% block body %}
<main>
    <form action="/login" method="POST" id="UserSelect">
        <div>
            <select name="user", id="users">
            <option value="||">Select Nickname</option>
            <option value="Mika">Mika</option>
            <option value="Leon">Leon</option>
            </select>
            <input type="text" placeholder="New Nickname" id="NewNameField" name="NewNameField">
            <input type="submit" name="Add Nickname" id="AddNick" value="Add">
        </div>
    </form>
    <form action="/login.py" method="POST" id="Difficulty">
        <div>
            <input type="checkbox" id="hardmode" name="hardmode">
            <label for="hardmode">Hard Mode</label>
            <input type="range" id="colours" name="colours" min="6" max="10">
            <label for="colours">Amount of colours (6-10)</label>
            <input type="range" id="tries" name="tries" min="4" max="10">
            <label for="tries">Amount of tries (4-10)</label>
        </div>
    </form>
</main>
{% endblock %}