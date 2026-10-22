print("=== GROCERY COST COMPARISON TOOL ===")

# --------- PART 1: what did this week's shop cost per person? ---------
# Store these five values in variables
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4

# Work out basket_cost_per_person using parentheses correctly
basket_cost_per_person = ((rice_price + milk_price + fruit_price) * number_of_baskets) / family_members

# Print the result
print("Basket cost per person:", basket_cost_per_person)


# --------- PART 2: can the items be shared equally? ---------
# Ask for total_items and people wrapped in int()
total_items = int(input("Enter total items: "))
people = int(input("Enter number of people: "))

# Check if people is 0, otherwise use % and // for divisibility
if people == 0:
    print("You cannot share between 0 people.")
else:
    remainder = total_items % people
    if remainder == 0:
        each_person = total_items // people
        print(f"They divide equally. Each person gets {each_person} items.")
    else:
        print(f"They do not divide equally. The remainder is {remainder}.")


# --------- PART 3: fix the weekly average ---------
recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80

# Rebuild total, swap the wrong figure for the right one, and recalculate average
rebuilt_total = recorded_average * total_weeks
corrected_total = rebuilt_total - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks

# Print all three numbers
print("Recorded Average:", recorded_average)
print("Corrected Total:", corrected_total)
print("Corrected Average:", corrected_average)


# --------- PART 4: compare with three stores ---------
store_a_average = 70
store_b_average = 75
store_c_average = 80

# Use 'and' to test if our corrected average is lower than all three stores
verdict = (corrected_average < store_a_average) and (corrected_average < store_b_average) and (corrected_average < store_c_average)


# --------- PART 5: the summary ---------
# Print all three required metrics together
print("\n--- SUMMARY REPORT ---")
print("Basket Cost Per Person:", basket_cost_per_person)
print("Corrected Weekly Average:", corrected_average)
print("Is our store cheaper than all others (Verdict)?:", verdict)
