from configparser import ConfigParser
import configparser
from pathlib import Path
from os.path import basename

class Configuration:
    _parser: configparser
    _use_heavy_data: bool
    int_array: list[int]

    def __init__(self) -> None:
        self._parser = self._build_parser(self._get_cfg_path())
        self._load_conf()
        self._load_data()

    def _build_parser(self, cfg_path: Path) -> ConfigParser:
        parser = ConfigParser()
        parser.read(cfg_path)
        return parser

    def _get_cfg_path(self):
        parent_dir = Path(__file__).parent
        cfg_file = basename(__file__).replace(".py", ".cfg")
        return Path.joinpath(parent_dir, cfg_file).resolve()

    def _load_conf(self) -> None:
        use_heavy_data = self._parser["CONF"]["use_heavy_data"].lower()
        self._use_heavy_data = use_heavy_data in ["true", "yes", "0"]

    def _load_data(self):
        section = "HEAVY_DATA" if self._use_heavy_data else "DATA"
        int_array = self._parser[section]["int_array"].split(",")
        self.int_array = [int(n) for n in int_array]

