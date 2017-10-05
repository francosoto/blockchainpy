# -*- coding: utf-8 -*-
import redis, hashlib, json, sys, random
# I dont know where are your Redis server! 
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)


def hashMe(msg=""):
    # For convenience, this is a helper function that wraps our hashing algorithm
    if type(msg)!=str:
        msg = json.dumps(msg,sort_keys=True)  # If we don't sort keys, we can't guarantee repeatability!
        
    if sys.version_info.major == 2:
        return unicode(hashlib.sha256(msg).hexdigest(),'utf-8')
    else:
        return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

hashTransaction = hashMe('hola')
r.set('tran_' + hashTransaction, unicode('Soy una transacción','utf-8'))
print unicode('Nueva transacción: ','utf-8') + hashTransaction

# import random
random.seed(0)

# def makeTransaction(document,cert):
#     date = datetime.time
# 	  signlenght = strlen(pkcs11)
#     return {u'datetime':datetime.time,u'md5file':md5,u'initsign':asd,u'signlenght':signlenght}

# txnBuffer = [makeTransaction() for i in range(30)]

def isValidSign(txn,state):
    # Assume that the transaction is a dictionary keyed by account names

    # Check that the sum of the deposits and withdrawals is 0
    if sum(txn.values()) is not 0:
        return False
    
    # Check that the transaction does not cause an overdraft
    for key in txn.keys():
        if key in state.keys(): 
            acctBalance = state[key]
        else:
            acctBalance = 0
        if (acctBalance + txn[key]) < 0:
            return False
    
    return True