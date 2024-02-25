from mypackage import myModule

def test_top_n():
    """Makes sure top_n works correctly"""

    assert myModule.top_n([7,8,10,4,100],3) == [100,10,8], 'incorrect func'
