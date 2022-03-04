newhike = float(input("Enter New Hike Amount: "))
oldhike = float(input("Enter old Hike Amount: "))
hikepercentage=float((newhike-oldhike)/oldhike)
print("Hike Percentage: ",round(((hikepercentage)*100),2))