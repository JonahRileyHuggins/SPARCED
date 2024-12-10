#!/bin/bash

import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt

with open('p53-dynamics.pkl', 'rb') as f:
    data = pickle.load(f)
conditions = ['1 nM', '4 nM', '10 nM', '25 nM']
fig, axes = plt.subplots(4,1, figsize=(8,6))
for i, condition in enumerate(data):
    ax = axes[i]
    for cell in data[condition]:
        ax.plot(data[condition][cell]['p53_pulse']['toutS']/3600, data[condition][cell]['p53_pulse']['xoutS'], label=cell, linewidth=4)
        ax.text(1.1, 0.5, conditions[i], horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=12, weight='bold')
        if condition == 'DamageDSB_1':
            ax.set_ylim(0, 20) 
        else:
            ax.set_ylim(0, 1500)
        # ax.set_title(condition)
        # ax.legend()
        ax.set_xlim(0, 30)
        ax.set_xticks([])
    if i==3:
        ax.set_xticks(np.arange(0, 31, step=5))
    
    ax.set_xticklabels(ax.get_xticks(), fontsize=16, weight='bold')
    ax.set_yticklabels(ax.get_yticks(), fontsize=16, weight='bold')
plt.subplots_adjust(hspace=0.5)
        # Set the x-axis label
axes[3].set_xlabel('Time (hrs)', weight='bold', fontsize=20)

# Set the y-axis label
fig.text(-0.01, 0.55, 'Active p53 (nM)', va='center', rotation='vertical', weight='bold', fontsize=20)
plt.tight_layout()
fig.savefig('p53-dynamics.png')
