@Test.describe("Fixed tests")
def fixed_tests():
    Test.assert_equals(fibonacci(70), 190392490709135)
    Test.assert_equals(fibonacci(60), 1548008755920)
    Test.assert_equals(fibonacci(50), 12586269025)
    
MAX_FIB = 1000
MY_FIB_SEQ = [0]
a, b = 0, 1
for _ in range(MAX_FIB +1):
    a, b = b, a+b
    MY_FIB_SEQ.append(a)

from random import randint

@Test.describe("Random tests up to n = %s" % MAX_FIB)
def random_tests():
    for _ in range(20):
        n = randint(1, MAX_FIB)
        @Test.it("Testing fibonacci(%s)" % n)
        def single_test():
            Test.assert_equals(fibonacci(n), MY_FIB_SEQ[n])

@Test.describe("Performance tests")
def perf_tests():
    for tests in [10**3, 10**4, 10**5, 10**6]:
        @Test.it("%s consecutive random test" % tests)
        def single_test():
            for _ in range(tests):
                n = randint(1, MAX_FIB)
                if fibonacci(n) != MY_FIB_SEQ[n]:
                    Test.assert_equals(fibonacci(n), MY_FIB_SEQ[n])
            Test.assert_equals(True, True)
