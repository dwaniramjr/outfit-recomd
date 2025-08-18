def recommend_outfit(age, gender):
    gender = gender.strip().lower()

    if age < 0:
        return "Invalid age entered."

    if gender == "male":
        if age <= 12:
            return "T-shirt and shorts"
        elif age <= 20:
            return "Hoodie and jeans"
        elif age <= 35:
            return "Casual shirt and chinos"
        elif age <= 55:
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
        elif age <= 55:
            return "Saree or formal wear"
        else:
            return "Comfortable kurta or cardigan with pants"

    elif gender in ["non-binary", "other"]:
        if age <= 12:
            return "Comfortable casual wear"
        elif age <= 20:
            return "Trendy gender-neutral outfit"
        elif age <= 35:
            return "Smart-casual neutral fashion"
        elif age <= 55:
            return "Professional neutral outfit"
        else:
            return "Cozy and comfortable neutral wear"

    else:
        return "Invalid gender. Please enter 'male', 'female', or 'non-binary'."


def main():
    try:
        age_input = int(input("28: "))
    except ValueError:
        print("Please enter a valid number for age.")
        return

    gender_input = input("female: ")

    outfit = recommend_outfit(age_input, gender_input)
    print("\n👕 Recommended outfit:", outfit)

outfit = recommend_outfit(age_input, gender_input)
print("Recommended outfit:", outfit)

if __name__ == "__main__":
    main()
