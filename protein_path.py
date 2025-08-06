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

        dist = {NAME_1: 0}

        if p1 not in self.name_index.keys():
            print(f'{p1} is not included in our dataset.')
            return []
        if p2 not in self.name_index.keys():
            print(f'{p2} is not included in our dataset.')
            return []

        p1 = self.name_index[p1]
        if not isinstance(p1, list):
            p1 = [p1]
        p2 = self.name_index[p2]
        if not isinstance(p2, list):
            p2 = [p2]

        queue = p1.copy()

        end = False
        
        while len(queue) > 0:
            p_current = queue[0]
            name_current = self.name_index[p_current]
            queue.pop(0)
            
            try:
                for p in self.protein[p_current]:
                    name_neighbour = self.name_index[p]
                    if name_neighbour not in dist.keys():
                        dist[name_neighbour] = dist[name_current] + 1
                        queue.append(p)

            except:
                pass
            
        
        # if not end:
        #     print(f'Find no path from {NAME_1} to {NAME_2}')
        #     return None
        
        paths = []
        p1 = self.name_index[NAME_1][0]
        p2 = self.name_index[NAME_2][0]
        self.collect_paths(p1, p2, dist, [], paths)

        unique_paths = list(dict.fromkeys(tuple(row) for row in paths))
        unique_paths = [list(row) for row in unique_paths]

        return unique_paths
    

    def collect_paths(self, current, end, dist, path, paths):
        name_current = self.name_index[current]
        path.append(name_current)
        if current == end:
            paths.append(path[:])
        elif current in self.protein.keys():
            for p in self.protein[current]:
                try:
                    name_next = self.name_index[p]
                    if name_next in dist.keys() and dist[name_next] == dist[name_current] + 1:
                        self.collect_paths(p, end, dist, path, paths)
                except:
                    continue
        path.pop()


    def find_shortest(self):
        p1 = input('Protein1 : ')
        p2 = input('Protein2 : ')
        return self.shortest_path(p1, p2)