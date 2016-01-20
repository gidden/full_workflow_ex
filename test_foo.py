import foo

from nose.tools import assert_equal

def test_floats():
    a, b = 1.0, 2.0

    obs = foo.divide(a, b)
    exp = 0.5

    assert_equal(exp, obs)
    
