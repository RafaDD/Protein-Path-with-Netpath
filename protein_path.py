import numpy as np
import os

class protein_path:
    def __init__(self, data_path='./dataset/'):
        self.name_index = {}
        n_i_path = data_path + 'name_index/'
        n_i_files = os.listdir(n_i_path)
        for f in n_i_files:
            self.name_index.update(np.load(n_i_path + f, allow_pickle=True).item())
        
        self.protein = {}
        p_path = data_path + 'protein/'
        p_files = os.listdir(p_path)
        for f in p_files:
            self.protein.update(np.load(p_path + f, allow_pickle=True).item())
            
    def shortest_path(self, p1, p2):
        if p1 not in self.name_index.keys():
            print(f'{p1} is not included in our dataset.')
            return None
        if p2 not in self.name_index.keys():
            print(f'{p2} is not included in our dataset.')
            return None
        
        p1 = self.name_index[p1]
        f1 = False
        if isinstance(p1, list):
            f1 = True
        p2 = self.name_index[p2]
        f2 = False
        if isinstance(p2, list):
            f2 = True


        visited = set()
        prev = {}
        if f1:
            queue = p1.copy()
            for p in p1:
                prev[p] = p
                visited.add(p)
        else:
            queue = [p1]
            prev[p1] = p1
            visited.add(p1)
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
                    if f2:
                        if p in p2:
                            end = True
                            end_place = p
                            break
                    else:
                        if p == p2:
                            end = True
                            end_place = p
                            break 
            except:
                pass
            
            if end:
                break
        
        if not end:
            print(f'Find no path from {self.name_index[p1]} to {self.name_index[p2]}')
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