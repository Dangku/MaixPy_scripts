import lcd, time
import image

bg = (236,36,36)
lcd.init(freq=25000000)
lcd.direction(lcd.YX_RLUD)
lcd.clear(lcd.RED)
time.sleep(1)
lcd.clear(lcd.GREEN)
time.sleep(1)
lcd.clear(lcd.BLUE)
time.sleep(1)
lcd.draw_string(120, 120, "hello maixpy", lcd.WHITE, lcd.RED)
time.sleep(2)


img = image.Image()
img.draw_string(60, 100, "hello maixpy", scale=2)
img.draw_rectangle((120,120,30,30))
lcd.display(img)
