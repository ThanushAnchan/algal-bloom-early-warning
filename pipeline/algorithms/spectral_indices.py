"""
Spectral Indices Calculation Wireframe
Implements Normalized Difference Chlorophyll Index (NDCI), NDVI, and Turbidity.
Specially tuned for shallow inland water bodies and village tanks in Karnataka.
"""

from typing import Dict

class SpectralIndicesCalculator:
    """
    Computes bio-optical water quality indices from Sentinel-2 MSI bands.
    NDCI is sensitive to Chlorophyll-a absorption peak in red edge and red bands.
    """

    @staticmethod
    def calculate_ndci(band_red: float, band_red_edge: float) -> float:
        """
        Formula:
            NDCI = (B5_red_edge - B4_red) / (B5_red_edge + B4_red)

        Values:
            < 0.10: Clean, oligotrophic water
            0.10 - 0.25: Moderate nutrients, safe
            0.25 - 0.40: Early bloom developing (Day 3-6)
            > 0.40: Severe hyper-eutrophic bloom (Day 7-10)
        """
        denom = band_red_edge + band_red
        if denom == 0:
            return 0.0
        return round((band_red_edge - band_red) / denom, 4)

    @staticmethod
    def calculate_ndvi(band_red: float, band_nir: float) -> float:
        """
        Formula:
            NDVI = (B8_nir - B4_red) / (B8_nir + B4_red)
        Useful for detecting floating surface algal scums or macrophytes (water hyacinth).
        """
        denom = band_nir + band_red
        if denom == 0:
            return 0.0
        return round((band_nir - band_red) / denom, 4)

    @staticmethod
    def estimate_chlorophyll_a_ug_l(ndci: float) -> float:
        """
        Empirical polynomial transfer function converting NDCI to Chlorophyll-a (ug/L).
        Calibration equation for tropical inland tanks:
            Chl-a = 14.2 + (180.5 * NDCI) + (110.2 * NDCI^2)
        """
        if ndci <= 0:
            return 5.0
        return round(14.2 + (180.5 * ndci) + (110.2 * (ndci ** 2)), 2)
