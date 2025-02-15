import pickle
import numpy as np

with open('TRAIL_time-to-death.pkl', 'rb') as f:
    data = pickle.load(f)

traildoses = np.array([0.000385, 0.001925, 0.00385, 0.01925, 0.0385, 0.1925, 0.385, 1.9250, 3.85, 19.25, 38.5])
dosesngperml = traildoses*2.597402597402597e+01

conditions =[]
for condition in data:
    conditions.append(condition)

legend = []
for dose in traildoses:
    legend.append('TRAIL ' + str(dose) + 'nM')
fig, axs = plt.subplots(1, 2, figsize=(12.5, 5))
for i in range(1,11,2):
    axs[1].plot(data[conditions[i]]['cell 0']['cPARP_total']['toutS']/3600, data[conditions[i]]['cell 0']['cPARP_total']['xoutS'], linewidth=4)
    axs[1].set_xlim([0, 60])
    axs[1].set_xticklabels(axs[1].get_xticks(), fontsize=16, weight='bold')
    axs[1].set_yticklabels(axs[1].get_yticks(), fontsize=16, weight='bold')
    legend_properties = {'weight':'bold', 'size':16}
    axs[1].legend(labels=legend, bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=16, frameon=False, prop=legend_properties)


time_of_death = CellDeathMetrics(data, 'cPARP_total').average_time_to_death()

axs[0].plot(np.log10(dosesngperml),[tod/3600 for tod in time_of_death.values()],marker='s',linewidth=4, color='red')
axs[0].set_xticklabels(axs[0].get_xticks(), fontsize=16, weight='bold')
axs[0].set_yticklabels(axs[0].get_yticks(), fontsize=16, weight='bold', rotation=60)
axs[0].grid(True)

# Set the x-axis label
axs[0].set_xlabel('log10(TRAIL concentration (ng/ml))', weight='bold', fontsize=20)
axs[1].set_xlabel('Time (hrs)', weight='bold', fontsize=20)

# Set the y-axis label
fig.text(0.025, 0.5, 'Time to Death (hrs)', va='center', rotation='vertical', weight='bold', fontsize=20)

fig.savefig('TRAIL_time-to-death.png', dpi=300, bbox_inches='tight')
