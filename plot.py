import matplotlib.pyplot as plt
import numpy as np

def plot_figure1(T, mid_price, res_price, bid, ask):
    n_steps = len(mid_price)
    time_axis = np.linspace(0, T, n_steps)
    plt.figure(figsize=(10, 6))
    plt.plot(time_axis, mid_price, label='Mid-market price', color='black')
    plt.plot(time_axis, res_price, label='Indifference price', color='green')
    plt.plot(time_axis, bid, label='Price bid', color='blue')
    plt.plot(time_axis, ask, label='Price asked', color='red')
    plt.xlabel('Time')
    plt.ylabel('Stock Price')
    plt.legend()
    plt.show()

def plot_figure2(profit_inv, profit_nai):
    plt.hist(profit_inv, bins = 50, alpha = 0.5, label = 'Inventory Strategy', color = 'blue')
    plt.hist(profit_nai, bins = 50, alpha = 0.5, label = 'Symmetric Strategy', color = 'red')
    plt.xlabel('Profit')
    plt.legend()
    plt.show()