def outputs_num(f, b):
  for i in range(f, b+1):
    if i % 3 == 0 and i % 5 == 0:
      print('$$@@')

    elif i % 3 == 0:
      print('$$')

    elif i % 5 == 0:
      print('@@')
    
    else:
      print(i)

print(outputs_num(11, 79))