## Ideally, they have one file with the settings for the strat and deployment
## This file would allow them to configure so they can test, deploy and interact with the strategy
from dotmap import DotMap

WANT = "0xbcab7d083Cf6a01e0DdA9ed7F8a02b47d125e682" ## "wBTC/renBTC"
TARGET_VAULT = "0xb6d63a4e5ca740e96c26adabcac73be78ee39dc5"
BADGER_DEV_MULTISIG = "0x4c56ee3295042f8A5dfC83e770a21c707CB46f5b"
WHALE = "0xc009bc33201a85800b3593a40a178521a8e60a02"
sett_config = DotMap(
    native = DotMap(
        StrategyGenericSolidexDCA = DotMap(
            WANT = WANT,  
            TARGET_VAULT = TARGET_VAULT,
            WHALE = WHALE
        )
    )
)

## Fees in Basis Points
DEFAULT_GOV_PERFORMANCE_FEE = 1500
DEFAULT_PERFORMANCE_FEE = 0
DEFAULT_WITHDRAWAL_FEE = 10

FEES = [DEFAULT_GOV_PERFORMANCE_FEE, DEFAULT_PERFORMANCE_FEE, DEFAULT_WITHDRAWAL_FEE]

BADGER_TREE = "0x89122c767A5F543e663DB536b603123225bc3823"

REGISTRY = "0xFda7eB6f8b7a9e9fCFd348042ae675d1d652454f"  # Multichain BadgerRegistry
