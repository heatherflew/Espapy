from astropy.io import ascii
from lib import set_attributes
from . import header_access
from . import column_names
from . import order_splitting


class DataFile:

    def __init__(self, file_path, file_line_num_of_first_data=3):
        self.header_info = header_access.get_header_info(file_path)

        total_num_columns = self.header_info["num_additional_columns"] + 1
        data_column_names = column_names.generate_column_names(total_num_columns)

        self.whole_data = ascii.read(
            file_path,
            format='basic',
            data_start=file_line_num_of_first_data - 1,
            names=data_column_names
        )

        self.spectral_orders = order_splitting.split_into_spectral_orders(self.whole_data)

    def total_num_orders(self):
        return len(self.spectral_orders)
