# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from devtools_testutils import AzureRecordedTestCase
from azure.ai.translation.document import DocumentTranslationClient, SingleDocumentTranslationClient


class DocumentTranslationTest(AzureRecordedTestCase):
    def create_client(self, endpoint):
        credential = self.get_credential(DocumentTranslationClient)
        return self.create_client_from_credential(
            DocumentTranslationClient,
            credential=credential,
            endpoint=endpoint,
        )


class SingleDocumentTranslationTest(AzureRecordedTestCase):
    def create_client(self, endpoint):
        credential = self.get_credential(SingleDocumentTranslationClient)
        return self.create_client_from_credential(
            SingleDocumentTranslationClient,
            credential=credential,
            endpoint=endpoint,
        )
