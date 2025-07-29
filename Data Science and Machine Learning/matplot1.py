import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

# Functional style plotting
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.plot(x, y, label='Sine Wave', color='blue')
# plt.title('Sine Wave Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.xlim(0, 10)
# plt.ylim(-1, 1)
# plt.legend()
# plt.grid(True)

# plt.subplot(1, 2, 2)
# plt.plot(x, z, label='Cosine Wave', color='red')
# plt.title('Sine Wave Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.xlim(0, 10)
# plt.ylim(-1, 1)
# plt.legend()
# plt.grid(True)

# plt.show()


# Object-oriented style plotting
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(x, y, label='Sine Wave', color='blue')
# ax.set_title('Sine Wave Example')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_xlim(0, 10)
# ax.set_ylim(-1, 1)
# ax.legend()
# ax.grid(True)
# plt.show()

# Object-oriented style plotting with multiple subplots
# fig, axs = plt.subplots(1, 2, figsize=(10, 5), sharex=True, sharey=True)
# axs[0].plot(x, y, label='Sine Wave', color='blue')
# axs[0].set_title('Sine Wave Example')
# axs[0].set_xlabel('X-axis') 
# axs[0].set_ylabel('Y-axis')
# axs[0].set_xlim(0, 10)
# axs[0].set_ylim(-1, 1)
# axs[0].legend()
# axs[0].grid(True)
# axs[1].plot(x, z, label='Cosine Wave', color='red')
# axs[1].set_title('Cosine Wave Example')
# axs[1].set_xlabel('X-axis')
# axs[1].set_ylabel('Y-axis')
# axs[1].set_xlim(0, 10)
# axs[1].set_ylim(-1, 1)
# axs[1].legend()
# axs[1].grid(True)
# plt.show()


# Figure in figure
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(x, y, label='Sine Wave', color='blue')
# inset_ax = fig.add_axes([0.15, 0.15, 0.3, 0.3])  # [left, bottom, width, height]
# inset_ax.plot(x, z, label='Cosine Wave', color='red')
# inset_ax.set_title('Cosine Wave Example')
# inset_ax.set_xlabel('X-axis')
# inset_ax.set_ylabel('Y-axis')
# inset_ax.set_xlim(0, 10)
# inset_ax.set_ylim(-1, 1)
# inset_ax.legend()
# inset_ax.grid(True)
# ax.set_title('Sine Wave Example')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_xlim(0, 10)
# ax.set_ylim(-1, 1)
# ax.legend()
# ax.grid(True)
# plt.show()

# Interate over axes
# fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# for ax in axs:    
#     ax.plot(x, y, label='Sine Wave', color='blue')
#     ax.set_title('Sine Wave Example')
#     ax.set_xlabel('X-axis')
#     ax.set_ylabel('Y-axis')
#     ax.set_xlim(0, 10)
#     ax.set_ylim(-1, 1)
#     ax.legend()
#     ax.grid(True) 
# plt.show()


# fig, ax = plt.subplots(1,2)
# ax[0].plot(x, y, label='Sine Wave', color='blue')
# plt.tight_layout()
# plt.show()

#save the figure
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(x, y, label='Sine Wave', color='blue')
# ax.set_title('Sine Wave Example')
# ax.set_xlabel('X-axis')
# ax.set_ylabel('Y-axis')
# ax.set_xlim(0, 10)
# ax.set_ylim(-1, 1)
# ax.legend(loc=0)  # loc=0 automatically chooses the best location for the legend
# ax.grid(True)
# plt.savefig('sine_wave_example.png', dpi=300, bbox_inches='tight')  # Save the figure with high resolution
# plt.show()  # Display the plot
# # Note: The 'bbox_inches' parameter ensures that the saved figure does not have extra whitespace

fig, ax = plt.subplots(1,2, figsize=(10, 5))
ax[0].plot(x, y, label='Sine Wave', color='blue', linewidth=2, linestyle='--')  # Customizing line style and width
ax[0].set_title('Sine Wave Example')    
ax[1].plot(x, z, label='Cosine Wave', color='red', 
           linewidth=2, linestyle='-.', alpha=0.5, marker = 'o', markersize = 10,
           markerfacecolor = 'green', markeredgecolor = 'yellow')  # Customizing line style and width
plt.show()