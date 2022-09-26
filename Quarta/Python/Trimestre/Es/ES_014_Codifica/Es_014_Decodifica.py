f = open("./crypto.txt","r")
righe = f.readlines()
str = righe[0]
k = int (righe[-1])
f.close()
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Z"," "]
strdcrp = ""
for x in range(len(str)):
    for y in range(len(alfabeto)):
        if(alfabeto[y] == str[x]):
            if((y - k) <= 0):
                strdcrp += alfabeto[(y-k)%len(alfabeto)] 
            else:
                strdcrp += alfabeto[y - k] 
print(f"originale = {str}decriptato = {strdcrp}")
