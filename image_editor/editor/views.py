from django.shortcuts import render
from PIL import Image, ImageEnhance
import os


def home(request):
    return render(request, 'editor/home.html')


def edit_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        img = Image.open(image)

        # Crop
        left = int(request.POST['left'])
        top = int(request.POST['top'])
        right = int(request.POST['right'])
        bottom = int(request.POST['bottom'])
        img = img.crop((left, top, right, bottom))

        # Enhance brightness and contrast
        brightness = float(request.POST['brightness']) / 100.0
        contrast = float(request.POST['contrast']) / 100.0

        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness)

        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)

        # Rotate
        rotate_angle = float(request.POST['rotate'])
        img = img.rotate(rotate_angle, expand=True)

        # Generate edited image path and URL
        image_name = image.name.split('.')[0]  # Remove the file extension
        edited_image_name = f'edited_{image_name}.png'  # You can change the file extension to '.jpg' if needed
        edited_image_path = os.path.join('media', edited_image_name)
        edited_image_url = os.path.join('/media/', edited_image_name)

        img.save(edited_image_path, quality=90)  # Adjust the quality as desired

        return render(request, 'editor/result.html', {'edited_image_url': edited_image_url})

    return render(request, 'editor/edit_image.html')
