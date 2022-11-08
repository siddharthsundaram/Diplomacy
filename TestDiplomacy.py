from Diplomacy import *
from unittest import main, TestCase
from io import StringIO

class TestDiplomacy(TestCase):
    
    def test_solve_1(self):
        t = diplomacy_solve("A Madrid Move London\nB London Move Madrid\n")
        self.assertEqual(t, "A London\nB Madrid\n")
        # print("test 1 passed")

    def test_solve_2(self):
        t = diplomacy_solve("A Madrid Move London\n")
        self.assertEqual(t, "A London\n")
        # print("test 2 passed")

    def test_solve_3(self):
        t = diplomacy_solve("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        self.assertEqual(t, "A [dead]\nB Madrid\nC London\n")
        # print("test 3 passed")

    def test_solve_4(self):
        t = diplomacy_solve("A Madrid Move London\nB Paris Move London\nC Barcelona Move London\n")
        self.assertEqual(t, "A [dead]\nB [dead]\nC [dead]\n")
        # print("test 4 passed")

    def test_solve_5(self):
        t = diplomacy_solve("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        self.assertEqual(t, "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")
        # print("test 5 passed")

    def test_print_1(self):
        w = StringIO()
        diplomacy_print(w, "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n", "A [dead]\nB Madrid\nC London\n")
        self.assertEqual(w.getvalue(), "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nA [dead]\nB Madrid\nC London\n")
        # print("test 6 passed")

    def test_print_2(self):
        w = StringIO()
        diplomacy_print(w, "A Madrid Move London\n", "A London\n")
        self.assertEqual(w.getvalue(), "A Madrid Move London\nA London\n")
        # print("test 7 passed")

    def test_print_3(self):
        w = StringIO()
        diplomacy_print(w, "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n", "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")
        self.assertEqual(w.getvalue(), "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\nA [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")
        # print("test 8 passed")

    def test_eval_1(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\n")
        w = StringIO()
        diplomacy_eval(r, w)
        # print(w.getvalue())
        self.assertEqual(w.getvalue(), "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nA [dead]\nB Madrid\nC London\n")
        # print("test 9 passed")

    def test_eval_2(self):
        r = StringIO("A Lima Hold\nB Oslo Hold\n")
        w = StringIO()
        diplomacy_eval(r, w)
        # print(w.getvalue())
        self.assertEqual(w.getvalue(), "A Lima Hold\nB Oslo Hold\nA Lima\nB Oslo\n")
        # print("test 10 passed")

    def test_eval_3(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\n")
        w = StringIO()
        diplomacy_eval(r, w)
        # print(w.getvalue())
        self.assertEqual(w.getvalue(), "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A\nA [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")
        # print("test 11 passed")

a = TestDiplomacy()
a.test_solve_1()
a.test_solve_2()
a.test_solve_3()
a.test_solve_4()
a.test_solve_5()
a.test_print_1()
a.test_print_2()
a.test_print_3()
a.test_eval_1()
a.test_eval_2()
a.test_eval_3()

