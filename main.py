# Name: Xuan Dang

# Phase 1:
length = float(input("The length of the zander: "))
if length >= 42:
    print ("A zander fulfills the size limit")
else:
    print("The zander does not fulfill the size limit and release the fish back into the lake ")

# Phase 2:
cabin_class = input("The cabin class of a cruise ship: ")
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")

# Phase 3:
gender = input("Input females or males")
hemoglobin_value = float(input("Hemoglobin value is: "))
if gender == "female":
    if hemoglobin_value < 117:
        print("The Hemoglobin value is low")
    elif 117 < hemoglobin_value < 155:
        print("The Hemoglobin value is normal")
    else:
        print("The Hemoglobin value is high")
if gender == "male":
    if hemoglobin_value < 134:
        print("The Hemoglobin value is low")
    elif 134 < hemoglobin_value < 167:
        print("The Hemoglobin value is normal")
    else:
        print("The Hemoglobin value is high")

    # Phase 4



