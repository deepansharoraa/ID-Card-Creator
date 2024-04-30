from PIL import Image, ImageDraw, ImageFont

def create_id_card(name, dob, gender, institution, email, image_path, output_path):

    width, height = 800, 400
    img = Image.new("RGB", (width, height), "white")


    draw = ImageDraw.Draw(img)


    heading_font = ImageFont.truetype("constan.ttf", 36)


    heading_text = "ID CARD"
    heading_position = ((width - heading_font.getmask(heading_text).getbbox()[2]) // 2, (height - 300) // 2)
    draw.text(heading_position, heading_text, fill="black", font=heading_font)


    user_image = Image.open(image_path)
    user_image = user_image.resize((200, 300))
    img.paste(user_image, (width - 250, 50))


    font = ImageFont.truetype("constan.ttf", 18)

    #  text and position for name
    draw.text((50, 150), f"Name: {name}", fill="black", font=font)

    #  text and position for date of birth
    draw.text((50, 180), f"Date of Birth: {dob}", fill="black", font=font)

    # text and position for gender
    draw.text((50, 210), f"Gender: {gender}", fill="black", font=font)

    # text and position for institution
    draw.text((50, 240), f"Institution: {institution}", fill="black", font=font)

    # text and position for email
    draw.text((50, 270), f"Email: {email}", fill="black", font=font)

    # Save the edited image
    img.save(output_path)

    # Display the created ID card
    img.show()

def main():

    name = input("Enter your name: ")
    dob = input("Enter your date of birth (DD/MM/YY): ")
    gender = input("Enter your gender: ")
    institution = input("Enter your institution's name: ")
    email = input("Enter your email: ")
    image_path = input("Enter the path to your image: ")

    output_path = "id_card_with_image.png"  # Output path for the ID card

    # Create ID card
    create_id_card(name, dob, gender, institution, email, image_path, output_path)
    print("ID card created successfully!")

if __name__ == "__main__":
    main()
