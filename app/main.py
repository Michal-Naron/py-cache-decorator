from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_list = []  # prototype [[<args>, value]]

    def inner(*args, **kwargs) -> Any:
        for i in cache_list:
            if i[0] in args or i[0] in kwargs:
                print("Getting from cache")
                return i[1]
        function_result = func(*args, **kwargs)
        cache_list.append([*args, function_result])  # missing kwargs
        print("Calculating new result")
        return function_result

    return inner
