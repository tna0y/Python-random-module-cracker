import random
import time

import pytest

from ..randcrack import RandCrack


def test_submit_not_enough():
    random.seed(time.time())

    cracker = RandCrack()

    for i in range(623):
        cracker.submit(random.randint(0, 4294967294))

    with pytest.raises(ValueError):
        cracker.predict_randint(0, 1)


def test_submit_too_much():
    random.seed(time.time())

    cracker = RandCrack()

    for i in range(624):
        cracker.submit(random.randint(0, 4294967294))

    with pytest.raises(ValueError):
        cracker.submit(random.randint(0, 4294967294))


def test_predict_first_624():
    random.seed(time.time())

    cracker = RandCrack()

    for i in range(624):
        cracker.submit(random.randint(0, 4294967294))

    assert sum([random.getrandbits(32) == cracker.predict_getrandbits(32) for _ in range(1000)]) >= 620


def test_predict_first_1000_close():
    random.seed(time.time())

    cracker = RandCrack()

    for i in range(624):
        cracker.submit(random.randint(0, 4294967294))

    assert sum([random.getrandbits(32) == cracker.predict_getrandbits(32) for _ in range(1000)]) >= 980
