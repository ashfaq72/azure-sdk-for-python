# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from devtools_testutils import AzureRecordedTestCase
from azure.ai.translation.document import DocumentTranslationClient, SingleDocumentTranslationClient
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.ai.translation.document.models import SourceInput, TargetInput, BatchRequest, StartTranslationDetails
from testdocument import TestDocument
import random
import string
from preparer import DocumentTranslationPreparer

class DocumentTranslationTest(AzureRecordedTestCase):
    def create_client(self, endpoint):
        credential = self.get_credential(DocumentTranslationClient)
        return self.create_client_from_credential(
            DocumentTranslationClient,
            credential=credential,
            endpoint=endpoint,
        )    
    
    def create_source_container(self, documents, storage_name):
        container_name = self.generate_random_name("source", 10)
        account_url = f"https://{storage_name}.blob.core.windows.net"

        # Create the BlobServiceClient object
        default_credential = DefaultAzureCredential()       
        blob_service_client = BlobServiceClient(account_url, credential=default_credential)        
        try:
            container_client = blob_service_client.create_container(container_name)
        except Exception as e:
            print(f"Container '{container_name}' already exists or another error occurred: {e}")

        # Check if documents are provided
        if documents:
            # Upload each document using the file contents
            for document in documents:
                try:
                    blob_client = container_client.get_blob_client(document.name)
                    # Upload the contents directly
                    blob_client.upload_blob(document.content)
                    print(f"Blob '{document.name}' uploaded to container '{container_name}'.")
                except Exception as e:
                    print(f"Failed to upload blob '{document.name}': {e}")
        else:
            print("No documents provided to upload.")

        return container_client.url    
    
    def create_target_container(self, documents, storage_name):
        container_name = self.generate_random_name("target", 10)
        account_url = f"https://{storage_name}.blob.core.windows.net"

        # Create the BlobServiceClient object
        default_credential = DefaultAzureCredential()
        blob_service_client = BlobServiceClient(account_url, credential=default_credential)        
        try:
            container_client = blob_service_client.create_container(container_name)
        except Exception as e:
            print(f"Container '{container_name}' already exists or another error occurred: {e}")

        # Check if documents are provided
        if documents:
            # Upload each document using the file contents
            for document in documents:
                try:
                    blob_client = container_client.get_blob_client(document.name)
                    # Upload the contents directly
                    blob_client.upload_blob(document.content)
                    print(f"Blob '{document.name}' uploaded to container '{container_name}'.")
                except Exception as e:
                    print(f"Failed to upload blob '{document.name}': {e}")
        else:
            print("No documents provided to upload.")

        return container_client.url

    def generate_random_name(self, prefix, length):
        if length <= len(prefix):
            raise ValueError("Length must be greater than the length of the prefix.")

        # Generate a random suffix of the required length
        suffix_length = length - len(prefix)
        suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=suffix_length))
        
        return prefix + suffix
    
    def create_source_input(self, source_url, filter, source_language, storage_source):
        source_input = SourceInput(
            source_url=source_url,
            filter=filter if filter is not None else None,
            language=source_language if source_language is not None else None,
            storage_source=storage_source if storage_source is not None else None,
        )
        return source_input
    
    def create_target_input(self, target_url, target_language_code, category, glossaries, storage_source):
        target_input = TargetInput(
            target_url=target_url,
            language=target_language_code,
            category=category if category is not None else None,
            glossaries=glossaries if glossaries is not None else None,
            storage_source=storage_source if storage_source is not None else None,
        )
        return target_input
    
    def create_batch_request(self, source_input, target_inputs):
        return BatchRequest(source= source_input, targets=target_inputs)
    
    def get_start_translation_details_mulitple_docs(self, storage_name):
        documents = [
            TestDocument("Document1.txt", "First English test file"),
            TestDocument("File2.txt", "Second English test file")
        ]        
        source_url = self.create_source_container(documents=documents, storage_name=storage_name)
        source_input = self.create_source_input(source_url=source_url, filter=None, source_language=None, storage_source=None)

        target_url = self.create_target_container(documents=None, storage_name=storage_name)
        target_language_code = "fr"
        target_input = self.create_target_input(target_url=target_url, target_language_code=target_language_code, category=None, glossaries=None, storage_source=None)
        target_inputs = [target_input]        
        
        batch_request = self.create_batch_request(source_input=source_input, target_inputs=target_inputs)
        batch_requests = [batch_request]
        return StartTranslationDetails(inputs=batch_requests)
    
class SingleDocumentTranslationTest(AzureRecordedTestCase):
    def create_client(self, endpoint):
        credential = self.get_credential(SingleDocumentTranslationClient)
        return self.create_client_from_credential(
            SingleDocumentTranslationClient,
            credential=credential,
            endpoint=endpoint,
        )
    