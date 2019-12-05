import nes, lcd, time

# AUDIO_PA_EN_PIN = None  # Bit Dock and old MaixGo
#AUDIO_PA_EN_PIN = 32      # Maix Go(version 2.20)
# AUDIO_PA_EN_PIN = 2     # Maixduino

# open audio PA
#if AUDIO_PA_EN_PIN:
 #   fm.register(AUDIO_PA_EN_PIN, fm.fpioa.GPIO1, force=True)
 #   wifi_en=GPIO(GPIO.GPIO1, GPIO.OUT)
 #   wifi_en.value(1)

# sd check
os.listdir("/")
lcd.init(freq=25000000)
lcd.direction(lcd.YX_RLUD)

time.sleep(1)
nes.init(nes.KEYBOARD)
nes.run("/sd/mario.nes")

