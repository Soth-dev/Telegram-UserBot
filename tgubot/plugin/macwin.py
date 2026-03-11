from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from random import randint


def random_gradient(width, height):
    """Generate a random gradient as the background."""
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    color1 = (randint(0, 255), randint(0, 255), randint(0, 255))
    color2 = (randint(0, 255), randint(0, 255), randint(0, 255))
    for y in range(height):
        for x in range(width):
            r = int(color1[0] + (color2[0] - color1[0]) * y / height)
            g = int(color1[1] + (color2[1] - color1[1]) * y / height)
            b = int(color1[2] + (color2[2] - color1[2]) * y / height)
            draw.point((x, y), (r, g, b))
    return img


def get_img(width, height, image):
    """Resize and crop a image for the background."""
    with Image.open(image) as im:
        im_w, im_h = im.size
        scale = max(width / im_w, height / im_h)
        s_x, s_y = int(im_w * scale), int(im_h * scale)
        if im_w != width and im_h != height:
            im = im.resize((s_x, s_y), Image.Resampling.LANCZOS)
        if s_x != width or s_y != height:
            left = (s_x - width) / 2
            top = (s_y - height) / 2
            right = left + width
            bottom = top + height
            im = im.crop((left, top, right, bottom))
    return im


def draw_window(font_path, text, image_path=None):
    """Draw a window with rounded corners, three dots, and wrapped text below the dots."""
    patting = 28
    border_radius = 32
    dot_size = 16
    group_spacing = 8
    newline_spacing = 8

    # Add wrapped mono-font text inside the window, below the dots
    font_size = 32
    font = ImageFont.truetype(font_path, font_size)

    # Wrap text to fit the window width

    inner_height = inner_width = 0
    for i in text.split("\n"):
        inner_height += font_size + newline_spacing
        j = font.getbbox(i)[2]
        if j > inner_width:
            inner_width = j
    inner_width = inner_width + patting * 2 if inner_width + patting * 2 >= 128 else 128
    inner_height = (
        inner_height - newline_spacing * 2 - font_size
        if text.endswith("\n")
        else inner_height - newline_spacing
    )
    if inner_width < inner_height:
        width = inner_width / 0.88
        margin = inner_width * 3 / 22 + 10
        height = margin + inner_height
    else:
        inner_height = inner_height + patting * 3 + dot_size
        height = inner_height / 0.88
        margin = inner_height * 3 / 22 + 10
        width = margin + inner_width

        margin = margin / 2

    # Create the gradient background
    if image_path:
        background = get_img(width, height, image_path)
    else:
        background = random_gradient(width, height)

    blurred_bg = ImageEnhance.Brightness(
        background.filter(ImageFilter.GaussianBlur(radius=margin))
    ).enhance(0.7)
    # Define the rounded black window area
    # Create a mask for rounded rectangle
    mask_window = Image.new("L", background.size, 0)
    mask_draw = ImageDraw.Draw(mask_window)
    mask_draw.rounded_rectangle(
        [(margin - 1, margin - 1), (width - margin + 1, height - margin + 1)],
        fill=255,
        radius=border_radius,
    )

    mask_shadow = Image.new("RGBA", background.size, 0)
    mask_draw = ImageDraw.Draw(mask_shadow)
    mask_draw.rounded_rectangle(
        [(margin - 1, margin - 1), (width - margin + 1, height - margin + 1)],
        fill=(128, 128, 128, 128),
        radius=border_radius,
    )
    mask_shadow = mask_shadow.filter(ImageFilter.GaussianBlur(radius=margin / 5))

    # Composite the blurred region onto the original background
    background.paste(mask_shadow, (0, 0), mask_shadow)
    background = Image.composite(blurred_bg, background, mask_window)
    draw = ImageDraw.Draw(background)

    # Add the three dots in the top-left corner
    dot_positions = [
        (margin + patting, margin + patting),
        (margin + patting + dot_size + group_spacing, margin + patting),
        (margin + patting + 2 * (group_spacing + dot_size), margin + patting),
    ]
    dot_colors = [
        (255, 59, 48),
        (255, 204, 0),
        (76, 217, 100),
    ]  # Red, yellow, green (Mac OS-style)

    for pos, color in zip(dot_positions, dot_colors):
        draw.ellipse(
            [(pos[0], pos[1]), (pos[0] + dot_size, pos[1] + dot_size)], fill=color
        )

    current_height = (
        margin + patting + group_spacing + dot_size
    )  # Adjust margin to position below dots
    # Add the text
    for i in text.split("\n"):
        draw.text(
            (margin + patting, current_height), i, font=font, fill=(255, 255, 255)
        )
        current_height += font_size + newline_spacing

    return background
