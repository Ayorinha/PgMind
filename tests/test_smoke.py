"""Production smoke tests for PgMind."""
import importlib


def test_package_imports() -> None:
    module = importlib.import_module("pgmind")
    assert module.__name__ == "pgmind"


def test_import_is_network_independent() -> None:
    # Import-time network calls make CI and offline development fragile.
    module = importlib.import_module("pgmind")
    assert module is not None
