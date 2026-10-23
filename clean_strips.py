from PIL import Image
import numpy as np

def remove_strip_seamless(image_path, hem_bottom, strip_top, strip_bottom, strip_left, strip_right):
    img = Image.open(image_path)
    is_rgba = img.mode == 'RGBA'
    arr = np.array(img).astype(np.float32)
    
    # Sample background color in the gap right above the strip (between hem_bottom + 5 and strip_top - 2)
    # and below the strip (between strip_bottom + 5 and strip_bottom + 20)
    top_samples = arr[hem_bottom + 8 : strip_top - 2, strip_left + 20 : strip_right - 20]
    bot_samples = arr[strip_bottom + 5 : strip_bottom + 25, strip_left + 20 : strip_right - 20]
    
    # Calculate average color above and below the strip
    top_color = np.mean(top_samples, axis=(0, 1))
    bot_color = np.mean(bot_samples, axis=(0, 1))
    print(f"{image_path} top_color: {top_color}, bot_color: {bot_color}")
    
    # For every pixel in the strip bounding box (plus 4px margin for shadow):
    box_top = strip_top - 4
    box_bottom = strip_bottom + 6
    box_left = strip_left - 6
    box_right = strip_right + 6
    
    # Interpolate vertically between top_color and bot_color
    total_h = box_bottom - box_top
    for y in range(box_top, box_bottom):
        alpha_y = (y - box_top) / float(total_h)
        row_bg = (1.0 - alpha_y) * top_color + alpha_y * bot_color
        
        for x in range(box_left, box_right):
            # Distance to the four boundaries of the box to feather smoothly
            d_top = y - box_top
            d_bot = box_bottom - 1 - y
            d_left = x - box_left
            d_right = box_right - 1 - x
            d_edge = min(d_top, d_bot, d_left, d_right)
            
            # Feather radius of 5 pixels
            feather = min(1.0, d_edge / 5.0)
            
            # Replace pixel smoothly
            arr[y, x] = (1.0 - feather) * arr[y, x] + feather * row_bg

    result_arr = np.clip(arr, 0, 255).astype(np.uint8)
    result_img = Image.fromarray(result_arr, mode=img.mode)
    
    # Save back preserving original format
    fmt = img.format if img.format else ('PNG' if is_rgba else 'JPEG')
    result_img.save(image_path, format=fmt)
    print(f"Successfully cleaned strip from {image_path}")

# Blue jacket (Curiosity)
# Strip: y from 828 to 894, x from 154 to 525, hem bottom around 812
remove_strip_seamless(
    'assets/collection/nocturne/curiosity/curiosity.jpg',
    hem_bottom=812,
    strip_top=827,
    strip_bottom=895,
    strip_left=152,
    strip_right=527
)

# Green jacket (Temptation)
# Strip: y from 814 to 880, x from 155 to 527, hem bottom around 796
remove_strip_seamless(
    'assets/collection/nocturne/temptation/temptation.jpg',
    hem_bottom=796,
    strip_top=813,
    strip_bottom=881,
    strip_left=153,
    strip_right=529
)
