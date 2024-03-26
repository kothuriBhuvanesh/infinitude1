class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def test(self):
        print("student name is" + self.name, "age is " + self.age)

obj = student("bhuvanesh", "26")
obj.test()
