#include <stdio.h>
int main (void) {
    int res = 0;
    int number = 12;
    while (number > 0) {
        res += number % 10;
        number = number/10;
    }
    printf("%i",res);
}
