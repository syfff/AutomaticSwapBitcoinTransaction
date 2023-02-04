from sys import exit
from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


cust1_private_key = CBitcoinSecret(
    'cRaJRdNhmmnivCCL9QhRXLr7SeYP6ny6opRYaHHKLemxMwSDciQJ')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cQnqgUg5eg6Ar7c46tQeaRXuqx7H3KiT3kfsyF3azpKbucg1JVTK')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cSd6zABziiErTop2XGL6RLUN6GAcASr5mXm1NMjH5uLNNhPmNEcs')
cust3_public_key = cust3_private_key.pub


######################################################################
# Complete the scriptPubKey implementation for Exercise 3

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

Q3a_txout_scriptPubKey = [
        my_public_key,
        OP_CHECKSIGVERIFY, # have to add verify as don't want to leave 1 on the stack
        1,
        cust1_public_key,
        cust2_public_key,
        cust2_public_key,
        3,
        OP_CHECKMULTISIG
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    amount_to_send = 0.00005 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'cd3917ad4bddba7dec90a967c41129b7060fc4bb343122bf3819c92db8b344b5')
    utxo_index = 2 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(amount_to_send, txid_to_spend, 
        utxo_index, Q3a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
