import time


inicio = time.time()
# Código a medir
lista = [i for i in range(20000009) if i%2==0]
# -------------
fin = time.time()

print(fin-inicio)
# 1.5099220275878906
