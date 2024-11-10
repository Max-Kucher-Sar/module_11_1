from PIL import Image
file = input(f'Введите название файла: ')
file_type = input(f'Введите формат файла: ')

im = Image.open(f'{file}.{file_type}')
im = im.resize((128, 128))
im.save(f'{file}_0.{file_type}')

degrees = 0
image_filenames = [f'{file}_0.{file_type}']
for i in range(1, 4):
    degrees += 90
    rotated_im = im.rotate(degrees)
    rotated_filename = f'{file}_{i}.{file_type}'
    rotated_im.save(rotated_filename)
    image_filenames.append(rotated_filename)


images = [Image.open(files) for files in image_filenames]
images[0].save('some_gif.gif', save_all=True, append_images=images[1:], duration=500, loop=0)

