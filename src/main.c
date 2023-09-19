//
// main.c - Основной файл. Пишите тут свой код.
//


// INCLUDES:
#include <lib.h>


// DEFINES:
#define LED_PIN 17


// Один раз:
void setup() {
    pin_mode(LED_PIN, OUTPUT);  // Делаем пин светодиода выходным.
}


// Цикл:
void loop() {
    digital_write(LED_PIN, true);  // Включаем светодиод.
    delay(500);                    // Пауза 1/2 сек.

    digital_write(LED_PIN, false); // Выключаем светодиод.
    delay(500);                    // Пауза 1/2 сек.
}
