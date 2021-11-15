import os

from brownie import accounts


def deploy_simple_storage():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)

def main():
    deploy_simple_storage()
