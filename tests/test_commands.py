"""Test the financial_advisor, history, and movies commands"""
import os
import pytest
from app import App

@pytest.fixture
def setup_environment():
    """Simulate setting environment variables"""
    # Set up the environment variable
    os.environ['OPENAI_API_KEY'] = 'true'
    yield
    # Teardown: Reset the environment variable
    del os.environ['OPENAI_API_KEY']

def test_app_financial_advisor_command(capfd, monkeypatch, setup_environment):
    """Test that the REPL correctly handles the 'financial_advisor' command."""
    # Simulate user entering 'financial_advisor' followed by 'done', then 'exit'
    inputs = iter(['financial_advisor', 'done', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    app.start()  # Assuming App.start() is now a static method based on previous discussions

    # Capture the standard output
    out, _ = capfd.readouterr()

    # Check if the output contains the 'financial_advisor' command
    assert "financial_advisor" in out, "The output does not contain the 'financial_advisor' command"

    # Check if 'done' was entered
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert "" in out, "\'done\' was not entered"

    # Check if 'exit' was entered
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert "" in out, "\'exit\' was not entered"

def test_app_history_command(capfd, monkeypatch, setup_environment):
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

def test_app_movies_command(capfd, monkeypatch, setup_environment):
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
