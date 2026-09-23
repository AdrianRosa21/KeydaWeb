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
        
        // Validación personalizada para correos y descripciones
        const emailInputs = form.querySelectorAll('input[type="email"]');
        const descInputs = form.querySelectorAll('textarea[name="descripcion"]');
        
        emailInputs.forEach(input => {
            input.addEventListener('input', function() {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(this.value)) {
                    this.setCustomValidity('Por favor ingrese un correo válido.');
                    const feedback = this.nextElementSibling;
                    if (feedback && feedback.classList.contains('invalid-feedback')) {
                        feedback.textContent = 'Debe ser un correo electrónico válido (ej: nombre@dominio.com).';
                    }
                } else {
                    this.setCustomValidity('');
                }
            });
        });

        descInputs.forEach(input => {
            input.addEventListener('input', function() {
                if (this.value.trim().length < 15) {
                    this.setCustomValidity('Descripción muy corta.');
                    const feedback = this.nextElementSibling;
                    if (feedback && feedback.classList.contains('invalid-feedback')) {
                        feedback.textContent = 'Bríndanos un poco más de detalles (mínimo 15 caracteres) para ayudarte mejor.';
                    }
                } else {
                    this.setCustomValidity('');
                }
            });
        });

        form.addEventListener('submit', function (event) {
            
            // Forzar revisión manual antes del envío
            emailInputs.forEach(i => i.dispatchEvent(new Event('input')));
            descInputs.forEach(i => i.dispatchEvent(new Event('input')));

            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                if (form.id === 'contactForm' || form.id === 'cotizacionForm') {
                    event.preventDefault();
                    // Generate mailto link
                    const formData = new FormData(form);
                    let bodyText = '';
                    let subject = form.querySelector('[name="asunto"]') ? form.querySelector('[name="asunto"]').value : (form.id === 'cotizacionForm' ? 'Nueva solicitud de cotización' : 'Solicitud desde sitio web');
                    
                    for (let [key, value] of formData.entries()) {
                        bodyText += key.toUpperCase() + ': ' + value + '\n';
                    }
                    
                    const mailtoLink = 'mailto:muebleskeydasv@gmail.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(bodyText);
                    window.location.href = mailtoLink;
                    alert('Se abrirá su cliente de correo para enviar el mensaje.');
                }
            }
            form.classList.add('was-validated');
        }, false);
    });

});
