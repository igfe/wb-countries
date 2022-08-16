import wbgapi as wb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# shorthand codes for WB data string
# make this into a dict of dicts with name info attached
indicator_codes = {"GDP": "NY.GDP.MKTP.CD", "GDPG": "NY.GDP.MKTP.KD.ZG", 
		"TFR":"SP.DYN.TFRT.IN", "GDPC": "NY.GDP.PCAP.CD", "POP":"SP.POP.TOTL", 
		"HDI": "UNDP.HDI.XD", "LX": "SP.DYN.LE00.IN", 
		"GDPCP": "NY.GDP.PCAP.PP.CD"}

country_codes = wb.region.members("wld")

def _get_data(indicator):
	"""
		get data from specified indicator. 
		Return only results with data from 2020 either 2021
	"""
	print(f"_get_data for {indicator}")
	df = wb.data.DataFrame(indicator_codes[indicator], country_codes, [2020,2021])
	df.loc[df['YR2021'].isnull(),'YR2021'] = df['YR2020']
	df = df.dropna()
	df = df.drop('YR2020', axis=1)
	df = df.rename(columns={'YR2021': indicator})
	df = df.transpose()
	return df

def get_data(indicators=["GDPC", "TFR", "POP", "LX"]):
	"""
		get data from specified indicators
		return only data where there is at data for at least one of the last two
		years
	"""
	dfs = [] 
	for i in indicators:
		dfs += [_get_data(i)]
	df = pd.concat(dfs)
	df = df.transpose()
	df = df.dropna()
	df = add_names(df)
	return df

def add_names(df):
	"""
		add a names column to the df based on the ISO country code
	"""
	ndf = wb.economy.DataFrame(df.index)
	df = df.assign(name=ndf["name"])
	return df

def plot(df):
	"""
		make a pretty and interactive graph of the df.
		the x and y values are from the first and second columns
		the size is from the third column
		the color is from the fourth column
	"""
	cols = df.columns
	xs = df.iloc[:,0].values
	ys = df.iloc[:,1].values
	ss = df.iloc[:,2].values
	ssm = np.sqrt(ss/ss.max())*1000
	cs = df.iloc[:,3].values
	csm = cs/cs.max()
	names = df.iloc[:,4]

	fig, ax = plt.subplots()
	ax.set_facecolor('dimgrey')
	plt.xscale('log')
	plt.xlabel(cols[0])
	plt.ylabel(cols[1])


	ax.scatter(xs, ys, s=ssm, c=csm, alpha=0.7)
	plt.title("gdp per capita vs tfr on x and y axis\nsize = population\ncolor = life expectancy")
	# ax.legend(['sizes = population', 'colors = life expectancy', [df, df]])
	
	mplcursors.cursor(ax, hover=True).connect("add", 
		lambda sel: sel.annotation.set_text(names[sel.index] +
		f"\n{cols[0]}: {xs[sel.index]:2.2e}" + 
		f"\n{cols[1]}: {ys[sel.index]}" +
		f"\n{cols[2]}: {ss[sel.index]}" +
		f"\n{cols[3]}: {cs[sel.index]}")) 
	plt.show()

if __name__ == '__main__':
	indicators = ["GDPC", "TFR", "POP", "LX"]
	# df = get_data(indicators)
	# df.to_pickle("res/standard.pkl")
	df = pd.read_pickle('res/standard.pkl')
	plot(df)
