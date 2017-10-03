# -*- coding: utf-8 -*-
import redis, hashlib, json, sys
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
print(unicode('Nueva transacción: ','utf-8') + hashTransaction)