from random import triangular
from typing import List, Any

from MonkeyScope import distribution_timer


class LinearChoice:

    def __init__(self, values: List[Any]):
        self.values = values
        self.size = len(values)

    def front(self) -> Any:
        return self.values[int(triangular(0, self.size, 0))]

    def middle(self) -> Any:
        return self.values[int(triangular(0, self.size, self.size / 2))]

    def back(self) -> Any:
        return self.values[int(triangular(0, self.size, self.size))]


if __name__ == '__main__':
    lc = LinearChoice(["A", "B", "C", "D", "E", "F", "G"])
    distribution_timer(lc.front)
    distribution_timer(lc.middle)
    distribution_timer(lc.back)
