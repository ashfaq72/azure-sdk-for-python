# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


class TestDocument:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        self._content = content
