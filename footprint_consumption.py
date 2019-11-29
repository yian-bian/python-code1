# Part 4
# Footprint of computing and diet
# Author: Yian Bian 260886212

import doctest
from unit_conversion import *

######################################
days_in_year = 365.2425
pound_in_kg = 0.45359237
kg_in_ton = 0.001
kwh_in_mwh = 0.001
km_in_miles = 0.621371
g_in_ton = 0.000001

def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    daily_online_g = daily_online_use * 55 #use the daily hours online to multiply the CO2E produced by online use per hour to get the daily CO2E produced by online use(in gram)
    daily_online_ton = daily_online_g * g_in_ton#convert g to ton
    annual_online_ton = daily_online_ton * days_in_year # use the daily footprint to multiply the number of days in a year to get the annual footprint
    annual_phone_kg = daily_phone_use * 1250 #use the daily hours of phone use to multiply the CO2E produced for a year of using phone one hour a day to get the anuual CO2E(in kilograms)
    annual_phone_ton = annual_phone_kg * kg_in_ton #conver kg to tonnes
    new_light_kg = new_light_devices * 75 #use the number of new light devices to multiply the CO2E that produced by one new light devices to the total CO2E produced by new light devices
    new_light_ton = new_light_kg * kg_in_ton # convert kg to tonnes
    new_medium_kg = new_medium_devices * 200 #use the number of new medium devices to multiply the CO2E that produced by one new medium devices to the total CO2E produced by new medium devices
    new_medium_ton = new_medium_kg * kg_in_ton # convert kg to tonnes
    new_heavy_kg = new_heavy_devices * 800 #use the number of new heavy devices to multiply the CO2E that produced by one new heavy devices to the total CO2E produced by new heavy devices
    new_heavy_ton = new_heavy_kg * kg_in_ton # convert kg to tonnes
    fp_of_computing = annual_online_ton + annual_phone_ton + new_light_ton + new_medium_ton + new_heavy_ton # sum up to get the total tonnes of CO2E from computing
    return fp_of_computing


######################################

def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    vegan_diet = 2.89 * 1000 #convert kg to g
    daily_meat = daily_g_meat * 26.8 # use the grams of meat multiply the CO2E produced by having 1 gram of meat to get the total
    daily_cheese = daily_g_cheese * 12 # use the grams of cheese multiply the CO2E produced by having 1 gram of cheese to get the total
    daily_milk = daily_L_milk * 267.7777# use the litres of milk multiply the CO2E produced by having 1 litre of milk to get the total
    daily_eggs = daily_num_eggs * 300 # use the number of eggs multiply the CO2E produced by having an egg to get the total
    daily_diet = vegan_diet + daily_meat + daily_cheese + daily_milk + daily_eggs # sum up to get the daily CO2E produced by the diet
    annual_diet = daily_diet * days_in_year # use the number of days in a year multiply the daily CO2E to get the annual CO2E produced by diet
    fp_of_diet = annual_diet * g_in_ton #convert g to tonnes
    return fp_of_diet


#################################################

if __name__ == '__main__':
    doctest.testmod()

