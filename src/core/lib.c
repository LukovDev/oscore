//
// lib.c - Библиотека по умолчанию.
//


// INCLUDES:
#include "lib.h"


// Функция задержки времени:
void delay(double ms) {
    while (0 < ms) { _delay_ms(1); ms--; }
}


// Активность светодиода:
// TODO: Переделать. Работает явно неправильно:
void led_active(char pin, bool active) {
    if (active) { PORTB |= 1 << pin;    }
    else        { PORTB &= ~(1 << pin); }
}
