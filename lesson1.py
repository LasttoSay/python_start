'''
#First task
name = 'Slavik'
date = 13
print (name, date)

dish = input('Enter your favourite dish: ')
print(f'Your favourite dish is {dish}')
'''


'''
#Second task

time = int(input('Enter some amount of secconds: '))
hours = time // 3600
hours_24 = hours % 24
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f'{hours_24:02}:{minutes:02}:{seconds:02}')'''



'''
#third task

user_enter = int(input('Enter your number: '))
print(user_enter + (user_enter*2) + (user_enter*3))



'''


'''
#Fourth task
num = int(input('Enter your number, that greater than 0: '))
digit_big = num % 10
num_copy = num

while num_copy > 0:
  digit = num_copy % 10
  if digit > digit_big:
    digit_big = digit
    if digit_big == 9:
      break
  num_copy = num_copy // 10
  
print (f'The greatest digin in number {num} is {digit_big}')



'''
'''
#fifth task

revenue = float(input('Enter revenue of your company: '))
costs = float(input('Enter costs of your company: '))
fin_result = revenue - costs 
if fin_result > 0:
  print (f'Cong your company worth something')
  pure_result = fin_result / revenue * 100
  print(f'Your pure result is {pure_result:.2f}%')
  employes = int(input('Enter how much people work in your company: '))
  sallary = fin_result / employes
  print(f'Each of your employes will recive {sallary:.1f}')
else:
  print('Your company worth nothing')
  

'''

'''
#sixth task
while True:
  day = 1
  start = float(input('Enter your starting point in km: '))
  finish = float(input('Enter your goal: '))
  if start <= 0 or finish < 0:
    print('Enter correct values, that biger than 0!')
  else:
    while start < finish:
      start = start + (start / 100 * 10)
      day += 1
    print (f'You achived your goal in {day} days yove finished {start} km')
    break


'''
 
    


