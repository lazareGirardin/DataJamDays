#######################################
# Authors: Loic Tinguely, Antonin Danalet, EPFL
#######################################

from biogeme import *
from headers import *
from loglikelihood import *
from statistics import *

#Parameters to be estimated
# Arguments:
#   1  Name for report. Typically, the same as the variable
#   2  Starting value
#   3  Lower bound
#   4  Upper bound
#   5  0: estimate the parameter, 1: keep it fixed
ASC_BC = Beta('ASC_BC', 0, -100, 100, 0)
ASC_BM = Beta('ASC_BM ', 0, -100, 100, 0)
ASC_ELA = Beta('ASC_ELA ', 0, -100, 100, 0)
ASC_MX = Beta('ASC_MX ', 0, -100, 100, 0)
ASC_PH = Beta('ASC_PH ', 0, -100, 100, 0)
ASC_ATL = Beta('ASC_ATL ', 0, -100, 100, 0)
ASC_COR = Beta('ASC_COR ', 0, -100, 100, 0)
ASC_GIA = Beta('ASC_GIA ', 0, -100, 100, 0)
ASC_PAR = Beta('ASC_PAR ', 0, -100, 100, 0)
ASC_ESP = Beta('ASC_ESP ', 0, -100, 100, 1)
ASC_ORN = Beta('ASC_ORN ', 0, -100, 100, 0)
ASC_PIZ = Beta('ASC_PIZ ', 0, -100, 100, 0)
ASC_KEB = Beta('ASC_KEB ', 0, -100, 100, 0)
ASC_SAT = Beta('ASC_SAT ', 0, -100, 100, 0)
ASC_HOD = Beta('ASC_HOD ', 0, -100, 100, 0)
ASC_VAL = Beta('ASC_VAL ', 0, -100, 100, 0)
ASC_INM = Beta('ASC_INM ', 0, -100, 100, 0)
ASC_VIN = Beta('ASC_VIN', 0, -100, 100, 0)
ASC_COP = Beta('ASC_COP', 0, -100, 100, 0)
ASC_KLE = Beta('ASC_KLE', 0, -100, 100, 0)
ASC_ARC = Beta('ASC_ARC', 0, -100, 100, 0)
BETA_PRICE_STUDENT = Beta('BETA_PRICE_STUDENT', 0, -100, 100, 0)
BETA_PRICE_EMPLOYEE = Beta('BETA_PRICE_EMPLOYEE', 0, -100, 100, 0)
BETA_DINNER = Beta('BETA_DINNER', 0, -100, 100, 0)
BETA_DISTANCE_LUNCH_REST = Beta('BETA_DISTANCE_LUNCH_REST', 0, -100, 100, 0)
BETA_DISTANCE_LUNCH_SELF = Beta('BETA_DISTANCE_LUNCH_SELF', 0, -100, 100, 0)
BETA_DISTANCE_LUNCH_FASTFOOD = Beta('BETA_DISTANCE_LUNCH_FASTFOOD', 0, -100, 100, 0)
BETA_DISTANCE_LUNCH_OTHER = Beta('BETA_DISTANCE_LUNCH_OTHER', 0, -100, 100, 0)
BETA_DISTANCE_LUNCH_CAF = Beta('BETA_DISTANCE_LUNCH_CAF', 0, -100, 100, 0)
BETA_DISTANCE_MORNING = Beta('BETA_DISTANCE_MORNING', 0, -100, 100, 0)
BETA_DISTANCE_AFTERNOON = Beta('BETA_DISTANCE_AFTERNOON', 0, -100, 100, 0)
BETA_NO_DISTANCE_AV = Beta('BETA_NO_DISTANCE_AV', 0, -100, 100, 0)
BETA_TAP_BEER_AFTER_LUNCH = Beta('BETA_TAP_BEER_AFTER_LUNCH', 0, -100, 100, 0)
BETA_EVALUATION_SELF = Beta('BETA_EVALUATION_SELF', 0, -100, 100, 0)
BETA_EVALUATION_CAFET = Beta('BETA_EVALUATION_CAFET', 0, -100, 100, 0)
BETA_EVALUATION_FAST_FOOD = Beta('BETA_EVALUATION_FAST_FOOD', 0, -100, 100, 0)
BETA_METEO_TERRACE = Beta('BETA_METEO_TERRACE', 0, -100, 100, 1)
BETA_CAPACITY_INSIDE = Beta('BETA_CAPACITY_INSIDE', 0, -100, 100, 0)
RHO_PREVIOUS_LUNCH_CHOICE = Beta('RHO_PREVIOUS_LUNCH_CHOICE', 0, -100, 100, 0)
RHO_PREVIOUS_MORNING_CHOICE = Beta('RHO_PREVIOUS_MORNING_CHOICE', 0, -100, 100, 0)

# Variables
one = 1
lunch11 = (H_START == 11 * M_START > 29.9) > 0
lunch12 = H_START == 12 
lunch13 = H_START == 13
dinner18 = H_START == 18
dinner19 = H_START == 19
morning7 = H_START == 7
morning8 = H_START == 8
morning9 = H_START == 9
morning10 = H_START == 10
morning11 = (H_START == 11 * M_START < 29.8) > 0
afternoon14 = H_START == 14
afternoon15 = H_START == 15
afternoon16 = H_START == 16
afternoon17 = H_START == 17
night20 = H_START == 20
night21 = H_START == 21
night_end21 = H_END == 21
night_end22 = H_END == 22
night = (night20 + night21 + night_end21 + night_end22) > 0
afternoon = (afternoon15 + afternoon16 + afternoon17 + afternoon14) > 0
morning = (morning8 + morning9 + morning10 + morning7 + morning11) > 0
dinner = (dinner18 + dinner19) > 0
lunch = (lunch11 + lunch12 + lunch13) > 0
first_year = SEMESTER == 2
after_lunch = (afternoon + night + dinner) > 0
self_true = SELF == 1
restaurant_true = RESTAURANT == 1
caravan_true = CARAVAN == 1
cafet_true = CAFETERIA == 1
rain_and_cold_max_20 = SUN_AND_HEAT_MIN_20 == 0
perso = SECTION_ID == 5
student_true = STUDENT == 1
self_cafet = (cafet_true + self_true + caravan_true + restaurant_true) > 0
capacity_at_lunch_inside_av_1 = (lunch * self_cafet) * CAPACITY_INSIDE_1 
capacity_at_lunch_inside_av_2 = (lunch * self_cafet) * CAPACITY_INSIDE_2 
capacity_at_lunch_inside_av_3 = (lunch * self_cafet) * CAPACITY_INSIDE_3 
capacity_at_lunch_inside_av_4 = (lunch * self_cafet) * CAPACITY_INSIDE_4 
capacity_at_lunch_inside_av_5 = (lunch * self_cafet) * CAPACITY_INSIDE_5 
capacity_at_lunch_inside_av_6 = (lunch * self_cafet) * CAPACITY_INSIDE_6 
capacity_at_lunch_inside_av_7 = (lunch * self_cafet) * CAPACITY_INSIDE_7 
capacity_at_lunch_inside_av_8 = (lunch * self_cafet) * CAPACITY_INSIDE_8 
capacity_at_lunch_inside_av_9 = (lunch * self_cafet) * CAPACITY_INSIDE_9 
capacity_at_lunch_inside_av_10 = (lunch * self_cafet) * CAPACITY_INSIDE_10 
capacity_at_lunch_inside_av_11 = (lunch * self_cafet) * CAPACITY_INSIDE_11 
capacity_at_lunch_inside_av_12 = (lunch * self_cafet) * CAPACITY_INSIDE_12 
capacity_at_lunch_inside_av_13 = (lunch * self_cafet) * CAPACITY_INSIDE_13 
capacity_at_lunch_inside_av_14 = (lunch * self_cafet) * CAPACITY_INSIDE_14 
capacity_at_lunch_inside_av_15 = (lunch * self_cafet) * CAPACITY_INSIDE_15 
capacity_at_lunch_inside_av_16 = (lunch * self_cafet) * CAPACITY_INSIDE_16 
capacity_at_lunch_inside_av_17 = (lunch * self_cafet) * CAPACITY_INSIDE_17 
capacity_at_lunch_inside_av_18 = (lunch * self_cafet) * CAPACITY_INSIDE_18 
capacity_at_lunch_inside_av_19 = (lunch * self_cafet) * CAPACITY_INSIDE_19 
capacity_at_lunch_inside_av_20 = (lunch * self_cafet) * CAPACITY_INSIDE_20 
capacity_at_lunch_inside_av_21 = (lunch * self_cafet) * CAPACITY_INSIDE_21 
capacity_at_lunch_outside_av_1 = (lunch * self_cafet) * CAPACITY_OUTSIDE_1 
capacity_at_lunch_outside_av_2 = (lunch * self_cafet) * CAPACITY_OUTSIDE_2 
capacity_at_lunch_outside_av_3 = (lunch * self_cafet) * CAPACITY_OUTSIDE_3 
capacity_at_lunch_outside_av_4 = (lunch * self_cafet) * CAPACITY_OUTSIDE_4 
capacity_at_lunch_outside_av_5 = (lunch * self_cafet) * CAPACITY_OUTSIDE_5 
capacity_at_lunch_outside_av_6 = (lunch * self_cafet) * CAPACITY_OUTSIDE_6 
capacity_at_lunch_outside_av_7 = (lunch * self_cafet) * CAPACITY_OUTSIDE_7 
capacity_at_lunch_outside_av_8 = (lunch * self_cafet) * CAPACITY_OUTSIDE_8 
capacity_at_lunch_outside_av_9 = (lunch * self_cafet) * CAPACITY_OUTSIDE_9 
capacity_at_lunch_outside_av_10 = (lunch * self_cafet) * CAPACITY_OUTSIDE_10 
capacity_at_lunch_outside_av_11 = (lunch * self_cafet) * CAPACITY_OUTSIDE_11 
capacity_at_lunch_outside_av_12 = (lunch * self_cafet) * CAPACITY_OUTSIDE_12 
capacity_at_lunch_outside_av_13 = (lunch * self_cafet) * CAPACITY_OUTSIDE_13 
capacity_at_lunch_outside_av_14 = (lunch * self_cafet) * CAPACITY_OUTSIDE_14 
capacity_at_lunch_outside_av_15 = (lunch * self_cafet) * CAPACITY_OUTSIDE_15 
capacity_at_lunch_outside_av_16 = (lunch * self_cafet) * CAPACITY_OUTSIDE_16 
capacity_at_lunch_outside_av_17 = (lunch * self_cafet) * CAPACITY_OUTSIDE_17 
capacity_at_lunch_outside_av_18 = (lunch * self_cafet) * CAPACITY_OUTSIDE_18 
capacity_at_lunch_outside_av_19 = (lunch * self_cafet) * CAPACITY_OUTSIDE_19 
capacity_at_lunch_outside_av_20 = (lunch * self_cafet) * CAPACITY_OUTSIDE_20 
capacity_at_lunch_outside_av_21 = (lunch * self_cafet) * CAPACITY_OUTSIDE_21  
meteo_terrace_av_1 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_1) * capacity_at_lunch_outside_av_1 
meteo_terrace_av_2 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_2) * capacity_at_lunch_outside_av_2 
meteo_terrace_av_3 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_3) * capacity_at_lunch_outside_av_3 
meteo_terrace_av_4 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_4) * capacity_at_lunch_outside_av_4 
meteo_terrace_av_5 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_5) * capacity_at_lunch_outside_av_5 
meteo_terrace_av_6 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_6) * capacity_at_lunch_outside_av_6 
meteo_terrace_av_7 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_7) * capacity_at_lunch_outside_av_7 
meteo_terrace_av_8 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_8) * capacity_at_lunch_outside_av_8 
meteo_terrace_av_9 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_9) * capacity_at_lunch_outside_av_9 
meteo_terrace_av_10 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_10) * capacity_at_lunch_outside_av_10 
meteo_terrace_av_11 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_11) * capacity_at_lunch_outside_av_11 
meteo_terrace_av_12 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_12) * capacity_at_lunch_outside_av_12 
meteo_terrace_av_13 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_13) * capacity_at_lunch_outside_av_13 
meteo_terrace_av_14 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_14) * capacity_at_lunch_outside_av_14 
meteo_terrace_av_15 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_15) * capacity_at_lunch_outside_av_15 
meteo_terrace_av_16 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_16) * capacity_at_lunch_outside_av_16 
meteo_terrace_av_17 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_17) * capacity_at_lunch_outside_av_17 
meteo_terrace_av_18 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_18) * capacity_at_lunch_outside_av_18 
meteo_terrace_av_19 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_19) * capacity_at_lunch_outside_av_19 
meteo_terrace_av_20 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_20) * capacity_at_lunch_outside_av_20 
meteo_terrace_av_21 = (SUN_AND_HEAT_MIN_20 * TERRACE_AV_21) * capacity_at_lunch_outside_av_21 
cap_inside_av_1 = capacity_at_lunch_inside_av_1 
cap_inside_av_2 = capacity_at_lunch_inside_av_2 
cap_inside_av_3 = capacity_at_lunch_inside_av_3 
cap_inside_av_4 = capacity_at_lunch_inside_av_4 
cap_inside_av_5 = capacity_at_lunch_inside_av_5 
cap_inside_av_6 = capacity_at_lunch_inside_av_6 
cap_inside_av_7 = capacity_at_lunch_inside_av_7 
cap_inside_av_8 = capacity_at_lunch_inside_av_8 
cap_inside_av_9 = capacity_at_lunch_inside_av_9 
cap_inside_av_10 = capacity_at_lunch_inside_av_10 
cap_inside_av_11 = capacity_at_lunch_inside_av_11 
cap_inside_av_12 = capacity_at_lunch_inside_av_12 
cap_inside_av_13 = capacity_at_lunch_inside_av_13 
cap_inside_av_14 = capacity_at_lunch_inside_av_14 
cap_inside_av_15 = capacity_at_lunch_inside_av_15 
cap_inside_av_16 = capacity_at_lunch_inside_av_16 
cap_inside_av_17 = capacity_at_lunch_inside_av_17 
cap_inside_av_18 = capacity_at_lunch_inside_av_18 
cap_inside_av_19 = capacity_at_lunch_inside_av_19 
cap_inside_av_20 = capacity_at_lunch_inside_av_20 
cap_inside_av_21 = capacity_at_lunch_inside_av_21 
morning_coffee_1 = morning * CAFE_AV_1 
morning_coffee_2 = morning * CAFE_AV_2 
morning_coffee_3 = morning * CAFE_AV_3 
morning_coffee_4 = morning * CAFE_AV_4 
morning_coffee_5 = morning * CAFE_AV_5 
morning_coffee_6 = morning * CAFE_AV_6 
morning_coffee_7 = morning * CAFE_AV_7 
morning_coffee_8 = morning * CAFE_AV_8 
morning_coffee_9 = morning * CAFE_AV_9 
morning_coffee_10 = morning * CAFE_AV_10 
morning_coffee_11 = morning * CAFE_AV_11 
morning_coffee_12 = morning * CAFE_AV_12 
morning_coffee_13 = morning * CAFE_AV_13 
morning_coffee_14 = morning * CAFE_AV_14 
morning_coffee_15 = morning * CAFE_AV_15 
morning_coffee_16 = morning * CAFE_AV_16 
morning_coffee_17 = morning * CAFE_AV_17 
morning_coffee_18 = morning * CAFE_AV_18 
morning_coffee_19 = morning * CAFE_AV_19 
morning_coffee_20 = morning * CAFE_AV_20 
morning_coffee_21 = morning * CAFE_AV_21 
distance_filter_1 = DISTANCE_1 > -1 
distance_filter_2 = DISTANCE_2 > -1 
distance_filter_3 = DISTANCE_3 > -1 
distance_filter_4 = DISTANCE_4 > -1 
distance_filter_5 = DISTANCE_5 > -1 
distance_filter_6 = DISTANCE_6 > -1 
distance_filter_7 = DISTANCE_7 > -1 
distance_filter_8 = DISTANCE_8 > -1 
distance_filter_9 = DISTANCE_9 > -1 
distance_filter_10 = DISTANCE_10 > -1 
distance_filter_11 = DISTANCE_11 > -1 
distance_filter_12 = DISTANCE_12 > -1 
distance_filter_13 = DISTANCE_13 > -1 
distance_filter_14 = DISTANCE_14 > -1 
distance_filter_15 = DISTANCE_15 > -1 
distance_filter_16 = DISTANCE_16 > -1 
distance_filter_17 = DISTANCE_17 > -1 
distance_filter_18 = DISTANCE_18 > -1 
distance_filter_19 = DISTANCE_19 > -1 
distance_filter_20 = DISTANCE_20 > -1 
distance_filter_21 = DISTANCE_21 > -1 
distance_no_av_1 = DISTANCE_1 == -1 
distance_no_av_2 = DISTANCE_2 == -1 
distance_no_av_3 = DISTANCE_3 == -1 
distance_no_av_4 = DISTANCE_4 == -1 
distance_no_av_5 = DISTANCE_5 == -1 
distance_no_av_6 = DISTANCE_6 == -1 
distance_no_av_7 = DISTANCE_7 == -1 
distance_no_av_8 = DISTANCE_8 == -1 
distance_no_av_9 = DISTANCE_9 == -1 
distance_no_av_10 = DISTANCE_10 == -1 
distance_no_av_11 = DISTANCE_11 == -1 
distance_no_av_12 = DISTANCE_12 == -1 
distance_no_av_13 = DISTANCE_13 == -1 
distance_no_av_14 = DISTANCE_14 == -1 
distance_no_av_15 = DISTANCE_15 == -1 
distance_no_av_16 = DISTANCE_16 == -1 
distance_no_av_17 = DISTANCE_17 == -1 
distance_no_av_18 = DISTANCE_18 == -1 
distance_no_av_19 = DISTANCE_19 == -1 
distance_no_av_20 = DISTANCE_20 == -1 
distance_no_av_21 = DISTANCE_21 == -1 
afternoon_workspace_av_1 = afternoon * WORKSPACE_AV_1 
afternoon_workspace_av_2 = afternoon * WORKSPACE_AV_2 
afternoon_workspace_av_3 = afternoon * WORKSPACE_AV_3 
afternoon_workspace_av_4 = afternoon * WORKSPACE_AV_4 
afternoon_workspace_av_5 = afternoon * WORKSPACE_AV_5 
afternoon_workspace_av_6 = afternoon * WORKSPACE_AV_6 
afternoon_workspace_av_7 = afternoon * WORKSPACE_AV_7 
afternoon_workspace_av_8 = afternoon * WORKSPACE_AV_8 
afternoon_workspace_av_9 = afternoon * WORKSPACE_AV_9 
afternoon_workspace_av_10 = afternoon * WORKSPACE_AV_10 
afternoon_workspace_av_11 = afternoon * WORKSPACE_AV_11 
afternoon_workspace_av_12 = afternoon * WORKSPACE_AV_12 
afternoon_workspace_av_13 = afternoon * WORKSPACE_AV_13 
afternoon_workspace_av_14 = afternoon * WORKSPACE_AV_14 
afternoon_workspace_av_15 = afternoon * WORKSPACE_AV_15 
afternoon_workspace_av_16 = afternoon * WORKSPACE_AV_16 
afternoon_workspace_av_17 = afternoon * WORKSPACE_AV_17 
afternoon_workspace_av_18 = afternoon * WORKSPACE_AV_18 
afternoon_workspace_av_19 = afternoon * WORKSPACE_AV_19 
afternoon_workspace_av_20 = afternoon * WORKSPACE_AV_20 
afternoon_workspace_av_21 = afternoon * WORKSPACE_AV_21 
lunch_distance_1 = lunch * ((distance_filter_1 * DISTANCE_1) + (distance_no_av_1 * 0))
lunch_distance_2 = lunch * ((distance_filter_2 * DISTANCE_2) + (distance_no_av_2 * 0))
lunch_distance_3 = lunch * ((distance_filter_3 * DISTANCE_3) + (distance_no_av_3 * 0))
lunch_distance_4 = lunch * ((distance_filter_4 * DISTANCE_4) + (distance_no_av_4 * 0))
lunch_distance_5 = lunch * ((distance_filter_5 * DISTANCE_5) + (distance_no_av_5 * 0))
lunch_distance_6 = lunch * ((distance_filter_6 * DISTANCE_6) + (distance_no_av_6 * 0))
lunch_distance_7 = lunch * ((distance_filter_7 * DISTANCE_7) + (distance_no_av_7 * 0))
lunch_distance_8 = lunch * ((distance_filter_8 * DISTANCE_8) + (distance_no_av_8 * 0))
lunch_distance_9 = lunch * ((distance_filter_9 * DISTANCE_9) + (distance_no_av_9 * 0))
lunch_distance_10 = lunch * ((distance_filter_10 * DISTANCE_10) + (distance_no_av_10 * 0))
lunch_distance_11 = lunch * ((distance_filter_11 * DISTANCE_11) + (distance_no_av_11 * 0))
lunch_distance_12 = lunch * ((distance_filter_12 * DISTANCE_12) + (distance_no_av_12 * 0))
lunch_distance_13 = lunch * ((distance_filter_13 * DISTANCE_13) + (distance_no_av_13 * 0))
lunch_distance_14 = lunch * ((distance_filter_14 * DISTANCE_14) + (distance_no_av_14 * 0))
lunch_distance_15 = lunch * ((distance_filter_15 * DISTANCE_15) + (distance_no_av_15 * 0))
lunch_distance_16 = lunch * ((distance_filter_16 * DISTANCE_16) + (distance_no_av_16 * 0))
lunch_distance_17 = lunch * ((distance_filter_17 * DISTANCE_17) + (distance_no_av_17 * 0))
lunch_distance_18 = lunch * ((distance_filter_18 * DISTANCE_18) + (distance_no_av_18 * 0))
lunch_distance_19 = lunch * ((distance_filter_19 * DISTANCE_19) + (distance_no_av_19 * 0))
lunch_distance_20 = lunch * ((distance_filter_20 * DISTANCE_20) + (distance_no_av_20 * 0))
lunch_distance_21 = lunch * ((distance_filter_21 * DISTANCE_21) + (distance_no_av_21 * 0))
morning_coffee_distance_1 = morning_coffee_1 * ((distance_filter_1 * DISTANCE_1) + (distance_no_av_1 * 0))
morning_coffee_distance_2 = morning_coffee_2 * ((distance_filter_2 * DISTANCE_2) + (distance_no_av_2 * 0))
morning_coffee_distance_3 = morning_coffee_3 * ((distance_filter_3 * DISTANCE_3) + (distance_no_av_3 * 0))
morning_coffee_distance_4 = morning_coffee_4 * ((distance_filter_4 * DISTANCE_4) + (distance_no_av_4 * 0))
morning_coffee_distance_5 = morning_coffee_5 * ((distance_filter_5 * DISTANCE_5) + (distance_no_av_5 * 0))
morning_coffee_distance_6 = morning_coffee_6 * ((distance_filter_6 * DISTANCE_6) + (distance_no_av_6 * 0))
morning_coffee_distance_7 = morning_coffee_7 * ((distance_filter_7 * DISTANCE_7) + (distance_no_av_7 * 0))
morning_coffee_distance_8 = morning_coffee_8 * ((distance_filter_8 * DISTANCE_8) + (distance_no_av_8 * 0))
morning_coffee_distance_9 = morning_coffee_9 * ((distance_filter_9 * DISTANCE_9) + (distance_no_av_9 * 0))
morning_coffee_distance_10 = morning_coffee_10 * ((distance_filter_10 * DISTANCE_10) + (distance_no_av_10 * 0))
morning_coffee_distance_11 = morning_coffee_11 * ((distance_filter_11 * DISTANCE_11) + (distance_no_av_11 * 0))
morning_coffee_distance_12 = morning_coffee_12 * ((distance_filter_12 * DISTANCE_12) + (distance_no_av_12 * 0))
morning_coffee_distance_13 = morning_coffee_13 * ((distance_filter_13 * DISTANCE_13) + (distance_no_av_13 * 0))
morning_coffee_distance_14 = morning_coffee_14 * ((distance_filter_14 * DISTANCE_14) + (distance_no_av_14 * 0))
morning_coffee_distance_15 = morning_coffee_15 * ((distance_filter_15 * DISTANCE_15) + (distance_no_av_15 * 0))
morning_coffee_distance_16 = morning_coffee_16 * ((distance_filter_16 * DISTANCE_16) + (distance_no_av_16 * 0))
morning_coffee_distance_17 = morning_coffee_17 * ((distance_filter_17 * DISTANCE_17) + (distance_no_av_17 * 0))
morning_coffee_distance_18 = morning_coffee_18 * ((distance_filter_18 * DISTANCE_18) + (distance_no_av_18 * 0))
morning_coffee_distance_19 = morning_coffee_19 * ((distance_filter_19 * DISTANCE_19) + (distance_no_av_19 * 0))
morning_coffee_distance_20 = morning_coffee_20 * ((distance_filter_20 * DISTANCE_20) + (distance_no_av_20 * 0))
morning_coffee_distance_21 = morning_coffee_21 * ((distance_filter_21 * DISTANCE_21) + (distance_no_av_21 * 0))
afternoon_workspace_distance_1 = afternoon_workspace_av_1 * ((distance_filter_1 * DISTANCE_1) + (distance_no_av_1 * 0))
afternoon_workspace_distance_2 = afternoon_workspace_av_2 * ((distance_filter_2 * DISTANCE_2) + (distance_no_av_2 * 0))
afternoon_workspace_distance_3 = afternoon_workspace_av_3 * ((distance_filter_3 * DISTANCE_3) + (distance_no_av_3 * 0))
afternoon_workspace_distance_4 = afternoon_workspace_av_4 * ((distance_filter_4 * DISTANCE_4) + (distance_no_av_4 * 0))
afternoon_workspace_distance_5 = afternoon_workspace_av_5 * ((distance_filter_5 * DISTANCE_5) + (distance_no_av_5 * 0))
afternoon_workspace_distance_6 = afternoon_workspace_av_6 * ((distance_filter_6 * DISTANCE_6) + (distance_no_av_6 * 0))
afternoon_workspace_distance_7 = afternoon_workspace_av_7 * ((distance_filter_7 * DISTANCE_7) + (distance_no_av_7 * 0))
afternoon_workspace_distance_8 = afternoon_workspace_av_8 * ((distance_filter_8 * DISTANCE_8) + (distance_no_av_8 * 0))
afternoon_workspace_distance_9 = afternoon_workspace_av_9 * ((distance_filter_9 * DISTANCE_9) + (distance_no_av_9 * 0))
afternoon_workspace_distance_10 = afternoon_workspace_av_10 * ((distance_filter_10 * DISTANCE_10) + (distance_no_av_10 * 0))
afternoon_workspace_distance_11 = afternoon_workspace_av_11 * ((distance_filter_11 * DISTANCE_11) + (distance_no_av_11 * 0))
afternoon_workspace_distance_12 = afternoon_workspace_av_12 * ((distance_filter_12 * DISTANCE_12) + (distance_no_av_12 * 0))
afternoon_workspace_distance_13 = afternoon_workspace_av_13 * ((distance_filter_13 * DISTANCE_13) + (distance_no_av_13 * 0))
afternoon_workspace_distance_14 = afternoon_workspace_av_14 * ((distance_filter_14 * DISTANCE_14) + (distance_no_av_14 * 0))
afternoon_workspace_distance_15 = afternoon_workspace_av_15 * ((distance_filter_15 * DISTANCE_15) + (distance_no_av_15 * 0))
afternoon_workspace_distance_16 = afternoon_workspace_av_16 * ((distance_filter_16 * DISTANCE_16) + (distance_no_av_16 * 0))
afternoon_workspace_distance_17 = afternoon_workspace_av_17 * ((distance_filter_17 * DISTANCE_17) + (distance_no_av_17 * 0))
afternoon_workspace_distance_18 = afternoon_workspace_av_18 * ((distance_filter_18 * DISTANCE_18) + (distance_no_av_18 * 0))
afternoon_workspace_distance_19 = afternoon_workspace_av_19 * ((distance_filter_19 * DISTANCE_19) + (distance_no_av_19 * 0))
afternoon_workspace_distance_20 = afternoon_workspace_av_20 * ((distance_filter_20 * DISTANCE_20) + (distance_no_av_20 * 0))
afternoon_workspace_distance_21 = afternoon_workspace_av_21 * ((distance_filter_21 * DISTANCE_21) + (distance_no_av_21 * 0))
lunch_hot_meal_av_1 = lunch * HOT_MEAL_AV_1 
lunch_hot_meal_av_2 = lunch * HOT_MEAL_AV_2 
lunch_hot_meal_av_3 = lunch * HOT_MEAL_AV_3 
lunch_hot_meal_av_4 = lunch * HOT_MEAL_AV_4 
lunch_hot_meal_av_5 = lunch * HOT_MEAL_AV_5 
lunch_hot_meal_av_6 = lunch * HOT_MEAL_AV_6 
lunch_hot_meal_av_7 = lunch * HOT_MEAL_AV_7 
lunch_hot_meal_av_8 = lunch * HOT_MEAL_AV_8 
lunch_hot_meal_av_9 = lunch * HOT_MEAL_AV_9 
lunch_hot_meal_av_10 = lunch * HOT_MEAL_AV_10 
lunch_hot_meal_av_11 = lunch * HOT_MEAL_AV_11 
lunch_hot_meal_av_12 = lunch * HOT_MEAL_AV_12 
lunch_hot_meal_av_13 = lunch * HOT_MEAL_AV_13 
lunch_hot_meal_av_14 = lunch * HOT_MEAL_AV_14 
lunch_hot_meal_av_15 = lunch * HOT_MEAL_AV_15 
lunch_hot_meal_av_16 = lunch * HOT_MEAL_AV_16 
lunch_hot_meal_av_17 = lunch * HOT_MEAL_AV_17 
lunch_hot_meal_av_18 = lunch * HOT_MEAL_AV_18 
lunch_hot_meal_av_19 = lunch * HOT_MEAL_AV_19 
lunch_hot_meal_av_20 = lunch * HOT_MEAL_AV_20 
lunch_hot_meal_av_21 = lunch * HOT_MEAL_AV_21 
lunch_price_min_1 = (lunch * MIN_PRICE_1) * lunch_hot_meal_av_1 
lunch_price_min_2 = (lunch * MIN_PRICE_2) * lunch_hot_meal_av_2 
lunch_price_min_3 = (lunch * MIN_PRICE_3) * lunch_hot_meal_av_3 
lunch_price_min_4 = (lunch * MIN_PRICE_4) * lunch_hot_meal_av_4 
lunch_price_min_5 = (lunch * MIN_PRICE_5) * lunch_hot_meal_av_5 
lunch_price_min_6 = (lunch * MIN_PRICE_6) * lunch_hot_meal_av_6 
lunch_price_min_7 = (lunch * MIN_PRICE_7) * lunch_hot_meal_av_7 
lunch_price_min_8 = (lunch * MIN_PRICE_8) * lunch_hot_meal_av_8 
lunch_price_min_9 = (lunch * MIN_PRICE_9) * lunch_hot_meal_av_9 
lunch_price_min_10 = (lunch * MIN_PRICE_10) * lunch_hot_meal_av_10 
lunch_price_min_11 = (lunch * MIN_PRICE_11) * lunch_hot_meal_av_11 
lunch_price_min_12 = (lunch * MIN_PRICE_12) * lunch_hot_meal_av_12 
lunch_price_min_13 = (lunch * MIN_PRICE_13) * lunch_hot_meal_av_13 
lunch_price_min_14 = (lunch * MIN_PRICE_14) * lunch_hot_meal_av_14 
lunch_price_min_15 = (lunch * MIN_PRICE_15) * lunch_hot_meal_av_15 
lunch_price_min_16 = (lunch * MIN_PRICE_16) * lunch_hot_meal_av_16 
lunch_price_min_17 = (lunch * MIN_PRICE_17) * lunch_hot_meal_av_17 
lunch_price_min_18 = (lunch * MIN_PRICE_18) * lunch_hot_meal_av_18 
lunch_price_min_19 = (lunch * MIN_PRICE_19) * lunch_hot_meal_av_19 
lunch_price_min_20 = (lunch * MIN_PRICE_20) * lunch_hot_meal_av_20 
lunch_price_min_21 = (lunch * MIN_PRICE_21) * lunch_hot_meal_av_21 
beer_in_the_afternoon_dinner_night_av_1 = after_lunch * TAP_BEER_AV_1 
beer_in_the_afternoon_dinner_night_av_2 = after_lunch * TAP_BEER_AV_2 
beer_in_the_afternoon_dinner_night_av_3 = after_lunch * TAP_BEER_AV_3 
beer_in_the_afternoon_dinner_night_av_4 = after_lunch * TAP_BEER_AV_4 
beer_in_the_afternoon_dinner_night_av_5 = after_lunch * TAP_BEER_AV_5 
beer_in_the_afternoon_dinner_night_av_6 = after_lunch * TAP_BEER_AV_6 
beer_in_the_afternoon_dinner_night_av_7 = after_lunch * TAP_BEER_AV_7 
beer_in_the_afternoon_dinner_night_av_8 = after_lunch * TAP_BEER_AV_8 
beer_in_the_afternoon_dinner_night_av_9 = after_lunch * TAP_BEER_AV_9 
beer_in_the_afternoon_dinner_night_av_10 = after_lunch * TAP_BEER_AV_10 
beer_in_the_afternoon_dinner_night_av_11 = after_lunch * TAP_BEER_AV_11 
beer_in_the_afternoon_dinner_night_av_12 = after_lunch * TAP_BEER_AV_12 
beer_in_the_afternoon_dinner_night_av_13 = after_lunch * TAP_BEER_AV_13 
beer_in_the_afternoon_dinner_night_av_14 = after_lunch * TAP_BEER_AV_14 
beer_in_the_afternoon_dinner_night_av_15 = after_lunch * TAP_BEER_AV_15 
beer_in_the_afternoon_dinner_night_av_16 = after_lunch * TAP_BEER_AV_16 
beer_in_the_afternoon_dinner_night_av_17 = after_lunch * TAP_BEER_AV_17 
beer_in_the_afternoon_dinner_night_av_18 = after_lunch * TAP_BEER_AV_18 
beer_in_the_afternoon_dinner_night_av_19 = after_lunch * TAP_BEER_AV_19 
beer_in_the_afternoon_dinner_night_av_20 = after_lunch * TAP_BEER_AV_20 
beer_in_the_afternoon_dinner_night_av_21 = after_lunch * TAP_BEER_AV_21 
service_at_table_lunch_av_1 = (lunch * SERVICE_TABLE_AV_1) * perso 
service_at_table_lunch_av_2 = (lunch * SERVICE_TABLE_AV_2) * perso 
service_at_table_lunch_av_3 = (lunch * SERVICE_TABLE_AV_3) * perso 
service_at_table_lunch_av_4 = (lunch * SERVICE_TABLE_AV_4) * perso 
service_at_table_lunch_av_5 = (lunch * SERVICE_TABLE_AV_5) * perso 
service_at_table_lunch_av_6 = (lunch * SERVICE_TABLE_AV_6) * perso 
service_at_table_lunch_av_7 = (lunch * SERVICE_TABLE_AV_7) * perso 
service_at_table_lunch_av_8 = (lunch * SERVICE_TABLE_AV_8) * perso 
service_at_table_lunch_av_9 = (lunch * SERVICE_TABLE_AV_9) * perso 
service_at_table_lunch_av_10 = (lunch * SERVICE_TABLE_AV_10) * perso 
service_at_table_lunch_av_11 = (lunch * SERVICE_TABLE_AV_11) * perso 
service_at_table_lunch_av_12 = (lunch * SERVICE_TABLE_AV_12) * perso 
service_at_table_lunch_av_13 = (lunch * SERVICE_TABLE_AV_13) * perso 
service_at_table_lunch_av_14 = (lunch * SERVICE_TABLE_AV_14) * perso 
service_at_table_lunch_av_15 = (lunch * SERVICE_TABLE_AV_15) * perso 
service_at_table_lunch_av_16 = (lunch * SERVICE_TABLE_AV_16) * perso 
service_at_table_lunch_av_17 = (lunch * SERVICE_TABLE_AV_17) * perso 
service_at_table_lunch_av_18 = (lunch * SERVICE_TABLE_AV_18) * perso 
service_at_table_lunch_av_19 = (lunch * SERVICE_TABLE_AV_19) * perso 
service_at_table_lunch_av_20 = (lunch * SERVICE_TABLE_AV_20) * perso 
service_at_table_lunch_av_21 = (lunch * SERVICE_TABLE_AV_21) * perso 
sandwich_lunch_av_1 = lunch * SANDWICH_AV_1 
sandwich_lunch_av_2 = lunch * SANDWICH_AV_2 
sandwich_lunch_av_3 = lunch * SANDWICH_AV_3 
sandwich_lunch_av_4 = lunch * SANDWICH_AV_4 
sandwich_lunch_av_5 = lunch * SANDWICH_AV_5 
sandwich_lunch_av_6 = lunch * SANDWICH_AV_6 
sandwich_lunch_av_7 = lunch * SANDWICH_AV_7 
sandwich_lunch_av_8 = lunch * SANDWICH_AV_8 
sandwich_lunch_av_9 = lunch * SANDWICH_AV_9 
sandwich_lunch_av_10 = lunch * SANDWICH_AV_10 
sandwich_lunch_av_11 = lunch * SANDWICH_AV_11 
sandwich_lunch_av_12 = lunch * SANDWICH_AV_12 
sandwich_lunch_av_13 = lunch * SANDWICH_AV_13 
sandwich_lunch_av_14 = lunch * SANDWICH_AV_14 
sandwich_lunch_av_15 = lunch * SANDWICH_AV_15 
sandwich_lunch_av_16 = lunch * SANDWICH_AV_16 
sandwich_lunch_av_17 = lunch * SANDWICH_AV_17 
sandwich_lunch_av_18 = lunch * SANDWICH_AV_18 
sandwich_lunch_av_19 = lunch * SANDWICH_AV_19 
sandwich_lunch_av_20 = lunch * SANDWICH_AV_20 
sandwich_lunch_av_21 = lunch * SANDWICH_AV_21 
last_choice_filter_1 = LAST_CHOICE_LAST_TIME_TRUE_1 > -1 
last_choice_filter_2 = LAST_CHOICE_LAST_TIME_TRUE_2 > -1 
last_choice_filter_3 = LAST_CHOICE_LAST_TIME_TRUE_3 > -1 
last_choice_filter_4 = LAST_CHOICE_LAST_TIME_TRUE_4 > -1 
last_choice_filter_5 = LAST_CHOICE_LAST_TIME_TRUE_5 > -1 
last_choice_filter_6 = LAST_CHOICE_LAST_TIME_TRUE_6 > -1 
last_choice_filter_7 = LAST_CHOICE_LAST_TIME_TRUE_7 > -1 
last_choice_filter_8 = LAST_CHOICE_LAST_TIME_TRUE_8 > -1 
last_choice_filter_9 = LAST_CHOICE_LAST_TIME_TRUE_9 > -1 
last_choice_filter_10 = LAST_CHOICE_LAST_TIME_TRUE_10 > -1 
last_choice_filter_11 = LAST_CHOICE_LAST_TIME_TRUE_11 > -1 
last_choice_filter_12 = LAST_CHOICE_LAST_TIME_TRUE_12 > -1 
last_choice_filter_13 = LAST_CHOICE_LAST_TIME_TRUE_13 > -1 
last_choice_filter_14 = LAST_CHOICE_LAST_TIME_TRUE_14 > -1 
last_choice_filter_15 = LAST_CHOICE_LAST_TIME_TRUE_15 > -1 
last_choice_filter_16 = LAST_CHOICE_LAST_TIME_TRUE_16 > -1 
last_choice_filter_17 = LAST_CHOICE_LAST_TIME_TRUE_17 > -1 
last_choice_filter_18 = LAST_CHOICE_LAST_TIME_TRUE_18 > -1 
last_choice_filter_19 = LAST_CHOICE_LAST_TIME_TRUE_19 > -1 
last_choice_filter_20 = LAST_CHOICE_LAST_TIME_TRUE_20 > -1 
last_choice_filter_21 = LAST_CHOICE_LAST_TIME_TRUE_21 > -1 
no_previous_choice_filter_1 = LAST_CHOICE_LAST_TIME_TRUE_1 == -1 
no_previous_choice_filter_2 = LAST_CHOICE_LAST_TIME_TRUE_2 == -1 
no_previous_choice_filter_3 = LAST_CHOICE_LAST_TIME_TRUE_3 == -1 
no_previous_choice_filter_4 = LAST_CHOICE_LAST_TIME_TRUE_4 == -1 
no_previous_choice_filter_5 = LAST_CHOICE_LAST_TIME_TRUE_5 == -1 
no_previous_choice_filter_6 = LAST_CHOICE_LAST_TIME_TRUE_6 == -1 
no_previous_choice_filter_7 = LAST_CHOICE_LAST_TIME_TRUE_7 == -1 
no_previous_choice_filter_8 = LAST_CHOICE_LAST_TIME_TRUE_8 == -1 
no_previous_choice_filter_9 = LAST_CHOICE_LAST_TIME_TRUE_9 == -1 
no_previous_choice_filter_10 = LAST_CHOICE_LAST_TIME_TRUE_10 == -1 
no_previous_choice_filter_11 = LAST_CHOICE_LAST_TIME_TRUE_11 == -1 
no_previous_choice_filter_12 = LAST_CHOICE_LAST_TIME_TRUE_12 == -1 
no_previous_choice_filter_13 = LAST_CHOICE_LAST_TIME_TRUE_13 == -1 
no_previous_choice_filter_14 = LAST_CHOICE_LAST_TIME_TRUE_14 == -1 
no_previous_choice_filter_15 = LAST_CHOICE_LAST_TIME_TRUE_15 == -1 
no_previous_choice_filter_16 = LAST_CHOICE_LAST_TIME_TRUE_16 == -1 
no_previous_choice_filter_17 = LAST_CHOICE_LAST_TIME_TRUE_17 == -1 
no_previous_choice_filter_18 = LAST_CHOICE_LAST_TIME_TRUE_18 == -1 
no_previous_choice_filter_19 = LAST_CHOICE_LAST_TIME_TRUE_19 == -1 
no_previous_choice_filter_20 = LAST_CHOICE_LAST_TIME_TRUE_20 == -1 
no_previous_choice_filter_21 = LAST_CHOICE_LAST_TIME_TRUE_21 == -1 
last_choice_true_1 = (last_choice_filter_1 * LAST_CHOICE_LAST_TIME_TRUE_1) + (no_previous_choice_filter_1 * 0)
last_choice_true_2 = (last_choice_filter_2 * LAST_CHOICE_LAST_TIME_TRUE_2) + (no_previous_choice_filter_2 * 0)
last_choice_true_3 = (last_choice_filter_3 * LAST_CHOICE_LAST_TIME_TRUE_3) + (no_previous_choice_filter_3 * 0)
last_choice_true_4 = (last_choice_filter_4 * LAST_CHOICE_LAST_TIME_TRUE_4) + (no_previous_choice_filter_4 * 0)
last_choice_true_5 = (last_choice_filter_5 * LAST_CHOICE_LAST_TIME_TRUE_5) + (no_previous_choice_filter_5 * 0)
last_choice_true_6 = (last_choice_filter_6 * LAST_CHOICE_LAST_TIME_TRUE_6) + (no_previous_choice_filter_6 * 0)
last_choice_true_7 = (last_choice_filter_7 * LAST_CHOICE_LAST_TIME_TRUE_7) + (no_previous_choice_filter_7 * 0)
last_choice_true_8 = (last_choice_filter_8 * LAST_CHOICE_LAST_TIME_TRUE_8) + (no_previous_choice_filter_8 * 0)
last_choice_true_9 = (last_choice_filter_9 * LAST_CHOICE_LAST_TIME_TRUE_9) + (no_previous_choice_filter_9 * 0)
last_choice_true_10 = (last_choice_filter_10 * LAST_CHOICE_LAST_TIME_TRUE_10) + (no_previous_choice_filter_10 * 0)
last_choice_true_11 = (last_choice_filter_11 * LAST_CHOICE_LAST_TIME_TRUE_11) + (no_previous_choice_filter_11 * 0)
last_choice_true_12 = (last_choice_filter_12 * LAST_CHOICE_LAST_TIME_TRUE_12) + (no_previous_choice_filter_12 * 0)
last_choice_true_13 = (last_choice_filter_13 * LAST_CHOICE_LAST_TIME_TRUE_13) + (no_previous_choice_filter_13 * 0)
last_choice_true_14 = (last_choice_filter_14 * LAST_CHOICE_LAST_TIME_TRUE_14) + (no_previous_choice_filter_14 * 0)
last_choice_true_15 = (last_choice_filter_15 * LAST_CHOICE_LAST_TIME_TRUE_15) + (no_previous_choice_filter_15 * 0)
last_choice_true_16 = (last_choice_filter_16 * LAST_CHOICE_LAST_TIME_TRUE_16) + (no_previous_choice_filter_16 * 0)
last_choice_true_17 = (last_choice_filter_17 * LAST_CHOICE_LAST_TIME_TRUE_17) + (no_previous_choice_filter_17 * 0)
last_choice_true_18 = (last_choice_filter_18 * LAST_CHOICE_LAST_TIME_TRUE_18) + (no_previous_choice_filter_18 * 0)
last_choice_true_19 = (last_choice_filter_19 * LAST_CHOICE_LAST_TIME_TRUE_19) + (no_previous_choice_filter_19 * 0)
last_choice_true_20 = (last_choice_filter_20 * LAST_CHOICE_LAST_TIME_TRUE_20) + (no_previous_choice_filter_20 * 0)
last_choice_true_21 = (last_choice_filter_21 * LAST_CHOICE_LAST_TIME_TRUE_21) + (no_previous_choice_filter_21 * 0)
evaluation_filter_1 = EVALUATION_2013_1 > -1 
evaluation_filter_2 = EVALUATION_2013_2 > -1 
evaluation_filter_3 = EVALUATION_2013_3 > -1 
evaluation_filter_4 = EVALUATION_2013_4 > -1 
evaluation_filter_5 = EVALUATION_2013_5 > -1 
evaluation_filter_6 = EVALUATION_2013_6 > -1 
evaluation_filter_7 = EVALUATION_2013_7 > -1 
evaluation_filter_8 = EVALUATION_2013_8 > -1 
evaluation_filter_9 = EVALUATION_2013_9 > -1 
evaluation_filter_10 = EVALUATION_2013_10 > -1 
evaluation_filter_11 = EVALUATION_2013_11 > -1 
evaluation_filter_12 = EVALUATION_2013_12 > -1 
evaluation_filter_13 = EVALUATION_2013_13 > -1 
evaluation_filter_14 = EVALUATION_2013_14 > -1 
evaluation_filter_15 = EVALUATION_2013_15 > -1 
evaluation_filter_16 = EVALUATION_2013_16 > -1 
evaluation_filter_17 = EVALUATION_2013_17 > -1 
evaluation_filter_18 = EVALUATION_2013_18 > -1 
evaluation_filter_19 = EVALUATION_2013_19 > -1 
evaluation_filter_20 = EVALUATION_2013_20 > -1 
evaluation_filter_21 = EVALUATION_2013_21 > -1 
evaluation_2013_self_1 = ((evaluation_filter_1 * EVALUATION_2013_1) * self_true) * lunch 
evaluation_2013_self_2 = ((evaluation_filter_2 * EVALUATION_2013_2) * self_true) * lunch 
evaluation_2013_self_3 = ((evaluation_filter_3 * EVALUATION_2013_3) * self_true) * lunch 
evaluation_2013_self_4 = ((evaluation_filter_4 * EVALUATION_2013_4) * self_true) * lunch 
evaluation_2013_self_5 = ((evaluation_filter_5 * EVALUATION_2013_5) * self_true) * lunch 
evaluation_2013_self_6 = ((evaluation_filter_6 * EVALUATION_2013_6) * self_true) * lunch 
evaluation_2013_self_7 = ((evaluation_filter_7 * EVALUATION_2013_7) * self_true) * lunch 
evaluation_2013_self_8 = ((evaluation_filter_8 * EVALUATION_2013_8) * self_true) * lunch 
evaluation_2013_self_9 = ((evaluation_filter_9 * EVALUATION_2013_9) * self_true) * lunch 
evaluation_2013_self_10 = ((evaluation_filter_10 * EVALUATION_2013_10) * self_true) * lunch 
evaluation_2013_self_11 = ((evaluation_filter_11 * EVALUATION_2013_11) * self_true) * lunch 
evaluation_2013_self_12 = ((evaluation_filter_12 * EVALUATION_2013_12) * self_true) * lunch 
evaluation_2013_self_13 = ((evaluation_filter_13 * EVALUATION_2013_13) * self_true) * lunch 
evaluation_2013_self_14 = ((evaluation_filter_14 * EVALUATION_2013_14) * self_true) * lunch 
evaluation_2013_self_15 = ((evaluation_filter_15 * EVALUATION_2013_15) * self_true) * lunch 
evaluation_2013_self_16 = ((evaluation_filter_16 * EVALUATION_2013_16) * self_true) * lunch 
evaluation_2013_self_17 = ((evaluation_filter_17 * EVALUATION_2013_17) * self_true) * lunch 
evaluation_2013_self_18 = ((evaluation_filter_18 * EVALUATION_2013_18) * self_true) * lunch 
evaluation_2013_self_19 = ((evaluation_filter_19 * EVALUATION_2013_19) * self_true) * lunch 
evaluation_2013_self_20 = ((evaluation_filter_20 * EVALUATION_2013_20) * self_true) * lunch 
evaluation_2013_self_21 = ((evaluation_filter_21 * EVALUATION_2013_21) * self_true) * lunch 
evaluation_2013_cafet_1 = ((evaluation_filter_1 * EVALUATION_2013_1) * cafet_true) * lunch 
evaluation_2013_cafet_2 = ((evaluation_filter_2 * EVALUATION_2013_2) * cafet_true) * lunch 
evaluation_2013_cafet_3 = ((evaluation_filter_3 * EVALUATION_2013_3) * cafet_true) * lunch 
evaluation_2013_cafet_4 = ((evaluation_filter_4 * EVALUATION_2013_4) * cafet_true) * lunch 
evaluation_2013_cafet_5 = ((evaluation_filter_5 * EVALUATION_2013_5) * cafet_true) * lunch 
evaluation_2013_cafet_6 = ((evaluation_filter_6 * EVALUATION_2013_6) * cafet_true) * lunch 
evaluation_2013_cafet_7 = ((evaluation_filter_7 * EVALUATION_2013_7) * cafet_true) * lunch 
evaluation_2013_cafet_8 = ((evaluation_filter_8 * EVALUATION_2013_8) * cafet_true) * lunch 
evaluation_2013_cafet_9 = ((evaluation_filter_9 * EVALUATION_2013_9) * cafet_true) * lunch 
evaluation_2013_cafet_10 = ((evaluation_filter_10 * EVALUATION_2013_10) * cafet_true) * lunch 
evaluation_2013_cafet_11 = ((evaluation_filter_11 * EVALUATION_2013_11) * cafet_true) * lunch 
evaluation_2013_cafet_12 = ((evaluation_filter_12 * EVALUATION_2013_12) * cafet_true) * lunch 
evaluation_2013_cafet_13 = ((evaluation_filter_13 * EVALUATION_2013_13) * cafet_true) * lunch 
evaluation_2013_cafet_14 = ((evaluation_filter_14 * EVALUATION_2013_14) * cafet_true) * lunch 
evaluation_2013_cafet_15 = ((evaluation_filter_15 * EVALUATION_2013_15) * cafet_true) * lunch 
evaluation_2013_cafet_16 = ((evaluation_filter_16 * EVALUATION_2013_16) * cafet_true) * lunch 
evaluation_2013_cafet_17 = ((evaluation_filter_17 * EVALUATION_2013_17) * cafet_true) * lunch 
evaluation_2013_cafet_18 = ((evaluation_filter_18 * EVALUATION_2013_18) * cafet_true) * lunch 
evaluation_2013_cafet_19 = ((evaluation_filter_19 * EVALUATION_2013_19) * cafet_true) * lunch 
evaluation_2013_cafet_20 = ((evaluation_filter_20 * EVALUATION_2013_20) * cafet_true) * lunch 
evaluation_2013_cafet_21 = ((evaluation_filter_21 * EVALUATION_2013_21) * cafet_true) * lunch 
evaluation_2013_self_cafet_1 = ((evaluation_filter_1 * EVALUATION_2013_1) * self_cafet) * lunch 
evaluation_2013_self_cafet_2 = ((evaluation_filter_2 * EVALUATION_2013_2) * self_cafet) * lunch 
evaluation_2013_self_cafet_3 = ((evaluation_filter_3 * EVALUATION_2013_3) * self_cafet) * lunch 
evaluation_2013_self_cafet_4 = ((evaluation_filter_4 * EVALUATION_2013_4) * self_cafet) * lunch 
evaluation_2013_self_cafet_5 = ((evaluation_filter_5 * EVALUATION_2013_5) * self_cafet) * lunch 
evaluation_2013_self_cafet_6 = ((evaluation_filter_6 * EVALUATION_2013_6) * self_cafet) * lunch 
evaluation_2013_self_cafet_7 = ((evaluation_filter_7 * EVALUATION_2013_7) * self_cafet) * lunch 
evaluation_2013_self_cafet_8 = ((evaluation_filter_8 * EVALUATION_2013_8) * self_cafet) * lunch 
evaluation_2013_self_cafet_9 = ((evaluation_filter_9 * EVALUATION_2013_9) * self_cafet) * lunch 
evaluation_2013_self_cafet_10 = ((evaluation_filter_10 * EVALUATION_2013_10) * self_cafet) * lunch 
evaluation_2013_self_cafet_11 = ((evaluation_filter_11 * EVALUATION_2013_11) * self_cafet) * lunch 
evaluation_2013_self_cafet_12 = ((evaluation_filter_12 * EVALUATION_2013_12) * self_cafet) * lunch 
evaluation_2013_self_cafet_13 = ((evaluation_filter_13 * EVALUATION_2013_13) * self_cafet) * lunch 
evaluation_2013_self_cafet_14 = ((evaluation_filter_14 * EVALUATION_2013_14) * self_cafet) * lunch 
evaluation_2013_self_cafet_15 = ((evaluation_filter_15 * EVALUATION_2013_15) * self_cafet) * lunch 
evaluation_2013_self_cafet_16 = ((evaluation_filter_16 * EVALUATION_2013_16) * self_cafet) * lunch 
evaluation_2013_self_cafet_17 = ((evaluation_filter_17 * EVALUATION_2013_17) * self_cafet) * lunch 
evaluation_2013_self_cafet_18 = ((evaluation_filter_18 * EVALUATION_2013_18) * self_cafet) * lunch 
evaluation_2013_self_cafet_19 = ((evaluation_filter_19 * EVALUATION_2013_19) * self_cafet) * lunch 
evaluation_2013_self_cafet_20 = ((evaluation_filter_20 * EVALUATION_2013_20) * self_cafet) * lunch 
evaluation_2013_self_cafet_21 = ((evaluation_filter_21 * EVALUATION_2013_21) * self_cafet) * lunch
first_choice_true_filter_1 = FIRST_CHOICE_TRUE_1 > -1 
first_choice_true_filter_2 = FIRST_CHOICE_TRUE_2 > -1 
first_choice_true_filter_3 = FIRST_CHOICE_TRUE_3 > -1 
first_choice_true_filter_4 = FIRST_CHOICE_TRUE_4 > -1 
first_choice_true_filter_5 = FIRST_CHOICE_TRUE_5 > -1 
first_choice_true_filter_6 = FIRST_CHOICE_TRUE_6 > -1 
first_choice_true_filter_7 = FIRST_CHOICE_TRUE_7 > -1 
first_choice_true_filter_8 = FIRST_CHOICE_TRUE_8 > -1 
first_choice_true_filter_9 = FIRST_CHOICE_TRUE_9 > -1 
first_choice_true_filter_10 = FIRST_CHOICE_TRUE_10 > -1 
first_choice_true_filter_11 = FIRST_CHOICE_TRUE_11 > -1 
first_choice_true_filter_12 = FIRST_CHOICE_TRUE_12 > -1 
first_choice_true_filter_13 = FIRST_CHOICE_TRUE_13 > -1 
first_choice_true_filter_14 = FIRST_CHOICE_TRUE_14 > -1 
first_choice_true_filter_15 = FIRST_CHOICE_TRUE_15 > -1 
first_choice_true_filter_16 = FIRST_CHOICE_TRUE_16 > -1 
first_choice_true_filter_17 = FIRST_CHOICE_TRUE_17 > -1 
first_choice_true_filter_18 = FIRST_CHOICE_TRUE_18 > -1 
first_choice_true_filter_19 = FIRST_CHOICE_TRUE_19 > -1 
first_choice_true_filter_20 = FIRST_CHOICE_TRUE_20 > -1 
first_choice_true_filter_21 = FIRST_CHOICE_TRUE_21 > -1 
first_choice_filter_1 = FIRST_CHOICE_TRUE_1 * first_choice_true_filter_1 
first_choice_filter_2 = FIRST_CHOICE_TRUE_2 * first_choice_true_filter_2 
first_choice_filter_3 = FIRST_CHOICE_TRUE_3 * first_choice_true_filter_3 
first_choice_filter_4 = FIRST_CHOICE_TRUE_4 * first_choice_true_filter_4 
first_choice_filter_5 = FIRST_CHOICE_TRUE_5 * first_choice_true_filter_5 
first_choice_filter_6 = FIRST_CHOICE_TRUE_6 * first_choice_true_filter_6 
first_choice_filter_7 = FIRST_CHOICE_TRUE_7 * first_choice_true_filter_7 
first_choice_filter_8 = FIRST_CHOICE_TRUE_8 * first_choice_true_filter_8 
first_choice_filter_9 = FIRST_CHOICE_TRUE_9 * first_choice_true_filter_9 
first_choice_filter_10 = FIRST_CHOICE_TRUE_10 * first_choice_true_filter_10 
first_choice_filter_11 = FIRST_CHOICE_TRUE_11 * first_choice_true_filter_11 
first_choice_filter_12 = FIRST_CHOICE_TRUE_12 * first_choice_true_filter_12 
first_choice_filter_13 = FIRST_CHOICE_TRUE_13 * first_choice_true_filter_13 
first_choice_filter_14 = FIRST_CHOICE_TRUE_14 * first_choice_true_filter_14 
first_choice_filter_15 = FIRST_CHOICE_TRUE_15 * first_choice_true_filter_15 
first_choice_filter_16 = FIRST_CHOICE_TRUE_16 * first_choice_true_filter_16 
first_choice_filter_17 = FIRST_CHOICE_TRUE_17 * first_choice_true_filter_17 
first_choice_filter_18 = FIRST_CHOICE_TRUE_18 * first_choice_true_filter_18 
first_choice_filter_19 = FIRST_CHOICE_TRUE_19 * first_choice_true_filter_19 
first_choice_filter_20 = FIRST_CHOICE_TRUE_20 * first_choice_true_filter_20 
first_choice_filter_21 = FIRST_CHOICE_TRUE_21 * first_choice_true_filter_21 
dinner_av_1 = DINNER_HOT_MEAL_AV_1 * dinner 
dinner_av_2 = DINNER_HOT_MEAL_AV_2 * dinner 
dinner_av_3 = DINNER_HOT_MEAL_AV_3 * dinner 
dinner_av_4 = DINNER_HOT_MEAL_AV_4 * dinner 
dinner_av_5 = DINNER_HOT_MEAL_AV_5 * dinner 
dinner_av_6 = DINNER_HOT_MEAL_AV_6 * dinner 
dinner_av_7 = DINNER_HOT_MEAL_AV_7 * dinner 
dinner_av_8 = DINNER_HOT_MEAL_AV_8 * dinner 
dinner_av_9 = DINNER_HOT_MEAL_AV_9 * dinner 
dinner_av_10 = DINNER_HOT_MEAL_AV_10 * dinner 
dinner_av_11 = DINNER_HOT_MEAL_AV_11 * dinner 
dinner_av_12 = DINNER_HOT_MEAL_AV_12 * dinner 
dinner_av_13 = DINNER_HOT_MEAL_AV_13 * dinner 
dinner_av_14 = DINNER_HOT_MEAL_AV_14 * dinner 
dinner_av_15 = DINNER_HOT_MEAL_AV_15 * dinner 
dinner_av_16 = DINNER_HOT_MEAL_AV_16 * dinner 
dinner_av_17 = DINNER_HOT_MEAL_AV_17 * dinner 
dinner_av_18 = DINNER_HOT_MEAL_AV_18 * dinner 
dinner_av_19 = DINNER_HOT_MEAL_AV_19 * dinner 
dinner_av_20 = DINNER_HOT_MEAL_AV_20 * dinner 
dinner_av_21 = DINNER_HOT_MEAL_AV_21 * dinner 
lunch_price_min_student_1 = (lunch * MIN_PRICE_1) * student_true 
lunch_price_min_student_2 = (lunch * MIN_PRICE_2) * student_true 
lunch_price_min_student_3 = (lunch * MIN_PRICE_3) * student_true 
lunch_price_min_student_4 = (lunch * MIN_PRICE_4) * student_true 
lunch_price_min_student_5 = (lunch * MIN_PRICE_5) * student_true 
lunch_price_min_student_6 = (lunch * MIN_PRICE_6) * student_true 
lunch_price_min_student_7 = (lunch * MIN_PRICE_7) * student_true 
lunch_price_min_student_8 = (lunch * MIN_PRICE_8) * student_true 
lunch_price_min_student_9 = (lunch * MIN_PRICE_9) * student_true 
lunch_price_min_student_10 = (lunch * MIN_PRICE_10) * student_true 
lunch_price_min_student_11 = (lunch * MIN_PRICE_11) * student_true 
lunch_price_min_student_12 = (lunch * MIN_PRICE_12) * student_true 
lunch_price_min_student_13 = (lunch * MIN_PRICE_13) * student_true 
lunch_price_min_student_14 = (lunch * MIN_PRICE_14) * student_true 
lunch_price_min_student_15 = (lunch * MIN_PRICE_15) * student_true 
lunch_price_min_student_16 = (lunch * MIN_PRICE_16) * student_true 
lunch_price_min_student_17 = (lunch * MIN_PRICE_17) * student_true 
lunch_price_min_student_18 = (lunch * MIN_PRICE_18) * student_true 
lunch_price_min_student_19 = (lunch * MIN_PRICE_19) * student_true 
lunch_price_min_student_20 = (lunch * MIN_PRICE_20) * student_true 
lunch_price_min_student_21 = (lunch * MIN_PRICE_21) * student_true 
lunch_price_min_employee_1 = (lunch * MIN_PRICE_1) * perso 
lunch_price_min_employee_2 = (lunch * MIN_PRICE_2) * perso 
lunch_price_min_employee_3 = (lunch * MIN_PRICE_3) * perso 
lunch_price_min_employee_4 = (lunch * MIN_PRICE_4) * perso 
lunch_price_min_employee_5 = (lunch * MIN_PRICE_5) * perso 
lunch_price_min_employee_6 = (lunch * MIN_PRICE_6) * perso 
lunch_price_min_employee_7 = (lunch * MIN_PRICE_7) * perso 
lunch_price_min_employee_8 = (lunch * MIN_PRICE_8) * perso 
lunch_price_min_employee_9 = (lunch * MIN_PRICE_9) * perso 
lunch_price_min_employee_10 = (lunch * MIN_PRICE_10) * perso 
lunch_price_min_employee_11 = (lunch * MIN_PRICE_11) * perso 
lunch_price_min_employee_12 = (lunch * MIN_PRICE_12) * perso 
lunch_price_min_employee_13 = (lunch * MIN_PRICE_13) * perso 
lunch_price_min_employee_14 = (lunch * MIN_PRICE_14) * perso 
lunch_price_min_employee_15 = (lunch * MIN_PRICE_15) * perso 
lunch_price_min_employee_16 = (lunch * MIN_PRICE_16) * perso 
lunch_price_min_employee_17 = (lunch * MIN_PRICE_17) * perso 
lunch_price_min_employee_18 = (lunch * MIN_PRICE_18) * perso 
lunch_price_min_employee_19 = (lunch * MIN_PRICE_19) * perso 
lunch_price_min_employee_20 = (lunch * MIN_PRICE_20) * perso 
lunch_price_min_employee_21 = (lunch * MIN_PRICE_21) * perso 
previous_choice_morning_filter_1 = PREVIOUS_CHOICE_MORNING_TRUE_1 > -1 
previous_choice_morning_filter_2 = PREVIOUS_CHOICE_MORNING_TRUE_2 > -1 
previous_choice_morning_filter_3 = PREVIOUS_CHOICE_MORNING_TRUE_3 > -1 
previous_choice_morning_filter_4 = PREVIOUS_CHOICE_MORNING_TRUE_4 > -1 
previous_choice_morning_filter_5 = PREVIOUS_CHOICE_MORNING_TRUE_5 > -1 
previous_choice_morning_filter_6 = PREVIOUS_CHOICE_MORNING_TRUE_6 > -1 
previous_choice_morning_filter_7 = PREVIOUS_CHOICE_MORNING_TRUE_7 > -1 
previous_choice_morning_filter_8 = PREVIOUS_CHOICE_MORNING_TRUE_8 > -1 
previous_choice_morning_filter_9 = PREVIOUS_CHOICE_MORNING_TRUE_9 > -1 
previous_choice_morning_filter_10 = PREVIOUS_CHOICE_MORNING_TRUE_10 > -1 
previous_choice_morning_filter_11 = PREVIOUS_CHOICE_MORNING_TRUE_11 > -1 
previous_choice_morning_filter_12 = PREVIOUS_CHOICE_MORNING_TRUE_12 > -1 
previous_choice_morning_filter_13 = PREVIOUS_CHOICE_MORNING_TRUE_13 > -1 
previous_choice_morning_filter_14 = PREVIOUS_CHOICE_MORNING_TRUE_14 > -1 
previous_choice_morning_filter_15 = PREVIOUS_CHOICE_MORNING_TRUE_15 > -1 
previous_choice_morning_filter_16 = PREVIOUS_CHOICE_MORNING_TRUE_16 > -1 
previous_choice_morning_filter_17 = PREVIOUS_CHOICE_MORNING_TRUE_17 > -1 
previous_choice_morning_filter_18 = PREVIOUS_CHOICE_MORNING_TRUE_18 > -1 
previous_choice_morning_filter_19 = PREVIOUS_CHOICE_MORNING_TRUE_19 > -1 
previous_choice_morning_filter_20 = PREVIOUS_CHOICE_MORNING_TRUE_20 > -1 
previous_choice_morning_filter_21 = PREVIOUS_CHOICE_MORNING_TRUE_21 > -1 
no_previous_choice_morning_filter_1 = PREVIOUS_CHOICE_MORNING_TRUE_1 == -1 
no_previous_choice_morning_filter_2 = PREVIOUS_CHOICE_MORNING_TRUE_2 == -1 
no_previous_choice_morning_filter_3 = PREVIOUS_CHOICE_MORNING_TRUE_3 == -1 
no_previous_choice_morning_filter_4 = PREVIOUS_CHOICE_MORNING_TRUE_4 == -1 
no_previous_choice_morning_filter_5 = PREVIOUS_CHOICE_MORNING_TRUE_5 == -1 
no_previous_choice_morning_filter_6 = PREVIOUS_CHOICE_MORNING_TRUE_6 == -1 
no_previous_choice_morning_filter_7 = PREVIOUS_CHOICE_MORNING_TRUE_7 == -1 
no_previous_choice_morning_filter_8 = PREVIOUS_CHOICE_MORNING_TRUE_8 == -1 
no_previous_choice_morning_filter_9 = PREVIOUS_CHOICE_MORNING_TRUE_9 == -1 
no_previous_choice_morning_filter_10 = PREVIOUS_CHOICE_MORNING_TRUE_10 == -1 
no_previous_choice_morning_filter_11 = PREVIOUS_CHOICE_MORNING_TRUE_11 == -1 
no_previous_choice_morning_filter_12 = PREVIOUS_CHOICE_MORNING_TRUE_12 == -1 
no_previous_choice_morning_filter_13 = PREVIOUS_CHOICE_MORNING_TRUE_13 == -1 
no_previous_choice_morning_filter_14 = PREVIOUS_CHOICE_MORNING_TRUE_14 == -1 
no_previous_choice_morning_filter_15 = PREVIOUS_CHOICE_MORNING_TRUE_15 == -1 
no_previous_choice_morning_filter_16 = PREVIOUS_CHOICE_MORNING_TRUE_16 == -1 
no_previous_choice_morning_filter_17 = PREVIOUS_CHOICE_MORNING_TRUE_17 == -1 
no_previous_choice_morning_filter_18 = PREVIOUS_CHOICE_MORNING_TRUE_18 == -1 
no_previous_choice_morning_filter_19 = PREVIOUS_CHOICE_MORNING_TRUE_19 == -1 
no_previous_choice_morning_filter_20 = PREVIOUS_CHOICE_MORNING_TRUE_20 == -1 
no_previous_choice_morning_filter_21 = PREVIOUS_CHOICE_MORNING_TRUE_21 == -1 
previous_choice_morning_1 = (previous_choice_morning_filter_1 * PREVIOUS_CHOICE_MORNING_TRUE_1) + (no_previous_choice_morning_filter_1 * 0)
previous_choice_morning_2 = (previous_choice_morning_filter_2 * PREVIOUS_CHOICE_MORNING_TRUE_2) + (no_previous_choice_morning_filter_2 * 0)
previous_choice_morning_3 = (previous_choice_morning_filter_3 * PREVIOUS_CHOICE_MORNING_TRUE_3) + (no_previous_choice_morning_filter_3 * 0)
previous_choice_morning_4 = (previous_choice_morning_filter_4 * PREVIOUS_CHOICE_MORNING_TRUE_4) + (no_previous_choice_morning_filter_4 * 0)
previous_choice_morning_5 = (previous_choice_morning_filter_5 * PREVIOUS_CHOICE_MORNING_TRUE_5) + (no_previous_choice_morning_filter_5 * 0)
previous_choice_morning_6 = (previous_choice_morning_filter_6 * PREVIOUS_CHOICE_MORNING_TRUE_6) + (no_previous_choice_morning_filter_6 * 0)
previous_choice_morning_7 = (previous_choice_morning_filter_7 * PREVIOUS_CHOICE_MORNING_TRUE_7) + (no_previous_choice_morning_filter_7 * 0)
previous_choice_morning_8 = (previous_choice_morning_filter_8 * PREVIOUS_CHOICE_MORNING_TRUE_8) + (no_previous_choice_morning_filter_8 * 0)
previous_choice_morning_9 = (previous_choice_morning_filter_9 * PREVIOUS_CHOICE_MORNING_TRUE_9) + (no_previous_choice_morning_filter_9 * 0)
previous_choice_morning_10 = (previous_choice_morning_filter_10 * PREVIOUS_CHOICE_MORNING_TRUE_10) + (no_previous_choice_morning_filter_10 * 0)
previous_choice_morning_11 = (previous_choice_morning_filter_11 * PREVIOUS_CHOICE_MORNING_TRUE_11) + (no_previous_choice_morning_filter_11 * 0)
previous_choice_morning_12 = (previous_choice_morning_filter_12 * PREVIOUS_CHOICE_MORNING_TRUE_12) + (no_previous_choice_morning_filter_12 * 0)
previous_choice_morning_13 = (previous_choice_morning_filter_13 * PREVIOUS_CHOICE_MORNING_TRUE_13) + (no_previous_choice_morning_filter_13 * 0)
previous_choice_morning_14 = (previous_choice_morning_filter_14 * PREVIOUS_CHOICE_MORNING_TRUE_14) + (no_previous_choice_morning_filter_14 * 0)
previous_choice_morning_15 = (previous_choice_morning_filter_15 * PREVIOUS_CHOICE_MORNING_TRUE_15) + (no_previous_choice_morning_filter_15 * 0)
previous_choice_morning_16 = (previous_choice_morning_filter_16 * PREVIOUS_CHOICE_MORNING_TRUE_16) + (no_previous_choice_morning_filter_16 * 0)
previous_choice_morning_17 = (previous_choice_morning_filter_17 * PREVIOUS_CHOICE_MORNING_TRUE_17) + (no_previous_choice_morning_filter_17 * 0)
previous_choice_morning_18 = (previous_choice_morning_filter_18 * PREVIOUS_CHOICE_MORNING_TRUE_18) + (no_previous_choice_morning_filter_18 * 0)
previous_choice_morning_19 = (previous_choice_morning_filter_19 * PREVIOUS_CHOICE_MORNING_TRUE_19) + (no_previous_choice_morning_filter_19 * 0)
previous_choice_morning_20 = (previous_choice_morning_filter_20 * PREVIOUS_CHOICE_MORNING_TRUE_20) + (no_previous_choice_morning_filter_20 * 0)
previous_choice_morning_21 = (previous_choice_morning_filter_21 * PREVIOUS_CHOICE_MORNING_TRUE_21) + (no_previous_choice_morning_filter_21 * 0)
previous_choice_afternoon_filter_1 = PREVIOUS_CHOICE_AFTERNOON_TRUE_1 > -1 
previous_choice_afternoon_filter_2 = PREVIOUS_CHOICE_AFTERNOON_TRUE_2 > -1 
previous_choice_afternoon_filter_3 = PREVIOUS_CHOICE_AFTERNOON_TRUE_3 > -1 
previous_choice_afternoon_filter_4 = PREVIOUS_CHOICE_AFTERNOON_TRUE_4 > -1 
previous_choice_afternoon_filter_5 = PREVIOUS_CHOICE_AFTERNOON_TRUE_5 > -1 
previous_choice_afternoon_filter_6 = PREVIOUS_CHOICE_AFTERNOON_TRUE_6 > -1 
previous_choice_afternoon_filter_7 = PREVIOUS_CHOICE_AFTERNOON_TRUE_7 > -1 
previous_choice_afternoon_filter_8 = PREVIOUS_CHOICE_AFTERNOON_TRUE_8 > -1 
previous_choice_afternoon_filter_9 = PREVIOUS_CHOICE_AFTERNOON_TRUE_9 > -1 
previous_choice_afternoon_filter_10 = PREVIOUS_CHOICE_AFTERNOON_TRUE_10 > -1 
previous_choice_afternoon_filter_11 = PREVIOUS_CHOICE_AFTERNOON_TRUE_11 > -1 
previous_choice_afternoon_filter_12 = PREVIOUS_CHOICE_AFTERNOON_TRUE_12 > -1 
previous_choice_afternoon_filter_13 = PREVIOUS_CHOICE_AFTERNOON_TRUE_13 > -1 
previous_choice_afternoon_filter_14 = PREVIOUS_CHOICE_AFTERNOON_TRUE_14 > -1 
previous_choice_afternoon_filter_15 = PREVIOUS_CHOICE_AFTERNOON_TRUE_15 > -1 
previous_choice_afternoon_filter_16 = PREVIOUS_CHOICE_AFTERNOON_TRUE_16 > -1 
previous_choice_afternoon_filter_17 = PREVIOUS_CHOICE_AFTERNOON_TRUE_17 > -1 
previous_choice_afternoon_filter_18 = PREVIOUS_CHOICE_AFTERNOON_TRUE_18 > -1 
previous_choice_afternoon_filter_19 = PREVIOUS_CHOICE_AFTERNOON_TRUE_19 > -1 
previous_choice_afternoon_filter_20 = PREVIOUS_CHOICE_AFTERNOON_TRUE_20 > -1 
previous_choice_afternoon_filter_21 = PREVIOUS_CHOICE_AFTERNOON_TRUE_21 > -1 
no_previous_choice_afternoon_filter_1 = PREVIOUS_CHOICE_AFTERNOON_TRUE_1 == -1 
no_previous_choice_afternoon_filter_2 = PREVIOUS_CHOICE_AFTERNOON_TRUE_2 == -1 
no_previous_choice_afternoon_filter_3 = PREVIOUS_CHOICE_AFTERNOON_TRUE_3 == -1 
no_previous_choice_afternoon_filter_4 = PREVIOUS_CHOICE_AFTERNOON_TRUE_4 == -1 
no_previous_choice_afternoon_filter_5 = PREVIOUS_CHOICE_AFTERNOON_TRUE_5 == -1 
no_previous_choice_afternoon_filter_6 = PREVIOUS_CHOICE_AFTERNOON_TRUE_6 == -1 
no_previous_choice_afternoon_filter_7 = PREVIOUS_CHOICE_AFTERNOON_TRUE_7 == -1 
no_previous_choice_afternoon_filter_8 = PREVIOUS_CHOICE_AFTERNOON_TRUE_8 == -1 
no_previous_choice_afternoon_filter_9 = PREVIOUS_CHOICE_AFTERNOON_TRUE_9 == -1 
no_previous_choice_afternoon_filter_10 = PREVIOUS_CHOICE_AFTERNOON_TRUE_10 == -1 
no_previous_choice_afternoon_filter_11 = PREVIOUS_CHOICE_AFTERNOON_TRUE_11 == -1 
no_previous_choice_afternoon_filter_12 = PREVIOUS_CHOICE_AFTERNOON_TRUE_12 == -1 
no_previous_choice_afternoon_filter_13 = PREVIOUS_CHOICE_AFTERNOON_TRUE_13 == -1 
no_previous_choice_afternoon_filter_14 = PREVIOUS_CHOICE_AFTERNOON_TRUE_14 == -1 
no_previous_choice_afternoon_filter_15 = PREVIOUS_CHOICE_AFTERNOON_TRUE_15 == -1 
no_previous_choice_afternoon_filter_16 = PREVIOUS_CHOICE_AFTERNOON_TRUE_16 == -1 
no_previous_choice_afternoon_filter_17 = PREVIOUS_CHOICE_AFTERNOON_TRUE_17 == -1 
no_previous_choice_afternoon_filter_18 = PREVIOUS_CHOICE_AFTERNOON_TRUE_18 == -1 
no_previous_choice_afternoon_filter_19 = PREVIOUS_CHOICE_AFTERNOON_TRUE_19 == -1 
no_previous_choice_afternoon_filter_20 = PREVIOUS_CHOICE_AFTERNOON_TRUE_20 == -1 
no_previous_choice_afternoon_filter_21 = PREVIOUS_CHOICE_AFTERNOON_TRUE_21 == -1 
previous_choice_afternoon_1 = (previous_choice_afternoon_filter_1 * PREVIOUS_CHOICE_AFTERNOON_TRUE_1) + (no_previous_choice_afternoon_filter_1 * 0)
previous_choice_afternoon_2 = (previous_choice_afternoon_filter_2 * PREVIOUS_CHOICE_AFTERNOON_TRUE_2) + (no_previous_choice_afternoon_filter_2 * 0)
previous_choice_afternoon_3 = (previous_choice_afternoon_filter_3 * PREVIOUS_CHOICE_AFTERNOON_TRUE_3) + (no_previous_choice_afternoon_filter_3 * 0)
previous_choice_afternoon_4 = (previous_choice_afternoon_filter_4 * PREVIOUS_CHOICE_AFTERNOON_TRUE_4) + (no_previous_choice_afternoon_filter_4 * 0)
previous_choice_afternoon_5 = (previous_choice_afternoon_filter_5 * PREVIOUS_CHOICE_AFTERNOON_TRUE_5) + (no_previous_choice_afternoon_filter_5 * 0)
previous_choice_afternoon_6 = (previous_choice_afternoon_filter_6 * PREVIOUS_CHOICE_AFTERNOON_TRUE_6) + (no_previous_choice_afternoon_filter_6 * 0)
previous_choice_afternoon_7 = (previous_choice_afternoon_filter_7 * PREVIOUS_CHOICE_AFTERNOON_TRUE_7) + (no_previous_choice_afternoon_filter_7 * 0)
previous_choice_afternoon_8 = (previous_choice_afternoon_filter_8 * PREVIOUS_CHOICE_AFTERNOON_TRUE_8) + (no_previous_choice_afternoon_filter_8 * 0)
previous_choice_afternoon_9 = (previous_choice_afternoon_filter_9 * PREVIOUS_CHOICE_AFTERNOON_TRUE_9) + (no_previous_choice_afternoon_filter_9 * 0)
previous_choice_afternoon_10 = (previous_choice_afternoon_filter_10 * PREVIOUS_CHOICE_AFTERNOON_TRUE_10) + (no_previous_choice_afternoon_filter_10 * 0)
previous_choice_afternoon_11 = (previous_choice_afternoon_filter_11 * PREVIOUS_CHOICE_AFTERNOON_TRUE_11) + (no_previous_choice_afternoon_filter_11 * 0)
previous_choice_afternoon_12 = (previous_choice_afternoon_filter_12 * PREVIOUS_CHOICE_AFTERNOON_TRUE_12) + (no_previous_choice_afternoon_filter_12 * 0)
previous_choice_afternoon_13 = (previous_choice_afternoon_filter_13 * PREVIOUS_CHOICE_AFTERNOON_TRUE_13) + (no_previous_choice_afternoon_filter_13 * 0)
previous_choice_afternoon_14 = (previous_choice_afternoon_filter_14 * PREVIOUS_CHOICE_AFTERNOON_TRUE_14) + (no_previous_choice_afternoon_filter_14 * 0)
previous_choice_afternoon_15 = (previous_choice_afternoon_filter_15 * PREVIOUS_CHOICE_AFTERNOON_TRUE_15) + (no_previous_choice_afternoon_filter_15 * 0)
previous_choice_afternoon_16 = (previous_choice_afternoon_filter_16 * PREVIOUS_CHOICE_AFTERNOON_TRUE_16) + (no_previous_choice_afternoon_filter_16 * 0)
previous_choice_afternoon_17 = (previous_choice_afternoon_filter_17 * PREVIOUS_CHOICE_AFTERNOON_TRUE_17) + (no_previous_choice_afternoon_filter_17 * 0)
previous_choice_afternoon_18 = (previous_choice_afternoon_filter_18 * PREVIOUS_CHOICE_AFTERNOON_TRUE_18) + (no_previous_choice_afternoon_filter_18 * 0)
previous_choice_afternoon_19 = (previous_choice_afternoon_filter_19 * PREVIOUS_CHOICE_AFTERNOON_TRUE_19) + (no_previous_choice_afternoon_filter_19 * 0)
previous_choice_afternoon_20 = (previous_choice_afternoon_filter_20 * PREVIOUS_CHOICE_AFTERNOON_TRUE_20) + (no_previous_choice_afternoon_filter_20 * 0)
previous_choice_afternoon_21 = (previous_choice_afternoon_filter_21 * PREVIOUS_CHOICE_AFTERNOON_TRUE_21) + (no_previous_choice_afternoon_filter_21 * 0)

# Utility functions
V1 = ASC_KLE \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_1 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_1 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_1 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_1 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_1 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_1\
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_1 \
    + BETA_NO_DISTANCE_AV * distance_no_av_1 \
    + BETA_DINNER * dinner_av_1 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_1 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_1 \
    + BETA_METEO_TERRACE * meteo_terrace_av_1 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_1

V2 = ASC_BC \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_2 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_2 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_2 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_2 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_2 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_2 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_2 \
    + BETA_NO_DISTANCE_AV * distance_no_av_2 \
    + BETA_DINNER * dinner_av_2 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_2 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_2 \
    + BETA_METEO_TERRACE * meteo_terrace_av_2 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_2
    
V3 = ASC_BM \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_3 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_3 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_3 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_3 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_3 \
    + BETA_NO_DISTANCE_AV * distance_no_av_3 \
    + BETA_DINNER * dinner_av_3 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_3 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_3 \
    + BETA_METEO_TERRACE * meteo_terrace_av_3 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_3 + BETA_DISTANCE_LUNCH_OTHER * lunch_distance_3
    
V4 = ASC_ELA \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_4 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_4 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_4 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_4 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_4 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_4 \
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_4 \
    + BETA_NO_DISTANCE_AV * distance_no_av_4 \
    + BETA_DINNER * dinner_av_4 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_4 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_4 \
    + BETA_METEO_TERRACE * meteo_terrace_av_4 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_4

    
V5 = ASC_INM \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_5 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_5 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_5 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_5 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_5 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_5 \
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_5 \
    + BETA_NO_DISTANCE_AV * distance_no_av_5 \
    + BETA_DINNER * dinner_av_5 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_5 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_5 \
    + BETA_METEO_TERRACE * meteo_terrace_av_5 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_5
    
V6 = ASC_MX \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_6 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_6 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_6 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_6 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_6 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_6 \
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_6 \
    + BETA_NO_DISTANCE_AV * distance_no_av_6 \
    + BETA_DINNER * dinner_av_6 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_6 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_6 \
    + BETA_METEO_TERRACE * meteo_terrace_av_6 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_6
    
V7 = ASC_PH \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_7 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_7 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_7 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_7 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_7 \
    + BETA_NO_DISTANCE_AV * distance_no_av_7 \
    + BETA_DINNER * dinner_av_7 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_7 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_7 \
    + BETA_METEO_TERRACE * meteo_terrace_av_7 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_7 + BETA_DISTANCE_LUNCH_OTHER * lunch_distance_7
    
V8 = ASC_ARC \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_8 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_8 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_8 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_8 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_8 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_8 \
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_8 \
    + BETA_NO_DISTANCE_AV * distance_no_av_8 \
    + BETA_DINNER * dinner_av_8 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_8 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_8 \
    + BETA_METEO_TERRACE * meteo_terrace_av_8 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_8
    
V9 = ASC_ATL \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_9 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_9 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_9 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_9 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_9 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_9 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_9 \
    + BETA_NO_DISTANCE_AV * distance_no_av_9 \
    + BETA_DINNER * dinner_av_9 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_9 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_9 \
    + BETA_METEO_TERRACE * meteo_terrace_av_9 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_9
    
V10 = ASC_COP \
    + BETA_DISTANCE_LUNCH_REST * lunch_distance_10 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_10 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_10 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_10 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_10 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_10 \
    + BETA_NO_DISTANCE_AV * distance_no_av_10 \
    + BETA_DINNER * dinner_av_10 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_10 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_10 \
    + BETA_METEO_TERRACE * meteo_terrace_av_10 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_10
    
V11 = ASC_COR \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_11 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_11 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_11 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_11 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_11 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_11 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_11 \
    + BETA_NO_DISTANCE_AV * distance_no_av_11 \
    + BETA_DINNER * dinner_av_11 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_11 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_11 \
    + BETA_METEO_TERRACE * meteo_terrace_av_11 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_11
    
V12 = ASC_GIA \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_12 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_12 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_12 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_12 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_12 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_12 \
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_12 \
    + BETA_NO_DISTANCE_AV * distance_no_av_12 \
    + BETA_DINNER * dinner_av_12 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_12 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_12 \
    + BETA_METEO_TERRACE * meteo_terrace_av_12 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_12
    
V13 = ASC_PAR \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_13 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_13 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_13 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_13 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_13 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_13 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_13 \
    + BETA_NO_DISTANCE_AV * distance_no_av_13 \
    + BETA_DINNER * dinner_av_13 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_13 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_13 \
    + BETA_METEO_TERRACE * meteo_terrace_av_13 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_13
    
V14 = ASC_VIN \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_14 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_14 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_14 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_14 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_14 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_14 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_14 \
    + BETA_NO_DISTANCE_AV * distance_no_av_14 \
    + BETA_DINNER * dinner_av_14 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_14 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_14 \
    + BETA_METEO_TERRACE * meteo_terrace_av_14 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_14
    
V15 = ASC_ESP \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_15 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_15 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_15 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_15 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_15 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_15 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_15 \
    + BETA_NO_DISTANCE_AV * distance_no_av_15 \
    + BETA_DINNER * dinner_av_15 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_15 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_15 \
    + BETA_METEO_TERRACE * meteo_terrace_av_15 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_15
    
V16 = ASC_ORN \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_16 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_16 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_16 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_16 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_16 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_16 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_16 \
    + BETA_NO_DISTANCE_AV * distance_no_av_16 \
    + BETA_DINNER * dinner_av_16 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_16 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_16 \
    + BETA_METEO_TERRACE * meteo_terrace_av_16 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_16
    
V17 = ASC_PIZ \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_17 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_17 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_17 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_17 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_17 \
    + BETA_NO_DISTANCE_AV * distance_no_av_17 \
    + BETA_DINNER * dinner_av_17 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_17 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_17 \
    + BETA_EVALUATION_FAST_FOOD * evaluation_2013_self_cafet_17 \
    + BETA_METEO_TERRACE * meteo_terrace_av_17 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_17 + BETA_DISTANCE_LUNCH_FASTFOOD * lunch_distance_17
    
V18 = ASC_KEB \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_18 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_18 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_18 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_18 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_18 \
    + BETA_NO_DISTANCE_AV * distance_no_av_18 \
    + BETA_DINNER * dinner_av_18 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_18 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_18 \
    + BETA_EVALUATION_FAST_FOOD * evaluation_2013_self_cafet_18 \
    + BETA_METEO_TERRACE * meteo_terrace_av_18 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_18 + BETA_DISTANCE_LUNCH_FASTFOOD * lunch_distance_18
    
V19 = ASC_SAT \
    + BETA_DISTANCE_LUNCH_CAF * lunch_distance_19 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_19 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_19 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_19 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_19 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_19 \
    + BETA_EVALUATION_CAFET * evaluation_2013_self_cafet_19 \
    + BETA_NO_DISTANCE_AV * distance_no_av_19 \
    + BETA_DINNER * dinner_av_19 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_19 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_19 \
    + BETA_METEO_TERRACE * meteo_terrace_av_19 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_19
    
V20 = ASC_HOD \
    + BETA_DISTANCE_LUNCH_SELF * lunch_distance_20 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_20 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_20 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_20 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_20 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_20 \
    + BETA_EVALUATION_SELF * evaluation_2013_self_cafet_20 \
    + BETA_NO_DISTANCE_AV * distance_no_av_20 \
    + BETA_DINNER * dinner_av_20 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_20 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_20 \
    + BETA_METEO_TERRACE * meteo_terrace_av_20 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_20
    
V21 = ASC_VAL \
    + BETA_DISTANCE_LUNCH_REST * lunch_distance_21 \
    + BETA_DISTANCE_MORNING * morning_coffee_distance_21 \
    + RHO_PREVIOUS_LUNCH_CHOICE * last_choice_true_21 \
    + RHO_PREVIOUS_MORNING_CHOICE * previous_choice_morning_21 \
    + BETA_TAP_BEER_AFTER_LUNCH * beer_in_the_afternoon_dinner_night_av_21 \
    + BETA_DISTANCE_AFTERNOON * afternoon_workspace_distance_21 \
    + BETA_NO_DISTANCE_AV * distance_no_av_21 \
    + BETA_DINNER * dinner_av_21 \
    + BETA_PRICE_STUDENT * lunch_price_min_student_21 \
    + BETA_PRICE_EMPLOYEE * lunch_price_min_employee_21 \
    + BETA_METEO_TERRACE * meteo_terrace_av_21 \
    + BETA_CAPACITY_INSIDE * cap_inside_av_21

# Associate utility functions with the numbering of alternatives
V = {1: V1,
     2: V2,
     3: V3,
     4: V4,
     5: V5,
     6: V6,
     7: V7,
     8: V8,
     9: V9,
     10: V10,
     11: V11,
     12: V12,
     13: V13,
     14: V14,
     15: V15,
     16: V16,
     17: V17,
     18: V18,
     19: V19,
     20: V20,
     21: V21}

# Associate the availability conditions with the alternatives
# Catering locations are available when they are open
av = {1: OPEN_AV_1,
      2: OPEN_AV_2,
      3: OPEN_AV_3,
      4: OPEN_AV_4,
      5: OPEN_AV_5,
      6: OPEN_AV_6,
      7: OPEN_AV_7,
      8: OPEN_AV_8,
      9: OPEN_AV_9,
      10: OPEN_AV_10,
      11: OPEN_AV_11,
      12: OPEN_AV_12,
      13: OPEN_AV_13,
      14: OPEN_AV_14,
      15: OPEN_AV_15,
      16: OPEN_AV_16,
      17: OPEN_AV_17,
      18: OPEN_AV_18,
      19: OPEN_AV_19,
      20: OPEN_AV_20,
      21: OPEN_AV_21}

# The choice model is a logit, with availability conditions
prob = bioLogit(V, av, CHOICE)

# Defines an iterator on the data
rowIterator('obsIter') 

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(log(prob), 'obsIter')

# All observations verifying the following expression will not be
# considered for estimation
# Activity episodes shorter than 5 minutes are excluded
exclude = DURATION < 5

BIOGEME_OBJECT.EXCLUDE = exclude

# Statistics
nullLoglikelihood(av, 'obsIter')
choiceSet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
cteLoglikelihood(choiceSet, CHOICE, 'obsIter')
availabilityStatistics(av, 'obsIter')


BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "CFSQP"
BIOGEME_OBJECT.PARAMETERS['checkDerivatives'] = "0"
BIOGEME_OBJECT.PARAMETERS['numberOfThreads'] = "1"
