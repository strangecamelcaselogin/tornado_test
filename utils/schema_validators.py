import ujson
from functools import wraps
from voluptuous import Schema, MultipleInvalid, PREVENT_EXTRA


def construct_response(exception):
    """
    :param exception: MultipleInvalid exception
    :return: json

    Делает json с ошибками из MultipleInvalid exception.
    """
    result = []
    if isinstance(exception, MultipleInvalid):
        for e in exception.errors:
            result.append({
                'msg': str(e),
                'error_type': e.error_type
            })

    return ujson.dumps(result)


def dvalidate(schema, required=False, extra=PREVENT_EXTRA):
    """
    :param schema: dict в формате voluptuous
    :param required: если True, все параметры схемы оязательны
    :param extra: стратегия поведения в случае нехватки или избытка параметров
    :return: результат функции если параметры валидны, иначе сообщение об ошибке

    декоратор для валидации параметров у tornado хендлеров

    использование:
        class SomeTornadoHandler:
            @dvalidate({'a': int, 'b': str})
            def get(self):
                self.write('success')

    """
    assert isinstance(schema, dict)
    schema = Schema(schema, required, extra)

    def true_decorator(fun):
        @wraps(fun)
        def wrapper(_self, *args, **kwargs):
            try:
                schema(_self.args)
                result = fun(_self, *args, **kwargs)
                return result

            except MultipleInvalid as e:
                _self.write(construct_response(e))

        return wrapper

    return true_decorator


def mvalidate(required=False, extra=PREVENT_EXTRA, **schema):
    """
    параметры как у dvalidate

    ручной вариант dvalidate
    """
    schema = Schema(schema, required, extra)
    return schema
