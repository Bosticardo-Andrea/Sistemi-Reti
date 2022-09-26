f = open("./file.txt","w")
f.write("\n ciao a tutti")

f = open("./file.txt","r")
righe = f.readlines()
print(righe)

f.close()