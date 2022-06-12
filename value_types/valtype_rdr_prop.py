from enum import IntEnum

class EnumRdrPos(IntEnum):
    FRONT_CENTER    = 0     # front center  
    FRONT_LEFT      = 1     # front left
    MID_LEFT_A      = 2     # mid left (A)
    MID_LEFT_B      = 3     # mid left (B)
    MID_LEFT_C      = 4     # mid left (C)
    REAR_LEFT       = 5     # rear left
    REAR_CENTER     = 6     # rear center
    REAR_RIGHT      = 7     # rear right
    MID_RIGHT_A     = 8     # mid right (A)
    MID_RIGHT_B     = 9     # mid right (B)
    MID_RIGHT_C     = 10    # mid right (C)
    FRONT_RIGHT     = 11    # front right
    UNK             = 12    # unknown