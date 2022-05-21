from dataclasses import dataclass, astuple, asdict

@dataclass 
class ForceSensorDTO:
    right: int
    left: int
    top: int
    bottom: int

@dataclass
class LightTempDTO:
    light: int
    temp: int

