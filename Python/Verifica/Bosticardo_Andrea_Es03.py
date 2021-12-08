ip_address= ["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
f = open("./mask.txt","w")
for x in range (len(ip_address)):
    num = ip_address[x].split("/") #cosí  lo posso fare anche se l'ip non finisce con 0
    f.write(f"/{num[-1]}\n")#aggiungo alla fine lo /
f.close()