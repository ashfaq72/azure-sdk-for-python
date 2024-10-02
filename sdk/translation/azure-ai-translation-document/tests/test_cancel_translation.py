# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from devtools_testutils import recorded_by_proxy
from preparer import DocumentTranslationPreparer
from tests.testcase import DocumentTranslationTest
from tests.testHelper import TestHelper


class TestCancelTranslation(DocumentTranslationTest, TestHelper):
    @DocumentTranslationPreparer()
    @recorded_by_proxy
    def test_cancel_translation(self, **kwargs):
        endpoint = kwargs.get("document_translation_endpoint")
        storage_name = kwargs.get("document_translation_storage_name")
        client = self.create_client(endpoint)

        batch_requests = self.get_start_translation_details_mulitple_docs(storage_name)
        poller, translation_id = client.begin_start_translation(batch_requests)

        # Cancel Translation
        client.cancel_translation(translation_id)

        # Get Translation Status
        translation_status = client.get_translation_status(translation_id)
        assert translation_id == translation_status.id
        status = str(translation_status.status.value)
        assert status in ["Cancelled", "Cancelling", "NotStarted"]
