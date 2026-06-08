import numpy as np

class Agent:
    def __init__(self, inventory, cash, sigma, gamma, T, k):
        self.inventory = inventory
        self.cash = cash
        self.sigma = sigma
        self.gamma = gamma
        self.T = T
        self.k = k
    def reservation_price(self, s, t):
        res_price = s - self.inventory * self.gamma * self.sigma ** 2 * (self.T -t)
        return res_price
    def optimal_spread(self, t):
        bid_ask_spread = self.gamma * self.sigma ** 2 * (self.T - t) + (2 / self.gamma) * np.log(1 + (self.gamma / self.k))
        return bid_ask_spread
    def optimal_bid_ask(self, s, t):
        bid = self.reservation_price(s, t) - (self.optimal_spread(t) / 2)
        ask = self.reservation_price(s, t) + (self.optimal_spread(t) / 2)
        return bid, ask