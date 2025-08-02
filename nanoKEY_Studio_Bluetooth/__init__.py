import Live
from .nanoKEY_Studio_Bluetooth import nanoKEY_Studio_Bluetooth


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return nanoKEY_Studio_Bluetooth(c_instance)

# local variables:
# tab-width: 4
