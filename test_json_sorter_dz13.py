import unittest
import os.path
from dz14__json_sorter_to_oop import JsonSorter


class TestJsonSorter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"setUpClass\n{'='*50}")
        cls.jsonsorter = JsonSorter()

    def test_deserialize(self):
        print('\ntest_deserialize: ')
        self.assertEqual(type(self.jsonsorter.open_json_and_make_dict()), type({1:1,}))

    def test_serialize(self):
        print('\ntest_serailize: ')
        self.assertEqual(True, os.path.exists('HW_result.json'))

    def test_sort_of_dict(self):
        print('\ntest_sort_of_dict: ')
        test_dict = {"employee": 
                    [{"id": 33,
                      "firstName": "Tom",
                      "lastName": "Cruise",
                      "salary": 1.3},
                    ]}                    
        self.assertEqual(self.jsonsorter.dict_sort_by_type(test_dict)["employee"]['Tom Cruise']['float'], [1.3])
        
    @classmethod
    def tearDownClass(cls):
        print("Тестирование завершено")
        
           
    
    