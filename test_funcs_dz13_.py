import unittest
import dz12_funcs


class TestFuncs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"setUpClass\n{'='*50}")
    
    def setUp(self):
        print(f"\n{'-'*50}\nstart the test")

    def tearDown(self):
        print(f"\nend the test")

    @classmethod
    def tearDownClass(cls):
        print(f"\n{'='*50}\nFifnish all tests!")

    def test_to_even(self):
        print('\ntest_to_even: --> ')
        self.assertEqual(dz12_funcs.filter_to_even_list([2,3,4,5]), [2,4])
    
    def test_to_even_negative(self):
        print('\ntest_to_even_negative --> ')
        self.assertNotEqual(dz12_funcs.filter_to_even_list([2,3,4,5]), [3,5])

    def test_to_odd(self):
        print('\ntest_to_odd: --> ')
        self.assertEqual(dz12_funcs.filter_to_odd_list([2,3,4,5]), [3,5])

    def test_to_odd_negative(self):
        print('\ntest_to_odd_negative --> ')
        self.assertNotEqual(dz12_funcs.filter_to_odd_list([2,3,4,5]), [2,4])    

    def test_zip(self):
        print('\ntest_zip: --> ')
        self.assertEqual(dz12_funcs.zip_some_lists([2,],[2,],[2,]),[(2,2,2)])

    def test_zip_negative(self):
        print('\ntest_zip_negative: --> ')
        self.assertNotEqual(dz12_funcs.zip_some_lists([2,],[2,],[2,]),[2,2,2])

    def test_sum_tuples(self):
        print('\ntest_sum_tuples: --> ')
        self.assertEqual(dz12_funcs.sum_tuples_in_list([(1, 1, 1), (2, 2, 2)]), [3, 6])

    def test_sum_tuples_negative(self):
        print('\ntest_sum_tuples_negative: --> ')
        self.assertNotEqual(dz12_funcs.sum_tuples_in_list([(1, 1, 1), (2, 2, 2)]), [(3, 3, 3)])

