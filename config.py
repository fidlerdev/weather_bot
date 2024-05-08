from dataclasses import dataclass
from json import load

@dataclass
class _Config:
    weather_token: str
    bot_token: str

@dataclass
class _KBText:
    weather_by_geo: str
    weather_by_city: str

def get_config() -> _Config:
    return _Config(**load(open("config.json")))

def get_kb_text() -> _KBText:
    return _KBText(**load(open("keyboard_text.json")))