import json
from typing import Dict, Any, Optional

class ConfigManager:
    """
    Loads and caches a JSON configuration file.
    """
    def __init__(self, config_file: str) -> None:
        self.config_file = config_file
        self._config: Optional[Dict[str, Any]] = None

    def get(self) -> Dict[str, Any]:
        if self._config is None:
            with open(self.config_file, "r") as f:
                self._config = json.load(f)
        return self._config

    def reload(self) -> Dict[str, Any]:
        """Force reload of the configuration file."""
        with open(self.config_file, "r") as f:
            self._config = json.load(f)
        return self._config
