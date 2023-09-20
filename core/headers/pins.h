//
// pins.h - Заголовочный файл с функциями для работы с пинами.
//


#ifndef _PINS_H
#define _PINS_H

// DEFINES:
#define INPUT  0  // Вход.
#define OUTPUT 1  // Выход.


// FUNCTIONS:
void pin_mode(uchar pin, uchar mode);       // Функция установки режима пина (INPUT - вход, OUTPUT - выход).

void digital_write(uchar pin, bool value);  // Функция записи в цифровой выходной пин (false - LOW, true - HIGH).
uchar digital_read(uchar pin);              // Функция чтения из цифрового входного пина (false - LOW, true - HIGH).

void analog_write(uchar pin, uchar value);  // Функция записи в аналоговый выходной пин (PWM).
ushort analog_read(uchar pin);              // Функция чтения значения аналогового входа.

#endif
