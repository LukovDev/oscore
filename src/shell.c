//
// shell.c - Файл оболочки. Пишите тут свой код.
//


// INCLUDES:
#include "core/core.h"


// DEFINES:
#define LED_PIN 0


// Один раз:
void setup() {
    DDRB |= 1 << LED_PIN;  // Делаем пин светодиода выходным.
}


// Цикл:
void loop() {
    led_active(LED_PIN, true);   // Включаем светодиод.
    delay(1000);                 // Пауза 1 сек.

    led_active(LED_PIN, false);  // Выключаем светодиод.
    delay(1000);                 // Пауза 1 сек.
}
