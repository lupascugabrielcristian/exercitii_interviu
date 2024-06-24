# Staircase problem
for i in range(1, 5):
    print("%s%s"%((5-i)*' ', i*'#'))


# AM/PM to 24hour clock conversion
def timeConversion(s):
    hour = int(s.split(':')[0])
    min_sec = s[3:8]
    if "PM" in s:
        hour = hour + 12
        
    if hour % 12 == 0:
        hour -= 12
            
    return f"{hour:02d}:{min_sec}"