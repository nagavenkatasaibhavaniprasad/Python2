
# Student Email and Identifier Validation

email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

# Email Validation
print("\n--- Email Validation ---")

if email.count("@") != 1:
    print("Invalid email: Missing or extra @ separator")
else:
    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    if username == "":
        print("Invalid email: Missing username")
    elif domain == "":
        print("Invalid email: Missing domain")
    elif "." not in domain:
        print("Invalid email: Missing domain separator (.)")
    elif " " in email:
        print("Invalid email: Contains spaces")
    else:
        valid = True
        for ch in email:
            if not (ch.isalnum() or ch in "._-@"):
                valid = False

        if valid:
            print("Email format is valid")
        else:
            print("Invalid email: Invalid character group")

# Registration ID Validation
print("\n--- Registration ID Validation ---")

# Expected format: NRI followed by 4 digits
if len(reg_id) != 7:
    print("Invalid ID: Incorrect length")
elif reg_id[0:3] != "NRI":
    print("Invalid ID: Missing NRI prefix")
else:
    valid = True

    for ch in reg_id[3:]:
        if not ch.isdigit():
            valid = False

    if valid:
        print("Registration ID is valid")
    else:
        print("Invalid ID: Last 4 characters must be digits")
