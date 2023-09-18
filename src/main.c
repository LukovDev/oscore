//
// main.c - Основной файл. Пишите тут свой код.
//


// INCLUDES:
#include "core/lib.h"


// DEFINES:
#define LED_PIN 0


// Один раз:
void setup() {
    DDRB |= 1 << LED_PIN;  // Делаем пин светодиода выходным.
}


// Цикл:
void loop() {
    led_active(LED_PIN, true);   // Включаем светодиод.
    delay(500);                  // Пауза 1/2 сек.

    led_active(LED_PIN, false);  // Выключаем светодиод.
    delay(500);                  // Пауза 1/2 сек.
}
