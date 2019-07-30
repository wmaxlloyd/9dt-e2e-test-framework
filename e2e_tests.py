import unittest
import xmlrunner

test_results_directory = 'artifacts/test-reporters'
test_runner=xmlrunner.XMLTestRunner(output=test_results_directory)

tests = unittest.TestLoader().discover("src/e2e_tests", pattern="*.py")
results = test_runner.run(tests)