import time
import string

secret = b'\x0e6/+y;.< x-(7,,\xf0z48z:646<z*\x9a\xf3(64+<{'

def chiffre_xor(msg, cle):
    while len(cle) != len(msg):
	    coef = len(msg) - len(cle)
	    if coef > 0:
		    calc = coef % len(cle)
		    cle += cle[calc]
	    else:
		    cle = cle[:-1]
    msg, cle = msg.encode(), cle.encode()
    return bytes(msg[i] ^ cle[i] for i in range(len(msg)))

def force():
    alphabet = list(string )
    
print(chiffre_xor("test", 'cle'))

