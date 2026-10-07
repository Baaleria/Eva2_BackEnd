console.log("¡JavaScript cargado correctamente en el Proyecto de Películas!");
document.addEventListener("DOMContentLoaded", function() {
    const imagenesPeliculas = document.querySelectorAll('.card-img-top');
    imagenesPeliculas.forEach(imagen => {
        imagen.addEventListener('click', function() {
            const nombrePeli = this.getAttribute('alt');
            alert("¡Excelente elección! Preparando para ver: " + nombrePeli);
        });
    });
});