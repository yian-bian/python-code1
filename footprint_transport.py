# Part 3
# Footprint of local transportation and travel
# Author: Yian Bian 260886212

import doctest
from unit_conversion import *


################################################
days_in_year = 365.2425
pound_in_kg = 0.45359237
kg_in_ton = 0.001
kwh_in_mwh = 0.001
km_in_miles = 0.621371
g_in_kg = 0.001

def fp_from_driving(annual_km_driven):
    '''
    (num) -> flt
    Approximate CO2E footprint for one year of driving, based on total km driven.
    Result in metric tonnes.
    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
    "D.) Multiply total yearly mileage by .79 (for pounds)"

    >>> fp_from_driving(0)
    0.0
    >>> round(fp_from_driving(100), 4)
    0.0223
    >>> round(fp_from_driving(1234), 4)
    0.2748
    '''
    annual_mile_driven = annual_km_driven * km_in_miles # covert km to miles
    annual_pound = annual_mile_driven * 0.79 # use the total miles driven to calculate the pounds of CO2E that produced
    annual_kg = annual_pound * pound_in_kg # covert pound to kg
    fp_from_driving = annual_kg * kg_in_ton # covert kg to ton
    return fp_from_driving 


def fp_from_taxi_uber(weekly_uber_rides):
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the annual footprint from a given
    number of weekly uber/taxi/etc rides.

    Source: https://www.mapc.org/resource-library/the-growing-carbon-footprint-of-ride-hailing-in-massachusetts/
        81 million trips -> 100,000 metric tonnes

    >>> fp_from_taxi_uber(0)
    0.0
    >>> round(fp_from_taxi_uber(10), 4)
    0.6442
    >>> round(fp_from_taxi_uber(25), 4)
    1.6104
    '''
    number_of_million_trip = weekly_uber_rides / 81000000 # to calculate the number of 81 million trips
    weekly_ton = number_of_million_trip * 100000 # because 81 million trips will produce 100,000 tonnes of CO2E, use the nunber of 81 million trips to multiply 100,000 to get the weekly CO2E footprint
    daily_ton = weekly_ton / 7 # use the weekly footprint divided the number of days in a week to get the daily footprint
    fp_from_taxi_uber = daily_ton * days_in_year #use the daily footprint to multiply the number of days in a year to get the annual footprint
    return fp_from_taxi_uber


def fp_from_transit(weekly_bus_trips, weekly_rail_trips):
    '''
    (num, num) -> flt
    Annual CO2E tonnes from public transit based on number of weekly bus
    rides and weekly rail (metro/commuter train) rides.

    Source: https://en.wikipedia.org/wiki/Transportation_in_Montreal
    The average amount of time people spend commuting with public transit in Montreal, for example to and from work, on a weekday is 87 min. 29.% of public transit riders, ride for more than 2 hours every day. The average amount of time people wait at a stop or station for public transit is 14 min, while 17% of riders wait for over 20 minutes on average every day. The average distance people usually ride in a single trip with public transit is 7.7 km, while 17% travel for over 12 km in a single direction.[28]
    Source: https://en.wikipedia.org/wiki/Société_de_transport_de_Montréal
    As of 2011, the average daily ridership is 2,524,500 passengers: 1,403,700 by bus, 1,111,700 by rapid transit and 9,200 by paratransit service.

    Source: How Bad Are Bananas
        A mile by bus: 150g CO2E
        A mile by subway train: 160g CO2E for London Underground

    >>> fp_from_transit(0, 0)
    0.0
    >>> round(fp_from_transit(1, 0), 4)
    0.0374
    >>> round(fp_from_transit(0, 1), 4)
    0.0399
    >>> round(fp_from_transit(10, 2), 4)
    0.4544
    '''
    weekly_bus_km = weekly_bus_trips * 7.7 # The average transit trip in Montr´eal is 7.7 km.We use the average transit trip to multiply the number of weekly bus rides to get the weekly transit trip in a week.
    weekly_bus_mile = weekly_bus_km * km_in_miles # covert km to miles
    weekly_bus_g = weekly_bus_mile * 150 # a mile by bus will produce 150g CO2E.We use the transit trip(in miles) in a week tp multiply 150 to get the CO2E produced in a week(in gram)
    weekly_bus_kg = weekly_bus_g * g_in_kg # covert gram to kilogram
    weekly_bus_ton = weekly_bus_kg * kg_in_ton #covert kilogram to ton
    weekly_rail_km = weekly_rail_trips * 7.7 # The average transit trip in Montr´eal is 7.7 km.We use the average transit trip to multiply the number of weekly rail rides to get the weekly transit trip in a week.
    weekly_rail_mile = weekly_rail_km * km_in_miles # covert km ton miles
    weekly_rail_g = weekly_rail_mile * 160 # a mile by rail will produce 160g CO2E.We use the transit trip(in miles) in a week tp multiply 150 to get the CO2E produced in a week(in gram)
    weekly_rail_kg = weekly_rail_g * g_in_kg #convert gram to kilogram
    weekly_rail_ton = weekly_rail_kg * kg_in_ton # convert kilogram to tonnes
    weekly_both = weekly_rail_ton + weekly_bus_ton # calculate the whole CO2E produced by rail and bus in a week
    daily_both = weekly_both / 7 # use the weekly produced CO2E to divide the number of days in a week to get the daily produced CO2E
    fp_from_transit = daily_both * days_in_year # use the daily produced CO2E to multiply the number of days in a year to get the annual produced CO2E
    return fp_from_transit


def fp_of_transportation(weekly_bus_rides, weekly_rail_rides, weekly_uber_rides, weekly_km_driven):
    '''(num, num, num, num) -> flt
    Estimate in tonnes of CO2E the footprint of weekly transportation given
    specified annual footprint in tonnes of CO2E from diet.

    >>> fp_of_transportation(0, 0, 0, 0)
    0.0
    >>> round(fp_of_transportation(2, 2, 1, 10), 4)
    0.3354
    >>> round(fp_of_transportation(1, 2, 3, 4), 4)
    0.3571
    '''
    weekly_bus_km = weekly_bus_rides * 7.7 # The average transit trip in Montr´eal is 7.7 km.We use the average transit trip to multiply the number of weekly bus rides to get the weekly transit trip in a week.
    weekly_bus_mile = weekly_bus_km * km_in_miles # covert km to miles
    weekly_bus_g = weekly_bus_mile * 150 # a mile by bus will produce 150g CO2E.We use the transit trip(in miles) in a week tp multiply 150 to get the CO2E produced in a week(in gram)
    weekly_bus_kg = weekly_bus_g * g_in_kg # covert gram to kilogram
    weekly_bus_ton = weekly_bus_kg * kg_in_ton #covert kilogram to ton
    weekly_rail_km = weekly_rail_rides * 7.7 # The average transit trip in Montr´eal is 7.7 km.We use the average transit trip to multiply the number of weekly rail rides to get the weekly transit trip in a week.
    weekly_rail_mile = weekly_rail_km * km_in_miles # covert km ton miles
    weekly_rail_g = weekly_rail_mile * 160 # a mile by rail will produce 160g CO2E.We use the transit trip(in miles) in a week tp multiply 150 to get the CO2E produced in a week(in gram)
    weekly_rail_kg = weekly_rail_g * g_in_kg #convert gram to kilogram
    weekly_rail_ton = weekly_rail_kg * kg_in_ton # convert kilogram to tonnes
    weekly_both = weekly_rail_ton + weekly_bus_ton # calculate the whole CO2E produced by rail and bus in a week
    weekly_mile_driven = weekly_km_driven * km_in_miles # covert km to miles
    weekly_pound = weekly_mile_driven * 0.79 # use the total miles driven to calculate the pounds of CO2E that produced
    weekly_kg = weekly_pound * pound_in_kg # covert pound to kg
    weekly_ton = weekly_kg * kg_in_ton # covert kg to ton
    number_of_million_trip = weekly_uber_rides / 81000000 # to calculate the number of 81 million trips
    weekly_uber_ton = number_of_million_trip * 100000 # because 81 million trips will produce 100,000 tonnes of CO2E, use the nunber of 81 million trips to multiply 100,000 to get the weekly CO2E footprint
    whole_weekly_ton = weekly_bus_ton + weekly_rail_ton + weekly_ton + weekly_uber_ton #sum up all the weekly produced CO2E to get the whole weekly produced footprint
    daily_ton = whole_weekly_ton / 7 #use the weekly footprint to divide the number of days in a week to get the daily footprint
    fp_of_transportation = daily_ton * days_in_year #use the daily CO2E to multiply the days in a year to get the annual footprint in tonnes of CO2E
    return fp_of_transportation


#################################################

def fp_of_travel(annual_long_flights, annual_short_flights, annual_train, annual_coach, annual_hotels):
    '''(num, num, num, num, num) -> float
    Approximate CO2E footprint in metric tonnes for annual travel, based on number of long flights (>4 h), short flights (<4), intercity train rides, intercity coach bus rides, and spending at hotels.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    "E.) Multiply the number of flights--4 hours or less--by 1,100 lbs
    F.) Multiply the number of flights--4 hours or more--by 4,400 libs"

    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
        -> 34.45 kg CO2E

    Source for buses: How Bad Are Bananas
        66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls
        I'm going to just assume that's an average length trip, because better data not readily avialible.

    Source for hotels: How Bad Are Bananas
        270 g CO2E for every dollar spent

    >>> fp_of_travel(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_travel(0, 1, 0, 0, 0), 4) # short flight
    0.499
    >>> round(fp_of_travel(1, 0, 0, 0, 0), 4) # long flight
    1.9958
    >>> round(fp_of_travel(2, 2, 0, 0, 0), 4) # some flights
    4.9895
    >>> round(fp_of_travel(0, 0, 1, 0, 0), 4) # train
    0.0345
    >>> round(fp_of_travel(0, 0, 0, 1, 0), 4) # bus
    0.033
    >>> round(fp_of_travel(0, 0, 0, 0, 100), 4) # hotel
    0.027
    >>> round(fp_of_travel(6, 4, 24, 2, 2000), 4) # together
    15.4034
    >>> round(fp_of_travel(1, 2, 3, 4, 5), 4) # together
    3.2304
    '''
    annual_long_flight_lbs = annual_long_flights * 4400 #use the number of long filghts multiply the lbs of CO2E that a single long flight produced to get the total lbs that the long flight produced
    annual_long_flight_kg = annual_long_flight_lbs * pound_in_kg #convert pound to kg
    long_flight_ton = annual_long_flight_kg * kg_in_ton #convert kg to ton
    annual_short_flight_lbs = annual_short_flights * 1100 #use the number of short filghts multiply the lbs of CO2E that a single short flight produced to get the total lbs that the short flight produced
    annual_short_flight_kg = annual_short_flight_lbs * pound_in_kg #convert pound to kg
    short_flight_ton = annual_short_flight_kg * kg_in_ton #convert kg to ton
    annual_train_kg = annual_train * 34.45 # use the number of trains multiply the kg of CO2E that a train produced to get the total kg that the train porduced
    train_ton = annual_train_kg * kg_in_ton #convert kg to ton
    annual_coach_kg = annual_coach * 33 # use the number of trains multiply the kg of CO2E that a train produced to get the total kg that the train porduced
    coach_ton = annual_coach_kg * kg_in_ton #convert kg to ton
    annual_hotel_g = annual_hotels * 270 # use the bill of hotel multiply the g of CO2E that produced by every dollar to get the total g
    hotel_kg = annual_hotel_g * g_in_kg #convert g to kg
    hotel_ton = hotel_kg * kg_in_ton # convert kg to ton
    fp_of_travel = long_flight_ton + short_flight_ton + train_ton + coach_ton + hotel_ton # sum up all the CO2E footprint to get the total
    return fp_of_travel

#################################################

if __name__ == '__main__':
    doctest.testmod()
