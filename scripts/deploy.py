from brownie import SimpleStorage, accounts


def deploy_simple_storage():
    # Select account
    account = accounts[0]
    # Deploy the Smart Contract
    simple_storage = SimpleStorage.deploy({"from": account})
    # retrive the stored value
    stored_value = simple_storage.retrieve()
    print(stored_value)
    # Store a value to the contract
    transaction = simple_storage.store(15, {"from": account})
    # wait the number of block
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
