import foo

from nose.tools import assert_equal

def test_spread():
    m = None
    obs = foo.spread(m)

    assert_equal(range(4), obs)
    assert_equal(range(5), obs)
    
