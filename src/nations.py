import wbgapi as wb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplcursors

# indicator_names = {z["code"]: z["name"] for z in info.items
indicator_codes = {"GDP": "NY.GDP.MKTP.CD", "GDPG": "NY.GDP.MKTP.KD.ZG", "TFR":"SP.DYN.TFRT.IN", 
		"GDPC": "NY.GDP.PCAP.CD", "POP":"SP.POP.TOTL", "HDI": "UNDP.HDI.XD", "LX": "SP.DYN.LE00.IN",
		"GDPCP": "NY.GDP.PCAP.PP.CD"}

country_codes = wb.region.members("wld")

def _get_data(indicator):
	"""
		returns only fields with value from last two years
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
	dfs = [] 
	for i in indicators:
		dfs += [_get_data(i)]
	df = pd.concat(dfs)
	df = df.transpose()
	df = df.dropna()
	df = add_names(df)
	return df

def add_names(df):
	ndf = wb.economy.DataFrame(df.index)
	df = df.assign(name=ndf["name"])
	return df

def plot(df):
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
	
	mplcursors.cursor(ax, hover=True).connect("add", lambda sel: sel.annotation.set_text(names[sel.index] + #))
		f"\n{cols[0]}: {xs[sel.index]:2.2e}" + 
		f"\n{cols[1]}: {ys[sel.index]}" +
		f"\n{cols[2]}: {ss[sel.index]}" +
		f"\n{cols[3]}: {cs[sel.index]}")) 
		# +f"\n{f1}:{f1s[sel.target.index]}\n{f2}:{f2s[sel.target.index]}\n{f3}:{f3s[sel.target.index]:e}\n{country_codes[sel.target.index]}"))

	plt.show()


indicators=["GDPC", "TFR", "POP", "LX"]

# df = get_data(indicators)
plot(df)

# indicators=["gdp", "tfr"] #, "pop", "lx"]
# ic = {z: indicator_codes[z] for z in indicators}
# breakpoint()
# print(ic.values())
# df = df.iloc[:,[-2,-1]]
# print(df)

# if __name__ == '__main__':
# 	get_data()
# help(wb)  
# help(wb.series)  
# rewrite all code systematically to use `wbgapi` instead of `wbpy`


# api = wbpy.IndicatorAPI()

# iso_country_codes = ["GB", "FR", "JP"]
# total_population = "SP.POP.TOTL"

# dataset = api.get_dataset(total_population, iso_country_codes, date="2010:2022")
# print(dataset)