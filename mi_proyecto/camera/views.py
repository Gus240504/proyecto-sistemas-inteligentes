from django.shortcuts import render
from .models import CameraStream

def index(request):
    # Lógica para obtener la transmisión de la cámara
    camera_stream = CameraStream.objects.first()  # Ejemplo: Obtener la primera transmisión de la cámara

    # Renderizar la plantilla con la transmisión de la cámara
    return render(request, 'camera/index.html', {'camera_stream': camera_stream})

from django.shortcuts import render

def camera_view(request):
    ip_address = '192.168.1.100'  # Reemplaza esto con la dirección IP de tu dispositivo Android
    port = '4747'  # Reemplaza esto con el puerto de tu dispositivo Android
    return render(request, 'camera.html', {'ip_address': ip_address, 'port': port})