//
// timer.c - Содержит функции для работы со временем.
//


// INCLUDES:
#include <lib.h>
#include <avr.h>


// Функция задержки времени:
void delay(ulong ms) {
    while (0 < ms) {
        _delay_ms(1);
        ms--;
    }
}
