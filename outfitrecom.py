def recommend_outfit(age, gender):
    gender = gender.lower()

    if gender == "male":
        if age <= 12:
            return "T-shirt and shorts"
        elif age <= 19:
            return "Hoodie and jeans"
        elif age <= 35:
            return "Casual shirt and chinos"
        elif age <= 60:
            return "Formal shirt and trousers"
        else:
            return "Sweater and comfortable pants"

    elif gender == "female":
        if age <= 12:
            return "Frock or top with leggings"
        elif age <= 19:
            return "Jeans and crop top"
        elif age <= 35:
            return "Kurti with jeans or a dress"
        elif age <= 60:
            return "Saree or formal wear"
        else:
            return "Comfortable kurta or cardigan with pants"

    else:
        return "Invalid gender. Please enter 'male' or 'female'."

# Main code
age_input = int(input("Enter your age: "))
gender_input = input("Enter your gender (male/female): ")

outfit = recommend_outfit(age_input, gender_input)
print("Recommended outfit:", outfit)
#Changes made
