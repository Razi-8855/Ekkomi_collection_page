import os
import shutil
from PIL import Image
import numpy as np

BRAIN_DIR = r"C:\Users\razi7\.gemini\antigravity-ide\brain\2766c843-fcee-47f0-bc63-276266ea7f66"
CUR_BACK_SRC = os.path.join(BRAIN_DIR, "curiosity_back_1791217000379.jpg")
TEM_BACK_SRC = os.path.join(BRAIN_DIR, "temptation_back_1791217035695.jpg")

CUR_DIR = r"assets\collection\nocturne\curiosity"
TEM_DIR = r"assets\collection\nocturne\temptation"

# 1. Copy back images
cur_back_dst = os.path.join(CUR_DIR, "curiosity_back.jpg")
tem_back_dst = os.path.join(TEM_DIR, "temptation_back.jpg")

shutil.copy2(CUR_BACK_SRC, cur_back_dst)
shutil.copy2(TEM_BACK_SRC, tem_back_dst)
print(f"Copied {cur_back_dst} and {tem_back_dst}")

# 2. Function to seamlessly remove floating bottom strip
def remove_strip_seamless(img_path, hem_bottom, strip_top, strip_bottom, strip_left, strip_right):
    # Ensure backup exists
    bak_path = img_path + ".bak"
    src_path = bak_path if os.path.exists(bak_path) else img_path
    
    img = Image.open(src_path)
    fmt = img.format or ('PNG' if img.mode == 'RGBA' else 'JPEG')
    arr = np.array(img).astype(np.float32)
    
    # Sample background color in the gap above strip and below strip
    top_samples = arr[hem_bottom + 6 : strip_top - 2, strip_left + 20 : strip_right - 20]
    bot_samples = arr[strip_bottom + 5 : strip_bottom + 25, strip_left + 20 : strip_right - 20]
    
    top_color = np.median(top_samples, axis=(0, 1))
    bot_color = np.median(bot_samples, axis=(0, 1))
    print(f"Color above strip: {top_color}, color below: {bot_color}")
    
    box_top = strip_top - 3
    box_bottom = strip_bottom + 5
    box_left = strip_left - 5
    box_right = strip_right + 5
    total_h = box_bottom - box_top
    
    for y in range(box_top, box_bottom):
        t = (y - box_top) / float(total_h)
        row_bg = (1.0 - t) * top_color + t * bot_color
        
        for x in range(box_left, box_right):
            d_top = y - box_top
            d_bot = box_bottom - 1 - y
            d_left = x - box_left
            d_right = box_right - 1 - x
            edge_dist = min(d_top, d_bot, d_left, d_right)
            feather = min(1.0, edge_dist / 4.0)
            
            arr[y, x] = (1.0 - feather) * arr[y, x] + feather * row_bg
            
    out_arr = np.clip(arr, 0, 255).astype(np.uint8)
    out_img = Image.fromarray(out_arr, mode=img.mode)
    out_img.save(img_path, format=fmt)
    print(f"Successfully cleaned: {img_path}")

# Blue jacket (Curiosity)
remove_strip_seamless(
    os.path.join(CUR_DIR, "curiosity.jpg"),
    hem_bottom=812,
    strip_top=827,
    strip_bottom=895,
    strip_left=153,
    strip_right=526
)

# Green jacket (Temptation)
remove_strip_seamless(
    os.path.join(TEM_DIR, "temptation.jpg"),
    hem_bottom=796,
    strip_top=813,
    strip_bottom=881,
    strip_left=154,
    strip_right=528
)

print("All asset updates completed successfully.")
