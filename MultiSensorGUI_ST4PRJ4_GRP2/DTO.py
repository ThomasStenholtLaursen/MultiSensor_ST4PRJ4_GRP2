from dataclasses import dataclass, astuple, asdict

@dataclass 
class ForceSensorDTO:
    right: int
    left: int
    top: int
    bottom: int

@dataclass 
class SettingsDTO:
    force_right: int
    force_left: int
    force_top: int
    force_bottom: int
    light_sensor: int
    temperature_sensor: int

@dataclass
class LightTempDTO:
    light: int
    temp: int

