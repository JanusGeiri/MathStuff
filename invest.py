import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from varname import nameof


init_investment = 1_000_000
exp_inflation = 0.03
tax = 0.21


class Asset:
    def __init__(self, com=0, init_com=0, std_dev=0.1, mean=0.02, r_min=None, r_max=None, cut_minmax=False):
        self.com = com
        self.init_com = init_com
        self.r_min = r_min
        self.r_max = r_max
        self.std_dev = std_dev
        self.center = mean
        self.cut_minmax = cut_minmax
        if self.r_min == None or self.r_max == None:
            self.r_min = None
            self.r_max = None
            self.cut_minmax = False

    def __str__(self):
        string = '\nInformation about Asset\n' + '----------------------\n'
        string += 'Yearly commision: ' + '{:.2%}'.format(self.com)
        string += '\nInitial commision: ' + '{:.2%}'.format(self.init_com)
        string += '\nMean: ' + '{:.2%}'.format(self.center)
        string += '\nStandard deviation: ' + '{:.2%}'.format(self.std_dev)
        return string

    def info(self):
        print(self)

    def simulate(self, init_investment, sim_time=3, total_sims=100_000, print_result=False):
        all_profits = []
        for _ in range(total_sims):

            value = [0 for i in range(sim_time+1)]
            value[0] = init_investment*(1-self.init_com)

            for i in range(1, sim_time+1):
                rate = np.random.normal(loc=self.center, scale=self.std_dev)
                if self.cut_minmax:
                    rate = max(rate, self.r_min)
                    rate = min(rate, self.r_max)
                value[i] = value[i-1]*(1-self.com)*(1+rate)
                if rate < -1:
                    value[i] = 0

            profit = (value[sim_time]-init_investment)*(
                1-tax) if value[sim_time] > init_investment else value[sim_time]-init_investment
            all_profits.append(profit)
        losses = [profit for profit in all_profits if profit < 0]
        tap = len(losses)
        if print_result:
            exp_profit = 'Expected profit: ' + \
                "{:,.2f} kr".format(np.mean(all_profits))
            prob_tap = '{:.2%}'.format(tap/total_sims)
            exp_loss = 'Expected loss ' + \
                "{:,.2f} kr".format(np.mean(losses)) + \
                ' with probability of ' + prob_tap
            print(exp_profit)
            print(exp_loss + '\n')
        return np.mean(all_profits), np.mean(losses), tap/total_sims, value


m = 0.2
V = Asset(com=0.0257, init_com=0.015, std_dev=0.2, mean=m)
I = Asset(com=0.013, init_com=0.005, std_dev=0.02, mean=0.05)
III = Asset(com=0.0199, init_com=0.01, std_dev=0.05, mean=0.1)

VC = Asset(0, 0, std_dev=5, mean=-0.7)

T = 5

v1 = V.simulate(1_000_000, sim_time=T, print_result=True)[3]
v2 = I.simulate(1_000_000, sim_time=T, print_result=True)[3]

plt.plot(range(len(v1)), v1, label='Asset V')
plt.plot(range(len(v2)), v2, label='Asset I')
plt.legend(loc=2)
plt.show()


# # VC.simulate(init_investment, print_result=True, sim_time=10)

# cash = 1_000_000
# T = 40
# # c1, l1, p1, v1 = V.simulate(cash, print_result=True, sim_time=T)
# # I.simulate(init_investment, print_result=True, sim_time=3)
# c2, l2, p2, v2 = III.simulate(400000, print_result=True, sim_time=1)

# inflated = [cash*(1+exp_inflation)**i for i in range(T+1)]
# test = [cash*(1+m)**i for i in range(T+1)]

# totalprofit = 'Expected profit: ' + "{:,.2f} kr".format(c1+c2)
# prob_tap = '{:.2%}'.format(p1+p2)
# exp_loss = 'Expected loss ' + \
#     "{:,.2f} kr".format(l1+l2) + \
#     ' with probability of ' + prob_tap
# print(totalprofit)
# print(exp_loss)

# plt.plot(range(len(v1)), v1)
# plt.plot(range(len(inflated)), inflated)
# plt.plot(range(len(v1)), test)
# plt.show()

# def gen_array(size,num_members):

# def f(total_investment, risk_tolerance, *Assets):
#     num_Assets = len(*Assets)
#     sims = 1
#     for k in range(sims):
