from configparser import ConfigParser
import configparser
from pathlib import Path
from os.path import basename

class Configuration:
    _parser: configparser
    _use_heavy_data: bool

    @property
    def int_array(self) -> list[int]: return self._get_int_array()

    def __init__(self) -> None:
        self._parser = self._build_parser(self._get_cfg_path())
        self._load_conf()

    def _build_parser(self, cfg_path: Path) -> ConfigParser:
        parser = ConfigParser()
        parser.read(cfg_path)
        return parser

    def _get_cfg_path(self) -> Path:
        cfg_path = Path.joinpath(Path(__file__).parent, basename(__file__).replace(".py", ".cfg"))
        if not Path.exists(cfg_path):
            raise Exception("cfg file not found")
        return cfg_path.resolve()

    def _load_conf(self) -> None:
        use_heavy_data = self._parser["CONF"]["use_heavy_data"].lower()
        self._use_heavy_data = use_heavy_data in ["true", "yes", "1"]

    def _build_data_path(self, dile_name: str) -> Path:
        return Path.joinpath(Path(__file__).parent, "data", dile_name).resolve()

    def _read_data(self, path: Path) -> str:
        with open(path, "r") as file:
            return [line for line in file if "#" not in line][0]

    def _get_int_array(self) -> list[int]:
        data_file = "int_array.big" if self._use_heavy_data else "int_array.small"
        data_path = self._build_data_path(data_file)
        data = self._read_data(data_path)
        return [int(n) for n in data.split(",")]
