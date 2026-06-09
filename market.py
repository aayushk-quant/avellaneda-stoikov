import numpy as np

class Market:
    def __init__(self, k, A, mid_price, sigma, dt):
        if k <= 0:
            raise ValueError("k must be positive")
        if A <= 0:
            raise ValueError("A must be positive")
        if mid_price <=  0:
            raise ValueError("Mid-price must be positive")
        if sigma < 0:
            raise ValueError("sigma must be non-negative")
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.k = k
        self.A = A
        self.mid_price = mid_price
        self.sigma = sigma
        self.dt = dt
    def mid_price_update(self):
        self.mid_price = self.mid_price + self.sigma * np.sqrt(self.dt) * np.random.standard_normal()
    def order_arrival(self, bid, ask):
        bid_rate = self.A * np.exp(-self.k * (self.mid_price - bid))
        ask_rate = self.A * np.exp(-self.k * (ask - self.mid_price))
        bid_pr = min(1, self.dt * bid_rate)
        ask_pr = min(1, self.dt * ask_rate)
        bid_draw = np.random.random() < bid_pr
        ask_draw = np.random.random() < ask_pr
        return bid_draw, ask_draw