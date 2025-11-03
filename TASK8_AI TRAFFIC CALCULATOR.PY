print("\n-----AI TRAFFIC CALCULATOR-----\n")
vehicle_number=(input("enter the vehicle_number"))
speed=int(input("enter the speed"))
if speed<=80:
        fine=0
        advice="safe driving!keep it up"
elif 81>=speed<=100:
        fine=3000
        advice="drive carefully"
elif 101>=speed<=120:
        fine=7000
        advice="high risk"
else:
        fine=15000
        advice="dangerous speed"
print(f"\n----- TRAFFIC FINE CALCULATOR-----")
print(f"vehicle number:{vehicle_number}")
print(f"speed:{speed}")
print(f"fine:KES{fine}")
print(f"AI SAFETY ADVICE:{advice}")