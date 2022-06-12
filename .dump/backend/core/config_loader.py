import glob
import pathlib
import sys

import dotenv

from backend.commons.enums import Config
from backend.utils import config_utils


def _detect_home_location() -> pathlib.Path:
    """Detects the location of the root directory"""

    # path/to/home/backend/core/config_loader.py
    path_to_self = pathlib.Path(__file__).absolute()

    # path/to/home/backend/core/
    path_to_core_module = path_to_self.parent

    # path/to/home/backend/
    path_to_backend_module = path_to_core_module.parent

    # path/to/home/
    path_to_home = path_to_backend_module.parent

    return path_to_home


def init_configs() -> None:
    """Initialize All Configurations"""

    # Load home directory
    config_utils.write_config(Config.APP.HOME, _detect_home_location())

    # Load Configurations
    for conf_file in glob.glob(
            pathname=f'{config_utils.read_config(Config.APP.HOME)}/configurations/*.conf',
    ):
        dotenv.load_dotenv(dotenv_path=conf_file, override=False)

    # Add home dir to python path
    sys.path.append(config_utils.read_config(Config.APP.HOME))
