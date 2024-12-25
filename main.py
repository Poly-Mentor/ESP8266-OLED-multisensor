from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(14), scl=Pin(12))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.text('Hello, World!', 0, 0, 1)
display.text('Hello, World!', 0, 16, 1)
display.text('Hello, World!', 0, 32, 1)
display.text('Hello, World!', 0, 48, 1)
display.show()