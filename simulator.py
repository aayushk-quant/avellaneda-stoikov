from agent import Agent
from market import Market

class Simulator:
    def __init__(self, n_simulations, agent, market):
        self.n_simulations = n_simulations
        self.agent = agent
        self.market = market
    def market_simulation(self):
        initial_inventory = self.agent.inventory
        initial_cash = self.agent.cash
        initial_mid_price = self.market.mid_price
        initial_wealth = initial_cash + initial_inventory * initial_mid_price
        final_inv = []
        final_prof = []
        final_mid_price = []
        for _ in range(self.n_simulations):
            inventory = initial_inventory
            cash = initial_cash
            self.agent.inventory = initial_inventory
            self.agent.cash = initial_cash
            self.market.mid_price = initial_mid_price
            sim_q = []
            sim_x = []
            sim_s = []
            for i in range(int(self.agent.T / self.market.dt)):
                bid, ask = self.agent.optimal_bid_ask(self.market.mid_price, self.market.dt * i)
                bid_draw, ask_draw = self.market.order_arrival(bid, ask)
                if bid_draw:
                    inventory += 1
                    cash -= bid
                if ask_draw:
                    inventory -= 1
                    cash += ask
                self.agent.inventory = inventory
                sim_q.append(inventory)
                self.agent.cash = cash
                sim_x.append(cash)
                self.market.mid_price_update()
                sim_s.append(self.market.mid_price)
            final_wealth = cash + inventory * self.market.mid_price
            final_inv.append(inventory)
            final_prof.append(final_wealth - initial_wealth)
            final_mid_price.append(self.market.mid_price)
        return final_inv, final_prof, final_mid_price