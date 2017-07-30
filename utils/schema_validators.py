from functools import wraps
from voluptuous import Schema, MultipleInvalid


def dvalidate(schema, **params):
    assert isinstance(schema, dict)
    schema = Schema(schema, params)

    def true_decorator(fun):
        @wraps(fun)
        def wrapper(_self, *args, **kwargs):
            try:
                schema(_self.args)
                result = fun(_self, *args, **kwargs)
            except Exception as e:
                return _self.write('wrong request args: ' + str(e))

            return result

        return wrapper

    return true_decorator


def mvalidate(**kwargs):
    schema = Schema(kwargs)
    return schema