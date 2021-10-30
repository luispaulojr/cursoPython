# https://hub.mybinder.turing.ac.uk/user/ipython-ipython-in-depth-7kg1zqoj/notebooks/binder/Index.ipynb#
from matplotlib import pyplot as plt

grupos = ['produto A', 'produto B', 'produto C']
valores = [1,10,20]
plt.bar(grupos, valores)
#plt.barh(grupos, valores) # barras deitadas
plt.show

"""
# usando dois gráficos
"""
grupos = ['produto A', 'produto B', 'produto C']
valores = [15,50,100]
plt.bar(grupos,valores)
plt.plot([15,50,100])
plt.show

"""
# usando dois gráficos
"""
grupos = ['x','y','z']
valores = [10,30,50]
plt.plot(grupos,valores)
plt.bar(grupos,valores)
plt.show