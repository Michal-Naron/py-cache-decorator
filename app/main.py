from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_list = []

    def inner(*args, **kwargs) -> Any:
        for cached_args, cached_kwargs, result in cache_list:
            if cached_args == args and cached_kwargs == kwargs:
                print("Getting from cache")
                return result
        function_result = func(*args, **kwargs)
        cache_list.append([args, kwargs, function_result])
        print("Calculating new result")
        return function_result

    return inner
