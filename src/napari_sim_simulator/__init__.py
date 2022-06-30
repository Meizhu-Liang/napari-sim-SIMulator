__version__ = "0.0.1"
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
__author__ = "Meizhu Liang"
__email__ = "meizhu.liang18@imperial.ac.uk"


from ._widget import SIMulator_widget
