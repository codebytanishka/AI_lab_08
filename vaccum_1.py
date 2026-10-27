room = {
    'A' : 'Dirty',
    'B' : 'Dirty'
}

location = 'A'

while True:
    print("Location:", location)
    print("Room Status:", room)

    if room[location] == 'Dirty':
        print("Action: Suck!")
        room[location] = 'Clean'

    elif location == 'A':
        print("Action: Move Right!")
        location = 'B'

    elif location == 'B':
        print("Action: Move Left!")
        location = 'A'

    if room['A'] == 'Clean' and room['B'] == 'Clean':
        print("Both Rooms Are Clean")
        break