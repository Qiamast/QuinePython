import inspect

def Say_Hello(name):
    return(f"Hi {name}")

Say_Hello("Qiamast")

# Get Source Code 
frame = inspect.currentframe()
print(inspect.getsource(frame))


# thank you for watching :) @Qiamast
