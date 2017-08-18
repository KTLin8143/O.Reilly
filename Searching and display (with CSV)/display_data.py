# -*- coding: UTF-8 -*-

def find_id(n):
    data = open("surfing_data.csv")
    for line in data:
        s = {}
        (s['id'], s['name'], s['country'], s['average'], s['board'], s['age']) = line.split(";")
        if n == int(s['id']):
            data.close()
            return (s)
    data.close()
    return ({})


search = int(input("Please Enter Player ID: "))
player_data = find_id(search)
if id:
    print "ID:      " + player_data['id']
    print "Player:  " + player_data['name']
    print "Country: " + player_data['country']
    print "Board:   " + player_data['board']
    print "Age:     " + player_data['age']
