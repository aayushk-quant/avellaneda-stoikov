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

def plot_inventory_paths(all_inv_paths, naive_all_inv_paths, T):
    avg_inv_path = np.mean(np.abs(np.array(all_inv_paths)), axis = 0)
    naive_avg_inv_path = np.mean(np.abs(np.array(naive_all_inv_paths)), axis = 0)
    if len(naive_avg_inv_path) != len(avg_inv_path):
        raise ValueError('To compare the simulations must be the same')
    time = np.linspace(0, T, len(avg_inv_path))
    plt.figure(figsize=(10, 6))
    plt.plot(time, avg_inv_path, label='Inventory strategy')
    plt.plot(time, naive_avg_inv_path, label='Symmetric strategy')
    plt.xlabel('Time')
    plt.ylabel('Average absolute inventory')
    plt.legend()
    plt.show()
