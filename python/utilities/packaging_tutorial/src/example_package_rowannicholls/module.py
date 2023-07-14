"""Content of the example_package_rowannicholls package."""
import numpy as np


def spud_gun_firing_distance(v_0, r_y0, theta):
    """
    Determine the distance that a spud gun fires.

    Projectile motion with uniform acceleration in a straight line (downwards)
    is described by the following equations:

    - Equation 1: v_1 = a * t + v_0
    - Equation 2: r_1 = r_0 + v_0 * t + 0.5 * a * t**2
    - Equation 3: r_1 = r_0 + 0.5 * (v_1 + v_0) * t
    - Equation 4: v_1**2 = v_0**2 + 2 * a * (r_1 - r_0)
    - Equation 5: r_1 = r_0 + v_1 * t - 0.5 * a * t**2

    See https://en.wikipedia.org/wiki/Equations_of_motion

    Parameters
    ----------
    v_0 : float
        Initial velocity.
    r_y0 : float
        Initial y position (height about the ground).
    theta : float
        Angle of inclination in **radians**.

    Examples
    --------
    >>> spud_gun_firing_distance(10, 125, 0)
    50.48187773461522
    >>> spud_gun_firing_distance(10, 0, 53 * np.pi / 180)
    9.79879404626217
    >>> spud_gun_firing_distance(27, 1.8, 58 * np.pi / 180)
    67.89755324030912
    """
    # Known variables
    v_x0 = v_0 * np.cos(theta)  # m/s
    v_y0 = v_0 * np.sin(theta)  # m/s
    r_x0 = 0  # m
    r_y1 = 0  # m
    a_x = 0  # m/s²
    a_y = -9.81  # m/s²

    # Equation 5
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

    # Equation 2
    r_x1 = r_x0 + v_x0 * t + 0.5 * a_x * t**2  # m

    return r_x1


def _test():
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    _test()
