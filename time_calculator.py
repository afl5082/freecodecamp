

def add_time(start, duration,day=None):
  time_added = start

  duration_list = duration.split(":")
  duration_hour = int(duration_list[0])
  duration_minute = int(duration_list[1])

  start_list = start.split(":")
  start_hour = int(start_list[0])

  start_list_minute = start_list[1].split(" ")
  start_minute = int(start_list_minute[0])
  ampm = start_list_minute[1]

  add_day = False
  if start_minute + duration_minute >= 60:
    output_minute = (start_minute + duration_minute) - 60
    add_day = True
  else:
    output_minute = start_minute + duration_minute

  if ampm == "PM":
    start_hour+=12
  
  if add_day == True:
    duration_hour+=1

  
  midnight = False


 
  if start_hour + duration_hour > 24:
    
    days_passed =  int((start_hour + duration_hour) / 24)
    
    output_hour =  (24 * days_passed) - (start_hour + duration_hour) 
    #print(output_hour)
    if output_hour == 0 or output_hour == -12:
      midnight = True
      print(output_hour)
      output_hour = 12
    else:
      pass
  else:
    days_passed =0
    output_hour = start_hour + duration_hour
  



  if output_hour >= 12 and midnight == False:
    ampm_str = " PM"
    #converting out from military time
    if output_hour == 12:
      pass
    else:
      output_hour = output_hour - 12


  else: 
    ampm_str = " AM"



  if output_hour <10:
    output_hour = str(abs(output_hour))
  

  if output_minute <10:
    output_minute = "0" +str(output_minute)





  day_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  
  string_for_day =""
  days_passedforday = days_passed

  if day:
    for index,days in enumerate(day_list):
      if days.lower() == day.lower():
        starting_day = index
  else:
    starting_day=0

  
  if days_passed >0:
    index_remaining_current_week = 6 - starting_day
    
    if days_passed > index_remaining_current_week:
      days_passedforday = days_passed - index_remaining_current_week

      if days_passed < 7:
        day_for_print = day_list[days_passedforday -1]
      else:
        print(days_passedforday)
        day_for_print = day_list[ (days_passedforday-1) % 7]
    
    else:
      day_for_print = day_list[days_passed + starting_day]
      #day_for_print = day_list[index_remaining_current_week]
  else:
    day_for_print = day_list[starting_day]

      
  
  if days_passed ==1:
    string_for_day = " (next day)"
  elif days_passed ==0:
    string_for_day=""
  else:
    string_for_day = " (" + str(days_passed) +" days later)"
  
  if day:
    return (str(output_hour) + ":" + str(output_minute) +ampm_str  + ", " + day_for_print + string_for_day)
  else:
    return (str(output_hour) + ":" + str(output_minute) +ampm_str  + string_for_day)

  
 






