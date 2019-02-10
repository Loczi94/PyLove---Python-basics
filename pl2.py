def ex1():
    dict_name={}
    with open('file1.txt', 'r') as file:
        for line in file:
            dict_infos = {}
            iteration=0
            has = False
            iss = False
            end_name = False
            name = ""
            height = 0
            color = ""
            info = line.split()
            for i in info:
                iteration+=1
                if iteration!=1:
                    if(i=="has"):
                        has=True
                        end_name=True
                    elif has==True:
                        color=i
                        has=False
                    elif(i=="is"):
                        iss=True
                    elif(iss==True):
                        height=int(i)
                        iss=False
                    elif(end_name==False):
                        name=name+" "+i
            dict_infos["height"]=height
            dict_infos["eye"]=color
            dict_name[name]=dict_infos
    print(dict_name)

def ex2():
    file_short=open("hero_short.txt",'w')
    file_200_plus=open("hero_200_plus.txt",'w')
    with open('file1.txt', 'r') as file:
        for line in file:
            name=line[line.find(".")+2:line.find(" has")]
            height=int(line[line.find(" is ")+3:line.find(" cm")])
            if height>200:
                file_200_plus.write(name+"\n")
            else:
                file_short.write(name+"\n")
    file_short.close()
    file_200_plus.close()

def ex3_4():
    dict={}
    dict_colors={'yellow':'żółty', 'black':'czarny', 'blue':'niebieski', 'orange':'pomarańczowy', 'green, yellow':'zielono-żółty', 'red':'czerwony', 'brown':'brązowy', 'unknown':'nieokreślony', 'gold':'złoty', 'blue-gray':'niebiesko-szary', 'pink':'różowy', 'hazel':'orzechowy', 'red, blue':'czerwono-niebieski'}
    with open('file1.txt', 'r') as file:
        for line in file:
            color=line[line.find(" has ")+5:]
            color=color[:color.find(" and")]
            height = int(line[line.find(" is ") + 3:line.find(" cm")])
            if color in dict:
                dict[color][0]=dict[color][0]+height
                dict[color][1]=dict[color][1]+1
            else:
                dict[color]=[height,1]
    for word in dict:
        mean=round(int(dict[word][0])/int(dict[word][1]),2)
        print("Średni wzrost osób z kolorem oczu "+dict_colors[word]+" wynosi "+str(mean)+" cm.")

if __name__ == '__main__':
    ex3_4()
    ex2()
    ex1()