from Diplomacy import *
from unittest import main, TestCase

class TestDiplomacy(TestCase):
    
    def test_solve_1(self):
        t = diplomacy_solve("A Madrid Move London\nB London Move Madrid\n")
        self.assertEqual(t, "A London\nB Madrid")
        print("test 1 passed")

    def test_solve_2(self):
        t = diplomacy_solve("A Madrid Move London\n")
        self.assertEqual(t, "A London")
        print("test 2 passed")

    def test_solve_3(self):
        t = diplomacy_solve("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        self.assertEqual(t, "A [dead]\nB Madrid\nC London")
        print("test 3 passed")

    def test_solve_4(self):
        t = diplomacy_solve("A Madrid Move London\nB Paris Move London\nC Barcelona Move London\n")
        self.assertEqual(t, "A [dead]\nB [dead]\nC [dead]")
        print("test 4 passed")

    def test_solve_5(self):
        t = diplomacy_solve("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        self.assertEqual(t, "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin")
        print("test 5 passed")

a = TestDiplomacy()
a.test_solve_1()
a.test_solve_2()
a.test_solve_3()
a.test_solve_4()
a.test_solve_5()

