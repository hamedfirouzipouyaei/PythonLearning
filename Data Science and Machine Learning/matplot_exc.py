import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y= x*2
z= x**2

# # Exercise 1:
# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # [left, bottom, width, height]
# ax1.plot(x, y)
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.set_title('title')

# plt.show()

# # Exercise 2:
# fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])  # [left, bottom, width, height]
# ax2 = fig.add_axes([0.2,0.5,.2,.2])  # [left, bottom, width, height]

# ax1.plot(x, y, label='Linear', color='red')
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.set_title('Linear Plot')
# ax2.plot(x, y, label='Linear', color='red')
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_title('Inset Linear Plot')
# plt.show()

# # Exercise 3:
# fig = plt.figure()
# ax1 = fig.add_axes([0,0,1,1])  # [left, bottom, width, height]
# ax2 = fig.add_axes([0.2,0.5,.4,.4])

# ax1.plot(x,z, label='Quadratic', color='blue')
# ax1.set_xlabel('X')
# ax1.set_ylabel('Z')
# ax1.set_title('Quadratic Plot')

# ax2.plot(x,y, label='Linear', color='red')
# ax2.set_xlabel('X')
# ax2.set_ylabel('Y')
# ax2.set_title('Inset Linear Plot')
# ax2.set_xlim(20, 22)
# ax2.set_ylim(30, 50)

# plt.show()

# # Exercise 4:
fig, axs = plt.subplots(1, 2, figsize=(10, 2))  # 1 row, 2 columns
axs[0].plot(x, y, label='Linear', color='red', linestyle='--')
axs[0].set_title('Linear Plot')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')
axs[0].set_xlim(0, 100)
axs[0].set_ylim(0, 200)
axs[1].plot(x, z, label='Quadratic', color='purple')
axs[1].set_title('Quadratic Plot')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')
axs[1].set_xlim(0, 100)
axs[1].set_ylim(0, 10000)
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()