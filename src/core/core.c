//
// core.c - Ядро.
//


// INCLUDES:
#include "core.h"
#include "shell.h"


// -------------------------------- Основной код: --------------------------------
// Основная функция ядра:
void core() {
    setup();  // Вызываем один раз.

    // Вечный цикл:
    while(true) {
        loop();  // Вызываем функцию-цикл.
    }
}


// -------------------------------- Прочие штуки: --------------------------------
// Своеобразная точка входа в ядро:
int main() { core(); return 0; }


// Функция задержки:
void delay(double ms) {
    while (0 < ms) { _delay_ms(1); ms--; }
}


// Активность светодиода:
void led_active(char pin, bool active) {
    if (active) { PORTB |= 1 << pin;    }
    else        { PORTB &= ~(1 << pin); }
}
