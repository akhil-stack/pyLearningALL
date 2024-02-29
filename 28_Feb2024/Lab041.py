# Single inheritance
# Multiple Inheritance
# Multi leve Inheritance
# Hybrid Inheritance
# Herirachical Inheritance
from pyclbr import Class


class Grandparent:
    def grand_parent_method(self):
        return "Grandparent's Method"


class parent(Grandparent):
    def Parent_method(self):
        return "Parent Method"


class Child(parent):
    def Child_method(self):
        return "Child method"


child = Child()
print(child.Parent_method())
print(child.grand_parent_method())
print(child.Child_method())
