
year = 2018
leap = False
if year%400 == 0:
    leap = True
if year%400!=0 and year%100!=0 and year%4 == 0 :
    leap = True

print(str(year) + " -> " + str(leap))