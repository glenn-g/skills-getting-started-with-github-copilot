"""Shared pytest fixtures for the backend API tests."""

import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """A TestClient for making requests against the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Snapshot and restore the in-memory activities store around each test.

    `activities` is a module-level mutable dict used as the app's "database",
    so signups/unregistrations in one test would otherwise leak into others.
    """
    original_state = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
