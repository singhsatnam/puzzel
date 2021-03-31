logs = [
    'a1 9 2 3 1',
'g1 act car',
'aa1 act car',
'zo4, 4 7',
'ab1 off key dog',
'a8 act zoo']

str_logs = []
dig_logs = []

for log in logs:
    if log.split()[1].isdigit():
        dig_logs.append(log)
    else:
        str_logs.append(log)
print(str_logs)
str_logs.sort(key=lambda log: log.split()[0])  # when suffix is tie, sort by identifier
print(str_logs)
str_logs.sort(key=lambda log: log.split()[1:])  # sorted by suffix
print(str_logs)

#
# print(str_logs)
# print("god")
# print(dig_logs)

