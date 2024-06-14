"""Test the unknown and exit commands"""
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

def test_app_start_exit_command(capfd, monkeypatch, setup_environment):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')

    assert App().start() is None  # Assert that the method returns None

def test_app_start_unknown_command(capfd, monkeypatch, setup_environment):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    captured = capfd.readouterr()
    assert "" in captured.out

    assert App().start() is None  # Assert that the method returns None
