MOD = 256
def KSA(key): #Key-Scheduling Algorithm
    key_length = len(key) #prendo la lunghezza della chiave
    S,j = list(range(MOD)),0  # creo  l'array S da 0 a 255]
    for i in range(MOD):
        #print(j,S[i],i,key[i % key_length],MOD,key_length)
        j = (j + S[i] + key[i % key_length]) % MOD
        S[i], S[j] = S[j], S[i]  # swap dei valori
    return S


def PRGA(S): #Pseudo-Random Generation Algorithm
    i,j = 0,0
    while True:
        i = (i + 1) % MOD
        j = (j + S[i]) % MOD
        S[i], S[j] = S[j], S[i]  # swap dei valori
        K = S[(S[i] + S[j]) % MOD]
        yield K
def get_keystream(key):
    S = KSA(key)
    return PRGA(S)

def encrypt(key, plaintext):
    text = [ord(c) for c in plaintext] #rendo la stringa(testo da crittografare) una lista di caratteri ascii
    key = [ord(c) for c in key] #rendo la stringa(key) una lista di caratteri ascii 
    keystream = get_keystream(key)
    res = []
    for c in text:
        val = chr((c ^ next(keystream)))
        res.append(val)
    return ''.join(res)


def decrypt(key, ciphertext):
    text = ciphertext
    print(text)
    key = [ord(c) for c in key] #rendo la stringa(key) una lista di caratteri ascii 
    keystream = get_keystream(key)
    res = []
    for c in text:
        val = chr((ord(c) ^ next(keystream)))
        res.append(val)
    res = ''.join(res)
    return res


def main():
    key = 'Chiave'  #chiave
    plaintext = 'Ciao, come va?'  # testo in chiaro
    print('plaintext:', plaintext)
    print('ciphertext:',  encrypt(key, plaintext))#testo criptato
    print('decrypted:', decrypt(key, encrypt(key, plaintext)))#testo decriptato
#assert --> controlla se restituisce TRUE
if __name__ == '__main__':
    main()