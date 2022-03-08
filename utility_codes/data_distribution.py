from math import e, factorial


class BinomialDistribution:
    def __init__(self, x, n, p):
        self.x = x
        self.n = n
        self.p = p

    def binomial_distribution(self):
        return (factorial(self.n) / (factorial(self.x) * factorial(self.n - self.x))) * (self.p ** self.x) * ((1 - self.p) ** (self.n - self.x))

    def mean(self):
        return self.n * self.p

    def variance(self):
        return self.n * self.p * (1 - self.p)


def poisson_distribution_function(x, u):
    return ((e ** -u) * (u ** x)) / factorial(x)


if __name__ == '__main__':
    print(BinomialDistribution(x=6, n=10, p=0.5).binomial_distribution())
    print(poisson_distribution_function(u=2, x=1))
