"""Test helpers"""
from contextlib import contextmanager
from tempfile import NamedTemporaryFile, mkdtemp
import os
from StringIO import StringIO
import imp
import shutil
import sys
import unittest


@contextmanager
def redirect_stdout(new_target):
    """Similar to contextlib.redirect_stdout from Python 3.4."""
    old_target, sys.stdout = sys.stdout, new_target
    try:
        yield new_target
    finally:
        sys.stdout = old_target


def run_program(program, args=[], raises=None):
    old_args = sys.argv
    assert all(isinstance(a, str) for a in args)
    try:
        path = 'modules/{program}'.format(program=program)
        sys.argv = [program] + args
        with redirect_stdout(StringIO()) as stdout:
            try:
                if '__main__' in sys.modules:
                    del sys.modules['__main__']
                imp.load_source('__main__', path)
            except raises:
                return stdout.getvalue()
            if raises is not None:
                raise AssertionError("{} not raised".format(raises))
            return stdout.getvalue()
    finally:
        sys.argv = old_args


def import_module(module, args=[]):
    path = 'modules/{module}.py'.format(module=module)
    return imp.load_source(module, path)


@contextmanager
def cd(new_directory):
    original_directory = os.getcwd()
    os.chdir(os.path.expanduser(new_directory))
    try:
        yield
    finally:
        os.chdir(original_directory)


@contextmanager
def TemporaryDirectory():
    """Similar to tempfile.TemporaryDirectory from Python 3.2."""
    dirpath = mkdtemp()
    yield dirpath
    with cd(dirpath):
        shutil.rmtree(dirpath)


@contextmanager
def make_file(contents=None):
    with NamedTemporaryFile(mode='wt', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


@contextmanager
def capture_stdin(data):
    old_stdin, sys.stdin = sys.stdin, StringIO()
    try:
        sys.stdin.write(data)
        sys.stdin.seek(0)
        yield sys.stdin
    finally:
        sys.stdin = old_stdin


class ModuleTestCase(unittest.TestCase):

    """TestCase for module/program tests."""

    @classmethod
    def setUpClass(cls):
        if not hasattr(cls, 'module_path'):
            raise NotImplementedError('Test needs "module_path" attribute')
