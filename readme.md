## Fetching protein path

### Introduction
- As is known, proteins interact with each other intracellularly, which has led to a series of studies focusing on revealing the relationships between different proteins. Moreover, when we learn about a specific pathway or function centered on one specific protein, we need to get a general idea of other related proteins and pathways to help us better understand what we are doing or even pop up with new ideas that we can work on.
- Thus, we are interested to develop a tool to assist with deciding the shortest pathway between two interested proteins.


### Methods

- We use selenium to get all sourcecode of the HPRD database, then select all proteins with their interactors, saving them as dictionaries for further use.
- Considering the difficulty that may arise during the process of deciding the interaction intensity between proteins, we assume that all intensity of interactions stay the same for various proteins. As a result, the shortest path between two proteins is a pathway that contains the least number of proteins. Thus we use BSF to figure out the shortest interaction pathway.

### Usage

```python
 from protein_path import protein_path

 finder = protein_path()
 path = finder.find_shortest()
 print(path)
 ```
Input two proteins of your interest, then a shortest interaction pathway of these two proteins will be returned as a result.
