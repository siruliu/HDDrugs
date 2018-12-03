import numpy as np 
import pandas as pd 
import re


urllist = []
with open('drugurl.txt') as fp:
    lines = fp.readlines()
    for line in lines:
        # return a list that contain 1-2 tuples (url, website name)
        name = re.findall(r'<A[^>]+HREF=["](.*?)["]>(.*?)</A>', line)

        url_drug = []

        if len(name)==2:
        	url_drug=[name[0][0],name[1][0]]
        else:
        	if name[0][1]=='DailyMed':
        		url_drug=[name[0][0],""]
        	elif name[0][1]=='DrugBank':
        		url_drug=["",name[0][0]]
        	else:
        		url_drug=["",""]


        urllist.append(url_drug)

print(urllist)

df = pd.DataFrame(urllist,columns=['DailyMed','DrugBank'])
print(df)


df.to_csv("drugurl.csv",index=False)





