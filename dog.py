import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def calc(R):
    a = -24.
    b = (16. * R + 4. * np.pi * R)
    c = -np.pi * R**2

    x = (-b + np.sqrt(b**2 - 4 * a * c)) / (2 * a)

    r = R - 4 * x
    return (R, r, x)


# R = 16.4
for i in range(1000):
    R = i / 50.
    # print "({:0.2f},\t{:0.2f}, \t{:0.2f})".format(*calc(R))

R=16.3
_, r, s = calc(R)

fig = plt.figure() # figsize=(8,8))
ax=plt.subplot(aspect='equal')

#plot one circle (the biggest one on bottom-right)
# plt.scatter(0, 0, s, 'b')
size = 50 * s
base_color = "lightgray"

for k, color in enumerate(["magenta", "cyan", "yellow", "lightgreen"]):
# for k, color in enumerate(["red"]):
    angles_r = np.array([(k * np.pi / 2) + (i * s / r) for i in range(-1, 3)])
    x = r * np.cos(angles_r)
    y = r * np.sin(angles_r)
    plt.scatter(x, y, size, base_color)

    angles_R = np.array([(np.pi / 4) + (k * np.pi / 2) + (i * s / R) for i in range(-2, 3)])
    x = R * np.cos(angles_R)
    y = R * np.sin(angles_R)
    plt.scatter(x, y, size, base_color)

    angles_R_home = np.array([(np.pi / 4) + (k * np.pi / 2) + ((i+.5) * s / R) for i in range(3, 7)])
    x = R * np.cos(angles_R_home)
    y = R * np.sin(angles_R_home)
    plt.scatter(x, y, size, color)

    i = 2
    angles_R_last = (np.pi / 4) + (k * np.pi / 2) + (i * s / R)
    x = R * np.cos(angles_R_last)
    y = R * np.sin(angles_R_last)
    plt.scatter(x, y, size, color)

    i = -2
    angles_r_2 = ((k+1) * np.pi / 2) + (i * s / r)
    # import ipdb; ipdb.set_trace()
    x = r * np.cos(angles_r_2)
    y = r * np.sin(angles_r_2)
    plt.scatter(x, y, size, base_color)

    a_R = angles_R[3]
    kat = np.sqrt((s**2)/2)
    r_mid = kat + 2 * s + r
    offset = R - r_mid - s
    x = (r_mid + offset) * np.cos(a_R)
    y = (r_mid + offset) * np.sin(a_R)
    plt.scatter(x, y, size, color)

    for i in range(3):
        a_R = angles_R[2]
        r_mid = i*s+r + offset
        x = r_mid * np.cos(a_R)
        y = r_mid * np.sin(a_R)
        plt.scatter(x, y, size, color)

        a_R = angles_R[0]
        a_r = angles_r[3]

        x_R = R * np.cos(a_R)
        x_r = r * np.cos(a_r)
        x_diff = (x_R - x_r)

        y_R = R * np.sin(a_R)
        y_r = r * np.sin(a_r)
        y_diff = (y_R - y_r)

        x = np.array([1, 2, 3]) * x_diff / 4 + x_r
        y = np.array([1, 2, 3]) * y_diff / 4 + y_r
        plt.scatter(x, y, size, base_color)

        a_R = angles_R_last
        a_r = angles_r_2
        x_R = R * np.cos(a_R)
        x_r = r * np.cos(a_r)
        x_diff = (x_R - x_r)

        y_R = R * np.sin(a_R)
        y_r = r * np.sin(a_r)
        y_diff = (y_R - y_r)

        x = np.array([1, 2, 3]) * x_diff / 4 + x_r
        y = np.array([1, 2, 3]) * y_diff / 4 + y_r
        plt.scatter(x, y, size, base_color)

font = FontProperties()
font.set_family("fantasy")
plt.text(0.5, 0.5, 'WILHELMSEN\'S\nDOG', horizontalalignment='center',
         verticalalignment='center',
         transform=ax.transAxes, color=base_color, fontproperties=font)

plt.axis('off')
# plt.show()
filename = "dog.pdf"
plt.savefig(filename, bbox_inches='tight', pad_inches=0)
print filename
