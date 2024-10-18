from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError  # Correct import for ResourceNotFoundError
from dotenv import load_dotenv
import os
import PyPDF2
import io

# Load environment variables
load_dotenv()

# Set up your Azure storage account details
account_name = os.getenv('ACCOUNT_NAME')
account_key = os.getenv('ACCOUNT_KEY')
container_name = "mechanic"  # The name of the container where the PDF is stored

def getContent(blob_name):
    try:
        # Create the BlobServiceClient
        blob_service_client = BlobServiceClient(
            account_url=f"https://{account_name}.blob.core.windows.net/",
            credential=account_key
        )

        # Get the blob client for the PDF file
        blob_client = blob_service_client.get_blob_client(container_name, blob_name)

        # Stream the PDF file from Azure Blob Storage (in memory)
        stream = blob_client.download_blob()
        pdf_stream = io.BytesIO(stream.readall())  # Read the blob directly into memory

        # Use PyPDF2 to read the PDF contents
        reader = PyPDF2.PdfReader(pdf_stream)

        # Extract text from each page
        pdf_text = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text.append(text)

        # Join all text into a single string
        full_text = "\n".join(pdf_text)

        return full_text

    except ResourceNotFoundError:
        print(f"Blob '{blob_name}' not found in container '{container_name}'.")
        return "Blob not found."

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error while reading the blob: {str(e)}"
