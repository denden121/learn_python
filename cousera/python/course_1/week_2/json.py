import json
from functools import wraps


def to_json(fun):
    @wraps(fun)
    def wrapped(*args, **kwargs):
        return json.dumps(fun(*args, **kwargs))
    return wrapped

