import matplotlib.pyplot as plt
import numpy as np
import time

fig, ax = plt.subplots()

tstart = time.time()
num_plots = 0
while time.time()-tstart < 1:
    ax.clear()
    ax.imshow(np.random.randn(100,100))
    plt.pause(0.001)
    num_plots += 1
print(num_plots)
