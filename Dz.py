class Parent1:
    def __init__(self, attr1_parent1):
        self.attr1_parent1 = attr1_parent1

    def method1_parent1(self):
        print("Method from Parent1")


class Parent2:
    def __init__(self, attr2_parent2):
        self.attr2_parent2 = attr2_parent2

    def method2_parent2(self):
        print("Method from Parent2")
class Super(Parent1, Parent2):
    def __init__(self):
        def method_super(self):
            super().method1_parent1()
            super().method2_parent2()