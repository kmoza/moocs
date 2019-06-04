def increment_func(var):
    temp = 0
    while temp < var:
        yield temp
        temp = temp + 1

def test_increment_func():
    for item in increment_func(10):
        print item

test_increment_func()

