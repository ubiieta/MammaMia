/*!
=========================================================
* FoodHut Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
});

new WOW().init();

function initMap() {
    var uluru = {lat: 43.4833534609328, lng: -3.8000910982811797};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('reserva-form');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', function (event) {
        const guests = document.getElementById('booktable-guests').value;
        const time = document.getElementById('booktable-time').value;
        const date = document.getElementById('booktable-date').value;
        const email = document.getElementById('booktable-email').value;

        if (!guests || !time || !date || !email) {
            event.preventDefault(); 
            errorMessage.style.display = 'block';
            errorMessage.textContent = 'Todos los campos son obligatorios.';
        } else {
            errorMessage.style.display = 'none'; 
        }
    });

    const masaSelect = document.getElementById('masa-select');
    const pizzaList = document.getElementById('pizza-list');

    masaSelect.addEventListener('change', function () {
        const masaId = this.value;

        if (masaId) {
            fetch(`/pizzas_por_masa/${masaId}/`, {
                headers: {
                    'x-requested-with': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                pizzaList.innerHTML = '';

                if (data.pizzas.length > 0) {
                    data.pizzas.forEach(pizza => {
                        const pizzaDiv = document.createElement('div');
                        pizzaDiv.classList.add('pizza-card');
                        pizzaDiv.innerHTML = `
                            <h4>${pizza.nombre}</h4>
                            <p>${pizza.descripcion}</p>
                            <p>Precio: €${pizza.precio}</p>
                        `;
                        pizzaList.appendChild(pizzaDiv);
                    });
                } else {
                    pizzaList.innerHTML = '<p>No hay pizzas disponibles para esta masa.</p>';
                }
            })
            .catch(error => {
                console.error('Error al cargar las pizzas:', error);
                pizzaList.innerHTML = '<p>Hubo un error al cargar las pizzas. Intenta de nuevo.</p>';
            });
        } else {
            pizzaList.innerHTML = '<p>Selecciona un tipo de masa para ver las pizzas disponibles.</p>';
        }
    });
});
