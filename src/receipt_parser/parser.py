from datetime import datetime
from typing import Any, Dict, List


def get_version(data: Any) -> int:
    if type(data) is list:
        return 2
    else:
        return 1


def parse_item(data: Any) -> Dict[str, Any]:
    return {
        "name": data["name"],
        "price": int(data["price"]) / 100.0,
        "sum": int(data["sum"]) / 100.0,
        "quantity": float(data["quantity"]),
    }


def parse_receipt_v1(data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "seller": data["user"],
        "sum": int(data["totalSum"]) / 100.0,
        "date": datetime.strptime(data["localDateTime"], "%Y-%m-%dT%H:%M"),
        "items": [parse_item(item) for item in data["items"]],
    }


def parse_receipt_v2(data: List[Any]) -> Dict[str, Any]:
    data0 = data[0]

    items = data0["ticket"]["document"]["receipt"]["items"]
    return {
        "seller": data0["seller"]["name"],
        "sum": int(data0["query"]["sum"]) / 100.0,
        "date": datetime.strptime(data0["query"]["date"], "%Y-%m-%dT%H:%M"),
        "items": [parse_item(item) for item in items],
    }


def parse_receipt(data: Any) -> Dict[str, Any]:
    parser = {
        1: parse_receipt_v1,
        2: parse_receipt_v2,
    }

    return parser[get_version(data)](data)
