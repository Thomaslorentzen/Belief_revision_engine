# Belief revision engine

This is a python implementation for a belief revision engine. 

### Authors
* Niels George Vendelø
* Thomas Kristian Lorentzen
* Morten Allan Jensen


### Project structure
* `belief_base.py`: the main class that implements the belief base and it's core functions such as expand, contration and revise.
* `cli.py`: The command-line interface for the user to perform operations on the belief base
* `entailment.py`: implementation of entailment algorithm for propositional logic
* `utils.py`: utility functions for operations on our structures or Sympy structures


### Installation
To install the required library, run the following command:
```bash
$ pip install -r requirements.txt
```

### Run the program
The engine can be started through the command-line interface (CLI) using the following command:
```bash
$ python cli.py
```

### Admin command
if the user would like to add a formula to the beliefbase without revising it they can write following command: 
```bash
$ e
```
The command calls the expand_belief_base method without revision. 
