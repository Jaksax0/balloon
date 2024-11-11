from Balon.sequences import ArithmeticSequence

def test_next():
    sequence = ArithmeticSequence(5, 3)
    assert sequence.next() == 5
    assert sequence.next() == 8
    assert sequence.next() == 11

def test_reset():
    sequence = ArithmeticSequence(5, 3)

    sequence.next()
    sequence.next()
    sequence.reset()

    assert sequence.current_index == 0
    assert sequence.next() == 5