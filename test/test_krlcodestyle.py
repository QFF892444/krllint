#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import filecmp
from unittest import TestCase, main

from krlcodestyle import _create_arg_parser, StyleChecker

class TestKrlCodeStyle(TestCase):
    def test_integration(self):
        test_dir = os.path.dirname(__file__)
        dirty_file = os.path.relpath(os.path.join(test_dir, "dirty.src"), os.getcwd())
        clean_file = os.path.relpath(os.path.join(test_dir, "clean.src"), os.getcwd())
        test_file = os.path.relpath(os.path.join(test_dir, "test.src"), os.getcwd())

        if os.path.exists(test_file):
            os.remove(test_file)
        shutil.copyfile(dirty_file, test_file)

        options = _create_arg_parser().parse_args(["--fix", test_file])
        style_checker = StyleChecker(options)
        style_checker.check()

        self.assertTrue(filecmp.cmp(test_file, clean_file))


if __name__ == "__main__":
    main()