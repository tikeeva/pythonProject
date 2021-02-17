from random import gauss


class CustomFloat:
    def __int__(self):
        return int(float(self))

    def __add__(self, other):       # +
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) + other

    def __radd__(self, other):
        return self + other  # float()??
# add all methods


class RandomFloat(CustomFloat):
    def __init__(self, mu: float, /, *, sigma: float = 1.):
        if not isinstance(mu, float) or not  isinstance(sigma, float):
            raise TypeError
        self.mu = mu
        self.sigma = sigma
 #       self.      погрешность

    def __float__(self):
        return gauss(self.mu, self.sigma)


class EpsilonFloat(CustomFloat):
    def __init__(self, /, data, *, epsilon=1e-5):
        if isinstance(data, float):
            if data > 0:        # epsilon > 0

        self.data = data
        self.epsilon = epsilone

    def __float__(self):
        return self.data

    def __eq__(self, other):
        ...
# c = RandomFloat(10.) # for i-methods
# print(c, id(c))
# c += 1
# print(c, id(c))
# c = (RandomFloat(10.),)
# print(c, c[0].mu)
# try:
#     c[0] += 1
# except:
#     pass
# print(c, id(c))
c = RandomFloat(10.)
print(c)
c += 1.
print(c)
