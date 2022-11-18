from main import fib
from main import fib_iter
from main import fib_gen_ver
from main import FibonacchiLst
import pytest


@pytest.mark.parametrize("n, res", [
    (-10, [0]),
    (0, [0]),
    (1, [0, 1, 1]),
    (4, [0, 1, 1, 2, 3]),
    (9, [0, 1, 1, 2, 3, 5, 8]),
    (21, [0, 1, 1, 2, 3, 5, 8, 13, 21])])
def test_fib_equal(n, res):
    assert fib(n) == res


@pytest.mark.parametrize("l, res", [
    ([1, 1, 1, 1, 1, 1], [1, 1]),
    ([0, 4, 5, 13, 14], [0, 5, 13]),
    ([0, 88, 4, 6, 9, 12, 100], [0]),
    ([4, 6, 9, 14], []),
    ([0, 1, 1, 2, 3, 5, 8, 13, 21], [0, 1, 1, 2, 3, 5, 8, 13, 21]),
    ([0, 1, 5, 5, 7, 7, 9, 9, 10, 13, 13], [0, 1, 1, 5, 13])])
def test_fib_iter_equal(l, res):
    assert fib_iter(l) == res


@pytest.mark.parametrize("l, res", [
    ([1, 1, 1, 1, 1, 1], [1, 1]),
    ([0, 4, 5, 13, 14], [0, 5, 13]),
    ([0, 88, 4, 6, 9, 12, 100], [0]),
    ([4, 6, 9, 14], []),
    ([0, 1, 1, 2, 3, 5, 8, 13, 21], [0, 1, 1, 2, 3, 5, 8, 13, 21]),
    ([0, 1, 5, 5, 7, 7, 9, 9, 10, 13, 13], [0, 1, 1, 5, 13])])
def test_FibonacchiLst(l, res):
    assert list(FibonacchiLst(l)) == res


@pytest.mark.parametrize("n, res", [
    (-10, [0]),
    (0, [0]),
    (1, [0, 1, 1]),
    (4, [0, 1, 1, 2, 3]),
    (9, [0, 1, 1, 2, 3, 5, 8]),
    (21, [0, 1, 1, 2, 3, 5, 8, 13, 21])])
def test_fib_gen_ver_equal(n, res):
    assert fib_gen_ver(n) == res