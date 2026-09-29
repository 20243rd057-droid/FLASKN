week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
out = []
for i, day in enumerate(week):
    if day == 'Saturday' or day == 'Sunday':
        out.append(i)
print(out)




