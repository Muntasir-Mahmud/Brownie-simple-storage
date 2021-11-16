from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]  # -1 is to get the latest deployed contract

def main():
    read_contract()
