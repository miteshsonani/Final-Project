def time_calculator(begin, duration, start_day=None):
   # Parsing input
  start_time, period = begin.split()
  start_hr, start_min = start_time.split(":")
  duration_hr, duration_min = duration.split(":")
  # Convert start time to total minutes
  total_min = int(start_hr) * 60 + int(start_min)
  total_duration_min = int(duration_hr) * 60 + int(duration_min)
  if period == "PM":
    total_min += 12 * 60

  # Add the duration in minutes
  total_min += total_duration_min
  # Calculate days later
  days_later_num = int(total_min) // (24 * 60)
  days_later = ""
  if days_later_num >= 2:
    days_later = "(" + str(days_later_num) + " " + "days later)"
  elif days_later_num == 1:
    days_later = "(next day)"
  else:
    pass
  # Calculate the time of the day
  total_min %= (24 * 60)
  #period
  new_period = ""
  if total_min >= 720:
    new_period = "PM"
  else:
    new_period = "AM"
  #new time
  derived_min = int(total_min) % 60
  derived_hr = int(total_min) // 60
  derived_hr %= 12

  # Format time
  if derived_hr == 0: # Convert 0 hour to 12 in 12-hour format
    derived_hr = 12
    derived_time = derived_time = str(derived_hr) + ":" + str(derived_min).zfill(2)
  else:
    derived_time = str(derived_hr).zfill(2) + ":" + str(derived_min).zfill(2)
  ## Calculate the day of the week if provided
  day_lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
  derived_day = ""
  #returns = derived_time + " " + new_period + " " + derived_day + " " + days_later
  if start_day is not None:
    if start_day in day_lst:
      start_day_index = day_lst.index(start_day)
      new_index = start_day_index + days_later_num
      if new_index > 6:
        derived_index = (new_index) % 7
        derived_day = day_lst[derived_index]
      else:
        derived_index = new_index
        derived_day = day_lst[derived_index]
    returns = derived_time + " " + new_period + " " + derived_day + " " + days_later
    print(returns)
  else:
    returns = derived_time + " " + new_period + " " + days_later
    print(returns)


#examples
time_calculator("3:00 PM", "3:10")
time_calculator("11:30 AM", "2:32", "Monday")
time_calculator("11:43 AM", "00:20")
time_calculator("10:10 PM", "3:30")
time_calculator("11:43 PM", "24:20", "tueSday")
time_calculator("6:30 PM", "205:12")
