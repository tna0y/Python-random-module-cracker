import random
import time

import pytest

from randcrack import RandCrack


def test_submit_not_enough():
    random.seed(time.time())

    cracker = RandCrack()

    for _ in range(623):
        cracker.submit(random.randint(0, 4294967294))

    with pytest.raises(ValueError):
        cracker.predict_randint(0, 1)


def test_submit_too_much():
    random.seed(time.time())

    cracker = RandCrack()

    for _ in range(624):
        cracker.submit(random.randint(0, 4294967294))

    with pytest.raises(ValueError):
        cracker.submit(random.getrandbits(32))


def test_predict_first_624():
    random.seed(time.time())

    cracker = RandCrack()

    for _ in range(624):
        cracker.submit(random.randint(0, 4294967294))

    assert sum([random.getrandbits(32) == cracker.predict_getrandbits(32) for _ in range(1000)]) == 1000


def test_predict_first_1000_close():
    random.seed(time.time())

    cracker = RandCrack()

    for _ in range(624):
        cracker.submit(random.randint(0, 4294967294))

    assert sum([random.getrandbits(32) == cracker.predict_getrandbits(32) for _ in range(1000)]) == 1000


def test_predict_random():
    random.seed(time.time())

    cracker = RandCrack()

    for _ in range(624):
        cracker.submit(random.randint(0, 4294967294))

    assert sum([random.random() == cracker.predict_random() for _ in range(1000)]) == 1000


def test_predict_previous():
    random.seed(time.time())

    unknown = [random.getrandbits(32) for _ in range(1000)]

    cracker = RandCrack()

    for _ in range(624):
        cracker.submit(random.getrandbits(32))

    cracker.offset(-624)
    cracker.offset(-1000)

    assert unknown == [cracker.predict_getrandbits(32) for _ in range(1000)]


def test_predict_previous_randbelow():
    random.seed(time.time())

    # randint() uses randbelow() internally
    unknown = [random.randint(1, 800) for _ in range(1000)]

    cracker = RandCrack()

    for _ in range(624):
        cracker.submit(random.getrandbits(32))

    cracker.offset(-624)
    cracker.offset(-2000)  # Go back too far to include everything

    guesses = [cracker.predict_randint(1, 800) for _ in range(2000)]

    def is_subseq(x, y):
        return all(any(c == ch for c in y) for ch in x)

    # The sequence of unknown numbers should be in guesses, but there may be numbers before and after
    # (e.g. if the sequence is [1, 2, 3], guesses may be [123, 42, 1, 2, 3, 1337])
    assert is_subseq(unknown, guesses)
