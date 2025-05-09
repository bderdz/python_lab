import matplotlib.pyplot as plt
import numpy as np

month = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']
temp_war = [-2, -1, 3, 8, 14, 17, 20, 18, 13, 8, 3, 0]
temp_lon = [5, 5, 8, 11, 14, 17, 19, 19, 16, 12, 8, 6]
temp_war = np.array(temp_war)
temp_lon = np.array(temp_lon)
temp_diff = temp_war - temp_lon

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.set_size_inches(6, 12)
ax1.plot(month, temp_war, label="Warszawa", color="blue", marker="o")
ax1.plot(month, temp_lon, label="Londyn", color="green", marker="s")
ax1.legend()
ax2.bar(month, temp_diff, color=['red' if t < 0 else 'blue' for t in temp_diff])
sc = ax3.scatter(x=temp_war,
                 y=temp_lon,
                 c=temp_diff,
                 cmap='coolwarm',
                 vmin=-max(abs(temp_diff)),
                 vmax=max(abs(temp_diff)))
ax3.plot([min(temp_war.min(), temp_lon.min()), max(temp_war.max(), temp_lon.max())],
         [min(temp_war.min(), temp_lon.min()), max(temp_war.max(), temp_lon.max())], linestyle='--', label='y=x')
plt.colorbar(sc, ax=ax3)
ax3.legend()

plt.savefig("weather.png", dpi=300)
plt.show()
