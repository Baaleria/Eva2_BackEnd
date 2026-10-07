from django.shortcuts import render

def inicio(request):
    #Aun no me convence asi, modificar!!
    contexto = {
        'generos': [
            {
                'id': 1,
                'nombre': 'Animación',
                'descripcion': 'Técnica artística y cinematográfica que consiste en dar ilusión de movimiento a imágenes, dibujos, objetos inanimados o modelos digitales mediante la proyección rápida de una sucesión de fotogramas.',
                'portada': 'images/portada_animacion.jfif',  
                'peliculas': [
                    {'nombre': 'South Park: Bigger, Longer & Uncut', 'edad': 'Adultos y mayores de 17 o 18 años', 'imagen': 'images/SouthPark.png'},
                    {'nombre': 'El Increiblemente Mundo De Jack', 'edad': 'Mayores de 7 años', 'imagen': 'images/Jack.jfif'},
                    {'nombre': 'El Cadaver De La Novia', 'edad': 'Mayores de 7 años', 'imagen': 'images/Novia.webp'}
                ]
            },
            {
                'id': 2,
                'nombre': 'Comedia Romántica',
                'descripcion': 'Género artístico y cinematográfico que mezcla una trama de amor con situaciones humorísticas, enredos y un tono ligero.',
                'portada': 'images/portada_comedia.jpg',
                'peliculas': [
                    {'nombre': 'A El No Le Gustas Tanto', 'edad': '+18', 'imagen': 'images/NoLeGustas.jpg'},
                    {'nombre': 'La Propuesta', 'edad': '+18', 'imagen': 'images/LaPropuesta.jpg'},
                    {'nombre': 'Como Perder Un Hombre En 10 Días', 'edad': '+18', 'imagen': 'images/PerderEn10Dias.jpg'}
                ]
            }
        ]
    }
    return render(request, 'Home/inicio.html', contexto)

def vista_animacion(request):
    return render(request, 'Home/vista_animacion.html')

def vista_comedia(request):
    return render(request, 'Home/vista_comedia.html')