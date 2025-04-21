from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dictionary = {}

    def inner(*args, **kwargs) -> Any:

        cache_key = (id(func), args, tuple(sorted(kwargs.items())))

        if cache_dictionary.get(cache_key, False):
            print("Getting from cache")
            return cache_dictionary[cache_key]

        function_result = func(*args, **kwargs)
        cache_dictionary[cache_key] = function_result
        print("Calculating new result")
        return function_result

    return inner
