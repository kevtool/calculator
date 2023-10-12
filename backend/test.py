import unittest
import convert


class TestSum(unittest.TestCase):

    def test_to_infix(self):
        self.assertEqual(convert.to_infix("7"), "7")
        self.assertEqual(convert.to_infix("3958"), "3958")
        self.assertEqual(convert.to_infix("3.5"), "3.5")
        self.assertEqual(convert.to_infix("9 + 8"), "9+8")
        self.assertEqual(convert.to_infix("-3 + 2"), "n3+2")
        self.assertEqual(convert.to_infix("6 / 0"), "6/0")
        self.assertEqual(convert.to_infix("(9 + 8)"), "(9+8)")
        self.assertEqual(convert.to_infix("(9 + 8) x (5 + 6)"), "(9+8)*(5+6)")
        self.assertEqual(convert.to_infix("3.5 x (2 + 4.53)"), "3.5*(2+4.53)")
        self.assertEqual(convert.to_infix("()"), "ERROR")
        self.assertEqual(convert.to_infix("(8)"), "8")
        self.assertEqual(convert.to_infix(".72(.414)"), ".72*.414")
        self.assertEqual(convert.to_infix("(.8).2"), ".8*.2")
        self.assertEqual(convert.to_infix("(132.23)(44.55)"), "132.23*44.55")
        self.assertEqual(convert.to_infix("5 + ()"), "ERROR")
        self.assertEqual(convert.to_infix("(8 + 5) x 3 + (2"), "ERROR")
        self.assertEqual(convert.to_infix("(8 + 5(3 + 5)"), "ERROR")
        self.assertEqual(convert.to_infix(".8(.2 + .5)"), ".8*(.2+.5)")
        self.assertEqual(convert.to_infix("2. - 5"), "2.-5")
        self.assertEqual(convert.to_infix("2 + 3 x 4 / 5"), "2+3*4/5")
        self.assertEqual(convert.to_infix("4(2.5 - 9)"), "4*(2.5-9)")
        self.assertEqual(convert.to_infix("(1.5 + 13)2"), "(1.5+13)*2")
        self.assertEqual(convert.to_infix("(158 + 6)(158 - 6)"), "(158+6)*(158-6)")
        self.assertEqual(convert.to_infix("(12 + 26)2(8 / 4)"), "(12+26)*2*(8/4)")
        self.assertEqual(convert.to_infix("(6 x 7)2.3(7 - 2)"), "(6*7)*2.3*(7-2)")
        self.assertEqual(convert.to_infix("2.5 + (5(3.5 + 2))"), "2.5+(5*(3.5+2))")
        self.assertEqual(convert.to_infix("12.2 + (8 + 5(3 + 6 - (4(8)2)) + 3)"), "12.2+(8+5*(3+6-(4*8*2))+3)")
        self.assertEqual(convert.to_infix("(1 + (5).3) + (8 + .2(22 x 43 - (4.3(8))) / 2)"), "(1+5*.3)+(8+.2*(22*43-(4.3*8))/2)")

    def test_to_postfix(self):
        self.assertEqual(convert.to_postfix("ERROR"), ["ERROR"])
        self.assertEqual(convert.to_postfix("7"), ["7"])
        self.assertEqual(convert.to_postfix("3958"), ["3958"])
        self.assertEqual(convert.to_postfix("3.5"), ["3.5"])
        self.assertEqual(convert.to_postfix("5+6"), ["5", "6", "+"])
        self.assertEqual(convert.to_postfix("n3+2"), ["-3", "2", "+"])
        self.assertEqual(convert.to_postfix("(44.23-18.246)"), ["44.23", "18.246", "-"])
        self.assertEqual(convert.to_postfix("(9+8)*(5+6)"), ['9', '8', '+', '5', '6', '+', '*'])
        self.assertEqual(convert.to_postfix(".72*.414"), ['.72', '.414', '*'])
        self.assertEqual(convert.to_postfix("(6*7)*2.3*(7-2)"), ['6', '7', '*', '2.3', '*', '7', '2', '-', '*'])
        self.assertEqual(convert.to_postfix("12.2+(8+5*(3+6-(4*8*2))+3)"), ['12.2', '8', '5', '3', '6', '+', '4', '8', '*', '2', '*', '-', '*', '+', '3', '+', '+'])
    
    def test_to_result(self):
        self.assertEqual(convert.to_result(["ERROR"]), "ERROR")
        self.assertEqual(convert.to_result(["7"]), 7)
        self.assertEqual(convert.to_result(["5", "6", "+"]), 11)
        self.assertEqual(convert.to_result(["-3", "2", "+"]), -1)
        self.assertEqual(convert.to_result(["44.23", "18.246", "-"]), 25.984)
        self.assertEqual(convert.to_result(["6", "0", "/"]), "UNDEFINED")
        self.assertEqual(convert.to_result(["23.3", ".", "-"]), "ERROR")
        self.assertEqual(convert.to_result(['9', '8', '+', '5', '6', '+', '*']), 187)
        

if __name__ == '__main__':
    unittest.main()