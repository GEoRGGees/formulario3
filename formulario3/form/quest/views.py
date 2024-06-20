
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import Step1Form, Step2Form, Step3Form, Step4Form, Step5Form, Step6Form, Step7Form, Step8Form, Step10Form, Step11Form, Step12Form
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import tempfile
from .models import SurveyResponse
import numpy as np
import cv2
import os
from django.http import FileResponse


def resize_image(image, size):
    return cv2.resize(image, size)

def save_session_data(request, step, form):
    request.session[step] = form.cleaned_data
    print(f"{step} Data:", form.cleaned_data)

def step1_view(request):
    if request.method == 'POST':
        form = Step1Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step1_data', form)
            return redirect('step2')
    else:
        form = Step1Form()
    return render(request, 'quest/step1.html', {'form': form})

def step2_view(request):
    if request.method == 'POST':
        form = Step2Form(request.POST)
        if form.is_valid():
            style = form.cleaned_data['style']
            other_style = form.cleaned_data.get('other_style')
            if len(style) == 3 or (len(style) == 2 and other_style):
                save_session_data(request, 'step2_data', form)
                return redirect('step3')
            else:
                form.add_error('style', 'Por favor selecciona exactamente 3 palabras o 2 palabras y una adicional.')
        else:
            print("Step 2 Form is invalid")
            print(form.errors)
    else:
        form = Step2Form()
    return render(request, 'quest/step2.html', {'form': form})

def step3_view(request):
    if request.method == 'POST':
        form = Step3Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step3_data', form)
            return redirect('step4')
    else:
        form = Step3Form()
    return render(request, 'quest/step3.html', {'form': form})

def step4_view(request):
    if request.method == 'POST':
        form = Step4Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step4_data', form)
            return redirect('step5')
        else:
            print("Step 4 Form is invalid")
            print(form.errors)
    else:
        form = Step4Form()
    return render(request, 'quest/step4.html', {'form': form})

def step5_view(request):
    if request.method == 'POST':
        form = Step5Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step5_data', form)
            return redirect('step6')
        else:
            print("Step 5 Form is invalid")
            print(form.errors)
    else:
        form = Step5Form()
    return render(request, 'quest/step5.html', {'form': form})

def step6_view(request):
    if request.method == 'POST':
        form = Step6Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step6_data', form)
            return redirect('step7')
        else:
            print("Step 6 Form is invalid")
            print(form.errors)
    else:
        form = Step6Form()
    return render(request, 'quest/step6.html', {'form': form})

def step7_view(request):
    if request.method == 'POST':
        form = Step7Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step7_data', form)
            return redirect('step8')
        else:
            print("Step 7 Form is invalid")
            print(form.errors)
    else:
        form = Step7Form()
    return render(request, 'quest/step7.html', {'form': form})

def step8_view(request):
    if request.method == 'POST':
        form = Step8Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step8_data', form)
            return redirect('step10')
        else:
            print("Step 8 Form is invalid")
            print(form.errors)
    else:
        form = Step8Form()
    return render(request, 'quest/step8.html', {'form': form})

def step10_view(request):
    if request.method == 'POST':
        form = Step10Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step10_data', form)
            return redirect('step11')
        else:
            print("Step 10 Form is invalid")
            print(form.errors)
    else:
        form = Step10Form()
    return render(request, 'quest/step10.html', {'form': form})


def step11_view(request):
    if request.method == 'POST':
        form = Step11Form(request.POST)
        if form.is_valid():
            save_session_data(request, 'step11_data', form)
            return redirect('step12')
        else:
            print("Step 11 Form is invalid")
            print(form.errors)
    else:
        form = Step11Form()
    return render(request, 'quest/step11.html', {'form': form})

def step12_view(request):
    if request.method == 'POST':
        form = Step12Form(request.POST)
        if form.is_valid():
            wood_images = form.cleaned_data['pcolor_image']
            if len(wood_images) == 4:
                save_session_data(request, 'step12_data', form)
                return redirect('done')
            else:
                form.add_error('pcolor_image', 'Por favor, seleccione 4 imagenes.')
        else:
            print("Step 12 Form is invalid")
            print(form.errors)
    else:
        form = Step12Form()
    return render(request, 'quest/step12.html', {'form': form})



def done_view(request):
    step1_data = request.session.get('step1_data')
    step2_data = request.session.get('step2_data')
    step3_data = request.session.get('step3_data')
    step4_data = request.session.get('step4_data')
    step5_data = request.session.get('step5_data')
    step6_data = request.session.get('step6_data')
    step7_data = request.session.get('step7_data')
    step8_data = request.session.get('step8_data')
    step10_data = request.session.get('step10_data')
    step11_data = request.session.get('step11_data')
    step12_data = request.session.get('step12_data')


    if step1_data and step2_data and step3_data and step4_data and step5_data and step6_data and step7_data and step8_data and step10_data and step11_data :
        Nombre = step1_data['Nombre']
        email = step1_data['email']
        style = ', '.join(step2_data['style'])
        other_style = step2_data.get('other_style', '')
        bedroom_image = step3_data['bedroom_image']
        hall_image = step4_data['hall_image']
        dining_room_image = step5_data['dining_room_image']
        kitchen_image = step6_data['kitchen_image']
        bathroom_image = step7_data['bathroom_image']
        facade_image = step8_data['facade_image']
        studio_image = step10_data['studio_image']
        wood_images = step11_data['wood_images']
        pcolor_image = step12_data['pcolor_image']
        
        

        # Construir las rutas absolutas de las imágenes
        bedroom_image_path = os.path.join(settings.BASE_DIR, 'quest/static/images', bedroom_image)
        hall_image_path = os.path.join(settings.BASE_DIR, 'quest/static/images', hall_image)
        dining_room_path = os.path.join(settings.BASE_DIR, 'quest/static/images', dining_room_image)
        kitchen_path = os.path.join(settings.BASE_DIR, 'quest/static/images', kitchen_image)
        bathroom_path = os.path.join(settings.BASE_DIR, 'quest/static/images', bathroom_image)
        facade_path = os.path.join(settings.BASE_DIR, 'quest/static/images', facade_image)
        
        studio_path = os.path.join(settings.BASE_DIR, 'quest/static/images', studio_image)
        wood_image_paths = os.path.join(settings.BASE_DIR, 'quest/static/images', wood_images)
        
        
        pcolor_image_paths = [os.path.join(settings.BASE_DIR, 'quest/static/images', img) for img in pcolor_image]
       
        # Cargar las imágenes usando OpenCV
        bedroom_img = cv2.imread(bedroom_image_path)
        hall_img = cv2.imread(hall_image_path)
        dining_room_img = cv2.imread(dining_room_path)
        kitchen_img = cv2.imread(kitchen_path)
        bathroom_img = cv2.imread(bathroom_path)
        facade_img = cv2.imread(facade_path)
        studio_img = cv2.imread(studio_path)
        wood_imgs = cv2.imread(wood_image_paths)
        pcolor_imgs = [cv2.imread(img_path) for img_path in pcolor_image_paths]
        

        if any(img is None for img in [bedroom_img, hall_img, dining_room_img, kitchen_img, bathroom_img, facade_img, studio_img, wood_imgs]) or any(img is None for img in pcolor_imgs)  is None:
            print("Error: Una o más imágenes no se pudieron cargar.")
            return redirect('step1')

        # Redimensionar las imágenes
        size = (250, 350)
        bedroom_img_resized = resize_image(bedroom_img, size)
        hall_img_resized = resize_image(hall_img, size)
        dining_room_img_resized = resize_image(dining_room_img, size)
        kitchen_img_resized = resize_image(kitchen_img, size)
        bathroom_img_resized = resize_image(bathroom_img, size)
        facade_img_resized = resize_image(facade_img, size)
        studio_img_resized = resize_image(studio_img, size)
        wood_img_resized = resize_image(wood_imgs, size) 
        pcolor_img_resized = [resize_image(img, size) for img in pcolor_imgs]
        

        # Combinar las imágenes en una cuadrícula de 2 filas y 4 columnas
        row1 = np.hstack((bedroom_img_resized, hall_img_resized, dining_room_img_resized, kitchen_img_resized))
        row2 = np.hstack((bathroom_img_resized, facade_img_resized, studio_img_resized, wood_img_resized))
        row21 = np.hstack((pcolor_img_resized[0], pcolor_img_resized[1], pcolor_img_resized[2], pcolor_img_resized[3]))
        
        
        combinado = np.vstack((row1, row2, row21))

        # Guardar la imagen combinada
        combined_image_path = os.path.join(settings.BASE_DIR, 'quest/static/images', 'combinado.jpg')
        cv2.imwrite(combined_image_path, combinado)
        
        # Crear el PDF en un archivo temporal
        logo_path = os.path.join(settings.BASE_DIR, 'quest/static/images/KREALIS.png')  # Path to your logo
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            pdf_path = tmp_file.name
            c = canvas.Canvas(pdf_path, pagesize=letter)
            width, height = letter

            # Register fonts
            pdfmetrics.registerFont(TTFont('CeraPro', os.path.join(settings.BASE_DIR, 'quest/static/fonts/CeraPro-Light.ttf')))
            pdfmetrics.registerFont(TTFont('CeraPro-Bold', os.path.join(settings.BASE_DIR, 'quest/static/fonts/CeraPro-Bold.ttf')))

            # Set background color
            c.setFillColorRGB(0.35, 0.18, 0.54)
            c.rect(0, 0, width, height, fill=True)

            # Draw the logo
            c.drawImage(logo_path, width/2 - 100, height - 90, width=200, height=45, mask='auto')

            # Add text
            c.setFont("CeraPro-Bold", 16)
            c.setFillColorRGB(1, 1, 1)
            c.drawCentredString(width / 2, height - 125, "¡Gracias por responder nuestra encuesta!")

            c.setFont("CeraPro", 12)
            c.drawCentredString(width / 2, height - 160, f'Nombre:   {Nombre}')
            c.drawCentredString(width / 2, height - 200, f"Email:   {email}")
            c.drawCentredString(width / 2, height - 240, f'Estilo:   {style}')
            c.drawCentredString(width / 2, height - 280, f'Otro estilo:   {other_style}')

            # Add the combined image era 700
            c.drawImage(combined_image_path, width / 2 - 200, height - 700, width=400, height=400)

            c.save()

        survey_response = SurveyResponse(
            Nombre=Nombre,
            email=email,
            style=style,
            other_style=other_style,
            bedroom_image=bedroom_image,
            hall_image=hall_image,
            dining_room_image=dining_room_image,
            kitchen_image=kitchen_image,
            bathroom_image=bathroom_image,
            facade_image=facade_image,
            studio_image=studio_image,
            wood_images=wood_images,
            pcolor_image=pcolor_image,
        )
        survey_response.save()

        print("Survey Response Saved:", survey_response)
        
        # Enviar el PDF por correo electrónico a info@krealis.mx
        subject = "Formulario Krealis"
        message = "Formulario respondido por " + Nombre
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ["info@krealis.mx"]

        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )
        email_message.attach_file(pdf_path)

        try:
            email_message.send()
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {e}")
            return render(request, 'quest/done.html', {
                'Nombre': Nombre,
                'email': email,  # Usar la variable email correcta
                'style': style,
                'other_style': other_style,
                'combined_image': 'images/combinado.jpg',
                'error': f"Failed to send email: {e}"
            })
        
        

        return render(request, 'quest/done.html', {
            'Nombre': Nombre,
            'email': email,
            'style': style,
            'other_style': other_style,
            'bedroom_image': bedroom_image,
            'hall_image': hall_image,
            'dining_room_image': dining_room_image,
            'kitchen_image': kitchen_image,
            'bathroom_image': bathroom_image,
            'facade_image': facade_image,
            'studio_image': studio_image,
            'wood_images': wood_images,
            'pcolor_image': pcolor_image,
            'combined_image': 'images/combinado.jpg'
        })
    print("Redirecting to step1 due to missing session data")
    return redirect('step1')
