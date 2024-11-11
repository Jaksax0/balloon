from Balon.sequences import FibonacciSequence

def test_next():
    sequence = FibonacciSequence()
    assert sequence.next() == 0
    assert sequence.next() == 1
    assert sequence.next() == 1
    assert sequence.next() == 2
    assert sequence.next() == 3
    assert sequence.next() == 5

def test_reset():
    sequence = FibonacciSequence()

    sequence.next()
    sequence.next()
    sequence.next()
    sequence.next()
    sequence.reset()

    assert sequence.current_index == 1
    assert sequence.next() == 0