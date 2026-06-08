from agent import Agent
from market import Market
from simulator import Simulator
import numpy as np

agent = Agent(0, 0, 2, 0.1, 1, 1.5)
market = Market(1.5, 140, 100, 2, 0.005)
simulator = Simulator(10000, agent, market)
final_inv, final_prof, final_mid_price = simulator.market_simulation()
print(np.std(final_inv), np.mean(final_inv), np.std(final_prof), np.mean(final_prof), np.mean(final_mid_price))
