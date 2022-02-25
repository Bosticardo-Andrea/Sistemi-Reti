import Quadrato as q

def main():
    quadrato = q.Quadrato(1,1,50)
    print(f"area: {quadrato.getArea()} perimetro: {quadrato.getPerimetro()}")
    if quadrato.IsAppartiene(10,20):
        print("é esterno del quadrato")
    else:
        print("é interno del quadrato")
    quadrato.Draw()
if __name__ =="__main__":
    main()