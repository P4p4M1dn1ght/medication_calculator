drug_name = input("Enter the name of the drug: ")
doctors_dosage = input("Please insert the dosage as prescribed by the doctor: ")
pills_in_packet = input("Please insert the pills within the packet: ")
time_period = input("Are there prescribed number of months or days for the medication: ")

if time_period == "days":
    for_days = input("Enter the number of days: ")
    dosage_as_per_days = int(doctors_dosage) * int(for_days)
    packs_required = int(dosage_as_per_days) / int(pills_in_packet)
    zero_out = 1 * int(packs_required)
    print(f"You need {zero_out} packs of {drug_name} for {for_days} days..")

elif time_period == "months":
    for_months = input("Enter the number of months: ")
    months = int(for_months) * 31
    dosage_as_per_month = int(doctors_dosage) * int(months)
    packs_required = int(dosage_as_per_month) / int(pills_in_packet)
    zero_out = 1 * int(packs_required)
    print(f"You need {zero_out} packs of {drug_name} for {for_months} months..")

else:
    print("Error running script!")

