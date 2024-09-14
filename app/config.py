import json


class Config:
    _config = None

    @classmethod
    def get_all(cls, filepath="app/config-model.json"):
        """Carga y devuelve todos los valores del archivo config-model.json."""
        if cls._config is None:
            with open(filepath, "r") as f:
                cls._config = json.load(f)
        return cls._config
