def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) != len(expected_types):
                raise TypeError(f"Ожидалось {len(expected_types)} аргументов, получено {len(args)}")
            
            for i, (arg, expected) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"Аргумент {i+1} ({arg}) должен быть {expected.__name__}, "
                        f"а получен {type(arg).__name__}"
                    )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))