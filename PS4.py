class Progression:
# error 3: defined 'self'
    def __init__(self, start=0):
       self._current = start

    def _advance(self):
       self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self

# error 2: wrong way to do inheritance
class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

# error 4: added an underscore so that the function actually gets called
    def _advance(self):
# error 5: flipped self._current and self._increment
        self._current += self._increment

if __name__ == "__main__":
# error 1: line indented to far
    a = ArithmeticProgression(2, 1)
    print(" ".join(str(next(a)) for _ in range(10)))

'''
ORIGINAL CODE

class Progression:
    def __init__(start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

class ArithmeticProgression extends Progression
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def advance(self):
        self._increment += self._current

if __name__ == "__main__":
        a = ArithmeticProgression(2, 1)
    print(" ".join(str(next(a)) for _ in range(10)))
'''