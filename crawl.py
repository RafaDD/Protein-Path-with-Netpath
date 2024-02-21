from selenium import webdriver
from selenium.webdriver.edge.options import Options
import re
import numpy as np
from tqdm import trange
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', default=1, type=int)
parser.add_argument('--step', default=10000, type=int)
args = parser.parse_args()

options = Options()
options.add_argument("headless")
options.add_argument("disable-gpu")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Edge(options=options)
name_index = {}
protein = {}

for n in trange(args.start, args.start+args.step, ncols=60):
    if n % 50 == 0:
        np.save(f'./dataset/name_index/name_index{args.start}.npy', name_index)
        np.save(f'./dataset/protein/protein{args.start}.npy', protein)
    try:
        driver.get(f'http://netpath.org/molecule?molecule_id=NetPath_M{n}')
        page_source_n = driver.page_source
        phy_inter = re.findall('Physical Interaction', page_source_n)
        if len(phy_inter) == 0:
            continue
        name = re.findall('<td class="moleculename"> .+?</td>', page_source_n)
        if len(re.findall('Catalysis', page_source_n)) != 0:
            cat = re.search('Catalysis', page_source_n).start()
            page_source_n = page_source_n[:cat]
        if len(name) > 0:
            name = name[0][26: -5]
        name_index[n] = name
        name_index[name] = n
        protein[n] = []
        prot = re.findall('molecule\?molecule_id=NetPath_M[0-9,]+?">.+?<', page_source_n)
        for p in prot:
            name_b = re.search('>', p).start()
            p_n = p[name_b+1: -1]
            index_b = re.search('_M', p).end()
            index_e = re.search('"', p).start()
            p_i = int(p[index_b: index_e])
            if p_i != n:
                name_index[p_i] = p_n
                name_index[p_n] = p_i
                protein[n].append(p_i)
        
        prot = re.findall('molecule\?molecule_id=NetPath_M[0-9,]+?" class="bluhead">.+?<', page_source_n)
        for p in prot:
            name_b = re.search('>', p).start()
            p_n = p[name_b+1: -1]
            index_b = re.search('_M', p).end()
            index_e = re.search('"', p).start()
            p_i = p[index_b: index_e]
            if ',' in p_i:
                nums = p_i.split(',')
                for i in range(len(nums)):
                    nums[i] = int(nums[i])
                    if nums[i] == n:
                        continue
                    name_index[nums[i]] = p_n
                name_index[p_n] = nums
                protein[n] += nums
            else:
                p_i = int(p_i)
                if p_i != n:
                    name_index[p_i] = p_n
                    name_index[p_n] = p_i
                    protein[n].append(p_i)
            
    except:
        continue

np.save(f'./dataset/name_index/name_index{args.start}.npy', name_index)
np.save(f'./dataset/protein/protein{args.start}.npy', protein)