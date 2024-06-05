import functools
import json


def jsonify(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return inner


@jsonify
def make_user(id, live, options):
    return {"id": id, "live": live, "options": options}


print(make_user(4, False, None))
