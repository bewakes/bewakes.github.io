import os
import sys
import hashlib
from pathlib import Path
from PIL import Image, ImageDraw

def generate_hashes_until_length(inp: str, n: int) -> str:
    """
    Keeps generating SHA-256 hashes of the input string until the concatenated binary mask length exceeds or equals n bits.

    Args:
        inp (str): The input string to hash.
        n (int): The required length of the binary mask in bits.

    Returns:
        str: A concatenation of hex-encoded SHA-256 hashes.
    """
    result = ''
    current_inp = inp
    while len(result) * 4 < n:  # Each hex digit represents 4 bits
        hash_hex = hashlib.sha256(current_inp.encode('utf-8')).hexdigest()
        result += hash_hex
        current_inp = hash_hex
    return result

def get_colors_and_mask(hexstr: str, n_colors: int = 1) -> tuple:
    """
    Extracts a list of RGB colors and a binary mask from the given hex string.

    Args:
        hexstr (str): The hex string to process.
        n_colors (int): The number of colors to extract.

    Returns:
        tuple: A tuple containing a list of RGB colors and a binary mask string.
    """
    skip = 6  # Number of hex characters per color (2 per channel, 3 channels)
    colors = [
        (
            int(hexstr[i * skip : i * skip + 2], 16),
            int(hexstr[i * skip + 2 : i * skip + 4], 16),
            int(hexstr[i * skip + 4 : i * skip + 6], 16)
        )
        for i in range(n_colors)
    ]
    mask = bin(int(hexstr, 16))[2:]  # Convert hex string to binary mask
    return colors, mask


def generate_identicon(content: str, width: int = 500, height: int = 200, block_size: int = 10) -> Image.Image:
    """
    Generates an identicon image based on the given content.

    Args:
        content (str): The input content to generate the identicon.
        width (int): The width of the image.
        height (int): The height of the image.
        block_size (int): The size of each block in the grid.

    Returns:
        Image: The generated identicon image.
    """
    if width % block_size != 0 or height % block_size != 0:
        raise ValueError("block_size should divide width and height evenly")

    x_grids = width // block_size
    y_grids = height // block_size
    required_mask_length = x_grids * y_grids

    # Hash the content
    mask_hex = generate_hashes_until_length(content, required_mask_length)
    colors, mask = get_colors_and_mask(mask_hex)

    # Create the image
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    one_count = 0
    # Generate the pattern
    for y in range(y_grids):
        for x in range(x_grids):
            key = y * x_grids + x
            color = colors[one_count % len(colors)]
            if mask[key] == '1':
                one_count += 1
                draw.rectangle(
                    [x * block_size, y * block_size, (x + 1) * block_size, (y + 1) * block_size],
                    fill=color
                )

    return image


if __name__ == "__main__":
    filepath = sys.argv[1]
    content = open(filepath).read()

    filename = filepath.split("/")[-1]
    name = filename.split(".")[0]

    target_dir = Path("docs/images/")
    target_name = Path(name + ".png")

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    target_path = target_dir / target_name

    width = 1000
    height = 200
    block_size = 25

    identicon_image = generate_identicon(content, width, height, block_size)

    # Save the image
    identicon_image.save(target_path)
    with open("/tmp/a.log", "w") as f:
        f.write(f'wrote {filepath}')
