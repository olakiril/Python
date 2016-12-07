
def gabor(size, lambda_, theta, sigma, phase, trim=.005):

    """Create a Gabor Patch

    size : int
        Image size (n x n)

    lambda_ : int
        Spatial frequency (px per cycle)

    theta : int or float
        Grating orientation in degrees

    sigma : int or float
        gaussian standard deviation (in pixels)

    phase : float
        0 to 1 inclusive
    """

    import numpy as np
    # make linear ramp
    X0 = (np.linspace(1, size, size) / size) - .5

    # Set wavelength and phase
    freq = size / float(lambda_)
    phaseRad = phase * 2 * np.pi

    # Make 2D grating
    Xm, Ym = np.meshgrid(X0, X0)

    # Change orientation by adding Xm and Ym together in different proportions
    thetaRad = (theta / 360.) * 2 * np.pi
    Xt = Xm * np.cos(thetaRad)
    Yt = Ym * np.sin(thetaRad)
    grating = np.sin(((Xt + Yt) * freq * 2 * np.pi) + phaseRad)

    # 2D Gaussian distribution
    gauss = np.exp(-((Xm ** 2) + (Ym ** 2)) / (2 * (sigma / float(size)) ** 2))

    # Trim
    gauss[gauss < trim] = 0

    return grating * gauss