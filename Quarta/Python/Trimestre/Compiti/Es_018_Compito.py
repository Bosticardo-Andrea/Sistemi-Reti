import random
lancio = {"alice":random.randint(1,6),"bob":random.randint(1,6)}

if(lancio["alice"] > lancio["bob"]):
    print(f"vinve alice con {lancio['alice']}")
else:
    print(f"vince bob con {lancio['bob']}")
