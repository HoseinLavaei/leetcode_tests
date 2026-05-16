from amir.LC001 import test_linkedlist_sum as a_lc001
from hosein.LC001 import test_add_two_numbers as h_lc001
from hosein.LC002 import test_lswrc as h_lc002
from hosein.LC003 import test_valid_sudoku as h_lc003
from hosein.LC004 import test_median_of_two_sorted_arrays as h_lc004

def main():
    hosein_tests()
    amir_tests()

def hosein_tests():
    h_lc001()
    h_lc002()
    h_lc003()
    h_lc004()

def amir_tests():
    a_lc001()

if __name__ == "__main__":
    main()
