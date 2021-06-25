def add_time(start_time, duration_time, day_of_week = ""):
    days = 0
    hour = []
    minute = []
    ampm = ""


    # Split initial time into lists
    time_ampm = start_time.split()
    time = time_ampm[0].split(":")
  
    ampm = time_ampm[1] # AM or PM
    hour.append(time[0]) # hour count
    minute.append(time[1]) # minute count

    # Split duration time into lists
    time_ampm2 = duration_time.split()
    time2 = time_ampm2[0].split(":")

    hour.append(time2[0]) # hour count
    minute.append(time2[1]) # minute count

    # Calculate final time and days passed
    fhour = 0
    fmin = 0
    fmin = int(minute[0]) + int(minute[1])
    fhour = fhour + int(hour[0]) + int(hour[1])

    if fmin >= 60: # If fmin is over 60, add to hour
        fhour = fhour + 1
        fmin = fmin - 60
        if fhour == 12: # AM to PM and add days
            if ampm == "PM":
                days = days + 1
                ampm = "AM"
            elif ampm == "AM":
                ampm = "PM"
    fmin = str(fmin).zfill(2) # Add 0 in front if single digit
   
    # AM or PM
    while fhour > 12:
        fhour = fhour - 12
        if ampm == "PM": # AM to PM and add days
            days = days + 1
            ampm = "AM"
            continue
        elif ampm == "AM":
            ampm = "PM"
            continue
    #print(fhour)
    #print(int(hour[1]))
    #print(ampm)
    #print(days)
    if int(hour[1]) > 0:
        if fhour == 12:
            if ampm == "AM":
                days = days + 1
                print(days)
                ampm = "PM"
            elif ampm == "PM":
                ampm = "AM"
    
    # Define final time
    final_time = f'{fhour}:{fmin} {ampm}'
    #print(fhour,":", fmin," ", ampm, sep="")

    # day of the week
    count = 0
    week = False
    day = ["monday", "tuesday", "wednesday", "thursday", 
           "friday", "saturday", "sunday"]
    for i in day:
        if day_of_week.lower() == i:
            count = day.index(i)
            week = True

    while (count + days) > 6:
        count = count - 7

    # define day_counter
    if days >= 1:
        if days == 1:
            day_counter = " (next day)"
        else:
            day_counter = (f' ({days} days later)')
    else:
        day_counter = ""


    # Final return and print
    if week == True:
        final_print = f'{final_time}, {((day[count + days]).capitalize())}{day_counter}'
        print(final_print)
        return (final_print)
    else:
        final_print_noweek = f'{final_time}{day_counter}'
        print(final_print_noweek)
        return final_print_noweek


# test
add_time("11:59 PM", "24:05")
