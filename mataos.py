import sys
from math import gcd
from functools import reduce

Dic={}
ABC=[]

EN_REL_FREQ = {'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.12702, 'F': 0.02228, 'G': 0.02015,
               'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,
               'Ñ': 0.00000, 'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
               'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074}


ES_REL_FREQ = { 'A': 0.11525,'B': 0.02215,'C': 0.04019,'D': 0.05010,'E': 0.12181,'F': 0.00692,'G': 0.01768,'H': 0.01973,
                'I': 0.06247,'J': 0.02493,'K': 0.00011,'L': 0.04967,'M': 0.03157,'N': 0.06712,'Ñ': 0.00311,'O': 0.08683,
                'P': 0.02510,'Q': 0.00877,'R': 0.06871,'S': 0.07977,'T': 0.04632,'U': 0.03927,'V': 0.01138,'W': 0.00017,
                'X': 0.00515,'Y': 0.01433,'Z': 0.00467}

FR_REL_FREQ = { 'A': 0.07636,'B': 0.00901,'C': 0.03260,'D': 0.03669,'E': 0.14715,'F': 0.01066,'G': 0.00866,'H': 0.00737,
                'I': 0.07529,'J': 0.00613,'K': 0.00074,'L': 0.05456,'M': 0.02968,'N': 0.07095,'Ñ': 0.00000,'O': 0.05796,
                'P': 0.02521,'Q': 0.01362,'R': 0.06693,'S': 0.07948,'T': 0.07244,'U': 0.06311,'V': 0.01838,'W': 0.00049,
                'X': 0.00427,'Y': 0.00128,'Z': 0.00326}

CastLet="EAOSNR"

def createDictionary(letters):
    ABC.clear()
    for i in range(0,len(letters)):
        Dic[letters[i]]=i
        ABC.append(letters[i])

def searchDuplicates(text,blocksize=2):
    used=[]
    distances=[]
    for i in range(0,len(text)-blocksize+1):
        if not(i in used):
            for j in range(i+blocksize,len(text)-blocksize+1):
                if(text[i:i+blocksize]==text[j:j+blocksize]):
                    #print(text[i:i+blocksize]," ",text[j:j+blocksize]," ",j-i)
                    used.append(j)
                    for x in range(1,blocksize):
                        used.append(j+x)
                        used.append(i+x)
                    distances.append(j-i)
    aux=distances[0]
    for i in distances:
        #print(aux, " " , i)
        aux=gcd(aux,i)
    if ((blocksize>(len(text)/2)) | (aux>1)):
      #  print("Clave de lonxitude",aux)
        return aux
    else:
        return searchDuplicates(text,blocksize+1)

def separar(text,n):
    Clave=""
    separations=[]
    
    for i in range(0,n):
        separations.append([0]*len(ABC))
        
    for i in range(0,len(text)):
        separations[i % n][Dic[text[i]]]+=1
        
    #print("\nFrecuencias:")
    
    for frec in separations:
        info=""
        for i in range(0,len(frec)):
            info+= ABC[i] + ":"+str(frec[i])+", "
        #print(info,"\n")
        maxFrec=0
        pos=0
        leng=""
        for j in range(0,len(frec)):
            aux=0
            for letter in ABC:
                aux+=frec[(j+Dic[letter]) % len(ABC)]*ES_REL_FREQ[letter]
            if(aux>maxFrec):
                maxFrec=aux
                pos=j
                leng="Castelan"
        for j in range(0,len(frec)):
            aux=0
            for letter in ABC:
                aux+=frec[(j+Dic[letter]) % len(ABC)]*EN_REL_FREQ[letter]
            if(aux>maxFrec):
                maxFrec=aux
                pos=j
                leng="Inglés"
        for j in range(0,len(frec)):
            aux=0
            for letter in ABC:
                aux+=frec[(j+Dic[letter]) % len(ABC)]*FR_REL_FREQ[letter]
            if(aux>maxFrec):
                maxFrec=aux
                pos=j
                leng="Francés"
        Clave+=ABC[pos]

    print("A clave é", Clave)
    #print("A clave é ",Clave," e o texto está en ",leng)



def attack(abc,t):
    createDictionary(abc)            

    large = searchDuplicates(t)

    separar(t,large)


def read_file(file_path):
    abecedario2="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            attack(abecedario2,content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python mataos.py <file_path>")
        sys.exit(1)

    file_path = args[1]
    read_file(file_path)




abecedario1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                
                

