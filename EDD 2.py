"""
This promgram computes the Expected Date of Delivery (EDD) when a user 
enters the date of their Last Menstrual Period (LMP).
"""

from datetime import timedelta, date

try:
    #getting LMP from the user
    lmp = input("Enter the date of your last period in DD-MM-YYYY format: ")  
    lst = lmp.split("-")    #splitting the date to change to int numbers
        
    day, month, year = int(lst[0]), int(lst[1]), int(lst[2]) 
    
    lmp_date = date(year, month, day)  #converting the LMP to datetime object
    delta = timedelta(days = 280)
    edd_date = lmp_date + delta    #adding 280 days which is the duration of pregnancy
    print(f"Your expected date of delivery is {edd_date}.")
   
except:
    print("Error! Please enter a valid date in the specified format.")
    
   
   
#another method by addid 40 weeks to LMP
# delta5 = timedelta(weeks = 40)
# date5 = date1 + delta5
# print(date5)

#using naegl;e's rules are
# delta1 = timedelta(days = 7, weeks = -13)
# date2 = date + delta1       #adding 7 to days and subtracting 3 months i.e 13 weeks
# delta2 = timedelta(weeks = 52)
# date3 = date2 + delta2      #adding 1 year to the date i.e 52 weeks
# print(date3)



