from PIL import Image
import stepic
img = Image.open(r"upz.png")
print(stepic.decode(img))