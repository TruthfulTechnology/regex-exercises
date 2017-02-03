#!/usr/bin/env python
from collections import OrderedDict, defaultdict
import inspect
from importlib import import_module as import_test_module
import os
import re
import sys
import unittest

from helpers import import_module, ModuleTestCase


def get_test_modules(directory):
    test_files = (
        f
        for f in os.listdir(directory)
        if f.endswith('_test.py')
    )
    return (re.sub(r'^(.*)\.py$', r'\1', f) for f in test_files)


class DummyObject:
    ""


def get_test_classes(module_name):
    module = import_test_module(module_name)
    module_members = OrderedDict(inspect.getmembers(module))
    classes = (
        value
        for name, value in module_members.items()
        if inspect.isclass(value)
        and issubclass(value, unittest.TestCase)
        and not value == ModuleTestCase
    )
    for cls in classes:
        if issubclass(cls, ModuleTestCase):
            try:
                module = import_module(cls.module_path)
            except BaseException:
                module = type(cls.module_path, (), {})
            thing = module
        else:
            doc = cls.__doc__
            if not doc:
                raise SystemExit("{module}.{cls} has no docstring.".format(
                    module=module_name,
                    cls=cls.__name__,
                ))
            thing_name = re.search(r' (\w+)\.$', doc).group(1)
            thing = module_members[thing_name]
        class_path = ".".join([module_name, cls.__name__])
        yield (thing, class_path)


def get_tests():
    test_modules = defaultdict(list)
    test_classes = OrderedDict()
    directory = os.path.dirname(os.path.realpath(__file__))
    for test_module_name in get_test_modules(directory):
        classes = get_test_classes(test_module_name)
        for subject, class_path in classes:
            test_classes[subject.__name__] = class_path
            test_modules[test_module_name[:-5]].append(subject)
    return test_modules, test_classes


MODULES, TESTS = get_tests()
assert len([x for items in MODULES.values() for x in items]) == len(TESTS)


def get_test(obj_name):
    if obj_name not in TESTS:
        raise SystemExit("Test for {} doesn't exist.".format(obj_name))
    return unittest.defaultTestLoader.loadTestsFromName(TESTS[obj_name])

def run_tests(tests):
    test_suite = unittest.TestSuite(tests)
    unittest.TextTestRunner().run(test_suite)


def print_object_names():
    for module_name, subjects in MODULES.items():
        print("\n{module_name}:\n".format(
            module_name=module_name,
        ))
        for subject in subjects:
            doc = subject.__doc__ or 'no documentation'
            print("{name}: {doc}".format(
                name=subject.__name__,

                doc=doc.strip().split('\n', 1)[0],
            ))


def main(*arguments):
    if '--all' in arguments:
        arguments = list(TESTS)
    if not arguments:
        print("Please select a thing to test")
        print_object_names()
    else:
        tests = [
            get_test(arg)
            for arg in arguments
        ]
        print("Testing {}\n".format(', '.join(arguments)))
        run_tests(tests)


if __name__ == "__main__":
    main(*sys.argv[1:])
