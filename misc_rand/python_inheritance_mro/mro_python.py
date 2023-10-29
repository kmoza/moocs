class ParentOne:
    def foo(self):
        print("Parent foo is called")

class ParentTwo:
    def foo(self):
        print("ParentTwo foo is called")

class Child(ParentOne, ParentTwo):
    def call_parent_two_foo(self):
        super(ParentOne, self).foo()

    def call_parent_foo(self):
        super(ParentTwo, self).foo()

    def call_super_foo(self):
        super(Child, self).foo()

    def foo(self):
        print("Child foo is called")

if __name__ == "__main__":
    child = Child()
    child.foo()
    child.call_super_foo()
    child.call_parent_two_foo()
    print(Child.__mro__)
