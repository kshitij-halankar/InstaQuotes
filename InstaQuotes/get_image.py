from PIL import Image, ImageDraw, ImageFont
import os
import textwrap
from get_quote import print_quote
import datetime
import shutil
import requests
import io

IMGUR_CLIENT_ID = "d8dbf3d1c64cf3c"
# IMGUR_CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")
# IMGUR_CLIENT_SECRET = os.getenv("IMGUR_CLIENT_SECRET")

def create_image_flie(img_path):
    try:
        # main_img = img_path + r"/main.png"
        # Check if the original file exists
        img_response = requests.get(img_path)
        if img_response.status_code == 200:
            new_img = Image.open(io.BytesIO(img_response.content))
            # Copy the original file to the new file
            # current_date = datetime.datetime.now().strftime("%Y%m%d")
            # print(current_date)
            new_img_path = "./new_img.png"
            # print("new_img_path: " + new_img_path)
            # shutil.copy(main_img, new_img_path)
            new_img.save(new_img_path)
            return new_img_path
            # print(f"File copied successfully: '{original_filename}' -> '{new_filename}'")
        else:
            print(f"The file '{img_path}' does not exist.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def add_centered_wrapped_text_to_image(image_path, quote_text, quote_author, font_path=None, font_size=40):
    # Open an image file
    with Image.open(image_path) as img:
        # Create a drawing object
        draw = ImageDraw.Draw(img)

        # Load a font
        if font_path is not None:
            font = ImageFont.truetype(font_path, font_size)
        else:
            font = ImageFont.truetype("arial.ttf", font_size)

        # Define the maximum width of a single line of text
        max_width = img.width - 40  # subtracting some padding from the image width

        # Wrap the text
        lines = textwrap.wrap(quote_text, width=40)  # Adjust the width as per your text size and font
        lines.append("- " + quote_author)

        # Get the height of each text line
        line_heights = [draw.textbbox((0, 0), line, font=font)[3] - draw.textbbox((0, 0), line, font=font)[1] for line
                        in lines]

        # Calculate the total height of the wrapped text block
        total_text_height = sum(line_heights)

        # Calculate the Y position to start drawing text so that it is centered vertically
        y = (img.height - total_text_height) / 2

        # Add each line of text
        shadow_offset = (2, 2)
        shadow_color = "white"
        text_color = "black"

        # Add each line of text
        for line in lines:
            # Calculate the width of the line
            line_width = draw.textbbox((0, 0), line, font=font)[2] - draw.textbbox((0, 0), line, font=font)[0]

            # Calculate X position to center the line
            x = (img.width - line_width) / 2

            # Draw the text line
            draw.text((x + shadow_offset[0], y + shadow_offset[1]), line, font=font, fill=shadow_color, align="center")
            draw.text((x, y), line, font=font, fill=text_color, align="center")

            # Move to the next line
            y += line_heights[0]  # Move down by the height of a line

        # Save the edited image
        # img.show()
        img.save(image_path)
        return image_path

def upload_img_imgur(img_path):
    url = "https://api.imgur.com/3/image"
    headers = {
        "Authorization": f"Client-ID {IMGUR_CLIENT_ID}"
    }
    with open(img_path, 'rb') as image_file:
        img_file = {
            'image': image_file
        }
        response = requests.post(url, headers=headers, files=img_file)

        if response.status_code == 200:
            imgur_response = response.json()
            img_url = imgur_response["data"]["link"]
            print("Image uploaded successfully:", img_url)
            return img_url + ".png"
        else:
            print("Failed to upload image:", response.status_code, response.text)
            return None

def get_image():
    image_path = r"https://raw.githubusercontent.com/kshitij-halankar/InstaQuotes/refs/heads/master/InstaQuotes/images/main.png"
    new_img_path = create_image_flie(image_path)
    quote = print_quote()
    quote_text = quote['quoteText']
    quote_author = quote['quoteAuthor']
    font_path = "AwesomeQuote.ttf"  # Provide path to .ttf file if needed
    font_size = 40
    add_centered_wrapped_text_to_image(new_img_path, quote_text, quote_author, font_path, font_size)
    return upload_img_imgur(new_img_path)

# get_image()

