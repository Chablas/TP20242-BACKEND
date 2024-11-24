import secrets
from PIL import Image
from fastapi import HTTPException, status, File, UploadFile
from src.controllers.c_gcs import upload_cs_file
import os

async def subir_imagen(file: UploadFile = File(...)):
    # Validar extensión del archivo
    filename = file.filename
    extension = filename.split(".")[-1].lower()

    if extension not in ["png", "jpg", "jpeg", "jpe", "jif", "jfif"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Extensión de archivo no aceptada. Formatos válidos: png, jpg, jpeg, jpe, jif, jfif"
        )

    # Generar nombre único para la imagen
    unique_name = "images" + secrets.token_hex(10) + "." + extension
    gcs_file_name = f"static/{unique_name}"  # Formato en GCS
    local_file_path = f"./{unique_name}"  # Guardar temporalmente en el mismo nivel del script

    # Guardar localmente la imagen temporal
    file_content = await file.read()
    with open(local_file_path, "wb") as f:
        f.write(file_content)

    # Procesar la imagen (opcional)
    img = Image.open(local_file_path)
    img.save(local_file_path)  # Guardar la imagen procesada
    print(f"Imagen guardada localmente como: {local_file_path}")

    # Subir la imagen a GCS
    if not upload_cs_file(local_file_path, gcs_file_name):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error al subir la imagen a Google Cloud Storage"
        )

    # Limpiar archivo temporal local
    os.remove(local_file_path)

    # Retornar la ruta que necesitas (con `/` como separador)
    return gcs_file_name