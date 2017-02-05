"""Test helpers"""
import imp
import unittest


def import_module(module, args=[]):
    path = 'modules/{module}.py'.format(module=module)
    return imp.load_source(module, path)


class ModuleTestCase(unittest.TestCase):

    """TestCase for module/program tests."""

    @classmethod
    def setUpClass(cls):
        if not hasattr(cls, 'module_path'):
            raise NotImplementedError('Test needs "module_path" attribute')
