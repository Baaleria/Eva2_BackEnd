from django.shortcuts import render

def inicio(request):

    contexto = {
        'generos': [
            {
                'id': 1,
                'nombre': 'Animación',
                'descripcion': 'Técnica artística y cinematográfica que consiste en dar ilusión de movimiento a imágenes, dibujos, objetos inanimados o modelos digitales mediante la proyección rápida de una sucesión de fotogramas.',
                'portada': 'images/portada_animacion.jfif'  
            },
            {
                'id': 2,
                'nombre': 'Comedia Romántica',
                'descripcion': 'Género artístico y cinematográfico que mezcla una trama de amor con situaciones humorísticas, enredos y un tono ligero.',
                'portada': 'images/portada_comedia.jpg'
            }
        ]
    }
    return render(request, 'Home/inicio.html', contexto)

def vista_genero(request):
    contexto = {
        'generos': [
            {
                'id': 1,
                'nombre': 'Animación',
                'descripcion': 'Técnica artística y cinematográfica que consiste en dar ilusión de movimiento a imágenes, dibujos, objetos inanimados o modelos digitales mediante la proyección rápida de una sucesión de fotogramas.',
                'portada': 'images/portada_animacion.jfif',  
                'peliculas': [
                    {'nombre': 'South Park: Bigger, Longer & Uncut', 'imagen': 'images/SouthPark.png'},
                    {'nombre': 'El Increiblemente Mundo De Jack' , 'imagen': 'images/Jack.jfif'},
                    {'nombre': 'El Cadaver De La Novia', 'imagen': 'images/Novia.webp'}
                ]
            },
            {
                'id': 2,
                'nombre': 'Comedia Romántica',
                'descripcion': 'Género artístico y cinematográfico que mezcla una trama de amor con situaciones humorísticas, enredos y un tono ligero.',
                'portada': 'images/portada_comedia.jpg',
                'peliculas': [
                    {'nombre': 'A El No Le Gustas Tanto', 'imagen': 'images/NoLeGustas.jpg'},
                    {'nombre': 'La Propuesta', 'imagen': 'images/LaPropuesta.jpg'},
                    {'nombre': 'Como Perder Un Hombre En 10 Días', 'imagen': 'images/PerderEn10Dias.jpg'}
                ]
            }
        ]
    }
    return render(request, 'Home/vista_genero.html', contexto)

def vista_animacion(request):
        animacion= {
            'peliculas': [
                {'nombre': 'South Park: Bigger, Longer & Uncut','edad' :'Adultos y mayores de 17 o 18 años', 'portada': 'images/SouthPark.png'},
                {'nombre': 'El Increiblemente Mundo De Jack','edad' :'Mayores de 7 años', 'portada': 'images/Jack.jfif'},
                {'nombre': 'El Cadaver De La Novia','edad' :'Mayores de 7 años', 'portada': 'images/Novia.webp'}
            ]
        }
        return render(request, 'Home/vista_animacion.html', animacion)

def vista_comedia(request):
    comedia= {
                'peliculas': [
                    {'nombre': 'A El No Le Gustas Tanto','edad' :'Mayores de 13 años', 'portada': 'images/NoLeGustas.jpg'},
                    {'nombre': 'La Propuesta','edad' :'Mayores de 12 a 13 años', 'portada': 'images/LaPropuesta.jpg'},
                    {'nombre': 'Cómo perder a un hombre en 10 días','edad' :'Mayores de 13 años', 'portada': 'images/PerderEn10Dias.jpg'}
                ]
            }
    return render(request, 'Home/vista_comedia.html', comedia)
    