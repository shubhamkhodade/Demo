import unittest
from unittest.suite import TestSuite

from tests.test_1_compare_mobiles import TestOne
from tests.test_2_price_range import TestTwo

if __name__ == "__main__":

	# create the suite from the test classes
    suite = TestSuite()
    # load the tests
    tests = unittest.TestLoader()

	# add the tests to the suite
    suite.addTests(tests.loadTestsFromTestCase(TestOne))
    suite.addTests(tests.loadTestsFromTestCase(TestTwo))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)