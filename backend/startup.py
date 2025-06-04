from db.database import Base, engine
from models import user, cover_letter  # asegúrate de importar todos los modelos


def init_db():
    Base.metadata.create_all(bind=engine)
