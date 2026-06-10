from agent import Agent
from market import Market
from simulator import Simulator
import numpy as np
import plot

def run_gamma_experiment(gamma_values, sigma = 2, T = 1, k = 1.5, A = 140, mid_price = 100, dt = 0.005, n_simulations = 1000):
    print(f"{'Strategy':<12}{'Profit':<12}{'std(Profit)':<14}{'Final q':<12}{'std(Final q)':<14}")
    for gamma in gamma_values:
        agent = Agent(0, 0, sigma, gamma, T, k)
        market = Market(k, A, mid_price, sigma, dt)
        simulator = Simulator(n_simulations, agent, market)
        inv_inv, inv_prof, _ = simulator.market_simulation(seed = 42)
        naive_inv, naive_prof, _ = simulator.market_simulation(naive = True, seed = 42)
        print(f"\nγ = {gamma}")
        print(f"{'Inventory':<12}{np.mean(inv_prof):<12.2f}{np.std(inv_prof):<14.2f}{np.mean(inv_inv):<12.2f}{np.std(inv_inv):<14.2f}")
        print(f"{'Symmetric':<12}{np.mean(naive_prof):<12.2f}{np.std(naive_prof):<14.2f}{np.mean(naive_inv):<12.2f}{np.std(naive_inv):<14.2f}")

if __name__ == "__main__":
    print("=== Paper replication ===")
    run_gamma_experiment([0.01, 0.1, 0.5])
    print("\n=== Stress test (extreme risk aversion) ===")
    run_gamma_experiment([1, 5, 10])   
