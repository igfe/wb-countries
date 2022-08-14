# wb-countries
View interactive graphs in python based on 4 economic indicators

## running
To run this project, it is recommended that you understand how to use [venv](https://docs.python.org/3/library/venv.html). Once `venv` is installed, `cd` to the root directory of this project and make, activate and install `requirements.txt` with:
```bash 
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

after doing this you can view the main graph with

```bash
python src/nations.py
```

## TODO
- add `venv` 
- add automatic or user defined scaling based on an arbitrary number of variables
- add command line interface
- maybe use something like d3.js