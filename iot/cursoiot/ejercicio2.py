import machine
import utime

adc = machine.ADC(machine.Pin(32))
adc.atten(machine.ADC.ATTN_11DB)


while True:
    valor = adc.read()
    voltaje = (valor * 3.3) / 4095
    print("valor {} volt{:.2f}v".format(valor, voltaje))
    utime.sleep_ms(500)