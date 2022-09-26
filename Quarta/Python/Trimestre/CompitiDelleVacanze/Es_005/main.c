#include <stdio.h>
#include <stdlib.h>
//legge il numero
int leggiN(int n, char frase[]) {
    do {
        printf("%s", frase);
        scanf("%d", &n);
    } while(n <= 0);
    return n;
}
//legge il carattere
char leggiC(char frase[]) {
    char car;
    printf("%s",frase);
    fflush(stdin);
    scanf("%c",&car);
    return car;
}
//funzione stampa
void stampa(char car, int num) {
    for(int i = 0; i < num; i++)
        printf("%c",car);
}
//stampa il quadrato
void stampaQuadrato(char car, int num) {
    for(int i = 0; i < num; i++) {
        stampa(car,num);
        printf("\n");
    }
}
//main
int main() {
    int n = 0;
    char c;
    n = leggiN(n,"Insersci un numero non negativo: ");
    c = leggiC("Insersci un carattere: ");
    stampaQuadrato(c,n);
    printf("\n");
    system("PAUSE");
    return 0;
}
//fine programma