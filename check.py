import numpy as np

i = 10001

a = np.load(f'./dataset/name_index/name_index{i}.npy', allow_pickle=True).item()
b = np.load(f'./dataset/protein/protein{i}.npy', allow_pickle=True).item()

print(a)
print(b)