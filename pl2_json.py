import json
import io
from operator import itemgetter

def ex5():
    women=io.open('sw_women.txt', "w", encoding="utf-8")
    men=io.open('sw_men.txt', 'w', encoding="utf-8")
    with io.open('file2.txt', encoding="utf-8") as file:
        data=json.load(file)
        for d in data:
            if d['gender']=='male':
                name=str(d['name'])
                men.write(name)
                men.write('\n')
            elif d['gender']=='female':
                name=str(d['name'])
                women.write(name)
                women.write('\n')
    women.close()
    men.close()

def ex6():
    heroes=io.open('sw_all_heroes.txt', 'w', encoding="utf-8")
    with io.open('file2.txt', encoding="utf-8") as file:
        data=json.load(file)
        for d in data:
            if d['gender']=='male':
                heroes.write((d['name']+' waży '+d['mass']+' kg, jest mężczyzną i pochodzi z '+d['homeworld']+'.\n'))
            elif d['gender']=='female':
                heroes.write((d['name'] + ' waży ' + d['mass'] + ' kg, jest kobietą i pochodzi z ' + d['homeworld'] + '.\n'))
    heroes.close()

def ex7():
    with open('shipsjson.txt') as file:
        data=json.load(file)
        for d in data:
            if d['cost_in_credits']!='unknown':
                d['cost_in_credits']=int(d['cost_in_credits'])
            else:
                d['cost_in_credits']=-1
    data_sorted=sorted(data, key=itemgetter('cost_in_credits'), reverse=True)
    cost = open('ships_costs.txt', 'w')
    for d in data_sorted:
        if d['cost_in_credits']==-1:
            cost.write(d['name']+' nie wiadomo ile kosztuje.\n')
        else:
            cost.write(d['name']+' kosztuje '+str(d['cost_in_credits'])+' credits.\n')
    cost.close()


if __name__ == '__main__':
    ex7()
    ex6()
    ex5()