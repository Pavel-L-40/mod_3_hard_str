data_structure = [[1, 2, 3], {'a': 4,'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban',
                  ('Urban2', 35))}])] #res 99
string_ = str(data_structure)
# print(type(string_))
sign = '[]{}(): '
for i in sign:
    string_ = string_.replace(i,',')
while ',,' in string_:
  string_ = string_.replace(',,',',')
string_new = string_.split(',')

count_res = 0 # искомое значение
count_int = 0
count_str = 0


for i in string_new:
    if i.isdigit():
      count_res += int(i)
      count_int += 1
    else:
      i = i.replace("'","")
      count_res += len(i)
      count_str += 1

# print(count_int,count_str)
print(count_res)
