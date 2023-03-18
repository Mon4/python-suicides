# python-suicides

Author: Monika Etrych
# The suicides in Poland (2018-2021)
The goal of this task is to determine whether the number of suicides in young people was significantly greater in the last year (2021, the most recent year for which data is available) than in previous years.

I assume that individuals up to 24 years of age are considered young people.

Some of used data.
 
![obraz](https://user-images.githubusercontent.com/44522588/226143305-d24f9038-73ba-493f-aab9-34d7f8f3eeb6.png)

 Let's take a first look at the data.
 ![obraz](https://user-images.githubusercontent.com/44522588/226143316-fe12bcc6-ccf9-4235-be58-1db7d71188bc.png)

 
As we can see,  there were much more suicides among young people last year.

I’ve made a t-test of two mean values, where hypotheses were:
H0: X1=X2
H1: X1<X2
1.	X2018 < X2021
statistic=-0.6706151057111899, pvalue=0.2695987630464987
I reject H0, statistic<=-pvalue. 
2.	X2019 < X2021
statistic=-0.5053201515202752, pvalue=0.3199531879287444
I reject H0, statistic<=-pvalue. 
3.	X2020 < X2021
statistic=-0.5557707058263687, pvalue=0.3039931563573781
I reject H0, statistic<=-pvalue.

In 2021 significantly more young people tried suicide than before.
