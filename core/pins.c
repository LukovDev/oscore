//
// pins.c - Создаёт функции для работы с пинами.
//


// INCLUDES:
#include <lib.h>
#include <avr.h>


// Функция установки режима пина (INPUT - вход, OUTPUT - выход):
// TODO: Проверить на работоспособность.
void pin_mode(uchar pin, uchar mode) {
    /*
    #define PORT_BASE_ADDRESS 0x20  // Базовый адрес порта.

    // Регистр DDR для управления режимом пина:
    volatile uchar *ddr_reg = (uchar *)(PORT_BASE_ADDRESS + 1);

    if (mode == OUTPUT)     { *ddr_reg |= (1 << pin);  }  // Установить бит для установки режима OUTPUT.
    else if (mode == INPUT) { *ddr_reg &= ~(1 << pin); }  // Сбросить бит для установки режима INPUT.
    */

    // Определяем порт и номер пина:
    volatile uchar *ddr;
    uchar bit;

    switch (pin / 8) {
        case 0:
            ddr = &DDRB;
            bit = pin % 8;
            break;
        case 1:
            ddr = &DDRC;
            bit = pin % 8;
            break;
        case 2:
            ddr = &DDRD;
            bit = pin % 8;
            break;

        // Добавьте код для других портов, если необходимо:
        default: return;
    }

    if (mode == 0) *ddr &= ~(1 << bit);  // Установка режима входа (бит 0).
    else           *ddr |= (1 << bit);   // Установка режима выхода (бит 1).
}


// Функция записи в цифровой выходной пин (false - LOW, true - HIGH):
// TODO: Проверить на работоспособность.
void digital_write(uchar pin, bool value) {
    // Определяем порт и номер пина:
    volatile uchar *port;
    uchar bit;

    switch (pin / 8) {
        case 0:
            port = &PORTB;
            bit = pin % 8;
            break;
        case 1:
            port = &PORTC;
            bit = pin % 8;
            break;
        case 2:
            port = &PORTD;
            bit = pin % 8;
            break;

        // Добавьте код для других портов, если необходимо:
        default: return;
    }

    if (value) *port |= (1 << bit);   // Установка HIGH (бит 1).
    else       *port &= ~(1 << bit);  // Установка LOW (бит 0).
}


// Функция чтения из цифрового входного пина (false - LOW, true - HIGH):
// TODO: Проверить. Изменить и сделать чтобы функция возвращала bool значение.
uchar digital_read(uchar pin) {
    // Определяем порт и номер пина:
    volatile uchar *pin_register;
    uchar bit;

    switch (pin / 8) {
        case 0:
            pin_register = &PINB;
            bit = pin % 8;
            break;
        case 1:
            pin_register = &PINC;
            bit = pin % 8;
            break;
        case 2:
            pin_register = &PIND;
            bit = pin % 8;
            break;

        // Добавьте код для других портов, если необходимо:
        default: return 0;
    }

    return (*pin_register >> bit) & 1;  // Возвращаем значение пина.
}


// Функция записи в аналоговый выходной пин (PWM):
// TODO: Проверить на работоспособность.
void analog_write(uchar pin, uchar value) {
    // Определяем порт и номер пина:
    volatile uchar *port;
    uchar bit;

    switch (pin / 8) {
        case 0:
            port = &PORTB;
            bit = pin % 8;
            break;
        case 1:
            port = &PORTC;
            bit = pin % 8;
            break;
        case 2:
            port = &PORTD;
            bit = pin % 8;
            break;

        // Добавьте код для других портов, если необходимо:
        default: return;
    }

    // Установка режима выхода:
    pin_mode(pin, OUTPUT);

    // Включение режима Fast PWM:
    TCCR1A |= (1 << COM1A1) | (1 << WGM10);

    // Установка значения ШИМ:
    OCR1A = value;

    // Включение ШИМ на пине:
    *port |= (1 << bit);
}


// Функция чтения значения аналогового входа:
// TODO: Проверить на работоспособность.
ushort analog_read(uchar pin) {
    // Настраиваем аналоговое чтение:
    ADMUX = (1 << REFS0) | (pin & 0x07);  // Напряжение опоры - AVCC с внутренним переключением, выбирается пин.

    // Запускаем преобразование:
    ADCSRA |= (1 << ADSC);

    // Ждем окончания преобразования:
    while (ADCSRA & (1 << ADSC));

    // Возвращаем результат преобразования:
    return ADC;
}
