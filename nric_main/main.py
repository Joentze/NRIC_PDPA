import itertools as it 
import time
def ChecksumNRIC(NRICstring):

  checkDigits = [2 ,7 ,6 ,5 ,4 ,3 ,2]

  FgArr = {0:'X', 1:'W', 2:'U', 3:'T', 4:'R', 5:'Q', 6:'P', 7:'N', 8:'M', 9:'L', 10:'K'}

  StArr = {0:'J', 1:'Z', 2:'I', 3:'H', 4:'G', 5:'F', 6:'E', 7:'D', 8:'C', 9:'B', 10:'A'}

  totalDigitSum = 0

  for i in range(1,len(NRICstring)-1):
    integer = int(NRICstring[i])
    multiply = integer*checkDigits[i-1]
    totalDigitSum+=multiply

  if str(NRICstring[0]) == 'T' :
    totalDigitSum+=4
  elif str(NRICstring[0]) == 'G':
    totalDigitSum+=4
  else:
    pass
  modulo =  totalDigitSum % 11
  
  if NRICstring[0] == 'T' or 'S':
    
    get_alpha = StArr[modulo]
  
    if get_alpha == NRICstring[-1]:
      return True
    else:
      return False

  elif NRICstring[0] == 'G' or 'F':
    
    get_alpha = FgArr[modulo]

    if get_alpha == NRICstring[-1]:
      return True
    else:
      return False

def returnNRICposs(yearOfBirth, BoolCtz, lastFourChar):
  return_list = []
  alpha_one = ""
  
  if yearOfBirth >= 2000 and BoolCtz == True:
    alpha_one = 'T'
  elif yearOfBirth<2000 and BoolCtz == True:
    alpha_one = 'S'
  elif yearOfBirth<2000 and BoolCtz == False:
    alpha_one = 'F'
  elif yearOfBirth>=2000 and BoolCtz == False:
    alpha_one = 'G'

  iteration = it.product(list(range(0,10)), repeat = 2)

  for currentCombo in iteration:
    fullNRIC = str(alpha_one)+str(yearOfBirth)[-2]+str(yearOfBirth)[-1] + ''.join(map(str,currentCombo)) + str(lastFourChar)
    #print(fullNRIC)
    boolean = ChecksumNRIC(fullNRIC)
    if boolean is True:
      return_list.append(fullNRIC)
    else:
      pass

  return return_list


if __name__ == "__main__":
  t1 = time.process_time()
  print(returnNRICposs(2001,True,'341B'))
  t2 = time.process_time()
  print(t2 - t1)