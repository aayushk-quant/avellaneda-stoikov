import numpy as np
import pytest

from agent import Agent
from market import Market
from simulator import Simulator

def test_reservation_price_formula():
    agent = Agent(inventory=5, cash=0, sigma=2, gamma=0.1, T=1, k=1.5)

    result = agent.reservation_price(s=100, t=0.25)

    expected = 100 - 5 * 0.1 * (2 ** 2) * (1 - 0.25)
    assert result == pytest.approx(expected)

def test_optimal_spread_decreases_over_time():
    agent = Agent(inventory=0, cash=0, sigma=2, gamma=0.1, T=1, k=1.5)

    spread_start = agent.optimal_spread(t=0)
    spread_mid = agent.optimal_spread(t=0.5)
    spread_end = agent.optimal_spread(t=1)

    assert spread_start > spread_mid > spread_end

def test_seed_reproducibility():
    agent = Agent(0, 0, 2, 0.1, 1, 1.5)
    market = Market(1.5, 140, 100, 2, 0.005)
    simulator = Simulator(100, agent, market)

    result_1 = simulator.market_simulation(seed=42)
    result_2 = simulator.market_simulation(seed=42)

    assert result_1 == result_2

def test_inventory_strategy_has_lower_inventory_risk_than_symmetric_strategy():
    agent = Agent(0, 0, 2, 0.1, 1, 1.5)
    market = Market(1.5, 140, 100, 2, 0.005)
    simulator = Simulator(1000, agent, market)

    inv_final_inventory, _, _ = simulator.market_simulation(seed=42)
    naive_final_inventory, _, _ = simulator.market_simulation(naive=True, seed=42)

    assert np.std(inv_final_inventory) < np.std(naive_final_inventory)