class Ide:
    def functionalities(self):
        func=['create_files','rename','delete']
        return func
class PyCharm(Ide):
    def functionalities(self):
        func=super().functionalities()
        func.append("execute")
        func.append("debug")
        return func

class Visualstudio(Ide):
    def functionalities(self):
        func=super().functionalities()
        func.append("formatting")
        func.append("yuegfyg")
        return func
py=PyCharm()
print(py.functionalities())

vsc=Visualstudio()
print(vsc.functionalities())