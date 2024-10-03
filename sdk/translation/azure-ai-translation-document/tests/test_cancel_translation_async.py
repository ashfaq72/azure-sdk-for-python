# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from devtools_testutils.aio import recorded_by_proxy_async
from preparer import DocumentTranslationPreparer
from tests.asynctestcase import DocumentTranslationTestAsync
from tests.testHelper import TestHelper


class TestCancelTranslationAsync(DocumentTranslationTestAsync, TestHelper):

    @DocumentTranslationPreparer()
    @recorded_by_proxy_async
    async def test_cancel_translation_async(self, **kwargs):
        """
        some notes (test sporadically failing):
        1. use a large number of translations
            - because when running tests the translation sometimes finishes with status 'Succeeded'
              before we call the 'cancel' endpoint!
        2. wait sometime after calling 'cancel' and before calling 'get status'
            - in order for the cancel status to propagate
        """
        endpoint = kwargs.get("document_translation_endpoint")
        storage_name = kwargs.get("document_translation_storage_name")
        async_client = self.create_async_client(endpoint)

        batch_requests = self.get_start_translation_details_mulitple_docs(storage_name)
        poller, translation_id = await async_client.begin_start_translation(batch_requests)

        # Cancel Translation
        await async_client.cancel_translation(translation_id)

        # Get Translation Status
        translation_status = await async_client.get_translation_status(translation_id)
        assert translation_id == translation_status.id
        status = str(translation_status.status.value)
        assert status in ["Cancelled", "Cancelling", "NotStarted"]
