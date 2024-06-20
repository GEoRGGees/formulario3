from django.db import models

class SurveyResponse(models.Model):
    #1
    Nombre = models.CharField(max_length=100)
    email = models.EmailField()
    #2
    style_choices = [
        ('Elegante', 'Elegante'),
        ('Clasico', 'Clasico'),
        ('Juvenil', 'Juvenil'),
        ('Calida', 'Calida'),
        ('Moderna', 'Moderna'),
        ('Unica', 'Unica'),
        ('Minimalista', 'Minimalista'),
        ('Acogedora', 'Acogedora'),
        ('Masculino', 'Masculino'),
        ]
    
    style = models.TextField(default='')
    other_style = models.CharField(max_length=100, blank=True, null=True)
    #3
    bedroom_image = models.ImageField(upload_to='static/images', default='static/images/bedroom1.jpg')
    #4 sala
    hall_image = models.ImageField(upload_to='static/images', default='static/images/hall1.jpg')
    #5 comedor
    dining_room_image = models.ImageField(upload_to='static/images', default='static/images/dining_room1.jpg')
    #6 cocina
    kitchen_image = models.ImageField(upload_to='static/images', default='static/images/kitchen1.jpg')
    #7 ba;o
    bathroom_image = models.ImageField(upload_to='static/images', default='static/images/bathroom1.jpg')
    #8 facade
    facade_image = models.ImageField(upload_to='static/images', default='static/images/facade.jpg')
    #9 garden
    #garden_image = models.ImageField(upload_to='static/images', default='static/images/garden1.jpg')
    #10 studio
    studio_image = models.ImageField(upload_to='static/images', default='static/images/studio1.jpg')
    #11 studio
    #wood_images = models.JSONField(blank=True, null=True)#(upload_to='static/images', default='static/images/wood1.jpg')
    wood_images = models.ImageField(upload_to='static/images', default='static/images/wood1.jpg')
    
    #12 arte
    pcolor_image = models.JSONField(blank=True, null=True)
    #color_palette = models.CharField(max_length=100, blank=True, default='static/images/monochrome_black_gray.jpg' )
    
    #favorite_color = models.CharField(max_length=100, blank=True, null=True)
    
    #color_image = models.CharField(max_length=100, blank=True, null=True)  # Agregar este campo
    


    def __str__(self):
        return f'Response from {self.Nombre} ({self.email})'
