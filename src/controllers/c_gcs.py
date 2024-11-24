from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'/etc/secrets/gcskey.json'
bucket_name="tallerdeproyectoscompusave"

# define function that uploads a file from the bucket
def upload_cs_file(local_file_path, gcs_file_name):
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(gcs_file_name.replace("\\", "/"))  # Usar siempre `/`
        blob.upload_from_filename(local_file_path)  # Subir el archivo desde local
        print(f"Archivo subido exitosamente a GCS como: {gcs_file_name}")
        return True
    except Exception as e:
        print(f"Error al subir el archivo: {e}")
        return False