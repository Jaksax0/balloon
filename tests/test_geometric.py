from Balon.sequences import GeometricSequence
import pytest

def test_next():
    sequence = GeometricSequence(2, 3)
    assert sequence.next() == 2
    assert sequence.next() == 6
    assert sequence.next() == 18

def test_next_neg():
    sequence = GeometricSequence(2, -2)
    assert sequence.next() == 2
    assert sequence.next() == -4
    assert sequence.next() == 8


def test_reset():
    sequence = GeometricSequence(2, 2)

    sequence.next()
    sequence.next()
    sequence.reset()

    assert sequence.current_index == 0
    assert sequence.next() == 2


def test_first_term_is_zero():
    with pytest.raises(ValueError, match="First term can't be equal to zero"):
        GeometricSequence(0, 2)
