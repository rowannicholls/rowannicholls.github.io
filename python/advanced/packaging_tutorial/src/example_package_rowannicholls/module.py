"""Content of the example_package_rowannicholls package."""
import numpy as np


def spud_gun_firing_distance(v_0, r_y0, theta):
    """
    Determine the distance a spud gun fires.

    https://en.wikipedia.org/wiki/Equations_of_motion
    Uniform acceleration in a straight line
    v_1 = a * t + v_0
    r_1 = r_0 + v_0 * t + 0.5 * a * t**2
    r_1 = r_0 + 0.5 * (v_1 + v_0) * t
    v_1**2 = v_0**2 + 2 * a * (r_1 - r_0)
    r_1 = r_0 + v_1 * t - 0.5 * a * t**2

    >>> spud_gun_firing_distance(10, 125, 0)
    50.48187773461522
    >>> spud_gun_firing_distance(10, 0, 53 * np.pi / 180))
    9.79879404626217
    >>> spud_gun_firing_distance(25, 60, 53 * np.pi / 180)
    90.19528515377786
    """
    v_x0 = v_0 * np.cos(theta)  # m/s
    v_y0 = v_0 * np.sin(theta)  # m/s
    r_x0 = 0  # m
    r_y1 = 0  # m
    a_x = 0  # m/s²
    a_y = -9.81  # m/s²

    # r_y1 = r_y0 + v_y0 * t + 0.5 * a_y * t**2
    # 0 = (r_y0 - r_y1) + v_y0 * t + 0.5 * a_y * t**2
    a = 0.5 * a_y
    b = v_y0
    c = r_y0 - r_y1
    # Only take the positive root
    t1 = (-b + np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    t2 = (-b - np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    if t1 > t2:
        t = t1  # s
    else:
        t = t2  # s

    # r_1 = r_0 + v_0 * t + 0.5 * a * t**2
    r_x1 = r_x0 + v_x0 * t + 0.5 * a_x * t**2  # m

    return r_x1


# distance = spud_gun_firing_distance(10, 125, 0)
# print(distance)
# distance = spud_gun_firing_distance(10, 0, 53 * np.pi / 180)
# print(distance)
# distance = spud_gun_firing_distance(25, 60, 53 * np.pi / 180)
# print(distance)
