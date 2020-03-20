---
description: How to code in C
---

# Intro to Embedded C Programming

## C Syntax

{% hint style="info" %}
A useful reference linked [**here**](https://docs.microsoft.com/en-us/cpp/c-language/c-language-reference).
{% endhint %}

**Primitive Data Types:** 

* int: integer
* float: floating-point number, used to store decimals.
* double: double-precision floating-point
* char:  ASCII character

In the &lt;stdint.h&gt; header, additional types are included for defining integers by size \(in bits\) and sign. A useful one is uint8\_t \(an unsigned 8-bit integer type\) to represent a byte.

#### Example:

```c
#include <stdlib.h> // atoi
#include <stdio.h> // printf
#include "some_other_header.h" // contains mul3

// a function named 'mul2' taking an int 'x', and returning an int
int mul2(int x) {
    return x * 2;
}

// a function 'print_repeat' that takes two ints, 'a', and 'n',
//   and does not return anything
void print_repeat(int a, int n) {
    // for loop for i = 0, 1, 2, ... n - 1
    for (int i = 0; i < n; ++i) {
        // the "%d" specifies that a base 10 number (decimal) is to be printed there.
        // the '\n' character specifies a new line. 
        // on Windows, a '\r' may be needed as well to return to beginning of line.
        // handy printf sheet: http://byuh.doncolton.com/courses/tut/printf.pdf
        printf("%d\n", a); 
    }
}

void print_forever(int a) {
    // infinite loop
    while (1) {
        printf("%d\n", a);
    }
}

int main(int argc, char *argv[]) {
    if (argc == 3) { // first element of argv is usually executable name.
        int a = atoi(argv[1]); // atoi converts string to integer
        int b = atoi(argv[2]);
        print_repeat(mul3(a), mul2(b));
    } else if (argc == 4) {
        printf("one too many arguments\n");
    } else {
        print_forever(-1);
    }
    return 0; // succesful program, no error
}
```

## Bit and bitwise operators

Computers prefer to interpret things in binary, so the use of bit operators is often useful in C to more accurately visualize what happens underneath the abstraction. The most common operators are:

```c
1 << 5; // left shift - shifts a 1 left 5 places, giving 0b100000 or 32.
32 >> 5; // right shift - the opposite of above.
0b1010 | 0b0101; /* OR - evaluates to true if at least one argument is true. 
This is done bitwise, so here the result is 0b1111. */
0b1010 & 0b0101; /* AND - evaluates to true if all arguments are true.
This is also bitwise, so we get 0b0000 here. */
0b1010 ^ 0b0101; /* XOR - with two arguments, this is true if one argument is true, 
BUT NOT BOTH. With more than two arguments, this is true if there are an odd number
of true arguments. Here, we get 0b1111 again. */
~(0b010); /* NOT - flips each bit. Here, we get 0b101. */
```

These don't seem super useful on the surface, but they will be once we start dealing with registers.

## Memory-mapped I/O

{% hint style="info" %}
The microcontroller datasheet is your best friend!
{% endhint %}

I/O devices in a microcontroller \(such as sensors or actuators\) are mapped to memory addresses - that is, you can get a sensor value by reading from a location in memory, or modify an actuator output by writing to another location. What does this mean for you? Embedded C handles this through the use of **registers**. A register is a storage element in the processor, often used to hold intermediate values during computations. However, certain specialized registers are used to perform hardware functions, and we can access these registers by using their names.

For an example, let's look at the I2C interface on the **Atmel ATMega328**, a common microcontroller that is famously used on Arduinos. I2C designates a master and a slave device, and the master can individually address a slave device by sending its address on the common bus line before sending or receiving data. There is also a common clock line. Taking a look at page 292 of the [datasheet](http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-42735-8-bit-AVR-Microcontroller-ATmega328-328P_Datasheet.pdf), we find descriptions for each register used in I2C operation.

![](../../.gitbook/assets/image%20%2831%29.png)

This register holds an 8-bit value that can be read from or written to \(as we see from R/W in the access line\), that determines the speed of the SCL line, which is the common I2C clock. The conversion of this value is as follows: SCL frequency = CPU clock frequency / \(16 + \(2 \* TWBR \* Prescaler\)\), where the prescaler is set in a different register.

Let's say I want an SCL frequency of 100 kHz from a CPU clock frequency of 16 MHz. I can achieve this with a prescaler of 1 and a TWBR of 72: 16 / \(16 + 2 \* 72 \* 1\) = 16 / 160 = 0.1 MHz. I can assign this TWBR rate simply like this:

```c
TWBR = 72; // simple, right?
TWBR = 0b01001000; // if you want to get fancy
TWBR = 0x48; // that looks nicer!
```

So far, so good. Let's move on.

![](../../.gitbook/assets/image%20%2813%29.png)

Whoa, okay. This one's a little trickier - we have two different values here. What should we do?

Let's go back to our bit operators from earlier. If I want to get only the TWI Status Bits \(that is, TWSR\[7:3\]\), I can simply right-shift the TWSR value to eliminate the three lowest-order bits.

```c
uint8_t twi_status = TWSR >> 3;
```

What if I want to write to the prescaler bits without overriding a bit I shouldn't be writing? Technically, I can't override a read-only bit even if I try, but this will illustrate my point just fine. A useful feature of the OR operator is that if I OR something with a 0, I just get that same value - that is, A OR 0 = A. But A OR 1 = 1 no matter what A is.

Now consider this code:

```c
TWSR = TWSR | 0b00000011;
```

What does this do? I'm ORing the TWSR value with a binary value that essentially passes the top six bits unchanged - since I'm ORing with zeroes. However, I'm forcing the bottom two bits to be 1s, because as I pointed out, 1 OR anything is 1. So this code forces the prescaler to 64, per the table above, but leaves the other bits unchanged! I can simplify this a bit:

```c
TWSR |= 0x03;
```

This is great, but what if those prescaler bits are already 1s and I'd like to set them back to 0s? ORing won't help, because they'll be 1s after the OR as well. This is where the AND operator comes in handy. Note that for any A, A AND 0 = 0, but A AND 1 = A.

Now consider this code:

```c
TWSR = TWSR & 0b11111100;
```

This is a similar trick. ANDing the top six bits with ones passes them unchanged, but ANDing the prescaler bits with zeroes forces them to zero. So the top six bits don't change, but the prescaler is now 1. Let's simplify this again:

```c
TWSR &= 0xFC;
```

Let's say now I want to make the prescaler 16, so I want to flip the single bit TWSR\[1\] to 1. Rather than typing out the binary mask I want to use, we can shortcut:

```c
TWSR |= 1 << 1;
```

This left shift operator evaluates to 0b00000010, which is exactly the mask I wanted to use. Similarly, I can flip it back to zero with this:

```c
TWSR &= ~(1 << 1);
```

This produces the mask 0b11111101.

Often, each bit in a register can signify different settings for the microcontroller, and is given a name.

![](../../.gitbook/assets/image%20%2849%29.png)

In the I2C control register \(TWCR\), each bit \(excluding bit 1\) defines a setting of I2C. The datasheet defines the purpose of each bit. Below is the definition of bit 2, TWEN.

![](../../.gitbook/assets/image%20%2890%29.png)

TWEN defines whether I2C is enabled or not. I can set this bit using the bit shifting, ANDing, ORing, and NOTing operations.

```c
TWCR |= (1 << TWEN); // sets TWEN to 1 in the control register, enabling I2C
TWCR &= ~(1 << TWEN); // sets TWEN to 0 in the control register, disabling I2C 
```

Using the predefined names makes the code easier to read and understand, and thus more maintainable, over using raw hex values.

And there you have it! You can use combinations of these tricks to do a lot of powerful things.

For a more complete reference on the C language, see the text below:

[http://www.dipmat.univpm.it/~demeio/public/the\_c\_programming\_language\_2.pdf](http://www.dipmat.univpm.it/~demeio/public/the_c_programming_language_2.pdf)

