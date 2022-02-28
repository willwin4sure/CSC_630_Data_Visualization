import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('data/harvard_dataverse_metadata_flipped.csv')

time = np.array(df['time'])

# for cat in ["agr","arts","astro","busin","chem","cs","earth","engin","law","math","med","phys","ss"]:
for cat in ["agr","astro","busin","chem","cs","earth","engin","math","med","phys"]:
    cat_data = np.array(df[cat])
    plt.plot(time, cat_data, '-o', label=cat)

plt.legend()

plt.savefig('orientation3.png')