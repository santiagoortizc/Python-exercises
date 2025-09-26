'''
  Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
'''

def time_mili(days=0, hours=0, minutes=0, seconds=0) :
  
  return f"{days}d {hours}h {minutes}m {seconds}s = {(((days*24 + hours)*60 +minutes)*60 +seconds)*1000:,} milisegundos"
  
print(time_mili(days=1, hours=12, minutes=48, seconds=36))
print(time_mili(days=1))
print(time_mili(hours=2, minutes=30, seconds=45))
print(time_mili(days=1, hours=5, minutes=20, seconds=30))
print(time_mili(seconds=10))
