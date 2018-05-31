from sources import daily, weekly
print("Daily forecast:", daily.forecast())
print("Weekly forecast:")

for number, outlook in enumerate(weekly.forecast(), 2):
    print(number, outlook)
