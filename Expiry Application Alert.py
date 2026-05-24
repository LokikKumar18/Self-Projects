from datetime import datetime
import time

# Main dictionary
Appliance_Lifespan = {
    "Refrigerator": 15,
    "AC": 15,
    "Fan": 10,
    "Washing Machine": 10,
    "Cooler": 12,
    "Microwave": 8
}

# Empty dictionary for new appliances
New_Appliances = {}

# Ask appliance name
appliance = input("Enter the Appliance Name: ")

# Check appliance
if appliance in Appliance_Lifespan:

    print("Wait!")
    time.sleep(2)

    print("Checking for the Input appliance")
    time.sleep(2)

    print("Appliance already registered and Lifespan also registered")

    lifespan = Appliance_Lifespan[appliance]

else:
    print("Wait!")
    time.sleep(2)
    print("Check for Input Appliance")
    time.sleep(2)
    print("Appliance is Not Registered")

    time.sleep(2)

    # Ask user for registration
    choice = input("\nDo you want to register this new appliance? (yes/no): ")

if choice.lower() == "yes":

        new_appliance = input("Enter New Appliance Name: ")

        time.sleep(1)

        # Ask lifespan
        new_lifespan = int(input(f"Enter lifespan of {appliance}: "))

        # Add in empty dictionary
        New_Appliances[appliance] = new_lifespan

        # Update main dictionary
        Appliance_Lifespan.update(New_Appliances)

        time.sleep(2)

        print("\nNew Appliance Registered Successfully!")

        time.sleep(2)

        print("Showning New Appliance Lifespan List")

        time.sleep(2)

        print("\nUpdated Appliance Lifespan List :", Appliance_Lifespan)

        time.sleep(2)

        # Ask again
        appliance = input("\nEnter Appliance Name Again: ")

if appliance in Appliance_Lifespan:
        lifespan = Appliance_Lifespan[appliance]

else:
        print("Registration Cancelled")
        exit()

# Purchase year
purchase_year = int(input("\nEnter Purchase Year Of the Appliance: "))

# Current year
current_year = datetime.now().year

# Expiry year
expiry_year = purchase_year + lifespan

# Remaining years
remaining = expiry_year - current_year

# Output
if remaining > 0:
    print(f"\nYour {appliance} will expire in {expiry_year}")
    print(f"Remaining lifespan: {remaining} years")

elif remaining == 0:
    print(f"\nYour {appliance} expires this year.")
    print("Repair or Change it.")

else:
    print(f"\nYour {appliance} already expired in {expiry_year}")
    print("Change it.")