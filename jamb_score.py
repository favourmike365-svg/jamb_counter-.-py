s = list(map( int ,  input("4 scores:   ") .split( )))
print(f"Total  {sum(s)}   -  {'PASS'  if sum(s)>=200 else  'FAIL' } " )