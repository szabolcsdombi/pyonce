import sys
import traceback
from typing import Any

counter = {}


def make_key():
    return tuple((id(a.f_code), b) for a, b in traceback.walk_stack(sys._getframe().f_back.f_back))


def once(every: int = 0, key: Any = None) -> bool:
    if key is None:
        key = make_key()
    value = counter.get(key)
    if not value:
        counter[key] = every - 1
        return True
    counter[key] = value - 1
    return False
