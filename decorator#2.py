def decor(name1, name2):
    print("args decorator: ", name1, name2)
    def my_decorator(function):
        def wrap(*args):
            print("args function: ", *args)
            return function(*args)
        return wrap
    return my_decorator


@decor("Sasha", "Masha")
def func(first_name, second_name):
    return first_name, second_name


func("Vasa", "Petya")

