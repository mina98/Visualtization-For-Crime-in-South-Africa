import matplotlib.pyplot as plt

x = range(10)
y = range(10)

fig, ax = plt.subplots(nrows=2, ncols=2)

for row in ax:
    print(ax)
    for col in row:
        col.plot(x, y)

plt.show()