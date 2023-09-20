//
// main.c - Основной файл. Пишите тут свой код.
//


// INCLUDES:
#include <lib.h>
#include "func.h"


// DEFINES:
#define LED_PIN 17


// Один раз:
void setup() {
    pin_mode(LED_PIN, OUTPUT);  // Делаем пин светодиода выходным.
}


// Цикл:
void loop() {
    turn_on(LED_PIN);   // Включаем светодиод.
    delay(500);         // Пауза 1/2 сек.

    turn_off(LED_PIN);  // Выключаем светодиод.
    delay(500);         // Пауза 1/2 сек.
}
