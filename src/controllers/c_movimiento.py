#from src.api.db.models.m_divisa import Divisa
#from src.api.db.models.m_cambio import Cambio
from src.api.db.schemas.s_divisa import DivisaCreate, DivisaResponse, DivisaCambioUpdate, DivisaCambioGet, CambioResponse
from fastapi import HTTPException, status

# BORRAR ESTE ARCHIVO EN UN FUTURO

def c_obtener_todas_las_divisas(db):
    try:
        divisas = db.query(Divisa).all()
        divisas_array = []
        for divisa in divisas:
            divisas_array.append(divisa)
        return divisas_array
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_obtener_divisa_por_abbr(db, abbr:str):
    # Validaciones inicio
    divisa=db.query(Divisa).filter(Divisa.abbr==abbr).first()
    if divisa is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La divisa no existe")
    # Validaciones fin
    try:
        respuesta=DivisaResponse(
            id=divisa.id,
            nombre=divisa.nombre,
            abbr=divisa.abbr
        )
        return respuesta
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def crear_divisa(db, entrada:DivisaCreate):
    # Validaciones inicio
    validacion = db.query(Divisa).filter(Divisa.abbr==entrada.abbr).first()
    if validacion is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La abreviación de divisa ya existe")
    # Validaciones fin
    try:
        divisa = Divisa(
            nombre = entrada.nombre,
            abbr = entrada.abbr,
        )
        db.add(divisa)
        db.commit()
        db.refresh(divisa)
        todas_las_divisas = db.query(Divisa).filter(Divisa.id != divisa.id).all()
        for otra_divisa in todas_las_divisas:
            tipo_cambio = Cambio(
                abbr_primary=entrada.abbr,
                abbr_secondary=otra_divisa.abbr,
                compra=0,
                venta=0
            )
            db.add(tipo_cambio)
            tipo_cambio_2 = Cambio(
                abbr_primary=otra_divisa.abbr,
                abbr_secondary=entrada.abbr,
                compra=0,
                venta=0
            )
            db.add(tipo_cambio_2)
        db.commit()
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def actualizar_tipo_cambio_divisa(db, entrada:DivisaCambioUpdate):
    # Validaciones inicio
    validacion=db.query(Divisa).filter(Divisa.abbr==entrada.abbr_primary).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La divisa principal no existe")
    validacion=db.query(Divisa).filter(Divisa.abbr==entrada.abbr_secondary).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La divisa secundaria no existe")
    # Validaciones fin
    try:
        divisa = db.query(Cambio).filter(Cambio.abbr_primary==entrada.abbr_primary,
                                        Cambio.abbr_secondary == entrada.abbr_secondary
                                        ).first()
        divisa.compra = entrada.compra
        divisa.venta = entrada.venta
        db.commit()
        db.refresh(divisa)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")

def c_tipo_cambio_divisa_por_abbr(db, abbr_primary, abbr_secondary):
    # Validaciones inicio
    validacion=db.query(Divisa).filter(Divisa.abbr==abbr_primary).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La divisa principal no existe")
    validacion=db.query(Divisa).filter(Divisa.abbr==abbr_secondary).first()
    if validacion is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="La divisa secundaria no existe")
    # Validaciones fin
    try:
        divisa = db.query(Cambio).filter(Cambio.abbr_primary==abbr_primary,
                                        Cambio.abbr_secondary==abbr_secondary).first()
        respuesta = CambioResponse(
            compra=divisa.compra,
            venta=divisa.venta,
        )
        return respuesta
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
    
def c_tipo_cambio_divisas(db):
    try:
        cambios = db.query(Cambio).all()
        divisas_array = []
        for cambio in cambios:
            divisas_array.append(cambio)
        return divisas_array
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error interno del servidor")
"""
def c_actualizar_cambio_auto_divisa(db, abbr_primary):
    try:
        url = f'https://v6.exchangerate-api.com/v6/bd26b297de3d94d41becd9e1/latest/{abbr_primary}'
        response_service = requests.get(url)
        json_data = response_service.json()
        dato = json_data.get('conversion_rates', {})
        cambios = db.query(Cambio).all()
        if 

"""