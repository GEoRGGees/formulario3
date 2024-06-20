from django import forms
from .models import SurveyResponse

class Step1Form(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = ['Nombre', 'email']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'input-field'}),
            'email': forms.EmailInput(attrs={'class': 'input-field'}),
        }
        labels = {
            'Nombre': 'Nombre',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super(Step1Form, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.label = field.label.replace(':', '')  # Elimina los dos puntos de las etiquetas
            self.fields[field_name].widget.attrs.update({
                'class': 'input-field step1-field'
            })
            
class Step2Form(forms.Form):
    STYLE_CHOICES = [
        ('Elegante', 'Elegante'),
        ('Clásico', 'Clásico'),
        ('Juvenil', 'Juvenil'),
        ('Cálida', 'Cálida'),
        ('Moderna', 'Moderna'),
        ('Única', 'Única'),
        ('Minimalista', 'Minimalista'),
        ('Acogedora', 'Acogedora'),
        ('Masculino', 'Masculino'),
    ]
    style = forms.MultipleChoiceField(
        choices=STYLE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='¿Cómo describirías tu espacio ideal en 3 palabras? (Escoge 3 opciones)'
    )
    other_style = forms.CharField(
        required=False,
        max_length=100,
        label='Otra (especificar)',
        widget=forms.TextInput(attrs={'placeholder': 'Escribe otra palabra si no se encuentra tu espacio ideal'})
    )

class Step3Form(forms.Form):
    BEDROOM_CHOICES = [
        ('bedroom1.jpg', 'Bedroom 1'),
        ('bedroom2.jpg', 'Bedroom 2'),
        ('bedroom3.jpg', 'Bedroom 3'),
        ('bedroom4.jpg', 'Bedroom 4'),
        ('bedroom5.jpg', 'Bedroom 5'),
    ]
    bedroom_image = forms.ChoiceField(
        choices=BEDROOM_CHOICES,
        widget=forms.RadioSelect,
        label='Cual recámara te gusta mas? '
    )
    
class Step4Form(forms.Form):
    HALL_CHOICES = [
        ('hall1.jpg', 'Hall 1'),
        ('hall2.jpg', 'Hall 2'),
        ('hall3.jpg', 'Hall 3'),
        ('hall4.jpg', 'Hall 4'),
        ('hall5.jpg', 'Hall 5'),
    ]
    hall_image = forms.ChoiceField(
        choices=HALL_CHOICES,
        widget=forms.RadioSelect,
        label='Cual sala te gusta mas? '
    )
    
class Step5Form(forms.Form):
    DINIG_ROOM_CHOICES = [
        ('dining_room1.jpg', 'Dining_room 1'),
        ('dining_room2.jpg', 'Dining_room 2'),
        ('dining_room3.jpg', 'Dining_room 3'),
        ('dining_room4.jpg', 'Dining_room 4'),
        ('dining_room5.jpg', 'Dining_room 5'),
    ]
    dining_room_image = forms.ChoiceField(
        choices=DINIG_ROOM_CHOICES,
        widget=forms.RadioSelect,
        label='Cual comedor te gusta mas? '
    )
    
class Step6Form(forms.Form):
    KITCHEN_CHOICES = [
        ('kitchen1.jpg', 'Kitchen 1'),
        ('kitchen2.jpg', 'Kitchen 2'),
        ('kitchen3.jpg', 'Kitchen 3'),
        ('kitchen4.jpg', 'Kitchen 4'),
        ('kitchen5.jpg', 'Kitchen 5'),
    ]
    kitchen_image = forms.ChoiceField(
        choices=KITCHEN_CHOICES,
        widget=forms.RadioSelect,
        label='Cual cocina te gusta mas? '
    )
    
    
class Step7Form(forms.Form):
    BATHROOM_CHOICES = [
        ('bathroom1.jpg', 'Bathroom 1'),
        ('bathroom2.jpg', 'Bathroom 2'),
        ('bathroom3.jpg', 'Bathroom 3'),
        ('bathroom4.jpg', 'Bathroom 4'),
        ('bathroom5.jpg', 'Bathroom 5'),
    ]
    bathroom_image = forms.ChoiceField(
        choices=BATHROOM_CHOICES,
        widget=forms.RadioSelect,
        label='Cual baño te gusta mas? '
    )
    
class Step8Form(forms.Form):
    FACADE_CHOICES = [
        ('facade1.jpg', 'Facade 1'),
        ('facade2.jpg', 'Facade 2'),
        ('facade3.jpg', 'Facade 3'),
        ('facade4.jpg', 'Facade 4'),
        ('facade5.jpg', 'Facade 5'),
    ]
    facade_image = forms.ChoiceField(
        choices=FACADE_CHOICES,
        widget=forms.RadioSelect,
        label='Cual fachada te gusta mas? '
    )
    
#class Step9Form(forms.Form):
#    GARDEN_CHOICES = [
#        ('garden1.jpg', 'Garden 1'),
#        ('garden2.jpg', 'Garden 2'),
#        ('garden3.jpg', 'Garden 3'),
#        ('garden4.jpg', 'Garden 4'),
#        ('garden5.jpg', 'Garden 5'),
#    ]
#    garden_image = forms.ChoiceField(
#        choices=GARDEN_CHOICES,
#        widget=forms.RadioSelect,
#        label='Cual jardin te gusta mas? '
#    )
    
    
    
class Step10Form(forms.Form):
    STUDIO_CHOICES = [
        ('studio1.jpg', 'Studio 1'),
        ('studio2.jpg', 'Studio 2'),
        ('studio3.jpg', 'Studio 3'),
        ('studio4.jpg', 'Studio 4'),
        ('studio5.jpg', 'Studio 5'),
    ]
    studio_image = forms.ChoiceField(
        choices=STUDIO_CHOICES,
        widget=forms.RadioSelect,
        label='Cual estudio te gusta mas? '
    )
    
#class Step11Form(forms.Form):
#    WOOD_CHOICES = [
#        ('wood1.jpg', 'Wood 1'),
#        ('wood2.jpg', 'Wood 2'),
#        ('wood3.jpg', 'Wood 3'),
#        ('wood4.jpg', 'Wood 4'),
#        ('wood5.jpg', 'Wood 5'),
#        ('wood6.jpg', 'Wood 6'),
#    ]
#    wood_images = forms.MultipleChoiceField(
#        choices=WOOD_CHOICES,
#        widget=forms.CheckboxSelectMultiple,
#        label='Cual de estas maderas te gusta mas? (Selecciona 2)',
#        required=True,
#    )
class Step11Form(forms.Form):
    WOOD_CHOICES = [
        ('wood1.jpg', 'Wood 1'),
        ('wood2.jpg', 'Wood 2'),
        ('wood3.jpg', 'Wood 3'),
        ('wood4.jpg', 'Wood 4'),
        ('wood5.jpg', 'Wood 5'),
        ('wood6.jpg', 'Wood 6'),
    ]
    wood_images = forms.ChoiceField(
        choices=WOOD_CHOICES,
        widget=forms.RadioSelect,
        label='Cual madera te gusta mas? '
    )
    
class Step12Form(forms.Form):
    PCOLOR_CHOICES = [
        ('black.jpg', 'Negro'),
        ('white.jpg', 'Blanco'),
        ('cold_gray.jpg', 'Gris frio'),
        ('warm_gray.jpg', 'Gris calido'),
        ('brown.jpg', 'Brown'),
        ('green.jpg', 'Verde'),
        ('bluish_green.jpg', 'Verde azulado'),
        ('blue.jpg', 'Blue'),
        ('beige.jpg', 'Beige'),
        ('orange.jpg', 'Naranja'),
        ('yellow.jpg', 'Amarillo'),
        ('pink.jpg', 'Pink'),
        ('purple.jpg', 'Morado'),
        ('mamey.jpg', 'Mamey'),
    ]
    pcolor_image = forms.MultipleChoiceField(
        choices=PCOLOR_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Elige 4 colores que te gustaria ver en tu casa? ',
        required=True,
    )
    
#class Step12Form(forms.Form):
#    COLOR_PALETTE_CHOICES = [
#        ('monochrome_black_gray', 'Colores monocromáticos (Negro y Gris)'),
#        ('monochrome_beige_subtones', 'Colores monocromáticos (Beige y Subtonos)'),
#        ('monochrome_with_tone', 'Monocromáticos con un tono de color'),
#        ('colorful', 'Colorido'),
#    ]
#    color_palette = forms.ChoiceField(
#        choices=COLOR_PALETTE_CHOICES,
#        widget=forms.RadioSelect,
#        label='¿Qué paleta de colores prefieres?'
#    )


#class Step13Form(forms.Form):
#    FAVORITE_COLOR_CHOICES = [
#        ('red', 'Rojo'),
#        ('blue', 'Azul'),
#        ('green', 'Verde'),
#        ('yellow', 'Amarillo'),
#    ]
#    favorite_color = forms.ChoiceField(
#        choices=FAVORITE_COLOR_CHOICES,
#        widget=forms.RadioSelect,
#        label='¿Qué color te gusta más?'
#    )

#class Step14Form(forms.Form):
#    ANOTHER_COLOR_CHOICES = [
#        ('pink', 'Rosa'),
#        ('orange', 'Naranja'),
#        ('purple', 'Púrpura'),
#        ('brown', 'Marrón'),
#    ]
#    another_color = forms.ChoiceField(
#        choices=ANOTHER_COLOR_CHOICES,
#        widget=forms.RadioSelect,
#        label='¿Qué otro color te gusta más?'
#    )
