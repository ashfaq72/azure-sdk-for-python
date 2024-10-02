# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
from devtools_testutils import recorded_by_proxy
from preparer import SingleDocumentTranslationPreparer
from tests.testcase import SingleDocumentTranslationTest
from azure.ai.translation.document.models import DocumentTranslateContent
from tests.testHelper import TestHelper
from azure.core.exceptions import HttpResponseError


class TestSingleDocumentTranslation(SingleDocumentTranslationTest, TestHelper):
    @SingleDocumentTranslationPreparer()
    @recorded_by_proxy
    def test_translate_text_document(self, **kwargs):
        if self.is_live:  # running these tests in Live mode only
            endpoint = kwargs.get("document_translation_endpoint")
            client = self.create_client(endpoint)

            # prepare translation content
            document_translate_content = DocumentTranslateContent(document=self._get_document_content())
            target_languages = "hi"

            # Invoke document translation
            response_stream = client.document_translate(
                body=document_translate_content, target_language=target_languages
            )

            # Read the response from the iterator
            full_response_bytes = b"".join(response_stream)  # Combine all chunks

            # Optionally decode the bytes if it's text
            translated_response = full_response_bytes.decode("utf-8-sig")

            # validate response
            assert translated_response is not None

    @SingleDocumentTranslationPreparer()
    @recorded_by_proxy
    def test_translate_single_csv_glossary(self, **kwargs):
        if self.is_live:  # running these tests in Live mode only
            endpoint = kwargs.get("document_translation_endpoint")
            client = self.create_client(endpoint)

            # prepare translation content
            document_translate_content = DocumentTranslateContent(
                document=self._get_document_content(), glossary=self._get_single_glossary_content()
            )
            target_languages = "hi"

            # Invoke document translation
            response_stream = client.document_translate(
                body=document_translate_content, target_language=target_languages
            )

            # Read the response from the iterator
            full_response_bytes = b"".join(response_stream)  # Combine all chunks

            # Optionally decode the bytes if it's text
            translated_response = full_response_bytes.decode("utf-8-sig")

            # validate response
            assert translated_response is not None
            assert "test" in translated_response, "Glossary 'test' not found in translated response"

    @SingleDocumentTranslationPreparer()
    @recorded_by_proxy
    def test_translate_multiple_csv_glossary(self, **kwargs):
        if self.is_live:  # running these tests in Live mode only
            endpoint = kwargs.get("document_translation_endpoint")
            client = self.create_client(endpoint)

            # prepare translation content
            document_translate_content = DocumentTranslateContent(
                document=self._get_document_content(), glossary=self._get_multiple_glossary_contents()
            )
            target_languages = "hi"

            # Invoke document translation and validate exception
            try:
                client.document_translate(body=document_translate_content, target_language=target_languages)
            except HttpResponseError as e:
                assert e.status_code == 400
