def main():
    str = input("inserisci una frase: ")
    k = int(input("numero: "))
    str = str.upper()
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","Z"," "]
    strcrp = ""
    for x in range(len(str)):
        for y in range(len(alfabeto)):
            if(alfabeto[y] == str[x]):
                if((y + k) >= len(alfabeto)):
                    strcrp += alfabeto[(y + k)%k] 
                else:
                    strcrp += alfabeto[y + k] 
    print(f"originale = {str}\ncriptato = {strcrp}")
    f = open("./crypto.txt","w")
    f.write(f"{strcrp}\n{k}")
    f.close()    


if __name__=="__main__":
    main()
#se creo una lista globale non possso modificarla
