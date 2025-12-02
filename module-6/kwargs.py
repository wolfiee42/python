# kwargs

def address (**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

address(state="dhaka", region="dhaka", area="kuril", house="torongo")