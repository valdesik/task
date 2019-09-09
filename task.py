def get_middle(s):
    VasiaMoney = 0
    ticketPrice = 25
    VasiaSay= ''
    for x in s:
      if x == ticketPrice:
            VasiaMoney+=x
            VasiaSay = 'Yes'
      elif x>ticketPrice:
            temp = x-ticketPrice
            if VasiaMoney>=temp:
               VasiaMoney-=temp
               VasiaMoney+=x
               VasiaSay = 'Yes'
            elif VasiaMoney<temp:
                VasiaSay = 'NO'
            
            
    return VasiaSay
   

print(get_middle([25,25,25,75,100]))
         
    