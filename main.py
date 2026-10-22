# ==========================================
# SCHOOL CLUB MEMBER BADGE
# ==========================================

# --------- PART 1: member details ---------
# Ask for the member name and the club name with input().
# Save each answer in its own variable.
name = input("Enter member name: ")
club = input("Enter club name: ")


# --------- PART 2: data types ---------
# Make member_number = 8, points = 9.5 and is_active = True.
member_number = 8
points = 9.5
is_active = True

# Print each one with its data type, using type().
print("member_number:", member_number, type(member_number))
print("points:", points, type(points))
print("is_active:", is_active, type(is_active))


# --------- PART 3: badge code ---------
# Join: the first 3 letters of the name,
# the last letter of the club,
# and the member number turned into text.
# Save it in badge_code and print it.
badge_code = name[:3] + club[-1] + str(member_number)
print("Badge Code:", badge_code)


# --------- PART 4: final badge ---------
print("===== CLUB BADGE =====")
# Print four lines: Member, Club, Code and Points | Active.
# Join the words and the values with +.
print("Member: " + name)
print("Club: " + club)
print("Code: " + badge_code)
print("Points | Active: " + str(points) + " | " + str(is_active))
