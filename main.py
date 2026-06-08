from agent import Agent
from market import Market
from simulator import Simulator
import numpy as np

agent = Agent(0, 0, 2, 0.1, 1, 1.5)
market = Market(1.5, 140, 100, 2, 0.005)
simulator = Simulator(1000, agent, market)

inv_final_inv, inv_final_prof, inv_final_mid = simulator.market_simulation(naive=False)
naive_final_inv, naive_final_prof, naive_final_mid = simulator.market_simulation(naive=True)

print(f"{'Strategy':<12}{'Profit':<12}{'std(Profit)':<14}{'Final q':<12}{'std(Final q)':<14}")
print(f"{'Inventory':<12}{np.mean(inv_final_prof):<12.2f}{np.std(inv_final_prof):<14.2f}{np.mean(inv_final_inv):<12.2f}{np.std(inv_final_inv):<14.2f}")
print(f"{'Symmetric':<12}{np.mean(naive_final_prof):<12.2f}{np.std(naive_final_prof):<14.2f}{np.mean(naive_final_inv):<12.2f}{np.std(naive_final_inv):<14.2f}")