import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool  # <--- IMPORTANTE
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.models import Base, User

# CONFIGURACIÓN CRÍTICA PARA SQLITE EN MEMORIA
# StaticPool asegura que todos los hilos y sesiones compartan LA MISMA conexión de memoria.
engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app, base_url="http://test")


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)

    # Usar un context manager asegura que la sesión se cierre tras el commit
    with TestingSessionLocal() as db:
        db.add(User(id=1, username="danilo_dev", email="danilo@example.com"))
        db.commit()

    yield  # Aquí corren los tests con la DB poblada

    Base.metadata.drop_all(bind=engine)


def test_read_user_success():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "danilo_dev"


def test_read_user_not_found():
    """
    Prueba que el endpoint devuelva 404 cuando el usuario no existe.
    """
    # Act: Buscamos un ID que no insertamos en el setup_db (ej: ID 99)
    response = client.get("/users/99")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario no encontrado"


def test_create_user_success():
    # El JSON debe tener exactamente las llaves que pide UserCreate
    payload = {
        "username": "jose_danilo",
        "email": "danilo.systems@example.com"
    }

    response = client.post("/users/", json=payload)

    # Si sale 422, imprime response.json() para ver qué campo falta
    if response.status_code == 422:
        print(response.json())

    assert response.status_code == 200
    assert response.json()["username"] == "jose_danilo"