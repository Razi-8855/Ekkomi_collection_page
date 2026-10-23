from PIL import Image, ImageFilter
import numpy as np

def clean_jacket(input_path, output_path, hem_y, strip_y_start, strip_y_end, left_x_margin, right_x_margin):
    img = Image.open(input_path).convert('RGBA')
    arr = np.array(img)
    H, W, _ = arr.shape

    # Find the average background color around the strip
    # Sample background pixels between the hem and strip, and below the strip
    bg_samples = []
    
    # Sample in the gap between hem and strip
    gap_y = (hem_y + strip_y_start) // 2
    for x in range(left_x_margin + 20, right_x_margin - 20, 5):
        bg_samples.append(arr[gap_y, x])
        
    # Sample below the strip
    for y in range(strip_y_end + 15, min(strip_y_end + 30, H)):
        for x in range(left_x_margin + 20, right_x_margin - 20, 10):
            bg_samples.append(arr[y, x])

    bg_samples = np.array(bg_samples)
    base_bg = np.median(bg_samples, axis=0).astype(np.uint8)
    print(f"Base background for {input_path}: {base_bg}")

    # Now, let's look at the strip region:
    # We want to replace the strip and its immediate drop shadow with the natural background
    # Left boundary: sleeve right edge + 10px shadow
    # Right boundary: right sleeve left edge - 10px shadow
    for y in range(hem_y + 10, min(strip_y_end + 30, H)):
        # find left sleeve solid edge at row y
        left_alphas = arr[y, :left_x_margin + 10, 3]
        solid_left = np.where(left_alphas > 150)[0]
        min_x = (solid_left.max() + 15) if len(solid_left) > 0 else left_x_margin

        # find right sleeve solid edge at row y
        right_alphas = arr[y, right_x_margin - 10:, 3]
        solid_right = np.where(right_alphas > 150)[0]
        max_x = (right_x_margin - 10 + solid_right.min() - 15) if len(solid_right) > 0 else right_x_margin

        # If we are below the hem, calculate distance from hem to feather hem shadow
        dist_from_hem = y - hem_y
        
        for x in range(min_x, max_x):
            # Distance from left sleeve
            d_left = x - min_x
            # Distance from right sleeve
            d_right = max_x - x
            
            # Natural soft shadow from hem
            # Shadow drops off over 15 pixels
            if dist_from_hem < 15:
                # Blend between hem shadow and base background
                shadow_factor = max(0.0, (15 - dist_from_hem) / 15.0)
                # gentle ambient shadow: slightly darker than base_bg
                shadow_color = (base_bg[:3] * (1.0 - 0.08 * shadow_factor)).astype(np.uint8)
                arr[y, x, :3] = shadow_color
                arr[y, x, 3] = base_bg[3]
            else:
                arr[y, x] = base_bg

    cleaned_img = Image.fromarray(arr)
    # Apply a very gentle blur only on the modified region boundary to avoid any harsh edges
    cleaned_img.save(output_path)
    print(f"Saved {output_path}")

# Clean Curiosity (Blue jacket)
# Hem ends around y=812, strip is from y=828 to y=895, left sleeve ~125, right sleeve ~555
clean_jacket(
    'assets/collection/nocturne/curiosity/curiosity.jpg.bak',
    'assets/collection/nocturne/curiosity/curiosity.jpg',
    hem_y=812,
    strip_y_start=826,
    strip_y_end=896,
    left_x_margin=135,
    right_x_margin=545
)

# Clean Temptation (Green jacket)
# Hem ends around y=796, strip is from y=814 to y=882, left sleeve ~125, right sleeve ~555
clean_jacket(
    'assets/collection/nocturne/temptation/temptation.jpg.bak',
    'assets/collection/nocturne/temptation/temptation.jpg',
    hem_y=796,
    strip_y_start=812,
    strip_y_end=882,
    left_x_margin=135,
    right_x_margin=545
)
