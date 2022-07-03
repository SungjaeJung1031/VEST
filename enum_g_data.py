from enum import Enum

class ListLogDataType(str, Enum):
    EGO     = "ego",
    TRK     = "trk",
    DTCT    = "dtct"