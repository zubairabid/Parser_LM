import sys
import pickle
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np


with open('tokens_'+str(sys.argv[1]), 'rb') as f:
	tks = pickle.load(f)

counter = defaultdict(lambda: 0)
for tok in tks:
    counter[tok] += 1

sortdict = np.array(sorted(counter.items(), key=lambda v: v[1], reverse=True))

# plt.plot(np.arange(0., 2000., 5), (sortdict[:2000][:,1])[::5])
plt.plot((sortdict[:2000][:,0])[::10], (sortdict[:2000][:,1])[::10])
plt.xticks(rotation=-90)
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.show()