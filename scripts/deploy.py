from brownie import SimpleStorage, accounts, config, network


def deploy_simple_storage():
    # Select account
    account = get_account()
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


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
