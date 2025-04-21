from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_list = []  # List to store cache entries as tuples

    def inner(*args, **kwargs) -> Any:
        # Convert kwargs to a sorted tuple of (key, value) pairs to make them hashable and consistent
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = (
        args, kwargs_tuple)  # Use (args, sorted(kwargs)) as the key

        # Iterate through cache and look for a matching cache key
        for cached_key, result in cache_list:
            if cached_key == cache_key:
                print("Getting from cache")
                return result

        # If not found in cache, calculate the result
        function_result = func(*args, **kwargs)
        cache_list.append(
            (cache_key, function_result))  # Store the cache entry as a tuple
        print("Calculating new result")
        return function_result

    return inner
