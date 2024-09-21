from PIL import Image
test_image = Image.open("IMG/img1.jpg")

print(f'{type(test_image)}')
print(f'{test_image.size =}')
print(f'{test_image.mode =}')
print(f'{test_image.width =}')
print(f'{test_image.height =}')

test_image.show()

