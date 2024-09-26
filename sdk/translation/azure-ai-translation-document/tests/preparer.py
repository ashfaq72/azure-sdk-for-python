# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from azure.ai.translation.document import DocumentTranslationClient, SingleDocumentTranslationClient
from devtools_testutils import EnvironmentVariableLoader
import functools

DocumentTranslationPreparer = functools.partial(
    EnvironmentVariableLoader,
    "translation",
    document_translation_endpoint="https://fakeendpoint.cognitiveservices.azure.com",
    document_translation_storage_name="redacted",    
)

SingleDocumentTranslationPreparer = functools.partial(
    EnvironmentVariableLoader,
    "translation",
    document_translation_endpoint="https://fakeendpoint.cognitiveservices.azure.com",
)
