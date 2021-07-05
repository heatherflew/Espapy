import numpy as np
from lib.indexes_in_domain import get_indexes_in_domain
from lib.data_point import DataPoint


def get_intensities_in_domain(spectral_order, domain):
    indexes_in_domain = get_indexes_in_domain(spectral_order.wavelength_data(), domain)
    intensities = spectral_order.intensity_data()[indexes_in_domain]

    return intensities


def get_wavelengths_in_domain(spectral_order, domain):
    indexes_in_domain = get_indexes_in_domain(spectral_order.wavelength_data(), domain)
    wavelengths = spectral_order.wavelength_data()[indexes_in_domain]

    return wavelengths


def get_max_intensity_point_in_spectral_order_in_domain(spectral_order, domain):

    intensities_in_domain = get_intensities_in_domain(spectral_order, domain)
    wavelengths_in_domain = get_wavelengths_in_domain(spectral_order, domain)
    max_intensity_index_in_domain = np.argmax(intensities_in_domain)
    max_intensity = intensities_in_domain[max_intensity_index_in_domain]
    wavelength_at_max_intensity = wavelengths_in_domain[max_intensity_index_in_domain]

    max_intensity_point = DataPoint(wavelength_at_max_intensity, max_intensity)

    return max_intensity_point


def get_max_intensity_point_in_domain(data_file, domain):

    orders_in_domain = get_spectral_orders_in_domain(data_file, domain)
    max_intensity_per_order = []
    for order in orders_in_domain:
        max_intensity = get_max_intensity_point_in_spectral_order_in_domain(
            order,
            domain
        )
        max_intensity_per_order.append(max_intensity)
    overall_max_intensity = max(max_intensity_per_order)

    return overall_max_intensity


def get_spectral_orders_in_domain(datafile, domain):
    orders_in_domain = []

    for order in datafile.spectral_orders:
        if overlaps(order.wavelength_domain(), domain):
            orders_in_domain.append(order)

    return orders_in_domain


def overlaps(domain1, domain2):
    return domain1.minimum <= domain2.maximum and domain2.minimum <= domain1.maximum
