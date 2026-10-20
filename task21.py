import time

def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        
        result = func(*args, **kwargs)
        
        end = time.time()
        
        elapsed_ms = (end - start) * 1000
        print(f"Функция {func.__name__} выполнялась {elapsed_ms:.2f} мс")
        
        return result
    return wrapper

@timing
def slow_function():
    time.sleep(0.5)

slow_function()