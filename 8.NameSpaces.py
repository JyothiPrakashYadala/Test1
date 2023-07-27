'''# Local and Global
def outer():
    x=500
    print(f'local variable x:{x}')
x=300
outer()
print(f'Global variable x:{x}')

# Global as local
def outer():
    print(f'Local variable x:{x}')
x=300
outer()
print(f'Global variable x:{x}')

# Local as Global
def outer():
    global x
    x=500
    print(f'Local variable x:{x}')
x=300
outer()
print(f'Global variable x:{x}')

# Global as Local and Non-Local
def outer():
    print(f'Local variable x:{x}')
    def inner():
        print(f'Non-Local variable x:{x}')
    inner()
x=300
outer()
print(f'Global variable x:{x}')

# Local as Global and Non-Local
def outer():
    global x
    x=500
    print(f'Local variable x:{x}')
    def inner():
        print(f'Non-Local variable x:{x}')
    inner()
x=300
outer()
print(f'Global variable x:{x}')

# Non-Local as Local
def outer():
    x=300
    print(f'Local Space x:{x}')
    def inner():
        nonlocal x
        x=200
        print(f'Non-Local Space x:{x}')
    inner()
    print(f'Local Space x:{x}')
x=500
outer()
print(f'Global Space x:{x}')'''

# Non-Local as Global
def outer():
    x=300
    print(f'Local Space x:{x}')
    def inner():
        global x
        x=200
        print(f'Non-Local Space x:{x}')
    inner()
    print(f'Local Space x:{x}')
x=500
outer()
print(f'Global Space x:{x}')