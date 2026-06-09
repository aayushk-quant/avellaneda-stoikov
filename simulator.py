from agent import Agent
from market import Market

class Simulator:
    def __init__(self, n_simulations, agent, market):
        self.n_simulations = n_simulations
        self.agent = agent
        self.market = market
    def market_simulation(self, naive = False, record_path = False):
        initial_inventory = self.agent.inventory
        initial_cash = self.agent.cash
        initial_mid_price = self.market.mid_price
        initial_wealth = initial_cash + initial_inventory * initial_mid_price
        final_inv = []
        final_prof = []
        final_mid_price = []
        path_data = None
        for n in range(self.n_simulations):
            inventory = initial_inventory
            cash = initial_cash
            bid_path = []
            ask_path = []
            reservation_path = []
            self.agent.inventory = initial_inventory
            self.agent.cash = initial_cash
            self.market.mid_price = initial_mid_price
            sim_q = []
            sim_x = []
            sim_s = []
            for i in range(int(self.agent.T / self.market.dt)):
                if not naive:
                    bid, ask = self.agent.optimal_bid_ask(self.market.mid_price, self.market.dt * i)
                else:
                    bid, ask = self.agent.naive_bid_ask(self.market.mid_price, self.market.dt * i)
                bid_path.append(bid)
                ask_path.append(ask)
                reservation_path.append(self.agent.reservation_price(self.market.mid_price, self.market.dt * i))
                sim_s.append(self.market.mid_price)
                bid_draw, ask_draw = self.market.order_arrival(bid, ask)
                if bid_draw:
                    inventory += 1
                    cash -= bid
                if ask_draw:
                    inventory -= 1
                    cash += ask
                self.agent.inventory = inventory
                self.agent.cash = cash
                sim_q.append(inventory)
                sim_x.append(cash)
                self.market.mid_price_update()
            final_wealth = cash + inventory * self.market.mid_price
            final_inv.append(inventory)
            final_prof.append(final_wealth - initial_wealth)
            final_mid_price.append(self.market.mid_price)
            if n == 0 and record_path:
                path_data = sim_q, sim_x, sim_s, bid_path, ask_path, reservation_path
        self.agent.inventory = initial_inventory
        self.agent.cash = initial_cash
        self.market.mid_price = initial_mid_price
        if record_path:
            return final_inv, final_prof, final_mid_price, path_data
        else:
            return final_inv, final_prof, final_mid_price