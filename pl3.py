import requests
from pprint import pprint as pp

def ex1():
    resp = requests.get('http://py.net/status')
    print(resp.json())
    resp = requests.post('http://py.net/status/set', json={'status': 'Bardzo nowy status'})
    print(resp.json())
    resp = requests.get('http://py.net/status')
    print(resp.json())

def ex2():
    resp = requests.post('http://py.net/register', json={'name':'Paulina94', 'password':'pyladies2017'})
    print(resp.json())

def ex3():
    resp = requests.post('http://py.net/auth', json={'name': 'Paulina94', 'password': 'pyladies2017'})
    print(resp.json())

def ex4():
    resp_set = requests.post('http://py.net/user_status/set', json={'api_key':'1359dc9f6add5725cd32922f92ef21bf1c52fa2f2e36047b40608340af84bb64', 'status':'successful'})
    print(resp_set.json())
    resp_get = requests.get('http://py.net/user_status')
    print(resp_get.json())

def ex5():
    resp_get = requests.get('http://py.net/cat')
    print(resp_get.status_code)
    with open('cat.jpg', 'wb') as file:
        file.write(resp_get.content)

def ex6():
    resp_get = requests.get('http://py.net/query_string?p1=value1&p2=value2')
    print(resp_get.json())

def ex7():
    resp = requests.get('https://swapi.co/api/planets/1')
    residents = resp.json()['residents']
    for r in residents:
        resp = requests.get(r)
        print(resp.json()['name'])

def ex8():
    resp = requests.get('https://swapi.co/api/films/')
    films = resp.json()['results']
    for film in films:
        if film['title']=='The Empire Strikes Back':
            species = film['species']
            break
    for s in species:
        resp = requests.get(s)
        print(resp.json()['name'])

def ex9():
    resp = requests.get('https://swapi.co/api/')
    api_starships = resp.json()['starships']
    resp = requests.get(api_starships)
    starships = resp.json()['results']
    for s in starships:
        if s['name']=='Millennium Falcon':
            pilots = s['pilots']
            break
    for p in pilots:
        resp = requests.get(p)
        mass = float(resp.json()['mass'])
        height = float(resp.json()['height'])/100
        BMI = round(mass/(height**2),2)
        name = resp.json()['name']
        print(name+'\tBMI: '+str(BMI))

def ex10():
    dict = {'Jar Jar Binks':'aguhwwgggghhh huuguughghg huuguughghg', 'Roos Tarpals':'uughguughhhghghghhhgh huurh huurh', 'Rugor Nass':'aaahnruh huuguughghg'}
    resp = requests.get('https://swapi.co/api/')
    resp_json = resp.json()['species']
    resp_species = requests.get(resp_json)
    species = resp_species.json()['results']
    people = []
    for s in species:
        if s['name']=='Gungan':
            people = s['people']
            break
    for p in people:
        resp_people = requests.get(p)
        name = resp_people.json()['name']
        print(dict[name])

if __name__ == '__main__':
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    ex6()
    ex7()
    ex8()
    ex9()
    ex10()
