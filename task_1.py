def slice_less(my_list, lesser):
  sw = True
  while sw:
    sw = False
    
    for i in range(len(my_list)-1):
      if my_list[i] < my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
        sw = True

  new_list = my_list.copy()
        
  for i in new_list:
    if i <= lesser:
      my_list.remove(i)

  return my_list
      
    

    

print(slice_less([1, 1, 1, 1, 3, 3, 3, 2, 5], 2))