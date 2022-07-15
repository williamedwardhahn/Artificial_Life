execfile("display_driver.py")

s.fill(0)
s.text('HELLO MPCR!!', 0, 25)
  
s.line(0, 0, 50, 25, 1)
s.show()

# s.poweroff()     # power off the display, pixels persist in memory
# s.poweron()      # power on the display, pixels redrawn
# s.contrast(0)    # dim
# s.contrast(255)  # bright
# s.invert(1)      # display inverted
# s.invert(0)      # display normal
# s.rotate(True)   # rotate 180 degrees
# s.rotate(False)  # rotate 0 degrees
# s.show()

# s.fill(0)                         # fill entire screen with colour=0
# s.pixel(0, 10)                    # get pixel at x=0, y=10
# s.pixel(0, 10, 1)                 # set pixel at x=0, y=10 to colour=1
# s.hline(0, 8, 4, 1)               # draw horizontal line x=0, y=8, width=4, colour=1
# s.vline(0, 8, 4, 1)               # draw vertical line x=0, y=8, height=4, colour=1
# s.line(0, 0, 127, 63, 1)          # draw a line from 0,0 to 127,63
# s.rect(10, 10, 107, 43, 1)        # draw a rectangle outline 10,10 to 117,53, colour=1
# s.fill_rect(10, 10, 107, 43, 1)   # draw a solid rectangle 10,10 to 117,53, colour=1
# s.text('Hello World', 0, 0, 1)    # draw some text at x=0, y=0, colour=1
# s.scroll(20, 0)                   # scroll 20 pixels to the right
# s.show()


# import framebuf
# fbuf = framebuf.FrameBuffer(bytearray(8 * 8 * 1), 8, 8, framebuf.MONO_VLSB)
# fbuf.line(0, 0, 7, 7, 1)
# s.blit(fbuf, 10, 10, 0)           # draw on top at x=10, y=10, key=0
# s.show()


s.fill(0)
s.fill_rect(0, 0, 32, 32, 1)
s.fill_rect(2, 2, 28, 28, 0)
s.vline(9, 8, 22, 1)
s.vline(16, 2, 22, 1)
s.vline(23, 8, 22, 1)
s.fill_rect(26, 24, 2, 4, 1)
s.text('MicroPython', 40, 0, 1)
s.text('SSD1306', 40, 12, 1)
s.text('OLED 128x64', 40, 24, 1)
s.show()


