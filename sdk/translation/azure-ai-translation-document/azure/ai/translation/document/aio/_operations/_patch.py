# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
import json
from typing import IO, Any, List, Optional, Tuple, Union, cast, overload
from azure.ai.translation.document.models import _models
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ._operations import JSON, ClsType, DocumentTranslationClientOperationsMixin as GeneratedDTClientOps


class DocumentTranslationClientOperationsMixin(GeneratedDTClientOps):
    @overload
    async def begin_start_translation(
        self, body: _models.StartTranslationDetails, *, content_type: str = "application/json", **kwargs: Any
    ) -> Tuple[AsyncLROPoller[None], str]:
        """Submit a document translation request to the Document Translation service.

        Use this API to submit a bulk (batch) translation request to the Document
        Translation service.
        Each request can contain multiple documents and must
        contain a source and destination container for each document.

        The
        prefix and suffix filter (if supplied) are used to filter folders. The prefix
        is applied to the subpath after the container name.

        Glossaries /
        Translation memory can be included in the request and are applied by the
        service when the document is translated.

        If the glossary is
        invalid or unreachable during translation, an error is indicated in the
        document status.
        If a file with the same name already exists at the
        destination, it will be overwritten. The targetUrl for each target language
        must be unique.

        :param body: Translation job submission batch request. Required.
        :type body: ~azure.ai.translation.document.models.StartTranslationDetails
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns None
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_start_translation(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> Tuple[AsyncLROPoller[None], str]:
        """Submit a document translation request to the Document Translation service.

        Use this API to submit a bulk (batch) translation request to the Document
        Translation service.
        Each request can contain multiple documents and must
        contain a source and destination container for each document.

        The
        prefix and suffix filter (if supplied) are used to filter folders. The prefix
        is applied to the subpath after the container name.

        Glossaries /
        Translation memory can be included in the request and are applied by the
        service when the document is translated.

        If the glossary is
        invalid or unreachable during translation, an error is indicated in the
        document status.
        If a file with the same name already exists at the
        destination, it will be overwritten. The targetUrl for each target language
        must be unique.

        :param body: Translation job submission batch request. Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns None
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_start_translation(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> Tuple[AsyncLROPoller[None], str]:
        """Submit a document translation request to the Document Translation service.

        Use this API to submit a bulk (batch) translation request to the Document
        Translation service.
        Each request can contain multiple documents and must
        contain a source and destination container for each document.

        The
        prefix and suffix filter (if supplied) are used to filter folders. The prefix
        is applied to the subpath after the container name.

        Glossaries /
        Translation memory can be included in the request and are applied by the
        service when the document is translated.

        If the glossary is
        invalid or unreachable during translation, an error is indicated in the
        document status.
        If a file with the same name already exists at the
        destination, it will be overwritten. The targetUrl for each target language
        must be unique.

        :param body: Translation job submission batch request. Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns None
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_start_translation(
        self, body: Union[_models.StartTranslationDetails, JSON, IO[bytes]], **kwargs: Any
    ) -> Tuple[AsyncLROPoller[None], str]:
        """Submit a document translation request to the Document Translation service.

        Use this API to submit a bulk (batch) translation request to the Document
        Translation service.
        Each request can contain multiple documents and must
        contain a source and destination container for each document.

        The
        prefix and suffix filter (if supplied) are used to filter folders. The prefix
        is applied to the subpath after the container name.

        Glossaries /
        Translation memory can be included in the request and are applied by the
        service when the document is translated.

        If the glossary is
        invalid or unreachable during translation, an error is indicated in the
        document status.
        If a file with the same name already exists at the
        destination, it will be overwritten. The targetUrl for each target language
        must be unique.

        :param body: Translation job submission batch request. Is one of the following types:
         StartTranslationDetails, JSON, IO[bytes] Required.
        :type body: ~azure.ai.translation.document.models.StartTranslationDetails or JSON or IO[bytes]
        :return: An instance of AsyncLROPoller that returns None
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._start_translation_initial(
                body=body, content_type=content_type, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs
            )
            await raw_result.http_response.read()  # type: ignore
        kwargs.pop("error_map", None)

        # get translation_id
        response_content = await raw_result.http_response.read()
        response_str = response_content.decode("utf-8")  # Decode and parse the response to get the id
        response_json = json.loads(response_str)
        translation_id = response_json["id"]  # Extract the id

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncLROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method), translation_id  # type: ignore


__all__: List[str] = [
    "DocumentTranslationClientOperationsMixin",
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
