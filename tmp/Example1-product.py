import pandas as pd

m1=pd.MultiIndex.from_product([['a1','a2'],['b1','b2','b3']],names=['a','b'])
m1
d1=pd.DataFrame({'a':['a1','a1','a2'],'b':['b1','b2','b2'],'c':[0,1,2]})
d1
d1.set_index(['a','b'],inplace=True)
d2=d1.set_index(['a','b'])
d2
d3=d2.reindex(m1)
d3
d3.count()
d3.reset_index(inplace=True)
d3
