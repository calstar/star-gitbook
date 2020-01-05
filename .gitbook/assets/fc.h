#pragma once

#include <stdbool.h>
#include <stdint.h>

void fc_setup(void);
void fc_loop(void);

uint64_t millis(void);

#define INPUT ((uint8_t)'I')
#define OUTPUT ((uint8_t)'O')
#define INPUT_PULLUP ((uint8_t)'P')
#define LOW ((uint8_t)0)
#define HIGH ((uint8_t)1)
#define A0 ((uint8_t)14)
#define A1 ((uint8_t)15)
#define A2 ((uint8_t)16)
#define A3 ((uint8_t)17)
#define A4 ((uint8_t)18)
#define A5 ((uint8_t)19)
bool digitalRead(uint8_t pin);
void digitalWrite(uint8_t pin, uint8_t value);
void pinMode(uint8_t pin, uint8_t mode);

uint32_t i2c_available();
void i2c_begin(void);
void i2c_begin_transmission(uint8_t addr);
uint32_t i2c_end_transmission();
uint8_t i2c_read();
uint32_t i2c_request_from(uint8_t addr, uint32_t quantity);
uint32_t i2c_write(uint8_t *data, uint32_t len);
