import unittest
import workflows

class ContractTests(unittest.TestCase):
    def test_quote_00(self):
        self.assertEqual(workflows.quote(*[1, 250, 0]), 250)

    def test_quote_01(self):
        self.assertEqual(workflows.quote(*[2, 251, 99]), 601)

    def test_quote_02(self):
        self.assertEqual(workflows.quote(*[3, 252, 450]), 1206)

    def test_quote_03(self):
        self.assertEqual(workflows.quote(*[4, 253, 0]), 1012)

    def test_quote_04(self):
        self.assertEqual(workflows.quote(*[5, 254, 99]), 1369)

    def test_quote_05(self):
        self.assertEqual(workflows.quote(*[6, 255, 450]), 1980)

    def test_quote_06(self):
        self.assertEqual(workflows.quote(*[7, 256, 0]), 1792)

    def test_quote_07(self):
        self.assertEqual(workflows.quote(*[8, 257, 99]), 2155)

    def test_quote_08(self):
        self.assertEqual(workflows.quote(*[9, 258, 450]), 2772)

    def test_quote_09(self):
        self.assertEqual(workflows.quote(*[10, 259, 0]), 2590)

    def test_quote_10(self):
        self.assertEqual(workflows.quote(*[11, 260, 99]), 2959)

    def test_quote_11(self):
        self.assertEqual(workflows.quote(*[12, 261, 450]), 3582)

    def test_quote_12(self):
        self.assertEqual(workflows.quote(*[13, 262, 0]), 3406)

    def test_quote_13(self):
        self.assertEqual(workflows.quote(*[14, 263, 99]), 3781)

    def test_quote_14(self):
        self.assertEqual(workflows.quote(*[15, 264, 450]), 4410)

    def test_quote_15(self):
        self.assertEqual(workflows.quote(*[16, 265, 0]), 4240)

    def test_quote_16(self):
        self.assertEqual(workflows.quote(*[17, 266, 99]), 4621)

    def test_quote_17(self):
        self.assertEqual(workflows.quote(*[18, 267, 450]), 5256)

    def test_quote_18(self):
        self.assertEqual(workflows.quote(*[19, 268, 0]), 5092)

    def test_quote_19(self):
        self.assertEqual(workflows.quote(*[20, 269, 99]), 5479)

    def test_late_00(self):
        self.assertEqual(workflows.late(*[10, 9, 0, False]), False)

    def test_late_01(self):
        self.assertEqual(workflows.late(*[11, 11, 1, True]), False)

    def test_late_02(self):
        self.assertEqual(workflows.late(*[12, 13, 2, True]), False)

    def test_late_03(self):
        self.assertEqual(workflows.late(*[13, 12, 3, True]), True)

    def test_late_04(self):
        self.assertEqual(workflows.late(*[14, 14, 0, True]), False)

    def test_late_05(self):
        self.assertEqual(workflows.late(*[15, 16, 1, False]), False)

    def test_late_06(self):
        self.assertEqual(workflows.late(*[16, 15, 2, True]), True)

    def test_late_07(self):
        self.assertEqual(workflows.late(*[17, 17, 3, True]), False)

    def test_late_08(self):
        self.assertEqual(workflows.late(*[18, 19, 0, True]), False)

    def test_late_09(self):
        self.assertEqual(workflows.late(*[19, 18, 1, True]), True)

    def test_late_10(self):
        self.assertEqual(workflows.late(*[20, 20, 2, False]), False)

    def test_late_11(self):
        self.assertEqual(workflows.late(*[21, 22, 3, True]), False)

    def test_late_12(self):
        self.assertEqual(workflows.late(*[22, 21, 0, True]), False)

    def test_late_13(self):
        self.assertEqual(workflows.late(*[23, 23, 1, True]), False)

    def test_late_14(self):
        self.assertEqual(workflows.late(*[24, 25, 2, True]), False)

    def test_late_15(self):
        self.assertEqual(workflows.late(*[25, 24, 3, False]), False)

    def test_late_16(self):
        self.assertEqual(workflows.late(*[26, 26, 0, True]), False)

    def test_late_17(self):
        self.assertEqual(workflows.late(*[27, 28, 1, True]), False)

    def test_late_18(self):
        self.assertEqual(workflows.late(*[28, 27, 2, True]), True)

    def test_late_19(self):
        self.assertEqual(workflows.late(*[29, 29, 3, True]), False)

    def test_reliability_00(self):
        self.assertEqual(workflows.reliability(*[0, 0, 0]), None)

    def test_reliability_01(self):
        self.assertEqual(workflows.reliability(*[1, 2, 1]), 50.0)

    def test_reliability_02(self):
        self.assertEqual(workflows.reliability(*[2, 4, 2]), 50.0)

    def test_reliability_03(self):
        self.assertEqual(workflows.reliability(*[3, 3, 3]), 100.0)

    def test_reliability_04(self):
        self.assertEqual(workflows.reliability(*[4, 5, 0]), 80.0)

    def test_reliability_05(self):
        self.assertEqual(workflows.reliability(*[0, 2, 1]), 0.0)

    def test_reliability_06(self):
        self.assertEqual(workflows.reliability(*[1, 1, 2]), 100.0)

    def test_reliability_07(self):
        self.assertEqual(workflows.reliability(*[2, 3, 3]), 66.7)

    def test_reliability_08(self):
        self.assertEqual(workflows.reliability(*[3, 5, 0]), 60.0)

    def test_reliability_09(self):
        self.assertEqual(workflows.reliability(*[4, 4, 1]), 100.0)

    def test_reliability_10(self):
        self.assertEqual(workflows.reliability(*[0, 1, 2]), 0.0)

    def test_reliability_11(self):
        self.assertEqual(workflows.reliability(*[1, 3, 3]), 33.3)

    def test_reliability_12(self):
        self.assertEqual(workflows.reliability(*[2, 2, 0]), 100.0)

    def test_reliability_13(self):
        self.assertEqual(workflows.reliability(*[3, 4, 1]), 75.0)

    def test_reliability_14(self):
        self.assertEqual(workflows.reliability(*[4, 6, 2]), 66.7)

    def test_reliability_15(self):
        self.assertEqual(workflows.reliability(*[0, 0, 3]), None)

    def test_reliability_16(self):
        self.assertEqual(workflows.reliability(*[1, 2, 0]), 50.0)

    def test_reliability_17(self):
        self.assertEqual(workflows.reliability(*[2, 4, 1]), 50.0)

    def test_reliability_18(self):
        self.assertEqual(workflows.reliability(*[3, 3, 2]), 100.0)

    def test_reliability_19(self):
        self.assertEqual(workflows.reliability(*[4, 5, 3]), 80.0)
