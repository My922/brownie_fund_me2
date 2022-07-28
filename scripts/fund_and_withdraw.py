from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
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
