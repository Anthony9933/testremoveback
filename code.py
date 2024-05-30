from rembg import remove
# fornece ao interpretador python recursos de edição de imagem
from PIL import Image

img_entrada = '_563f4f9c-0bb0-42c1-8a8b-8cad2d590c17.jpeg'
img_saida = 'output.png'
input = Image.open(img_entrada)
output = remove(input)
#salvando a imagem
output.save(img_saida)
