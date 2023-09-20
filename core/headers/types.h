//
// types.h - Объявляет новые типы данных.
//


#ifndef _TYPES_H
#define _TYPES_H

// Прочие типы данных:
typedef char           byte;
typedef unsigned char  uchar;
typedef unsigned short ushort;
typedef unsigned long  ulong;

// bool поддержка:
#define true  1
#define false 0

#ifndef bool
#define bool byte
#endif

// null поддержка:
#define null undefined

#endif
