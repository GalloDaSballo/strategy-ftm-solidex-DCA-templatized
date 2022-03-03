from config import (
    BADGER_DEV_MULTISIG,
    DEFAULT_GOV_PERFORMANCE_FEE,
    DEFAULT_PERFORMANCE_FEE,
    DEFAULT_WITHDRAWAL_FEE,
)
from config import sett_config
import pytest
from conftest import deploy


@pytest.mark.parametrize(
    "sett_id",
    sett_config.native,
)
def test_deploy_settings(sett_id):
    """
    Verifies that you set up the Strategy properly
    """
    config = sett_config.native[sett_id]
    deployed = deploy(config)
    
    strategy = deployed.strategy

    protected_tokens = strategy.getProtectedTokens()

    ## NOTE: Change based on how you set your contract
    assert protected_tokens[0] == strategy.want()
    assert protected_tokens[1] == strategy.SEX()
    assert protected_tokens[2] == strategy.SOLID()
    assert protected_tokens[3] == strategy.wFTM()
    assert protected_tokens[4] == strategy.token0() ## TODO Abstract
    assert protected_tokens[5] == strategy.token1()
    assert protected_tokens[6] == strategy.targetVault()
    assert protected_tokens[7] == strategy.targetVaultWant()
    assert protected_tokens[8] == strategy.targetVaultWantUnderlying0()
    assert protected_tokens[9] == strategy.targetVaultWantUnderlying1()

    assert strategy.governance() == BADGER_DEV_MULTISIG

    assert strategy.performanceFeeGovernance() == DEFAULT_GOV_PERFORMANCE_FEE
    assert strategy.performanceFeeStrategist() == DEFAULT_PERFORMANCE_FEE
    assert strategy.withdrawalFee() == DEFAULT_WITHDRAWAL_FEE
