from protein_path import protein_path


finder = protein_path()
path = finder.find_shortest()
print(path)