from enum import Enum

class TileType(Enum):
    EMPTY = 0
    LOW_COVER = 1
    HIGH_COVER = 2

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        if self.__class__ is int:
            return self < other.value
        if other.__class__ is int:
            return self.value < other
        return NotImplemented
    
    def __gt__(self, other):
        if self.__class__ is other.__class__:
            return self.value > other.value
        if self.__class__ is int:
            return self > other.value
        if other.__class__ is int:
            return self.value > other
        return NotImplemented
    
    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        if self.__class__ is int:
            return self == other.value
        if other.__class__ is int:
            return self.value == other
        return NotImplemented