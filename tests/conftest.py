import pytest
import copy
from src.app import activities as activities_dict

# Store initial state for resetting
initial_activities = copy.deepcopy(activities_dict)

@pytest.fixture
def client():
    """Test client for FastAPI app"""
    from fastapi.testclient import TestClient
    from src.app import app
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities dictionary to initial state before each test"""
    activities_dict.clear()
    activities_dict.update(copy.deepcopy(initial_activities))