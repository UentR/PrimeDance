import numpy as np
from PIL import Image
import imageio
from time import perf_counter as pf
from sys import getsizeof as get_size
deb = pf()

All = []

for t in range(0, 400, 1):
    Current = Image.open(f'Images/{t}.jpg')
    Current = Current.crop((76, 0, 500, 600))
    Current = np.asanyarray(Current)
    All.append(Current)
    print(t)
step = pf()
print(step-deb)
imageio.mimsave('Gif.gif', All, fps=50)
fin = pf()
print(fin-step, fin-deb)