import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.database import Base, get_db
from models.user import User
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def clean_tables():
    from tests.conftest import TestingSessionLocal
    db = TestingSessionLocal()
    db.query(User).delete()
    db.commit()
    db.close()


@pytest.fixture
def registered_user(client):
    payload = {
        "name": "Test",
        "lastname": "User",
        "email": "login@example.com",
        "password": "123456"
    }
    client.post("/users/register", json=payload)
    return payload
