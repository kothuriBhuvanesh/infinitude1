class student():
    desgination = "software"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def test(self):
        print("student name is" + self.name, "age is" + self.age, "designation is" + self.desgination)

obj = student("bhuvanesh","23")
obj2 = student("sai","24")
obj.test()
obj2.test()

