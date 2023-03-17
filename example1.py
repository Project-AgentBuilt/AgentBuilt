import AgentBuilt as ab
import numpy as np
import datetime
import matplotlib.pyplot as plt

layout=np.zeros((6,10))
layout[4,4]=1
layout[5,4]=1
st_date=datetime.datetime(2020,10,2)
m=ab.model(layout,start_date=st_date,time_step=1)

#a=agent(m,1,"2,2")
#a.set_path(path=[a.node,str(a.pos[0]+1)+','+str(a.pos[1]),a.node])
b=ab.agent(m,2,"3,3")
path1=["3,3","3,4","3,5","3,6","3,7","4,7","4,8","4,9"]
path=path1+path1[::-1]#,"3,5","4,5","5,5","5,6"]
#b.set_path([b.node,str(b.pos[0])+','+str(b.pos[1]+1),str(b.pos[0])+','+str(b.pos[1]+2),b.node])
b.set_path(path)
print(m.agents)
m.animate(interval=100)
plt.show()