from enum import Enum


class SiteType(str, Enum):
    LAND = "Land"
    DEEPWATER = "Deepwater"
    SHALLOW_WATER = "Shallow Water"
    SWAMP = "Swamp"
