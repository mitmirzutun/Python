class Error:
    def bmi():
        print("A person is not in a optimal bmi state")
        return "BMI not given"
class Person:
    def __init__(self, weight, height, age):
        self.weight = float(weight)
        self.height = height,
        age = age if age > 0 else 0
        self.age = age if age < 108 else 107
        self.bmi = self.weight/height ** 2 if self.weight/height ** 2 < 30 and self.weight/height ** 2 > 10 else Error.bmi()
    def bmi(self):
        if self.bmi == "BMI not given": print("Person cannot live in this state")
        else: return self.bmi
