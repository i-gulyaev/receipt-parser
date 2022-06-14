import json
import os
from distutils import dir_util

import pytest

from receipt_parser import parse_receipt


@pytest.fixture
def datadir(tmp_path, request):
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmp_path))

    return tmp_path


def test_parser_v1(datadir):
    with open(datadir / "receipt_v1.json") as f:
        result = parse_receipt(json.load(f))
        assert len(result["items"]) == 1
