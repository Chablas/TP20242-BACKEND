from src.api.db.conexion import SessionLocal, engine
from src.api.db.models.m_usuarios import Base
from src.api.db.models.m_almacenes import Base
from src.api.db.models.m_bienes import Base
from src.api.db.models.m_productos_almacenes import Base
from src.api.db.models.m_productos import Base
from src.api.db.models.m_proveedores_bienes import Base
from src.api.db.models.m_proveedores import Base
from src.api.db.models.m_servicios import Base
from src.api.db.models.m_categorias import Base
from src.api.db.models.m_movimientos_almacenes import Base
from src.api.db.models.m_roles import Base

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()