from starkware.crypto.signature.signature import (
    pedersen_hash, private_to_stark_key, sign)
from starkware.starknet.public.abi import get_storage_var_address

balance_key = get_storage_var_address('balance') # in our ContractBalance contract we have a storage variable "balance"
print(f'Balance key: {balance_key}')