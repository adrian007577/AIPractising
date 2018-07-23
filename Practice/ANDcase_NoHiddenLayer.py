import numpy


class Process:
    def __init__(self, size, standard):
        self.weight = numpy.ones(size)*standard

    def __call__(self, inputData):
        data = inputData * self.weight
        dataSum = data.sum()
        return (1 if dataSum>0.5 else 0)


cases = [numpy.array([0, 0]), numpy.array([0, 1]), numpy.array([1, 0]), numpy.array([1, 1])]

p = Process(2, 0.5)
for x in cases:
    print(x, p(x))