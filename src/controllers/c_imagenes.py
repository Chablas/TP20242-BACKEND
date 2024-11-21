import secrets
from PIL import Image
from fastapi import HTTPException, status, File, UploadFile

async def subir_imagen(file:UploadFile=File(...)):
    FILEPATH = "./static/images"
    filename = file.filename
    extension = filename.split(".")[1]
    if extension not in ["png", "jpg", "jpeg", "jpe", "jif", "jfif"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Extensión de archivo de imagen no aceptado. Los formatos válidos son: png, jpg, jpeg, jpe, jif, jfif")
    token_name = secrets.token_hex(10)+"."+extension
    generated_name = FILEPATH + token_name
    file_content = await file.read()
    with open (generated_name, "wb") as file:
        file.write(file_content)
    img  = Image.open(generated_name)
    #img = img.resize(size=(200,200))
    img.save(generated_name)
    file.close()
    return generated_name[1:]