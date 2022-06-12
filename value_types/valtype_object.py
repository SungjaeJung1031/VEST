from dataclasses import dataclass
from enum import Enum, IntEnum

from value_types.valtype_rdr_prop import EnumRdrPos


class EnumRefPnt(IntEnum):
    FRONT_CENTER    = 0     # front center  
    FRONT_LEFT      = 1     # front left
    MID_LEFT        = 2     # mid left
    REAR_LEFT       = 3     # rear left
    REAR_CENTER     = 4     # rear center
    REAR_RIGHT      = 5     # rear right
    MID_RIGHT       = 6     # mid right                 
    FRONT_RIGHT     = 7     # front right
    UNK             = 8     # unknown


class EnumObjType(IntEnum):
    PED                 = 0     # pedestrians
    VEH_SHORT_RNG       = 1     # short range vehicle, e.g. sedan, SUV
    VEH_LONG_RNG        = 2     # long range vehicle, e.g. truck, bus
    ANIMAL              = 3     # animal
    ROAD_BOUNDARY       = 4     # road boundary
    ROAD_EDGE           = 5     # road edge
    ROAD_BARRIER        = 6     # road barrier
    TRAFFIC_OBSTACLES   = 7     # road obstacles, e.g. traffic corns
    BRIDGE              = 8     # bridge
    TUNNEL              = 9     # tunnel
    UNK                 = 10    # unknown


class EnumObjStat(IntEnum):
    STATIONARY  = 0     # stationary
    MOVABLE     = 1     # movable
    MOVING      = 2     # moving
    UNK         = 3     # unknown


@dataclass
class DataclsObject:
    id: int           = int(0)      # [n/a] id of an object
    pos_lat: float    = float(0.0)  # [m] lateral position of an object
    pos_long: float   = float(0.0)  # [m] longitudinal position of an object
    pos_vert: float   = float(0.0)  # [m] vertical position of an object
    len: float        = float(0.0)  # [m] length of an object
    width: float      = float(0.0)  # [m] width of an object
    height: float     = float(0.0)  # [m] height of an object
    yawrate: float    = float(0.0)  # [rad/s] yaw-rate of an object
    velocity: float   = float(0.0)  # [m/s] velocity of an abject
    accel: float      = float(0.0)  # [m/s^2] acceleration of an object
    confid: float     = float(0.0)  # [prob] (0~1) confidence of an object

    status: EnumObjStat = EnumObjStat.UNK   # [enum] status of an object
    type: EnumObjType   = EnumObjType.UNK   # [enum] type of an object
    ref_pnt: EnumRefPnt = EnumRefPnt.UNK    # [enum] reference point of an object
    rdr_pos: EnumRdrPos = EnumRdrPos.UNK    # [enum] position of a radar which makes the object's information