from dataclasses import dataclass

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, * args, ** kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

@dataclass
class VestConfig(metaclass = SingletonMeta):
    config_name: str = ""
    num_samples: int = 0

    def displayVestConfig(self):
        print("config name: {}".format(self.config_name))
        print("num samples: {}".format(self.num_samples))
