# -*- coding: utf-8 -*-

from unittest import TestCase

import church._common as common
from church.church import File


class FileTestCase(TestCase):
    def setUp(self):
        self.file = File()

    def tearDown(self):
        del self.file

    def test_extension(self):
        text = self.file.extension()
        self.assertIn(text, common.EXTENSIONS['text'])
