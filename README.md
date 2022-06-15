# Receipt Parser

## Overview
This module provides functionality for parsing receipts.
Receipts are obtained with using the app provided by Federal Tax Authority [IOS](https://apps.apple.com/ru/app/%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D1%87%D0%B5%D0%BA%D0%BE%D0%B2-%D1%84%D0%BD%D1%81-%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B8/id1169353005), [Android](https://play.google.com/store/apps/details?id=ru.fns.billchecker&hl=ru&gl=US)

## Usage

```python
import json

import receipt_parser as rp

with open("receipt_file.json") as f:
    raw_receipt = json.load(f)
    r = rp.parse_receipt(raw_receipt)
    print(r)
```
