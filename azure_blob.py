from azure.storage.blob import BlobServiceClient
import os

connection_string = os.getenv('AZURE_BLOB_CONNECTION_STRING')
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_name = "user-uploads"

def upload_file_to_blob(file):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
    blob_client.upload_blob(file.read(), overwrite=True)
    return blob_client.url
