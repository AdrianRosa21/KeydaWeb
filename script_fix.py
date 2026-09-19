import random

mapping = {
    0: 'sala', 1: 'personalizados', 2: 'cocina', 3: 'closets', 4: 'escritorios',
    5: 'closets', 6: 'closets', 7: 'libreros', 8: 'bano', 9: 'libreros',
    10: 'libreros', 11: 'personalizados', 12: 'personalizados', 13: 'cocina', 14: 'cocina',
    15: 'personalizados', 16: 'libreros', 17: 'cocina', 18: 'cocina', 19: 'cocina',
    20: 'cocina', 21: 'personalizados', 22: 'personalizados', 23: 'cocina', 24: 'mesas',
    25: 'cocina', 26: 'bano', 27: 'cocina', 28: 'sala', 29: 'sala',
    30: 'cocina', 31: 'libreros', 32: 'mesas', 33: 'sala', 34: 'mesas',
    35: 'sala', 36: 'mesas', 37: 'libreros', 38: 'libreros', 39: 'mesas',
    40: 'sala', 41: 'mesas', 42: 'escritorios', 43: 'libreros', 44: 'sala',
    45: 'mesas', 46: 'sala', 47: 'libreros', 48: 'mesas', 49: 'bano',
    50: 'bano', 51: 'escritorios', 52: 'mesas', 53: 'escritorios', 54: 'sala',
    55: 'sala', 56: 'cocina', 57: 'cocina', 58: 'bano', 59: 'sala',
    60: 'cocina', 61: 'sillas', 62: 'closets', 63: 'closets', 64: 'closets',
    65: 'escritorios', 66: 'escritorios', 67: 'escritorios', 68: 'mesas', 69: 'sillas',
    70: 'mesas'
}

names = {
    'mesas': ['Mesa de Centro', 'Mesa de Comedor', 'Mesa Auxiliar', 'Mesa de Noche', 'Mesa Rústica', 'Mesa de Cristal'],
    'sillas': ['Silla de Comedor', 'Silla de Oficina', 'Sillón Individual', 'Silla Reclinable', 'Taburete', 'Silla Moderna'],
    'libreros': ['Librero de Pared', 'Estante Minimalista', 'Librero Clásico', 'Librero Industrial', 'Estante de Roble'],
    'closets': ['Closet Abierto', 'Armario de Melamina', 'Closet de Cedro', 'Armario Empotrado', 'Closet Moderno'],
    'cocina': ['Mueble de Cocina', 'Isla de Cocina', 'Alacena', 'Desayunador', 'Mueble Inferior'],
    'bano': ['Mueble de Lavabo', 'Gabinete de Baño', 'Estante para Baño', 'Mueble con Espejo'],
    'sala': ['Mueble para TV', 'Sofá Cama', 'Sofá 3 Plazas', 'Mesa de Sala', 'Seccional', 'Repisa Decorativa'],
    'escritorios': ['Escritorio Ejecutivo', 'Escritorio Minimalista', 'Mesa de Trabajo', 'Escritorio en L'],
    'personalizados': ['Mueble Comercial', 'Diseño a Medida', 'Mueble Único', 'Mueble de Exhibición', 'Proyecto Especial']
}

html_cards = []

for i in range(71):
    cat = mapping[i]
    cat_names = names[cat]
    product_name = random.choice(cat_names) + ' ' + str(random.randint(100, 999))
    
    new_img_name = f'cat_{i:03d}.jpg'
    dst = f'imgs/nuevas/{new_img_name}'
    
    label = "Baño" if cat == 'bano' else cat.capitalize()
    
    html = f'''
                <div class="col-md-4 col-sm-6 catalog-item" data-category="{cat}">
                    <div class="card card-custom h-100 text-center border-0 shadow-sm">
                        <img src="{dst}" class="card-img-top img-cover rounded-top" alt="{product_name}" style="height: 250px;">
                        <div class="card-body bg-blanco">
                            <h5 class="card-title text-primario fw-bold">{product_name}</h5>
                            <span class="product-label d-inline-block mt-2">{label}</span>
                        </div>
                    </div>
                </div>'''
    html_cards.append(html)

cards_string = ''.join(html_cards)

with open('catalogo.html', 'r', encoding='utf-8') as f:
    catalogo_html = f.read()

parts = catalogo_html.split('<div class="row g-4" id="catalog-container">')
head = parts[0] + '<div class="row g-4" id="catalog-container">'
tail = parts[1][parts[1].find('</main>') - 25:]

new_html = head + '\n' + cards_string + '\n            </div>\n        </div>\n    </main>\n\n    <!-- Footer -->' + catalogo_html.split('<!-- Footer -->')[1]

with open('catalogo.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

