// Funcionalidad para Catálogo y Comunes
document.addEventListener('DOMContentLoaded', () => {
    
    // Filtrado de Catálogo
    const filterButtons = document.querySelectorAll('.filter-btn');
    const catalogItems = document.querySelectorAll('.catalog-item');

    if (filterButtons.length > 0 && catalogItems.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                // Remover clase active de todos
                filterButtons.forEach(b => b.classList.remove('active'));
                // Agregar clase active al clickeado
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                catalogItems.forEach(item => {
                    if (filterValue === 'todos' || item.getAttribute('data-category') === filterValue) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                });
            });
        });
    }

    // Validación de formulario de Contacto / Cotizaciones
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                // If it's the contact form and validation passes, we simulate mailto
                if (form.id === 'contactForm' || form.id === 'cotizacionForm') {
                    event.preventDefault();
                    // Generate mailto link
                    const formData = new FormData(form);
                    let bodyText = '';
                    let subject = form.querySelector('[name="asunto"]') ? form.querySelector('[name="asunto"]').value : 'Solicitud desde sitio web';
                    
                    for (let [key, value] of formData.entries()) {
                        bodyText += `${key.toUpperCase()}: ${value}\n`;
                    }
                    
                    const mailtoLink = `mailto:contacto@muebleskeyda.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(bodyText)}`;
                    window.location.href = mailtoLink;
                    alert('Se abrirá su cliente de correo para enviar el mensaje.');
                }
            }
            form.classList.add('was-validated');
        }, false);
    });

});
