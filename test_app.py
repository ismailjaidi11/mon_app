from app import app

def test_accueil():
    client = app.test_client()
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert b"Bonjour depuis Docker" in reponse.data