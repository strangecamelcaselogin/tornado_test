from functools import wraps
from voluptuous import Schema, MultipleInvalid, PREVENT_EXTRA


def dvalidate(schema, required=False, extra=PREVENT_EXTRA):
    assert isinstance(schema, dict)
    schema = Schema(schema, required, extra)

    def true_decorator(fun):
        @wraps(fun)
        def wrapper(_self, *args, **kwargs):
            try:
                schema(_self.args)
                result = fun(_self, *args, **kwargs)
            except MultipleInvalid as e:
                return _self.write('wrong request args: ' + str(e))

            return result

        return wrapper

    return true_decorator


def mvalidate(required=False, extra=PREVENT_EXTRA, **schema):
    schema = Schema(schema, required, extra)
    return schema