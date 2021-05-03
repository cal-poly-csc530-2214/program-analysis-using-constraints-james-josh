from typing import *


def pv1( y: int ):
    x: int = -50
    while x < 0:
        x = x + y
        y += 1
    assert y > 0


pv1(-324)
