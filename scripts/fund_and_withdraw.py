from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def fund():
    if len(FundMe) <= 0:
        fund_me = deploy_fund_me()
    else:
        fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() + 100
    print(entrance_fee)
    print(f"The current entrance fee is: {entrance_fee}")
    print("Funding...")
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    return fund_me.addressToAmountFunded(account.address)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)
    return fund_me.addressToAmountFunded(account.address)


def main():
    fund()
    withdraw()
