
class Category:
  def __init__(self,category):
    self.ledger = []
    self.cat = category
  
  def __str__(self):
    
    cat_length = len(self.cat)
    ast_toprint = int((30 - cat_length) / 2)
    
    if ((30-cat_length) % 2 > 0):
      ast_toprint+= 1
  
    astericks =""
    for x in range(ast_toprint):
      astericks+="*"

    master_string = ""
    
    for x in self.ledger:
      item_string =""
      description_len = 0
      if len(x['description']) > 23:
        item_string+= x['description'][0:23]
        description_len = 23
      else:
        item_string+= x['description']
        description_len = len(x['description'])

      num_count = 0

      #if negative, add to numcount 
      if x['amount'] < 0:
        #THIS IS NOT WORKING
        num_count+= 1
      
      amount = abs(x['amount'])
      float_amount = float(x['amount'])
      float_amount_decimal = format(float_amount, '.2f')

      while(amount >0):
        amount = amount//10
        num_count = num_count + 1

      #spaces for decimal and period  
      num_count += 3
  
      total_spaces = 30 - (num_count + description_len)

      spaces = ""
      for x in range(total_spaces):
        spaces +=" "

      master_string+= item_string + spaces + str(float_amount_decimal) + '\n'


    return str(astericks + self.cat + astericks +'\n' + master_string + "Total: " + str(self.get_balance() ))

  def deposit(self,amount,description=""):
    self.ledger.append({'amount' : amount, 'description' : description})

  def withdraw(self,amount,description=""):
    if self.check_funds(amount) == True:
      amount = amount * -1
      self.ledger.append({'amount' : amount, 'description' : description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for x in self.ledger:
      balance+= x['amount']
    return balance

  def transfer(self,amount_transfer, categoryto):
    if self.check_funds(amount_transfer) == True: 
      categoryto.deposit(amount_transfer,"Transfer from " +self.cat)
      self.withdraw(amount_transfer,"Transfer to "+categoryto.cat)
      return True
  
    else:
      return False

  def check_funds(self,amount):
    if amount > self.get_balance():
      return False
    else:
      return True



def create_spend_chart(categories):

  percents = percent_round(categories)
  i = 100
  master_string =""
  while (i >= 0 ):
    text = str(i) + "| "
    master_string += text.rjust(5)

    for x in percents:
      if x >= i:
        master_string += "o  "
      else:
        master_string+= "   "
    master_string += '\n'
    i-=10
  
  max_length = 0
  for object in categories:
    if len(object.cat) > max_length:
      max_length = len(object.cat)  
    
  cat_string =""
  ticks = 0
  for x in range(max_length+1):
    cat_string+="     "
    for object in categories:
      
      if ticks > len(object.cat):
        cat_string += "   "
      else:
        cat_string += object.cat[x-1:x] + "  "
    
    if x == max_length:
      pass
    else:
      cat_string+= '\n'
    ticks+=1

  dashes = "    "
  length_to_loop = ((len(categories)+1) *2) + 2
  for x in range(length_to_loop):
    dashes += "-"

  
  return str("Percentage spent by category" + '\n' + master_string  + dashes + cat_string)
    



def percent_round(withdrawls):
  total_all = 0
  by_cat = []

  nearest_percent = []
   
  for x in withdrawls:
    within_cat = 0
    for item in x.ledger:
      
      if item['amount'] < 0:
        #print(item['amount'])
        total_all += abs(item['amount'])
        within_cat += abs(item['amount'])
      
      
    by_cat.append(within_cat)

  for x in by_cat:
    n = round((x / total_all) * 100)
    
    
    rem = n % 10
    if rem < 5:
      n = int(n/10) * 10
    else:
      n = int((n+10) /10) * 10

    nearest_percent.append(n)
    

  return nearest_percent

