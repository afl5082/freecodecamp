def arithmetic_arranger(problems,b=None):

  agg_string = ""
  first_line_string = ""
  second_line_string =""
  dashes =""
  calcs =""

  if len(problems) > 5:
    return "Error: Too many problems."

  for problem in problems:
    split_string = problem.split(" ")
    operator = split_string[1]
    first_num = split_string[0]
    second_num = split_string[2]

    try:
      first_num1  = int(first_num)
    except: 
      return "Error: Numbers must only contain digits."

    try:
      second_num1 = int(second_num)
    except:
      return "Error: Numbers must only contain digits."
      

    if operator == '+':
      calc = int(first_num) + int(second_num)
    elif operator == '-':
      calc = int(first_num) - int(second_num )
    else:
      return "Error: Operator must be '+' or '-'."

    


    first_numcount =0
    second_numcount = 0
    calc1 = int(calc)
    abs_calc1 = abs(calc1)
    calc_numcount =0



    while (first_num1 > 0):
      first_num1 = first_num1//10
      first_numcount = first_numcount + 1

    while (second_num1 >0):
      second_num1 = second_num1//10
      second_numcount = second_numcount + 1
    
    while (abs_calc1 >0):
      abs_calc1 = abs_calc1//10
      calc_numcount = calc_numcount + 1
    
    if calc < 0:
      calc_numcount = calc_numcount +1

    if first_numcount >= second_numcount:
      total_spaces = first_numcount +2
    else:
      total_spaces = second_numcount + 2
    
    if first_numcount > 4 or second_numcount >4:
      return "Error: Numbers cannot be more than four digits."

    top_space_count = total_spaces - first_numcount
    middle_space_count = (total_spaces - 1) - second_numcount
    bottom_space_count = total_spaces - calc_numcount

    top_spaces =""
    middle_spaces =""
    dash =""
    bottom_spaces = ""
    
    for x in range(top_space_count):
      top_spaces += " "
    for x in range(middle_space_count):
      middle_spaces +=" "
    for x in range(total_spaces):
      dash +="-"
    for x in range(bottom_space_count):
      bottom_spaces+=" "
    
    agg_string += (top_spaces + first_num + '\n' + operator +middle_spaces +second_num+'\n' + dash + '\n')

    if problem == problems[-1]:
      first_line_string += (top_spaces + first_num)
      second_line_string += (operator + middle_spaces + second_num)
      dashes += (dash)
      calcs += (bottom_spaces + str(calc) )
    else:
      first_line_string += (top_spaces + first_num + "    ")
      second_line_string += (operator + middle_spaces + second_num + "    ")
      dashes += (dash + "    ")
      calcs += (bottom_spaces + str(calc) + "    ")

  if b == True:
    return str((first_line_string + '\n' + second_line_string + '\n' + dashes + '\n' + calcs))
  else:
    return str((first_line_string + '\n' + second_line_string + '\n' + dashes))

  
   
