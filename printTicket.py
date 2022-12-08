import textwrap
surname=input("Please enter the surname of the passenger: ")
othername=input("Please enter the other name of the passenger: ")
title=input("Please enter the title of the passenger: ")
fullname=surname.upper()+"/"+othername.upper()+" "+title.upper()
filename=((title+" "+surname+" "+othername).upper())+".doc"
filehandle=open(filename,"w")
from datetime import date
today=date.today()
d3=today.strftime("%d %B %Y")
loop=int(input("Please enter the number of flights during the itinerary: "))
airline=input("Please enter the issuing airline: ")
TICKET=input("Please enter the ticket number: ")
booking_ref=input("Please enter the booking reference: ")
while len(booking_ref)!=6:
    print("incorrect entry. Booking Reference need to be 6 characters long")
    booking_ref=input("Please re-enter the correct booking reference: ")
filehandle.write(fullname.center(73))
filehandle.write("\n")
filehandle.write("-"*73)
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("ELECTRONIC TICKET".center(73))
filehandle.write("\n")
filehandle.write("PASSENGER ITINERARY RECEIPT".center(73))
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("{0:<36s}{1:>6s}{2:<31s}".format("","DATE: ",d3.upper()))
filehandle.write("\n")
filehandle.write("{0:<36s}{1:>6s}{2:<31s}".format("","NAME: ",fullname))
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("{0:<40s}{1:<2s}{2:<31s}".format("ISSUING AIRLINE",": ",airline.upper()))
filehandle.write("\n")
filehandle.write("{0:<40s}{1:<2s}{2:<31s}".format("TICKET NUMBER",": ",TICKET))
filehandle.write("\n")
filehandle.write("{0:<40s}{1:<2s}{2:<31s}".format("BOOKING REF",": ",booking_ref.upper()))
filehandle.write("\n")
filehandle.write("\n")
filehandle.write("{0:<15s}{1:<8s}{2:<3s}{3:<7s}{4:<6s}{5:<15s}{6:<6s}{7:<6s}{8:<5s}{9:<2s}".format("FROM /TO","FLIGHT","CL","DATE","DEP","FARE BASIS","NVB","NVA","BAG","ST"))
filehandle.write("\n")
filehandle.write("\n")
for c in range (loop):
    word_origin=[]
    word_destination=[]
    flight_no=input("Please enter the flight number "+str(c+1)+": ")
    origin=input("Please enter the origin: ")
    destination=input("Please enter the destination: ")
    CL=input("Please enter the booking class: ")
    while len(CL)!=1:
        print("incorrect entry. Booking Class need to be 1 character length:")
        CL=input("Please re-enter the correct booking class")
    departure_date=input("Please enter the departure date, e.g:03OCT: ")
    arrival_date=input("Please enter the arrival date, e.g:03OCT: ")
    departure_time=input("Please enter the departure time: ")
    while len(departure_time)!=4:
        print("incorrect entry")
        departure_time=input("Please re-enter the correct departure time: ")
    arrival_time=input("Please enter the arrival time: ")
    while len(arrival_time)!=4:
        print("incorrect entry")
        arrival_time=input("Please re-enter the correct arrival time")
    farebasis=input("Please enter the fare basis: ")
    NVB=input("Please enter the not valid before date (NVB), e.g:03OCT,if unknown please leave the field blank: ")
    NVA=input("Please enter the not valid after date (NVA), e.g:03OCT,if unknown please leave the field blank: ")
    baggage_allowance=input("Please enter the baggage allowance: ")
    seat=input("Please enter whether the seat is confirmed OK/NO: ")
    while seat!="ok"and seat!="OK"and seat!="no"and seat!="NO":
        print("incorrect entry")
        seat=input("Please re-enter whether the seat is confirmed OK/NO: ")
    seat_no=input("Please enter the seat number,if unknown please leave the field blank: ")
    if seat_no!="":
        s_no=("SEAT: "+seat_no).upper()
    else:
        s_no=""
    wrapper = textwrap.TextWrapper(width=14)
    word_list = wrapper.wrap(text=origin.upper()) 
    wrapper1 = textwrap.TextWrapper(width=14)
    word_list1 = wrapper1.wrap(text=destination.upper())
    for temp in word_list:
        word_origin.append(temp)
    for temp1 in word_list1:
        word_destination.append(temp1)
    filehandle.write("{0:<15s}{1:<8s}{2:<3s}{3:<7s}{4:<6s}{5:<15s}{6:<6s}{7:<6s}{8:<5s}{9:<2s}".format(word_origin[0],flight_no.upper(),CL.upper(),departure_date.upper(),departure_time,farebasis.upper(),NVB.upper(),NVA.upper(),baggage_allowance.upper(),seat.upper()))
    for count in range (1,len(word_origin)):
        filehandle.write("\n")
        filehandle.write("{0:<15s}".format(word_origin[count]))
    filehandle.write("\n")
    filehandle.write("{0:<15s}{1:<3s}{2:<9s}{3:<5s}{4:<21s}{5:<20s}".format(word_destination[0],"",s_no,"","ARRIVAL TIME: "+arrival_time,"ARRIVAL DATE: "+arrival_date.upper()))
    for count in range (1,len(word_destination)):
        filehandle.write("\n")
        filehandle.write("{0:<15s}".format(word_destination[count]))
    filehandle.write("\n")
    filehandle.write("\n")
filehandle.close()

