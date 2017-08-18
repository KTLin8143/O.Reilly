import sqlite3

def find_details(id2find):
    db = sqlite3.connect("surfersDB.sdb")
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute("select * from surfers")
    rows = cursor.fetchall()
    for row in rows:
        if row['id'] == id2find:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            return (s)
    cursor.close()
    return ({})


id = int(input("Enter the id of the surfer: "))
player_data = find_details(id)
if player_data:
    print("ID:         " + player_data['id'])
    print("Name:       " + player_data['name'])
    print("Country:    " + player_data['country'])
    print("Average:    " + player_data['average'])
    print("Board type: " + player_data['board'])
    print("Age:        " + player_data['age'])
