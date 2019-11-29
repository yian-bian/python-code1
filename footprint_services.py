# Part 2
# Footprint of utilities & university
# Author: Yian Bian 260886212

import doctest
from unit_conversion import *

######################################### Utilities
days_in_year = 365.2425
pound_in_kg = 0.45359237
kg_in_tonne = 0.001
kwh_in_mwh = 0.001

def fp_from_gas(monthly_gas):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on monthly natural gas bill in $.

    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
        B.) Multiply your monthly gas bill by 105 [lbs, to get annual amount] 

    >>> fp_from_gas(0)
    0.0
    >>> round(fp_from_gas(100), 4)
    4.7627
    >>> round(fp_from_gas(25), 4)
    1.1907
    '''
    gas_in_pound = monthly_gas * 105 # use the monthly bill to calculate the amouunt
    gas_in_kg = pound_in_kg * gas_in_pound # convert lbs to kg
    fp_from_gas = gas_in_kg * kg_in_tonne # covert kg to tonne
    return fp_from_gas



def fp_from_hydro(daily_hydro):
    '''(num) -> float
    Calculate metric tonnes of CO2E produced annually
    based on average daily hydro usage.

    To find out your average daily hydro usage in kWh:
        Go to https://www.hydroquebec.com/portail/en/group/clientele/portrait-de-consommation
        Scroll down to "Annual total" and press "kWh"

    Source: https://www.hydroquebec.com/data/developpement-durable/pdf/co2-emissions-electricity-2017.pdf
        0.6 kg CO2E / MWh

    >>> fp_from_hydro(0)
    0.0
    >>> round(fp_from_hydro(10), 4)
    0.0022
    >>> round(fp_from_hydro(48.8), 4)
    0.0107
    '''
    daily_hydro_in_mwh = daily_hydro * kwh_in_mwh #covert kwh to mwh
    daily_in_tonne = daily_hydro_in_mwh * 0.6 * kg_in_tonne # use the data to calculate the kg of CO2E and covert the kg to tonne
    fp_from_hydro = daily_in_tonne * days_in_year # use the tonnes of CO2E that daily produced to multiply the days in a year to calculate the tonnes of CO2E that annualy produced
    return fp_from_hydro



def fp_of_utilities(daily_hydro, monthly_gas):
    '''(num, num, num) -> float
    Calculate metric tonnes of CO2E produced annually from
    daily hydro (in kWh) and gas bills (in $) and monthly phone data (in GB).

    >>> fp_of_utilities(0, 0)
    0.0
    >>> round(fp_of_utilities(100, 0), 4)
    0.0219
    >>> round(fp_of_utilities(0, 100), 4)
    4.7627
    >>> round(fp_of_utilities(50, 20), 4)
    0.9635
    '''
    daily_hydro_in_mwh = daily_hydro * kwh_in_mwh # covert kwh to mwh
    daily_in_tonne = daily_hydro_in_mwh * 0.6 * kg_in_tonne # use the data to calculate the kg of CO2E and covert the kg to tonne
    fp_from_hydro = daily_in_tonne * days_in_year # use the tonnes of CO2E that daily produced to multiply the days in a year to calculate the tonnes of CO2E that annualy produced
    gas_in_pound = monthly_gas * 105 # use the monthly bill to calculate the amouunt
    gas_in_kg = pound_in_kg * gas_in_pound # convert lbs to kg
    fp_from_gas = gas_in_kg * kg_in_tonne # covert kg to tonne
    fp_of_utilities = fp_from_hydro + fp_from_gas
    return fp_of_utilities


#################################################


def fp_of_studies(annual_uni_credits):
    '''(num, num, num) -> flt
    Return metric tonnes of CO2E from being a student, based on
    annual university credits.

    Source: https://www.mcgill.ca/facilities/files/facilities/ghg_inventory_report_2017.pdf
        1.12 tonnes per FTE (30 credit) student

    >>> round(fp_of_studies(0), 4)
    0.0
    >>> round(fp_of_studies(30), 4)
    1.12
    >>> round(fp_of_studies(18), 4)
    0.672
    '''
    number_of_PTE_student = annual_uni_credits / 30 # use the annual university credits to divided by 30 to have the number of the PTE student
    fp_of_studies = number_of_PTE_student * 1.12 # use the number of PTE to multiply the tonnes of CO2E per PTE student to get the toones if CO2E from being a student
    return fp_of_studies


#################################################

if __name__ == '__main__':
    doctest.testmod()
