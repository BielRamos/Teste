
import unittest


class MyFun:
    def fun(self, n):
        return n + 1

class MyTest(unittest.TestCase):
    def test(self):
        obj = MyFun()
        self.assertEqual(obj.fun(3), 4)


if __name__ == '__main__' :
    unittest.main()

