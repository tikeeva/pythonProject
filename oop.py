from random import gauss


class RandomFloat:
    def __init__(self, mu: float, /, *, sigma: float = 1.):
        if not isinstance(mu, float) or not  isinstance(sigma, float):
            raise TypeError
        self.mu = mu
        self.sigma = sigma
 #       self.      погрешность

    def __float__(self):
        return gauss(self.mu, self.sigma)

    def __int__(self):
        return int(float(self))

    def __add__(self, other):       # +
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) + other

    def __radd__(self, other):
        return self + other     # float()??

    def __mul__(self, other):       # *
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) * other

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):       # -
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) - other

    def __rsub__(self, other):
        return -(self - other)

    def __pow__(self, other, modulo=None):      # **
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) ** other

    def __rpow__(self, other):      # **
        return other ** float(self)

    # 1 -  def __rpow__(self, other):
    #     other, self = self, other
    #     return self ** other
    # 2 -  def __rpow__(self, other):
    #       s = self
    #       self = other
    #       return self ** other

    def __truediv__(self, other):       # /
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) / other

    def __rtruediv__(self, other):
        return other / float(self)

    # def __rtruediv__(self, other):
    #     backdiv = (1 / self) * other
    #     copys = self
    #     return (1 / self) * other

    def __floordiv__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) // other

    # def __rfloordiv__(self, other):
    #     return int((1 / self) * other)

    def __rfloordiv__(self, other):
        return other // float(self)

    def __mod__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) % other

    # def __rmod__(self, other):
    #     return other - (other // self)

    def __rmod__(self, other):
        return other % float(self)

    def __round__(self, n=0): # округление
        return round(float(self))

    def __abs__(self):
        return abs(float(self))

#     def __eq__(self, other):        # method float
#         if isinstance(other, RandomFloat):
#             other = float(other)
#             if self.mu == other.mu:
#
# #    if (self - ) < e and > e                34 min
#         elif not isinstance(other, (float, int)):
#             raise TypeError
#         return float(self) == other

    def __lt__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) < other

    def __le__(self, other):        #??
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) <= other

    def __ne__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) != other

    def __ge__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) >= other

    def __gt__(self, other):
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) > other

    # def __iadd__(self, other):
    #     self.mu += other
    #     return self
    def __iadd__(self, other):
        if isinstance(other, RandomFloat):
            return RandomFloat(self.mu + other.mu)
        elif not isinstance(other, float):
            raise TypeError
        return RandomFloat(self.mu + other)

    # def __lshift__(self, other):
    #     if isinstance(other, RandomFloat):
    #         other = float(other)
    #     elif not isinstance(other, (float, int)):
    #         raise TypeError
    #     return float(self) << other


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
