import json
import os
from datetime import datetime
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
    with open(datadir / "receipt_v1.json") as a, open(
        datadir / "receipt_v1_expected.json"
    ) as e:
        result = parse_receipt(json.load(a))
        assert len(result["items"]) == 1

        expected = json.load(e)

        for key, value in expected.items():
            assert key in result
            if type(result[key]) == datetime:
                assert expected[key] == result[key].isoformat()
            else:
                assert expected[key] == result[key]


def test_parser_v2(datadir):
    with open(datadir / "receipt_v2.json") as a, open(
        datadir / "receipt_v2_expected.json"
    ) as e:
        result = parse_receipt(json.load(a))
        assert len(result["items"]) == 8

        expected = json.load(e)

        for key, value in expected.items():
            assert key in result
            if type(result[key]) == datetime:
                assert expected[key] == result[key].isoformat()
            else:
                assert expected[key] == result[key]
