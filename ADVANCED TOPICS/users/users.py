import json

def get_users():
    with open("users.json", encoding="utf8") as f:
        return json.load(f)

class Users:
    def get(self):
        data=get_users()
        return [u for u in data]
user=Users()
print(user.get())

class Userdetails:
    def get(self,**kwargs):
        id=kwargs.get("id")
        data = get_users()
        return [d for d in data if d["id"]==id]
ud=  Userdetails()
print(ud.get(id=10))
