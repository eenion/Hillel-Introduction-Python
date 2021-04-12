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


    # def test_add_not_eq(self):
    #     print('\ntest_add: ')
    #     self.assertNotEqual(self.calculator.add(4, 7), 10)

    # def test_add_1(self):
    #     print('\ntest_add: ')
    #     calc_response = self.calculator.add(4, 7)
    #     print('calc_response: ', calc_response)
    #     expactation = 11
    #     print('expactation: ', expactation)
    #     self.assertEqual(calc_response, expactation)

    # def test_subtract(self):
    #     print('\ntest_subtract: ')
    #     self.assertEqual(5, self.calculator.subtract(10, 5))

    # def test_multiply(self):
    #     print('\ntest_multiply: ')
    #     self.assertEqual(self.calculator.multiply(3, 7), 21)

    # def test_divide(self):
    #     print('\ntest_divide: ')
    #     self.assertEqual(self.calculator.divide(10, 2), 5)

    # def test_divide_on_zero(self):
    #     print('\ntest_divide_zero: ')
    #     self.assertEqual(self.calculator.divide(10, 0), 'infinity')
    #     self.assertRaises(ZeroDivisionError)

    # def test_divide_zero(self):
    #     print('\ntest_divide_zero: ')
    #     self.assertEqual(self.calculator.divide(0, 10), 0)
