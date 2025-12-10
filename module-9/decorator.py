def add_sprickles(func):
    def wrapper(*args, **kwargs):
        print("*You add some sprinkles*")
        return func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You have added fudge*")
        return func(*args, **kwargs)
    return wrapper


@add_sprickles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream ")
    
get_ice_cream("chocolate")