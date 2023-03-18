# Goal of this exercise is to check if in the last year(2021 - most recent data) was significantly more suicides in
# young age than in previous years.
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# read data and prepare
data = pd.read_excel('Poland_age_excel.xlsx').transpose()

data.drop(data.index[[0, 1]], inplace=True)
data.drop([2], axis=1, inplace=True)
data.fillna(method='ffill', inplace=True)

#rename
new_column_names = ['age', 'year', 'number_of_suicides']
data.columns = new_column_names

data.loc[data['age'].str.contains('ogółem'), 'age'] = 'total'
data.loc[data['age'].str.contains('12 lat i mniej'), 'age'] = '12 years or less'
data.loc[data['age'].str.contains('70 lat i więcej'), 'age'] = '70 years or more'
data.loc[data['age'].str.contains('nieustalony wiek'), 'age'] = 'age unknown'

data.index.values[:36] = 'total'
data.index.values[36:] = 'ended_dead'

data.set_index([data.index.values, 'age', 'year'], inplace=True)

print(data.to_string())
print("----------------------------------------------------------------------------")


def select_data(age):
    n = data.query(f'age=={age}').values.tolist()
    n_total = n[0:len(n) // 2]
    n_dead = n[len(n) // 2:len(n) + 1]
    return n_total, n_dead


n_total_ch, n_dead_ch = select_data("'12 years or less'")
n_total_t, n_dead_t = select_data("'13-18'")
n_total_y, n_dead_y = select_data("'19-24'")


years = data.index.unique('year').values

# plots
fig, (plt1, plt2, plt3) = plt.subplots(1, 3)
plt1.plot(years, n_total_ch, label='total')
plt1.plot(years, n_dead_ch, label='ended dead')
plt1.set_title('12 years or less')

plt2.plot(years, n_total_t)
plt2.plot(years, n_dead_t)
plt2.set_title('13-18')

plt3.plot(years, n_total_y)
plt3.plot(years, n_dead_y)
plt3.set_title('19-24')

fig.suptitle('Number of suicides by age')
fig.legend()
plt.show()


# tests

def select_year(value):
    n = data.query('year==@value').values.tolist()
    n_sum = sum(n, [])
    a = n_sum[1], n_sum[2], n_sum[3]
    b = n_sum[10], n_sum[11], n_sum[12]
    return a, b


total = []
dead = []

for i in range(2018, 2022):
    a, b = select_year(str(i))
    total.append(a)
    dead.append(b)

print("Young people are: between 12 years or less to 24 years.")
print("Total amount of young people trying suicide in years 2018-2021: ", total, "\nAmount of young people died due to suicide: ", dead)

print("H0: X1=X2\nH1: X1<X2")
print(stats.ttest_ind(a=total[0], b=total[3], equal_var=True, alternative='less'))
print("I reject H0, statistic<=-pvalue. In 2021 significantly more young people tried suicide than in 2018.\n")

print(stats.ttest_ind(a=total[1], b=total[3], equal_var=True, alternative='less'))
print("I reject H0, statistic<=-pvalue. In 2021 significantly more young people tried suicide than in 2019.\n")

print(stats.ttest_ind(a=total[2], b=total[3], equal_var=True, alternative='less'))
print("I reject H0, statistic<=-pvalue. In 2021 significantly more young people tried suicide than in 2020.")
print("----------------------------------------------------------------------------\n")
print("In 2021 significantly more young people tried suicide than before.")