# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from devtools_testutils import recorded_by_proxy
from preparer import DocumentTranslationPreparer
from tests.testcase import DocumentTranslationTest
from tests.testHelper import TestHelper

class TestDocumentStatus(DocumentTranslationTest, TestHelper):
    @DocumentTranslationPreparer()
    @recorded_by_proxy
    def test_documents_status(self, **kwargs):
        endpoint = kwargs.get("document_translation_endpoint")
        storage_name = kwargs.get("document_translation_storage_name")
        client = self.create_client(endpoint)

        target_language = "fr"
        batch_requests = self.get_start_translation_details_single_doc(storage_name=storage_name, target_language_code=target_language)
        poller, translation_id = client.begin_start_translation(batch_requests)
        
        # Make sure the Translation Status is not "NotStarted"
        while True:
            translation_status = client.get_translation_status(translation_id) 
            if translation_status.status.value not in ["NotStarted"]:                
                break

        # get doc statuses
        doc_statuses = client.get_documents_status(id=translation_id)
        assert doc_statuses is not None

         # get first doc
        first_doc = next(doc_statuses)
        assert first_doc.id is not None

        # get doc details
        doc_status = client.get_document_status(id=translation_id, document_id=first_doc.id)
        self._validate_doc_status(doc_status, target_language)
