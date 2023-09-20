//
// func.c - Вспомогательный файл для main.
//


// INCLUDES:
#include <lib.h>


// Включаем светодиод:
void turn_on(byte pin) {
    digital_write(pin, true);
}


// Выключаем светодиод:
void turn_off(byte pin) {
    digital_write(pin, false);
}
