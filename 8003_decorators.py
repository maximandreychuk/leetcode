

def validate_types(dict):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            if not isinstance(args[0].__class__, dict['name']) and not isinstance(args[1].__class__, dict['age']):
                    raise TypeError
            result = func(*args, **kwargs)
            return result
        return wrapper2
    return wrapper1

@validate_types({"name": str, "age": int})
def create_user(name, age):
    print(f"Создаем пользователя с именем {name} и возрастом {age}")

# create_user("Alice", 30)  # Должно работать
create_user("Bob", "25")