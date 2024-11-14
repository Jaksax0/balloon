class ArithmeticSequence:
    def __init__(self, first_term, common_difference):
        self.first_term = first_term
        self.common_difference = common_difference
        self.current_index = 0

    def next(self):
        next_term = self.first_term + self.common_difference * self.current_index
        self.current_index += 1
        return next_term

    def reset(self):
        self.current_index = 0

seq1 = ArithmeticSequence(2,3)

for i in range(10):
    print(seq1.next())


class GeometricSequence:
    def __init__(self, first_term, common_ratio):
        if first_term == 0:
            raise ValueError("First term can't be equal to zero")
        self.first_term = first_term
        self.common_ratio = common_ratio
        self.current_index = 0

    def next(self):
        next_term = self.first_term * self.common_ratio ** self.current_index
        self.current_index += 1
        return next_term

    def reset(self):
        self.current_index = 0

seq2 = GeometricSequence(2,2)

for i in range(10):
    print(seq2.next())


class FibonacciSequence:
    def __init__(self):
        self.__previous_term_2 = 0
        self.__previous_term = 1
        self.current_index = 1

    def next(self):
        if self.current_index == 1:
            self.current_index += 1
            return self.__previous_term_2
        elif self.current_index == 2:
            self.current_index += 1
            return self.__previous_term
        else:
            next_term = self.__previous_term + self.__previous_term_2
            self.__previous_term_2 = self.__previous_term
            self.__previous_term = next_term
            return next_term

    def reset(self):
        self.__previous_term_2 = 0
        self.__previous_term = 1
        self.current_index = 1

seq3 = FibonacciSequence()

for i in range(10):
    print(seq3.next())


class TribonacciSequence():
    def __init__(self):
        self.__previous_term_3 = 0
        self.__previous_term_2 = 1
        self.__previous_term = 1
        self.current_index = 1

    def next(self):
        if self.current_index == 1:
            self.current_index += 1
            return self.__previous_term_3
        elif self.current_index == 2:
            self.current_index += 1
            return self.__previous_term_2
        elif self.current_index == 3:
            self.current_index += 1
            return self.__previous_term
        else:
            next_term = self.__previous_term + self.__previous_term_2 + self.__previous_term_3
            self.__previous_term_3 = self.__previous_term_2
            self.__previous_term_2 = self.__previous_term
            self.__previous_term = next_term
            return next_term

    def reset(self):
        self.__previous_term_3 = 0
        self.__previous_term_2 = 1
        self.__previous_term = 1
        self.current_index = 1