# Resources I used to help guide me for this project are:
# Dr. Ricks flights starter file https://github.com/csci3320/example_final_projects/blob/main/flights2.py
# Michael Sambol Dijkstra's explanation video https://www.youtube.com/watch?v=_lHSawdgXpI

class Airport_Node:
    def __init__(self, code_name, full_name):
        self.code_name = code_name
        self.full_name = full_name
        self.airport_flights = []

    def __str__(self):
        return self.code_name

    def __repr__(self):
        return self.__str__()


class Flight_Details:
    def __init__(self, duration, destination, origin, price):
        self.duration = duration
        self.destination = destination
        self.origin = origin
        self.cost = price

    def __str__(self):
        return f"{str(self.origin)} to {str(self.destination)} is {str(self.duration)} hrs"

    def __repr__(self):
        return self.__str__()


# Data set 2

oma = Airport_Node("OMA", "Eppley Airfield")
bos = Airport_Node("BOS", "Boston Logan International Airport")
dfw = Airport_Node("DFW", "Dallas/Fort Worth International Airport")
den = Airport_Node("DEN", "Denver International Airport")
orD = Airport_Node("ORD", "O'Hare International Airport")
atl = Airport_Node("ATL", "Hartsfield-Jackson International Airport")
lax = Airport_Node("LAX", "Los Angeles International Airport")
jfk = Airport_Node("JFK", "John F. Kennedy International Airport")
las = Airport_Node("LAS", "Harry Reid International Airport")
mco = Airport_Node("MCO", "Orlando International Airport")  # orlando airport
mia = Airport_Node("MIA", "Miami International Airport")
clt = Airport_Node("CLT", "Charlotte Douglas International Airport")

sfo = Airport_Node("SFO", "San Francisco International Airport")
san = Airport_Node("SAN", "San Diego International Airport")
phx = Airport_Node("PHX", "Phoenix Sky Harbor International Airport")
phl = Airport_Node("PHL", "Philadelphia International Airport")
sea = Airport_Node("SEA", "Seattle-Tacoma International Airport")
stl = Airport_Node("STL", "St. Louis Lambert International Airport")
dca = Airport_Node("DCA", "Ronald Reagan Washington National Airport")
msp = Airport_Node("MSP", "Minneapolis-Saint Paul International Airport")

oma.airport_flights.append(Flight_Details(3, dfw, oma, 268))
oma.airport_flights.append(Flight_Details(2, den, oma, 150))
oma.airport_flights.append(Flight_Details(1, orD, oma, 200))

den.airport_flights.append(Flight_Details(2, las, den, 200))
den.airport_flights.append(Flight_Details(2, dfw, den, 180))

orD.airport_flights.append(Flight_Details(1, oma, orD, 200))
orD.airport_flights.append(Flight_Details(1, phl, orD, 160))
orD.airport_flights.append(Flight_Details(2, stl, orD, 150))

sea.airport_flights.append(Flight_Details(2, sfo, sea, 138))
sea.airport_flights.append(Flight_Details(3, lax, sea, 152))

sfo.airport_flights.append(Flight_Details(1, lax, sfo, 91))

lax.airport_flights.append(Flight_Details(3, msp, lax, 287))
lax.airport_flights.append(Flight_Details(3, dfw, lax, 407))

jfk.airport_flights.append(Flight_Details(1, bos, jfk, 137))
jfk.airport_flights.append(Flight_Details(4, dfw, jfk, 199))

san.airport_flights.append(Flight_Details(1, phx, san, 193))
san.airport_flights.append(Flight_Details(2, den, san, 159))

las.airport_flights.append(Flight_Details(1, lax, las, 89))

dfw.airport_flights.append(Flight_Details(3, oma, dfw, 239))
dfw.airport_flights.append(Flight_Details(2, atl, dfw, 286))

phx.airport_flights.append(Flight_Details(2, oma, phx, 257))

phl.airport_flights.append(Flight_Details(2, stl, phl, 268))
phl.airport_flights.append(Flight_Details(1, jfk, phl, 111))  # check this out later

stl.airport_flights.append(Flight_Details(2, atl, stl, 281))

atl.airport_flights.append(Flight_Details(2, dfw, atl, 268))
atl.airport_flights.append(Flight_Details(1, mco, atl, 249))

mco.airport_flights.append(Flight_Details(1, mia, mco, 231))

mia.airport_flights.append(Flight_Details(2, clt, mia, 195))

clt.airport_flights.append(Flight_Details(2, bos, clt, 127))
clt.airport_flights.append(Flight_Details(1, dca, clt, 162))

bos.airport_flights.append(Flight_Details(3, msp, bos, 235))
bos.airport_flights.append(Flight_Details(3, atl, bos, 317))

dca.airport_flights.append(Flight_Details(2, mco, dca, 137))
dca.airport_flights.append(Flight_Details(2, orD, dca, 209))

msp.airport_flights.append(Flight_Details(3, bos, msp, 221))
msp.airport_flights.append(Flight_Details(3, lax, msp, 387))
msp.airport_flights.append(Flight_Details(4, sfo, msp, 249))

# temp fix

# msp.airport_flights.append(Flight_Details(5, sea, msp))
# lax.airport_flights.append(Flight_Details(1, san, lax))


airports = [atl, bos, clt, den, dfw, jfk, las, lax, mco, mia, oma, orD, sfo, san, phx, phl, sea, stl, msp, dca]
str_airports = []

total_flights = 0
for airport in airports:
    str_airports.append(str(airport))
    for flights in airport.airport_flights:
        total_flights += 1

print(f"Airports you can start from {airports}")
print(f"Total number of airports: {len(airports)}")
print(f"Total number of flights: {total_flights}")

while True:
    try:
        origin = input("Select an airport to start with: ").upper()
        if origin not in str_airports:
            raise NameError
        break
    except NameError as error:
        print("Only enter an airport code you can start from! ", error)

while True:
    try:
        destination = input("What is your destination: ").upper()
        if destination not in str_airports:
            raise NameError
        break
    except NameError as error:
        print("That is not a possible destination!", error)
org = None
infinity = 1000000000

travel_time = {}
for airport in airports:
    x = airport.code_name
    if x == origin:
        travel_time[airport] = [0]
        org = airport
        travel_time[airport].append(0)
    else:
        travel_time[airport] = [infinity]
        travel_time[airport].append(0)

visited_airports = [org]
not_visited_airports = []

for airport in airports:
    if airport not in visited_airports:
        not_visited_airports.append(airport)

current = org

while True:
    if len(visited_airports) == len(airports):
        break

    temp_time = infinity

    for flight in current.airport_flights:
        distance = flight.duration + travel_time[current][0]
        count = travel_time[current][1]
        if flight.destination in visited_airports:
            continue
        elif distance < travel_time[flight.destination][0]:
            travel_time[flight.destination][0] = distance
            travel_time[flight.destination][1] = 1 + count

    current_time = 0
    for x in travel_time:
        if x in not_visited_airports:
            if travel_time[x][0] < temp_time:
                temp_time = travel_time[x][0]
                current = x
                current_time = travel_time[x][0]

    if temp_time == infinity:
        break
    else:
        visited_airports.append(current)
        not_visited_airports.remove(current)

for x in visited_airports:
    if x.code_name == destination:
        destination = x

print()
print(f"The shortest flight time from {str(org)} to {str(destination)} is: {travel_time[destination][0]} hours")

connecting_flights = travel_time[destination][1]
if connecting_flights == 1:
    print("This is a direct flight. ")
else:
    print(f"Number of connecting flights: {travel_time[destination][1]}")
