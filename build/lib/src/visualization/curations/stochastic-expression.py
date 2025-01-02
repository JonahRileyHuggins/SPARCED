#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script name: stochastic-expression.py
Author: Jonah R. Huggins
Created on: Tues. Dec. 3rd 23:46:00 2024

Description: Script to plot results of the Stochastic-Expression Benchmark. 
This script is only compatible with the Stochastic-Expression Benchmark.

While a user can run this script from the command line, it is recommended to
use the `sparced` CLI tool to run this script.

Usage:
`sparced visualize -i path/to/data.pkl -o path/to/output -n file_name`

"""
import os 
import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Import fixed path to the src directory
try: 
    sys.path.append(os.path.join(os.getcwd(), 'src'))

except FileNotFoundError:
    print('The system cannot find the specified src code path, verify the \
          stochastic-expression.py script is in the `curations` directory.')
    sys.exit(1)

from utils.arguments import parse_args
from datetime import datetime

# Parse command line arguments
args = parse_args()

def stochastic_expression(data_path: str, output_path: str = os.getcwd(),
                          file_name: str = ('stochastic-expression'+ datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
                          ) -> None:
    
    """Plot the stochastic expression of the model
    
    Parameters
    - data_path (str): path to the data file
    - output_path (str): path to the output file
    - file_name (str): name of the output file
    
    Returns
    - None
    """

    with open(data_path, 'rb') as f: 
        data = pickle.load(f)

    fig, ax = plt.subplots(4, 1, figsize=(5, 7))

    benchmark1_key = [key for key in data.keys()][0]

    ax[0].plot(data[benchmark1_key]['time']/3600.0,
        data[benchmark1_key][''],'b',linewidth=4)

    ax[0].grid(True)
    ax[0].set_xlim(0, 24)
    ax[0].set_xticks([])
    ax[0].set_yticklabels(ax[0].get_yticks(), fontsize=16, weight='bold')

    ax[1].plot(data[benchmark1_key]['toutS']/3600.0,
                    data[benchmark1_key]['xoutG'][:,116],'r',linewidth=4)
    ax[1].grid(True)
    ax[1].set_xlim(0, 24)
    ax[1].set_xticks([])
    ax[1].set_yticklabels(ax[0].get_yticks(), fontsize=16, weight='bold')

    mRNA_MAPK1_2mpc = (data[benchmark1_key]['MAPK1_mRNA']*
                    (1/(1.0E9/(5.2500E-12*6.023E+23))))
    mRNA_MAPK3_2mpc = (data[benchmark1_key]['MAPK3_mRNA']*
                    (1/(1.0E9/(5.2500E-12*6.023E+23))))

    ax[2].plot(data[benchmark1_key]['MAPK3_mRNA']/3600.0,
            mRNA_MAPK1_2mpc,'b',linewidth=4)
    ax[2].grid(True)
    ax[2].set_xlim(0, 24)

    ax[2].set_xticks([])
    ax[2].set_yticklabels(ax[0].get_yticks(), fontsize=16, weight='bold')

    ax[2].yaxis.get_offset_text().set_fontsize(24)
    ax[2].yaxis.get_offset_text().set_weight('bold')

    ax[2].plot(data[benchmark1_key]['toutS']/3600.0,mRNA_MAPK3_2mpc,
            'r',linewidth=4)

    ax[3].plot(data[benchmark1_key]['toutS']/3600.0,
            data[benchmark1_key]['ERK_total'],'k',linewidth=4, 
            color = 'purple')

    ax[3].set_xlabel('Time (hrs)')
    ax[3].set_ylabel('total ERK (nM)', multialignment='center')
    ax[3].grid(True)
    ax[3].set_xlim(0, 24)
    ax[3].set_xticklabels(np.arange(0,25,step=4), fontsize=16)

    # For setting x-tick properties
    ax[3].tick_params(axis='both', labelsize=16)
    ax[3].tick_params(axis='y', labelsize=16)

    plt.savefig(f'{output_path}/{file_name}.png')

stochastic_expression(args.input_data, args.output, args.name)
