"""Test the history and movies commands"""
from app import App

def test_app_history_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'history' command."""
    # Simulate user entering 'history' followed by 'done', then 'exit'
    inputs = iter(['history', 'done', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture the standard output
    out, _ = capfd.readouterr()

    # Check if the output contains the 'history' command
    assert "history" in out, "The output does not contain the 'history' command"

    # Check if 'done' was entered
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert "" in out, "\'done\' was not entered"

    # Check if 'exit' was entered
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert "" in out, "\'exit\' was not entered"

def test_app_movies_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'movies' command."""
    # Simulate user entering 'movies' followed by 'done', then 'exit'
    inputs = iter(['movies', 'done', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture the standard output
    out, _ = capfd.readouterr()

    # Check if the output contains the 'movies' command
    assert "movies" in out, "The output does not contain the 'movies' command"

    # Check if 'done' was entered
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert "" in out, "\'done\' was not entered"

    # Check if 'exit' was entered
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert "" in out, "\'exit\' was not entered"
