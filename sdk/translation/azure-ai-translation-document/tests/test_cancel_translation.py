# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from devtools_testutils import recorded_by_proxy
from preparer import DocumentTranslationPreparer
from tests.testcase import DocumentTranslationTest

class TestCancelTranslation(DocumentTranslationTest):
    @DocumentTranslationPreparer()
    @recorded_by_proxy
    def test_cancel_translation(self, **kwargs):
        endpoint = kwargs.get("document_translation_endpoint")
        storage_name = kwargs.get("document_translation_storage_name")
        client = self.create_client(endpoint)

        batch_requests = self.get_start_translation_details_mulitple_docs(storage_name)  
        poller = client.begin_start_translation(batch_requests)
        result = poller.result()
        status = poller.status() 

        # Cancel Translation
        translation_id = poller.id
        client.cancel_translation(translation_id)

        # Get Translation Status
        translation_status = client.get_translation_status(translation_id)
        assert translation_id == translation_status.id
        status = str(translation_status.status)
        assert status in ["Cancelled", "Cancelling", "NotStarted"]
        