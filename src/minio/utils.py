from minio import Minio

minio_client = Minio(
    "minio_host:9000",
    access_key="MINIO_ACCESS_KEY",
    secret_key="MINIO_SECRET_KEY",
    secure=False
)

# Subir archivo
minio_client.fput_object("datasets", "imagen_001.jpg", "/local/path/imagen_001.jpg")

# Descargar archivo
minio_client.fget_object("datasets", "imagen_001.jpg", "/local/path/imagen_001.jpg")
