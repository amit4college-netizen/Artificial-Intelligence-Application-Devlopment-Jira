# Table driven vacuum cleaner agent

# Define rooms and their status
rooms={}
rooms['A'] = input("Enter status of Room A (Clean/Dirty) :")
rooms['B'] = input("Enter status of Room B (Clean/Dirty) :")

#chk weather all rooms are already clean
if rooms['A'] == "Dirty":
    print("/nRoom A is Dirty")
    print("Action suck")
    rooms['A'] = "clean"
    print("Room A is cleaned")

else:
    print("\nRoom A is already clean")
    #now visit room B
    if rooms['B'] == "Dirty":
        print("\nRoom B is Dirty")
        print("Action:Suck")
        rooms['B']="Clean"
        print("Room B cleaned")

    else:
        print("Room is B already clean")

    print("\nAll rooms are clean. Task Completed.")
