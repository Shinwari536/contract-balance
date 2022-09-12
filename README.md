# ****** Account ******
acc name = myAcSha
Contract address: 0x07fbb12300da79641e3ea7a1374bdba79576b172bc5e7c9d62561823a30b3c85
Public key: 0x00ee7476218a9f659b41dccccbbd3a2eab1bbd7e3b86b62663ced5b5ced0b94c
Transaction hash: 0x213e352ed34d7ff63e3abb03b41ae7d7ef76689ce306b78681effeb94a660de


# ******  Declare Contract on Goerli ******
starknet declare --contract num_compiled.json --account myAcSha

Declare transaction was sent.
Contract class hash: 0x68704d18de8ccf71da7c9761ee53efd44dcfcfd512eddfac9c396e7d175e234
Transaction hash: 0x140904acdaad1e41eb036ad1be95229813583b8738df87d6d2c93fcf2f4d84f

# ******   Deploy Contract on Goerli   ******
starknet deploy --class_hash 0x68704d18de8ccf71da7c9761ee53efd44dcfcfd512eddfac9c396e7d175e234 --account=myAcSha

Invoke transaction for contract deployment was sent.
Contract address: 0x06d425a7fa9d38c03a7bced43cf8d171a45e8c7027c0bd806f8ca9706c4a3a3d
Transaction hash: 0x90f3d5c5651f20ddd9cf8d113bc2f078ef4e67a093efe27fa4efc0b8ca2749

# ******   Interaction with Contract on Goerli   ******
1)
starknet call --address ${CONTRACT_ADDRESS} --abi abi.json --function get_balance

0 ---> since by default the value is zero

2)
starknet invoke --address ${CONTRACT_ADDRESS} --abi abi.json --function increase_balance --inputs 13455 --account myAcSha

Sending the transaction with max_fee: 0.000000 ETH.
Invoke transaction was sent.
Contract address: 0x06d425a7fa9d38c03a7bced43cf8d171a45e8c7027c0bd806f8ca9706c4a3a3d
Transaction hash: 0x3bf190223b52be890f4542ac136d1307bf1eb37f7b6241d62ed56a502b821c8

3)
starknet call --address ${CONTRACT_ADDRESS} --abi abi.json --function get_balance

13445 ---> It is the input we gave in the last command. (0 + 13445 = 13445)

4)
starknet invoke --address ${CONTRACT_ADDRESS} --abi abi.json --function increase_balance --inputs 10000 --account myAcSha

Sending the transaction with max_fee: 0.000000 ETH.
Invoke transaction was sent.
Contract address: 0x06d425a7fa9d38c03a7bced43cf8d171a45e8c7027c0bd806f8ca9706c4a3a3d
Transaction hash: 0x32710c0332211dbe339da73a8136014b19e67d7c728079f97343bb3e96dcb1a

5)
starknet call --address ${CONTRACT_ADDRESS} --abi abi.json --function get_balance

23455 ---->>>  It is because of the input we gave in the last command. (13445 + 10000  = 23455)

6)
# Estimate fee
You can estimate the fee of a given transaction before executing it by adding the --estimate_fee flag to the invoke or declare commands. This will simulate the transaction and return the estimated fee associated with it. The result is presented in WEI and ETH, as shown below. 
Note: With the --estimate_fee flag, the state of the contracts does not change. For example, the following code will not affect the balance stored in BALANCE_CONTRACT.

To estimate the fee of a given transaction run the following:

starknet invoke --address 0x06d425a7fa9d38c03a7bced43cf8d171a45e8c7027c0bd806f8ca9706c4a3a3d --abi abi.json --function increase_balance --inputs 10000 --account myAcSha --network alpha-goerli --estimate_fee

The estimated fee is: 49169705469 WEI (0.000000 ETH).
Gas usage: 3867
Gas price: 12715207 WEI

# ****** Last transaction on Voyager ****** 
https://goerli.voyager.online/tx/0x32710c0332211dbe339da73a8136014b19e67d7c728079f97343bb3e96dcb1a