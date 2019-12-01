import pandas
import numpy 


"""Q1"""

data = ([2, 4, 6, 8, 10])
print(pandas.Series(data))


"""Q2"""

d1={'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print(pandas.Series(d1))


"""Q3"""


data = [20, 10, 150, 110, 100, 50]
mydata= pandas.Series(data)
mydata.plot(kind="bar", color=["red" , "black" , "green" , "blue" , "yellow" , "blue"])



"""Q4"""


Data = {
        'd1':[100,200,5,400,700,100,200,50,400,700],
        'd2':[140,0,300,400,200,140,0,700,400,200] 
        }
mydata2=pandas.DataFrame(Data,columns=['d1', 'd2'])
mydata2.plot()


"""Q5"""


import pandas

data={
      'X':[78,85,96,80,86],
      'Y':[84,94,89,83,86],
      'Z':[86,97,96,72,83]
      }

df= pandas.DataFrame(data)
print(df)


"""Q6"""


mychart=pandas.DataFrame({
        'names':['Bob','Jessica','Mary','John','Mel'],
        'birth':[968,155,77,578,973]
})
print(mychart)
plot =mychart.plot.pie(y='birth', figsize=(5,5))





"""Q7"""


data = [100, 2200, 300, 400, 500, 600,700,800,900]
d2 = pandas.Series(data)
print(d2.describe())
d2.to_csv('myDataFrame.csv', sep='\t')
d2.to_csv('myDataFrame.csv', sep=',')




"""Q8"""

import numpy as np
dates=pandas.date_range('20000101',periods=4)
df= pandas.DataFrame(np.random.randn(4, 2), index=dates, columns=['A','B'])
print(df)
print(df.head(2))
print(df[['A']])
print(df[0:1])
print(df['20000102':'20000104'])
print(df.loc['20000102':'20000104',['A']])
print(df.iloc[:,1:2])
print(df[df>0])
print(df[df.B>0])
df['A']=[100,200,300,100]
print(df)
print(df[df['A'].isin([200,300])])



