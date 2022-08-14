import wbpy
import json
import matplotlib.pyplot as plt
import mplcursors
import numpy as np

"""
	TODO:
		Refine list of iso codes to not include regions i.e. OECD members, world, EU etc...
		Add other indicators e.g. R&D spending, HDI... Preferably a list of all codes
		Interpret text input i.e. "gdp2018*(1+gdpg2018/100)*(1+rnd2018/100)"
"""
api = wbpy.IndicatorAPI()
# countries = api.get_countries().keys() #dict[str] : iso codes for countries
# regions = api.get_regions().keys()
# notc = []
country_codes = ['ABW', 'AFG', 'AGO', 'ALB', 'AND', 'ARB', 'ARE', 'ARG', 'ARM',
 'ASM', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR',
 'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 
 'BWA', 'CAF', 'CAN', 'CEB', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 
 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CSS', 'CUB', 'CUW', 'CYM', 'CYP', 'CZE', 
 'DEU', 'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'EAP', 'EAR', 'EAS', 'ECA', 'ECS', 
 'ECU', 'EGY', 'EMU', 'ERI', 'ESP', 'EST', 'ETH', 'EUU', 'FCS', 'FIN', 'FJI', 
 'FRA', 'FRO', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIB', 'GIN', 'GMB', 'GNB', 
 'GNQ', 'GRC', 'GRD', 'GRL', 'GTM', 'GUM', 'GUY', 'HIC', 'HKG', 'HND', 'HPC', 
 'HRV', 'HTI', 'HUN', 'IBD', 'IBT', 'IDA', 'IDB', 'IDN', 'IDX', 'IMN', 'IND', 
 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 
 'KGZ', 'KHM', 'KIR', 'KNA', 'KOR', 'KWT', 'LAC', 'LAO', 'LBN', 'LBR', 'LBY', 
 'LCA', 'LCN', 'LDC', 'LIC', 'LIE', 'LKA', 'LMC', 'LMY', 'LSO', 'LTE', 'LTU', 
 'LUX', 'LVA', 'MAC', 'MAF', 'MAR', 'MCO', 'MDA', 'MDG', 'MDV', 'MEA', 'MEX', 
 'MHL', 'MIC', 'MKD', 'MLI', 'MLT', 'MMR', 'MNA', 'MNE', 'MNG', 'MNP', 'MOZ', 
 'MRT', 'MUS', 'MWI', 'MYS', 'NAC', 'NAM', 'NCL', 'NER', 'NGA', 'NIC', 'NLD', 
 'NOR', 'NPL', 'NRU', 'NZL', 'OED', 'OMN', 'OSS', 'PAK', 'PAN', 'PER', 'PHL', 
 'PLW', 'PNG', 'POL', 'PRE', 'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'PSS', 'PST', 
 'PYF', 'QAT', 'ROU', 'RUS', 'RWA', 'SAS', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB', 
 'SLE', 'SLV', 'SMR', 'SOM', 'SRB', 'SSA', 'SSD', 'SSF', 'SST', 'STP', 'SUR', 
 'SVK', 'SVN', 'SWE', 'SWZ', 'SXM', 'SYC', 'SYR', 'TCA', 'TCD', 'TEA', 'TEC', 
 'TGO', 'THA', 'TJK', 'TKM', 'TLA', 'TLS', 'TMN', 'TON', 'TSA', 'TSS', 'TTO', 
 'TUN', 'TUR', 'TUV', 'TZA', 'UGA', 'UKR', 'UMC', 'URY', 'USA', 'UZB', 'VCT', 
 'VEN', 'VGB', 'VIR', 'VNM', 'VUT', 'WLD', 'WSM', 'XKX', 'YEM', 'ZAF', 'ZMB', 'ZWE']
# country_codes = ['AW', 'AF', 'AO', 'AL', 'AD', '1A', 'AE', 'AR', 'AM', 'AS', 'AG', 'AU', 'AT', 'AZ', 'BI', 'BE', 'BJ', 'BF', 'BD', 'BG', 'BH', 'BS', 'BA', 'BY', 'BZ', 'BM', 'BO', 'BR', 'BB', 'BN', 'BT', 'BW', 'CF', 'CA', 'B8', 'CH', 'JG', 'CL', 'CN', 'CI', 'CM', 'CD', 'CG', 'CO', 'KM', 'CV', 'CR', 'S3', 'CU', 'CW', 'KY', 'CY', 'CZ', 'DE', 'DJ', 'DM', 'DK', 'DO', 'DZ', '4E', 'V2', 'Z4', '7E', 'Z7', 'EC', 'EG', 'XC', 'ER', 'ES', 'EE', 'ET', 'EU', 'F1', 'FI', 'FJ', 'FR', 'FO', 'FM', 'GA', 'GB', 'GE', 'GH', 'GI', 'GN', 'GM', 'GW', 'GQ', 'GR', 'GD', 'GL', 'GT', 'GU', 'GY', 'XD', 'HK', 'HN', 'XE', 'HR', 'HT', 'HU', 'XF', 'ZT', 'XG', 'XH', 'ID', 'XI', 'IM', 'IN', 'IE', 'IR', 'IQ', 'IS', 'IL', 'IT', 'JM', 'JO', 'JP', 'KZ', 'KE', 'KG', 'KH', 'KI', 'KN', 'KR', 'KW', 'XJ', 'LA', 'LB', 'LR', 'LY', 'LC', 'ZJ', 'XL', 'XM', 'LI', 'LK', 'XN', 'XO', 'LS', 'V3', 'LT', 'LU', 'LV', 'MO', 'MF', 'MA', 'MC', 'MD', 'MG', 'MV', 'ZQ', 'MX', 'MH', 'XP', 'MK', 'ML', 'MT', 'MM', 'XQ', 'ME', 'MN', 'MP', 'MZ', 'MR', 'MU', 'MW', 'MY', 'XU', 'NA', 'NC', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OE', 'OM', 'S4', 'PK', 'PA', 'PE', 'PH', 'PW', 'PG', 'PL', 'V1', 'PR', 'KP', 'PT', 'PY', 'PS', 'S2', 'V4', 'PF', 'QA', 'RO', 'RU', 'RW', '8S', 'SA', 'SD', 'SN', 'SG', 'SB', 'SL', 'SV', 'SM', 'SO', 'RS', 'ZF', 'SS', 'ZG', 'S1', 'ST', 'SR', 'SK', 'SI', 'SE', 'SZ', 'SX', 'SC', 'SY', 'TC', 'TD', 'T4', 'T7', 'TG', 'TH', 'TJ', 'TM', 'T2', 'TL', 'T3', 'TO', 'T5', 'T6', 'TT', 'TN', 'TR', 'TV', 'TZ', 'UG', 'UA', 'XT', 'UY', 'US', 'UZ', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', '1W', 'WS']
# print("Country Codes")
# print(country_codes)

codes = {"gdp": "NY.GDP.MKTP.CD", "gdpg": "NY.GDP.MKTP.KD.ZG", "tfr":"sp.dyn.tfrt.in", 
		"gdpc": "NY.GDP.PCAP.CD", "pop":"sp.pop.totl", "hdi": "UNDP.HDI.XD", "lx": "SP.DYN.LE00.IN",
		"gdpcp": "NY.GDP.PCAP.PP.CD"}


# print("\n\ncountry_names")
gdp_data = api.get_dataset(codes["gdpc"], country_codes, date="2016:2018")
country_names = gdp_data.countries
# print(country_names)
# gdp_data = gdp_data.as_dict()
# gdpg_data = api.get_dataset(codes["gdpg"], countries[:2], date="2016:2018").as_dict()
# tfr_data = api.get_dataset(codes["tfr"], countries[:2]).as_dict()


def plot_2factor(f1="gdp", f2="tfr", f3="pop", f4="lx"):
	"""
		f1 - x axis
		f2 - y axis
		f3 - size
		f4 - color
	"""
	f1dat = api.get_dataset(codes[f1], country_codes, date="2016:2018").as_dict()
	f2dat = api.get_dataset(codes[f2], country_codes, date="2016:2018").as_dict()
	f3dat = api.get_dataset(codes[f3], country_codes, date="2016:2018").as_dict()
	f4dat = api.get_dataset(codes[f4], country_codes, date="2016:2018").as_dict()
	# print(f1dat)

	ndic = dict()
	names = []
	f1s = []
	f2s = []
	f3s = []
	f4s = []
	for c in country_codes:
		if c in f1dat and c in f2dat and c in f4dat and c in f3dat:
			if f1dat[c]["2018"] and f2dat[c]["2018"] and f3dat[c]["2018"] and f4dat[c]["2018"]:
				ndic[country_names[c]] = [f1dat[c]["2018"], f2dat[c]["2018"]]
				names += [country_names[c]]
				f1s += [f1dat[c]["2018"]]
				f2s += [f2dat[c]["2018"]]
				f3s += [f3dat[c]["2018"]]
				f4s += [f4dat[c]["2018"]]

	f3s = [np.sqrt(z/max(f3s))*500 for z in f3s]
	# print(f4s)
	f4s = [z/max(f4s) for z in f4s]


	# print(json.dumps(ndic, indent=4))
	print(f"f1s {len(f1s)}")
	print(f"f2s {len(f2s)}")
	print(f"f3s {len(f3s)}")
	print(f"f4s {len(f4s)}")

	fig, ax = plt.subplots()

	ax.scatter(f1s, f2s, s=f3s, c=f4s, alpha=0.7)
	ax.set_facecolor('dimgrey')
	# mplcursors.cursor(ax).connect("add", lambda sel: sel.annotation.set_text(names[sel.target.index]))
	mplcursors.cursor(ax, hover=True).connect("add", lambda sel: sel.annotation.set_text(names[sel.target.index] + 
		f"\n{f1}:{f1s[sel.target.index]}\n{f2}:{f2s[sel.target.index]}\n{f3}:{f3s[sel.target.index]:e}\n{country_codes[sel.target.index]}"))
	plt.xlabel(f1)
	plt.ylabel(f2)
	plt.xscale('log')
	# plt.legend()
	# for i1, i2, n in zip(f1s, f2s, names):
	# 	plt.annotate(n, (i1, i2), textcoords="offset points", xytext=(0,10), ha='center')

	# plt.axhline(y=2.1)
	plt.show()

if __name__ == '__main__':
	# plot_2factor("gdpc", "tfr")
	pass




# ndic = dict()
# for c in countries:
# 	if c in gdp_data and c in gdpg_data:
# 		if gdp_data[c]["2018"] and gdpg_data[c]["2018"]:
# 			ndic[country_names[c]] = gdp_data[c]["2018"]*(1 + gdpg_data[c]["2018"]/100)

# k=20
# ndic = {k: v for k, v in sorted(ndic.items(), key=lambda item: item[1], reverse=True)}
# print(json.dumps(ndic, indent=4))
# plt.bar(list(ndic.keys())[12:12+k], list(ndic.values())[12:12+k])
# plt.xticks(rotation=90)
# plt.show()
# print(ndic)