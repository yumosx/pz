import dataclasses
from typing import Dict, Any

import yaml

class ConfigProvider:
    def __init__(self, path: str):
        self.config_path = path
        self._config = None
    def load_config(self) -> Dict[str, any]:
        if self._config is None:
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self._config = yaml.safe_load(f)
            except yaml.YAMLError as e:
                raise RuntimeError(f"ConfigProvider | open | {self.config_path} - {str(e)}")
            except Exception as e:
                raise RuntimeError(f"ConfigProvider | open | {self.config_path} - {str(e)}")
        return self._config

@dataclasses.dataclass
class CacheConfig:
    cache_name: str

@dataclasses.dataclass
class DatabaseConfig:
    db_host: str
    db_port: int
    db_username: str
    db_password: str
    db_database: str
    db_charset: str = ""
    db_extras: str = ""
    sqlalchemy_database_uri_scheme: str = "postgresql"
    sqlalchemy_pool_size: int = 30
    sqlalchemy_max_overflow: int = 10
    sqlalchemy_pool_recycle: int = 3600
    sqlalchemy_pool_pre_ping: bool = False
    sqlalchemy_echo: bool = False


    @classmethod
    def form_dict(cls, config_dict: Dict[str, Any]) -> 'DatabaseConfig':
        return cls(
            db_host=config_dict.get('db_host', ''),
            db_port=config_dict.get('db_port', 5432),
            db_username=config_dict.get('db_username', ''),
            db_password=config_dict.get('db_password', ''),
            db_database=config_dict.get('db_database', ''),
            db_charset=config_dict.get('db_charset', ''),
            db_extras=config_dict.get('db_extras', ''),
            sqlalchemy_database_uri_scheme=config_dict.get('sqlalchemy_database_uri_scheme', 'postgresql'),
            sqlalchemy_pool_size=config_dict.get('sqlalchemy_pool_size', 30),
            sqlalchemy_max_overflow=config_dict.get('sqlalchemy_max_overflow', 10),
            sqlalchemy_pool_recycle=config_dict.get('sqlalchemy_pool_recycle', 3600),
            sqlalchemy_pool_pre_ping=config_dict.get('sqlalchemy_pool_pre_ping', False),
            sqlalchemy_echo=config_dict.get('sqlalchemy_echo', False)
        )


def db_config(path) -> DatabaseConfig:
    config = ConfigProvider(path)
    dic_config = config.load_config().get("database")
    return DatabaseConfig.form_dict(dic_config)


if __name__ == "__main__":
    c = db_config("./config.yaml")
    print(c)