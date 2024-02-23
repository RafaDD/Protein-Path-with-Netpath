import numpy as np
import os


class protein_path:
    def __init__(self, data_path='./dataset/'):
        self.name_index = {}
        n_i_path = data_path + 'name_index/'
        n_i_files = os.listdir(n_i_path)
        for f in n_i_files:
            tmp_file = np.load(n_i_path + f, allow_pickle=True).item()
            for k in tmp_file.keys():
                if isinstance(k, str):
                    if isinstance(tmp_file[k], int):
                        tmp_file[k] = [tmp_file[k]]
                    if k in self.name_index.keys():
                        self.name_index[k] = self.name_index[k] + tmp_file[k]
                    else:
                        self.name_index[k] = tmp_file[k]
                else:
                    self.name_index[k] = tmp_file[k]
        
        self.protein = {}
        p_path = data_path + 'protein/'
        p_files = os.listdir(p_path)
        for f in p_files:
            tmp_file = np.load(p_path + f, allow_pickle=True).item()
            for k in tmp_file.keys():
                if k in self.protein.keys():
                    self.protein[k] += tmp_file[k]
                else:
                    self.protein[k] = tmp_file[k]
            
    def shortest_path(self, p1, p2):
        p1 = p1.upper()
        p2 = p2.upper()
        NAME_1 = p1
        NAME_2 = p2

        if p1 not in self.name_index.keys():
            print(f'{p1} is not included in our dataset.')
            return None
        if p2 not in self.name_index.keys():
            print(f'{p2} is not included in our dataset.')
            return None

        p1 = self.name_index[p1]
        if not isinstance(p1, list):
            p1 = [p1]
        p2 = self.name_index[p2]
        if not isinstance(p2, list):
            p2 = [p2]


        visited = set()
        prev = {}

        queue = p1.copy()
        for p in p1:
            prev[p] = p
            visited.add(p)

        end = False
        end_place = None
        
        while len(queue) > 0:
            p_current = queue[0]
            queue.pop(0)
            
            try:
                for p in self.protein[p_current]:
                    if p in visited:
                        continue
                    visited.add(p)
                    prev[p] = p_current
                    queue.append(p)
                    if p in p2:
                        end = True
                        end_place = p
                        break
            except:
                pass
            
            if end:
                break
        
        if not end:
            print(f'Find no path from {NAME_1} to {NAME_2}')
            return None
        
        path = []
        p = end_place
        while prev[p] != p:
            path.append(p)
            p = prev[p]
        path.append(p)
        
        path.reverse()
        for i in range(len(path)):
            path[i] = self.name_index[path[i]]
        return path
    
    def find_shortest(self):
        p1 = input('Protein1 : ')
        p2 = input('Protein2 : ')
        return self.shortest_path(p1, p2)