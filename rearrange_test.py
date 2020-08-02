# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:18:39 2020

@author: Saurav
"""


from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_middle_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_single_name(self):
        testcase = "Madonna"
        expected = "Madonna"
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()