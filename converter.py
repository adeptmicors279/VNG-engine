def load_setting(file,head):
    with open(f'{file}','r',encoding='utf-8') as f:
        content=f.readlines()
        for i in content:
            try:
                s=i.replace('\n','').split(f'{head}==')[1]
                #print (s)
                return s
            except:
                pass
def load_game():
    pass