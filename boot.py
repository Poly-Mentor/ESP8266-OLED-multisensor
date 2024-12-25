# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()


def do_connect():
    import network
    from credentials import SSID, WiFi_Password
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, WiFi_Password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


do_connect()