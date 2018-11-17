from scipy.special import fresnel
from ..path import Path


class EulerSpiral(Path):

    def __init__(self, rate, center, bound):
        super().__init__(rate)
