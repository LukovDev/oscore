//
// lib.c - Заголовочный файл библиотеки по умолчанию.
//


// INCLUDES:
#include "types.h"
#include "avr.h"


// FUNCTIONS:
void delay(double ms);                   // Функция задержки времени.
void led_active(char pin, bool active);  // Функция для управления активностью светодиода.
