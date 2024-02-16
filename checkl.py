x = range(0,100000000)
while True:
  try: inp = int(input('enter a number '))
  except ValueError:
    print('Invalid Number')
    continue
  if inp not in x:
    print('the number entered is not within the range ')
    continue
  else:
    print('The number entered is valid')
    break
