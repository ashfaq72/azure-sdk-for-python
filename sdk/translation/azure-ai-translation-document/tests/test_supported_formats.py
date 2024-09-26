
from devtools_testutils import recorded_by_proxy
from preparer import DocumentTranslationPreparer
from azure.ai.translation.document.models import FileFormatType
from tests.testcase import DocumentTranslationTest

class TestSupportedFormats(DocumentTranslationTest):
    @DocumentTranslationPreparer()
    @recorded_by_proxy
    def test_supported_document_formats(self, **kwargs):
        endpoint = kwargs.get("document_translation_endpoint")
        client = self.create_client(endpoint)
        supported_doc_formats = client.get_supported_formats(type=FileFormatType.DOCUMENT)
        assert supported_doc_formats is not None
        # validate
        for doc_format in supported_doc_formats.value:
            self._validate_format(doc_format)

    @DocumentTranslationPreparer()
    @recorded_by_proxy
    def test_supported_glossary_formats(self, **kwargs):
        endpoint = kwargs.get("document_translation_endpoint")
        client = self.create_client(endpoint)
        supported_glossary_formats = client.get_supported_formats(type=FileFormatType.GLOSSARY)
        assert supported_glossary_formats is not None
        # validate
        for doc_format in supported_glossary_formats.value:
            self._validate_format(doc_format)

    def _validate_format(self, format):
        assert format.format is not None
        assert format.file_extensions is not None
        assert format.content_types is not None
