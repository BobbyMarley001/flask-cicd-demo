from app import app

def test_home():
    with app.app_context():
        response = app.test_client().get('/')
        assert response.status_code == 200
        assert b"\xf0\x9f\x9a\x80 Welcome to the, DevOps CI/CD World!" in response.data


