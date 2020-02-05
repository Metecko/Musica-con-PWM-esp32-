from machine import Pin, PWM
from time import sleep
import re

pin25 = Pin(25)

def cancion(tempo, n, *args):
    pwm25 = PWM(pin25, 0, 900)
    negra = float(60/tempo)
    semicorchea = negra/4
    corchea = negra/2
    blanca = negra*2
    for arg in args:
        nota = re.search(r'\(?([A-Za-z]+)\)?', arg).group(1)
        modificador = arg.replace(nota, "")
        
        if len(modificador) > 1:
            if modificador[0] == "-":
                n -= 1
            elif modificador [0] == "+":
                n += 1
        
        if nota == "do":
            pwm25.freq(33*2**n)
        elif nota == "re":
            pwm25.freq(37*2**n)
        elif nota == "mi":
            pwm25.freq(41*2**n)
        elif nota == "fa":
            pwm25.freq(44*2**n)
        elif nota == "sol":
            pwm25.freq(49*2**n)
        elif nota == "la":
            pwm25.freq(55*2**n)
        elif nota == "si":
            pwm25.freq(62*2**n)
        elif nota == "sl":
            pwm25.freq(0)
        
        tiempo = int(arg[-1])
        if tiempo == 0:
            sleep(semicorchea)
        elif tiempo == 1:
            sleep(corchea)
        elif tiempo == 2:
            sleep(negra)
        elif tiempo == 3:
            sleep(blanca)
    
    pwm25.deinit()

cancion(100, 6, "mi0", "mi1", "mi0", "sl0", "do0", "mi1", "sol2", "-sol2",
        "do1", "sl0", "-sol0", "sl1", "-mi1")

sleep(1)

cancion(80, 4, "mi0", "mi1", "mi0", "sl0", "do0", "mi1", "sol2", "-sol2",
        "do1", "sl0", "-sol0", "sl1", "-mi1")

sleep(1)

cancion(120, 5, "do1", "re1", "mi1", "fa1", "sol1", "la1", "si1", "+do1")
cancion(140, 6, "do1", "re1", "mi1", "fa1", "sol1", "la1", "si1", "+do1")
cancion(160, 7, "do1", "re1", "mi1", "fa1", "sol1", "la1", "si1", "+do1")
cancion(60, 7, "+mi3")

sleep(1)

cancion(200, 5, "-do1", "do1", "+do1")
