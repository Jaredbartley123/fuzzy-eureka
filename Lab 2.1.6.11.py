hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

refinedhour = hour * 60

finalHours = ((refinedhour + mins + dura) / 60)

finalMin = ((refinedhour + mins + dura) % 60)

roundedStuff = round(finalMin * 1.67)

badDecimal = finalHours - (roundedStuff / 100)

KindaFinalHours = finalHours - badDecimal

Finalhours = round(finalHours - KindaFinalHours)

Realfinalhour = Finalhours % 24

print(Realfinalhour, finalMin, sep=(":"))
