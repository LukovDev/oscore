//
// core.h - Заголовочный файл ядра.
//


#include "types.h"
#include "avr.h"


void delay(double ms);                   // Функция задержки времени.
void led_active(char pin, bool active);  // Функция для управления активностью светодиода.
