firstname = input("What is your first name? ")
neighbor = input("What is your neighbor's first name? ")
mnths_coding = int(input("How many months have you been coding? "))
nghbr_mnths_coding = int(input("How many months has your neighbor been coding? "))
print(str(firstname) + " has been coding for " + str(mnths_coding) + " months.")
print(str(neighbor) + " has been coding for " + str(nghbr_mnths_coding) + " months.")
print("We have been coding for a total of " + str(mnths_coding+nghbr_mnths_coding) + " months.")