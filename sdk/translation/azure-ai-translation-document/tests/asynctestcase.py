# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from devtools_testutils import AzureRecordedTestCase
from azure.ai.translation.document.aio import DocumentTranslationClient, SingleDocumentTranslationClient


class DocumentTranslationTestAsync(AzureRecordedTestCase):
    def create_async_client(self, endpoint):
        credential = self.get_credential(DocumentTranslationClient, is_async=True)
        return self.create_client_from_credential(
            DocumentTranslationClient,
            credential=credential,
            endpoint=endpoint,
        )


class SingleDocumentTranslationTestAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(SingleDocumentTranslationClient, is_async=True)
        return self.create_client_from_credential(
            SingleDocumentTranslationClient,
            credential=credential,
            endpoint=endpoint,
        )
