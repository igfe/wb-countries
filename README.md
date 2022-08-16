# wb-countries
Interactive graph based on 4 economic indicators from [World Bank Open Data](https://data.worldbank.org/)

## running
To run this project, it is assumed that [python-is-python3](https://askubuntu.com/questions/1296790/python-is-python3-package-in-ubuntu-20-04-what-is-it-and-what-does-it-actually) recommended that you understand how to use [venv](https://docs.python.org/3/library/venv.html). 
`cd` to the root directory of this project. To make and activate `venv` and install `requirements.txt`:

```bash 
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

after doing this you can view the main graph with

```bash
python src/nations.py
```

## output
This program plots an interactive graph of key economic indicators. It is currently hardcoded such that
- **x axis** - gdp per capita
- **y axis** - total fertility rate
- **size** - population
- **color** - life expectancy

Example ouput is given below:
![image](res/example.png)
Hovering over any of the datapoints will display information as in the **guam** example.

## TODO
- add user defined economic indicators
	- intelligently scale/format axes, and sizes based on the distribution of indicators
	- add command line interface
- maybe use something like `d3.js` to make it a web app