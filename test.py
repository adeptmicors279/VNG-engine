import  pickle
'''
li = ["nihao","haloo",{"sdf":123}]

with open("test.xxx","wb") as fb:
    pickle.dump(li,fb)'''

with open("C:\\Users\\1\\Desktop\\123\\reg.glg",'rb') as f:
    ss=pickle.load(f)
    print(ss)