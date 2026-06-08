import numpy as np
from agent import Agent
from market import Market

class Simulator:
    def __init__(self, n_simulations, agent, market):
        self.n_simulations = n_simulations
        self.agent = agent
        self.market = market