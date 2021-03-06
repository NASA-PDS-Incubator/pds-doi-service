# encoding: utf-8

'''
Planetary Data System's Digital Object Identifier service — tests for core actions
'''


import unittest
from . import check_test, draft_test, list_test, release_test, reserve_test


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(check_test))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(draft_test))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(list_test))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(release_test))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(reserve_test))
    return suite
