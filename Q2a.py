from sys import exit
from bitcoin.core.script import *

from lib.utils import *
from lib.config import (my_private_key, my_public_key, my_address,
                    faucet_address, network_type)
from Q1 import send_from_P2PKH_transaction


######################################################################
# Complete the scriptPubKey implementation for Exercise 2
Q2a_txout_scriptPubKey = [
        OP_2DUP,
        OP_ADD,
        664,
        OP_EQUALVERIFY,
        OP_SUB,
        9404,
        OP_EQUAL # at the end of ScriptPK, there needs to be a 1 on the stack in order for the transaction to succeed
    ]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # set these parameters correctly
    amount_to_send = 0.00005 # amount of BTC in the output you're sending minus fee
    txid_to_spend = (
        'cd3917ad4bddba7dec90a967c41129b7060fc4bb343122bf3819c92db8b344b5')
    utxo_index = 1 # index of the output you are spending, indices start at 0
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
