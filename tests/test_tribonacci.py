from balloon.sequences import TribonacciSequence

def test_next():
    sequence = TribonacciSequence()
    assert sequence.next() == 0
    assert sequence.next() == 1
    assert sequence.next() == 1
    assert sequence.next() == 2
    assert sequence.next() == 4
    assert sequence.next() == 7


def test_reset():
    sequence = TribonacciSequence()

    sequence.next()
    sequence.next()
    sequence.next()
    sequence.next()
    sequence.reset()

    assert sequence.current_index == 1
    assert sequence.next() == 0
