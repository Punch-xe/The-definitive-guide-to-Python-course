# x = float('2.1')
# print(x)
#
# help(float)


def avg(a, b, c, /):
    return (a + b + c) / 3


print(avg(1, 2, 3))


# print(avg(a=1, b=2, c=3))

def assert_equal(left, right, /, fail_message=' '):
    return (left == right, fail_message)


assert_equal(1, 1)
assert_equal(1, 1, fail_message='left not equals right')


# assert_equal(left=1, right=1)


def copy(*, sourse, destination, overwrite):
    print(f'copying from {sourse} to {destination} with overwrite = {overwrite}')


copy(sourse='C\\tmp\\file1.txt', destination='C\\tmp\\copy.txt', overwrite=True)


def copy(sourse, destination, /, *, overwrite):
    print(f'copying from {sourse} to {destination} with overwrite = {overwrite}')


copy('C\\tmp\\file1.txt', 'C\\tmp\\copy.txt', overwrite=True)
