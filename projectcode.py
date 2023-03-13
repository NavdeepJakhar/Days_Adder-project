import datetime as dt

# Set date functions
def today_date():
    inpdate=dt.date.today()
    return inpdate

def another_date():
    inpyear=int(input("Enter year : "))
    inpmonth=int(input("Enter month : "))
    inpday=int(input("Enter date : "))
    inpdate=dt.date(inpyear,inpmonth,inpday)
    return inpdate

# Operation functions
def add_day(idate,n):
    fdate=idate+dt.timedelta(days=n)
    return fdate

def sub_day(idate,n):
    fdate=idate-dt.timedelta(days=n)
    return fdate

# Print function
def sol_print(i_date,f_date,ndays,userch):
    print("__________________________________________________________________________")
    print("------------------------------------------------------------------------\n")
    from_date=i_date.strftime("%d/%m/%Y")
    sol_date=f_date.strftime("%d/%m/%Y")
    if userch==1: # future
        print(ndays,"days into the future from",from_date,'is :',sol_date)
    elif userch==2:
        print(ndays,"days into the past from",from_date,'is :',sol_date)



# Driver Code
print("************************************************************************")
print("------------------------------------------------------------------------\n")
print("\t\t\t~ DATE PROPHET ~\n")
print("------------------------------------------------------------------------")
print("( This program allows you to find the exact date after adding or subtracting\neither from today's date or a user-specified date.)")
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("\nWhich date which you would you like to choose the operations on?")
print("                 1. Today's date")
print("                 2. Another date")
ch=int(input("Your choice [1/2] : "))
print("")
if ch==1:
    inp_date=today_date()
elif ch==2:
    inp_date=another_date()
else:
    print("Invalid choice.")
    quit()

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

print("\nWould you like to look into the future or the past?")
print("                 1. Future")
print("                 2. Past")
ch1=int(input("Your choice [1/2] : "))
print("")
if(ch1<1 or ch1>2):
    print("Invalid choice.")
    quit()
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
ndayinp=int(input("Number of days : "))
if ch1==1:
    final_date=add_day(inp_date,ndayinp)
elif ch1==2:
    final_date=sub_day(inp_date,ndayinp)

sol_print(inp_date,final_date,ndayinp,ch1)

print("\n------------------------------------------------------------------------")
print("************************************************************************\n")