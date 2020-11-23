import unittest
from find_square import *

class TestStringMethods(unittest.TestCase):

    def test_string_to_matrix(self):
        string_map = "..o"
        self.assertEqual(type(string_to_matrix(string_map)), list)

    def test_check_lines_length(self):
        string_map_valid = "..\n..\n"
        matrix_valid = string_to_matrix(string_map_valid)
        self.assertTrue(check_lines_length(matrix_valid))
        string_map_not_valid = "..\n...\n"
        matrix_not_valid = string_to_matrix(string_map_not_valid)
        self.assertFalse(check_lines_length(matrix_not_valid))
    
    def test_check_map_valid(self):
        map_1 = ""
        map_2 = "."
        map_3 = "..\n.u\n"
        map_4 = "..\n..\n"
        self.assertFalse(check_map_valid(map_1))
        self.assertFalse(check_map_valid(map_2))
        self.assertFalse(check_map_valid(map_3))
        self.assertTrue(check_map_valid(map_4))

    def test_draw_square(self):
        string_map = "...\n...\n...\n"
        matrix = string_to_matrix(string_map)
        corner_position = [0,0]
        size = 2
        new_matrix = draw_square(matrix, corner_position, size)
        self.assertEqual(matrix_to_string(new_matrix), "xx.\nxx.\n...\n")

    def test_find_square(self):
        map_1 = "...\n...\n...\n"
        map_2 = "...\n.o.\n...\n"
        map_3 = "oo\noo\noo\n"
        self.assertEqual(find_square(map_1), "xxx\nxxx\nxxx\n")
        self.assertEqual(find_square(map_2), "x..\n.o.\n...\n")
        self.assertEqual(find_square(map_3), "oo\noo\noo\n")

if __name__ == '__main__':
    unittest.main()
