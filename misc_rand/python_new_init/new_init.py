class A(object):
    def __new__(cls):
        return object.__new__(cls)
    
    def __init__(self):
        self.instance_method()

    def instance_method(self):
            print("success")

newA = A()