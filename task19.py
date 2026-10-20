def cache(func):
    cache_dict = {}
    
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        
        if key in cache_dict:
            print(f"Возврат из кэша для {args}")
            return cache_dict[key]
        
        print(f"Вычисление для {args}")
        result = func(*args, **kwargs)
        
        cache_dict[key] = result
        return result
    
    return wrapper

@cache
def slow_add(a, b):
    return a + b

print(slow_add(2, 3))  
print(slow_add(2, 3))  
print(slow_add(5, 5)) 