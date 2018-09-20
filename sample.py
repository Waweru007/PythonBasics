import scipy.stats as stats
import pandas as pd

a, b = (76572-137916), (76572+137916)
mu, sigma = 59863, 65919
dist = stats.truncnorm((a - mu) / sigma, (b - mu) / sigma, loc=mu, scale=sigma)

values = dist.rvs(17)
values2=pd.DataFrame(values)

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

values2.to_excel(writer, sheet_name='Sheet1')

writer.save()




