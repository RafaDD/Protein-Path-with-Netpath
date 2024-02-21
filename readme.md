##Manual

###about the algorithm 
- We use selenium to get all sourcecode of the HPRD database, then select all proteins with their interactors, saving them as dictionaries for further use.
- Considering the difficulty that may arise during the process of deciding the interaction intensity between priteins, we assume that all  intensity of interactions stay the same for various proteins. As a result, the shortest path between two proteins is a pathway that contains the least number of proteins. Thus we use BSF to figure out the shortest interaction pathway.

###about application method
```python
 from protein_path import protein_path

 finder = protein_path()
 path = finder.find_shortest()
 print(path)
 ```
Input two proteins of your interest, then a shortest interaction pathway of these two proteins will be returned as a result.