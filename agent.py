import numpy as np

class Agent:
    def __init__(self, inventory, cash, sigma, gamma, T, k):
        if gamma <= 0:
            raise ValueError("gamma must be positive")
        if k <= 0:
            raise ValueError("k must be positive")
        if sigma < 0:
            raise ValueError("sigma must be non-negative")
        if T <= 0:
            raise ValueError("T must be positive")
        self.inventory = inventory
        self.cash = cash
        self.sigma = sigma
        self.gamma = gamma
        self.T = T
        self.k = k
    def _validate_time(self, t):
        if t < 0 or t > self.T:
            raise ValueError("t must be between 0 and T")
    def reservation_price(self, s, t):
        self._validate_time(t)
        res_price = s - self.inventory * self.gamma * self.sigma ** 2 * (self.T - t)
        return res_price
    def optimal_spread(self, t):
        self._validate_time(t)
        bid_ask_spread = self.gamma * self.sigma ** 2 * (self.T - t) + (2 / self.gamma) * np.log(1 + (self.gamma / self.k))
        return bid_ask_spread
    def optimal_bid_ask(self, s, t):
        res_price = self.reservation_price(s, t)
        half_spread = self.optimal_spread(t) / 2
        bid = res_price - half_spread
        ask = res_price + half_spread
        return bid, ask
    def naive_bid_ask(self, s, t):
        half_spread = self.optimal_spread(t) / 2
        bid = s - half_spread
        ask = s + half_spread
        return bid, ask