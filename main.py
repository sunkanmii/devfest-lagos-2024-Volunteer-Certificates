import csv
from PIL import Image, ImageDraw, ImageFont

def write_names_on_image(csv_file, image_path, output_dir, font_path, font_size, text_position):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):
            if index == 0:  # Skip the header if it exists
                continue
            name = row[0]  # Assuming names are in the first column
            
            # Create a copy of the image for each name
            img_copy = image.copy()
            draw_copy = ImageDraw.Draw(img_copy)
            
            
            draw_copy.text(text_position, name.upper(), fill="black", font=font)
            
            output_path = f"{output_dir}/{name}-certificate.png"
            img_copy.save(output_path)
            print(f"Image saved for {name} at {output_path}")


csv_file = "./volunteer-names.csv"
image_path = "./Certificate template (Final) Event day volunteers_page-0001.jpg"
output_dir = "./volunteer certificates 2024"
font_path = "./Urbanist-VariableFont_wght.ttf"
font_size = 80
text_position = (476, 924)

write_names_on_image(csv_file, image_path, output_dir, font_path, font_size, text_position)
