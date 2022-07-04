def admin_access(func):
    def wrapper(name,pin):
        if name == 'admin':
            return func(name,pin)
        else:
            raise Exception("ADMIN CAN ONLY ACCESS")

    return wrapper
@admin_access
def changepin(name,pin):
    mypin=pin
    return mypin
print(changepin('admin',8566))