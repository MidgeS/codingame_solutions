from enum import Enum
from rules.movingRules import MovingRules
from rules.shootingRules import ShootingRules
from rules.throwingRules import ThrowingRules
from rules.hunkerDownRules import HunkerDownRules

class RuleType(Enum):
    MOVING = 0
    SHOOTING = 1
    THROWING = 2
    HUNKER_DOWN = 3

def getRulesHandler(rule_type: RuleType):
    match rule_type:
        case RuleType.MOVING:
            return MovingRules()
        case RuleType.SHOOTING:
            return ShootingRules
        case RuleType.THROWING:
            return ThrowingRules
        case RuleType.HUNKER_DOWN:
            return HunkerDownRules
