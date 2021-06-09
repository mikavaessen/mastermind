<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="{{ url_for('static', filename='css/base.css')}}">
        {% block head %}
        {% endblock %}
    </head>
    <body>
        <header>
            <img src="GameLogo.jfif" alt="Logo" id="HeaderLogo">
            <h1 id="title">Mastermind</h1>
        </header>
        <main>
        {% block body %}
        {% endblock %}
        </main>
    </body>
</html>