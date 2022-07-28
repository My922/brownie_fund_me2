from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from scripts.fund_and_withdraw import fund, withdraw
from brownie import network, accounts, exceptions
import pytest


def test_fund_and_withdraw():
    fund_me = deploy_fund_me()
    tx1 = fund()
    assert tx1 == fund_me.getEntranceFee() + 100
    tx2 = withdraw()
    assert tx2 == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
