from rembg import remove
from PIL import Image

input_path = 'input.jpg'
output_path = 'output.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(output_path) 