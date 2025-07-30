from app import app

def test_home():
    with app.app_context():
        response = app.test_client().get('/')
        assert b"Welcome to the, DevOps CI/CD World!" in response.data

