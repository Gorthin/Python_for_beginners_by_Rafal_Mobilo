isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRainy = True

TurnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)

print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",TurnLightsOn)