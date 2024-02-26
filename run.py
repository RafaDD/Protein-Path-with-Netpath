from protein_path import protein_path


finder = protein_path()
path = finder.find_shortest()
print(f'Path:')
if path == None:
    print('None')
else:
    for i in range(len(path) - 1):
        print(f'{path[i]} -> ', end='')
    print(path[-1])