# class Students:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         self.money = 2000
#         print("I am alive")
#
# stepan = Student()
# print(stepan.height)
# print(stepan.money)
# stepan.money -= 500
# print(stepan.money)
class Students:
    amount_of_students = 0
    def __init__(self,height = 160):
        self.height = height
        self.money = 2000;
        Student.amount_of_students += 1
    def printHeight(self):
        print(self,height)
    def subMoney(self,countMoney):
        self.money -= countMoney
        Student.printCountMoney(self)
     def printCointMoney(self):
         print(self.money)
stepan = Student(height=180)
print(stepan.height)
stepan.printCountMoney()
print("-"*20)
katrin = Student(height=170)
print("Katrin",katrin.height,katrin.amount_of_students)
katrin.printCountMoney()
katrin.subMoney(200)
katrin.printCountMoney()
print("-"*20)
Oleh = Student()
Oleh.subMoney()
print("Oleh",Oleh.height,Oleh.amount_of_students)