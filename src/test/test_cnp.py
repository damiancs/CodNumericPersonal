# coding=utf-8
"""
Testing CNPs functionality.
"""

from datetime import date
from unittest import TestCase

from ..CodNumericPersonal.cnp import CNP
from ..CodNumericPersonal.errors import *
from ..CodNumericPersonal.utils import *


class TestCNP(TestCase):
    """
    Test cases for CNP class.
    """

    def test_bad_format_cnp(self):
        """
        Test cnp with bad format.
        """
        with self.assertRaises(CNPError):
            cnp = CNP("019120427002")
        with self.assertRaises(CNPError):
            cnp = CNP("bad_CNPformat")

    def test_bad_sex_cnp(self):
        """
        Test a cnp with sex = 0.
        """
        with self.assertRaises(SexError):
            cnp = CNP("0191204270029")

    def test_bad_date_cnp(self):
        """
        Test a cnp with bad date (month or day).
        """
        with self.assertRaises(DateError):
            cnp = CNP("1192204270029")
        with self.assertRaises(DateError):
            cnp = CNP("2191232270029")

    def test_bad_county_cnp(self):
        """
        Test cnp with bad county.
        """
        with self.assertRaises(CountyError):
            cnp = CNP("2191204980029")

    def test_self_representations(self):
        """
        Test __str__, __repr__ and as_list.
        """
        str_cnp = "3900101051235"
        cnp = CNP(str_cnp)
        self.assertEqual(len(str(cnp)), 13)
        self.assertEqual(len(repr(cnp)), 13)
        self.assertEqual(len(cnp.as_list()), 13)
        self.assertEqual(str(cnp), str_cnp)
        self.assertEqual(cnp.as_list(), [int(ch) for ch in str_cnp])
        self.assertIsInstance(cnp.as_list(), list)

    def test_checksum_calculation(self):
        """
        Test if the control digit is correctly calculated.
        """
        str_cnp = "3900101051235"
        cnp = CNP(str_cnp)
        self.assertEqual(cnp.as_list()[12], cnp.control_digit)
        self.assertEqual(cnp.control_digit, int(str_cnp[12]))

    def test_validity_check(self):
        """
        Test if the valid function returns correctly.
        """
        wrong_cnp = "3900101051234"
        cnp = CNP(wrong_cnp)
        self.assertFalse(cnp.valid())
        right_cnp = "3900101051235"
        cnp = CNP(right_cnp)
        self.assertTrue(cnp.valid())

    def test_date(self):
        """
        Test the date parsed from the cnp.
        """
        cnp_18 = "3900101051235"
        cnp = CNP(cnp_18)
        self.assertEqual(cnp.date, date(1890, 1, 1))
        cnp_19 = "1871203421239"
        cnp = CNP(cnp_19)
        self.assertEqual(cnp.date, date(1987, 12, 3))
        cnp_20 = "6900101051230"
        cnp = CNP(cnp_20)
        self.assertEqual(cnp.date, date(2090, 1, 1))

    def test_sex(self):
        """
        Test the sex parsed from the cnp.
        """
        cnp_m = "3900101051235"
        cnp = CNP(cnp_m)
        self.assertEqual(cnp.sex, SEX[True])
        cnp_f = "6900101051230"
        cnp = CNP(cnp_f)
        self.assertEqual(cnp.sex, SEX[False])
        cnp_r = "9871203421233"
        cnp = CNP(cnp_r)
        self.assertEqual(cnp.sex, SEX[None])

    def test_county(self):
        """
        Test the county parsed from the cnp.
        """
        cnp_bc = "2670904044560"
        cnp = CNP(cnp_bc)
        self.assertEqual(cnp.county, JJ[4])
        cnp_b_4 = "2670904444569"
        cnp = CNP(cnp_b_4)
        self.assertEqual(cnp.county, JJ[44])
