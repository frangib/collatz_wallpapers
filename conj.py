# Playing around with 3x+1 conjecture:
import matplotlib.pyplot as plt
import pandas as pd
import os


N = 100000      # Max computed seed is 10.000.000   
FIG_WIDTH = 10
FIG_HEIGHT = 7
HIST_BINS = 100

notOne = True
counter = 0
filename = str(N)+".csv"
seeds = []
counters = []

# If a file already contains the info for a higher N, use that file.
# Otherwise, compute the new .csv for N.
files = os.listdir()
maxValueComputated = 0
for f in files:
    if f.__contains__(".csv"):
        aux = int(f.split(".")[0])
    if aux > maxValueComputated:
        maxValueComputated = aux

if maxValueComputated > N:
    filename = str(maxValueComputated)+".csv"
    df_seedCount = pd.read_csv(filename)
    seeds = df_seedCount["seed"][0:N]
    counters = df_seedCount["counter"][0:N]
else:
    print("No file contains such a high seed")
    for i in range(N):
        next = i + 1
        seeds.append(next)
        print("Seed: {}".format(next))

        while notOne:
            if next % 2 != 0:
                next = 3 * next + 1
            else:
                next = next / 2
            if next == 1:
                notOne = False
            counter += 1

        print("Counter: {}".format(counter))
        
        counters.append(counter)
        notOne = True
        counter = 0

    df_seedCount = pd.DataFrame(columns=["seed","counter"])
    df_seedCount["seed"] = seeds
    df_seedCount["counter"] = counters
    df_seedCount.to_csv(filename)
    
plt.figure(figsize=(FIG_WIDTH,FIG_HEIGHT))
#plt.scatter(seeds,counters, s = 3, marker='o', c='r')
plt.semilogx(seeds,counters, c='r')
plt.grid()
plt.xlabel("Seed")
plt.ylabel("Length of path")
plt.show()


plt.figure(figsize=(FIG_WIDTH,FIG_HEIGHT))
plt.hist(counters,bins=HIST_BINS)
plt.xlabel("counter")
plt.ylabel("frequency")
plt.show()