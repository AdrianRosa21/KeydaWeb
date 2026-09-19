import random

# Mapping of index to (Category, Exact Name)
items = {
    0: ('sala', 'Mesa Lateral'),
    1: ('personalizados', 'Banco de Trabajo a Medida'),
    2: ('cocina', 'Cocina Integral Blanca'),
    3: ('closets', 'Closet de Madera'),
    4: ('escritorios', 'Escritorio Rústico'),
    5: ('closets', 'Closet Abierto'),
    6: ('closets', 'Closet con Puertas Corredizas'),
    7: ('libreros', 'Librero Moderno'),
    8: ('bano', 'Gabinete de Baño'),
    9: ('libreros', 'Librero Industrial'),
    10: ('libreros', 'Estante Industrial'),
    11: ('personalizados', 'Estantería Comercial'),
    12: ('personalizados', 'Mostrador Comercial'),
    13: ('cocina', 'Cocina de Madera'),
    14: ('cocina', 'Isla de Cocina'),
    15: ('personalizados', 'Estación de Café'),
    16: ('libreros', 'Exhibidor de Libros'),
    17: ('cocina', 'Cocina Integral'),
    18: ('cocina', 'Cocina en L'),
    19: ('cocina', 'Cocina Moderna'),
    20: ('cocina', 'Cocina con Isla'),
    21: ('personalizados', 'Mostrador de Recepción'),
    22: ('personalizados', 'Muebles de Recepción'),
    23: ('cocina', 'Cocina Blanca'),
    24: ('mesas', 'Mesa de Noche'),
    25: ('cocina', 'Cocina Rústica'),
    26: ('bano', 'Mueble de Lavabo Flotante'),
    27: ('cocina', 'Cocina Exterior'),
    28: ('sala', 'Repisa Decorativa'),
    29: ('sala', 'Mueble para TV'),
    30: ('cocina', 'Carrito de Café'),
    31: ('libreros', 'Librero Tipo Escalera'),
    32: ('mesas', 'Mesas de Centro Nido'),
    33: ('sala', 'Mesa Consola'),
    34: ('mesas', 'Mesa Lateral'),
    35: ('sala', 'Repisa para Plantas'),
    36: ('mesas', 'Mesas de Centro Nido'),
    37: ('libreros', 'Librero Divisor'),
    38: ('libreros', 'Librero Divisor Alto'),
    39: ('mesas', 'Burós Blancos'),
    40: ('sala', 'Mesa de Centro'),
    41: ('mesas', 'Mesas de Noche Modernas'),
    42: ('escritorios', 'Estante para Impresora'),
    43: ('libreros', 'Librero Minimalista'),
    44: ('sala', 'Mueble para TV Estilo Industrial'),
    45: ('mesas', 'Burós de Madera'),
    46: ('sala', 'Banca para Ventana'),
    47: ('libreros', 'Librero Blanco'),
    48: ('mesas', 'Mesa de Comedor Larga'),
    49: ('bano', 'Mueble de Baño Suspendido'),
    50: ('bano', 'Gabinete de Baño con Espejo'),
    51: ('escritorios', 'Estaciones de Trabajo'),
    52: ('mesas', 'Mesa de Comedor Redonda'),
    53: ('escritorios', 'Escritorio Gamer'),
    54: ('sala', 'Panel para TV'),
    55: ('sala', 'Centro de Entretenimiento'),
    56: ('cocina', 'Cocina Integral Pequeña'),
    57: ('cocina', 'Cocina Minimalista'),
    58: ('bano', 'Gabinete de Baño Sencillo'),
    59: ('sala', 'Mesa de Centro Moderna'),
    60: ('cocina', 'Alacena de Madera'),
    61: ('sillas', 'Sillas de Comedor'),
    62: ('closets', 'Vestidor Abierto'),
    63: ('closets', 'Closet Abierto Moderno'),
    64: ('closets', 'Closet Abierto Blanco'),
    65: ('escritorios', 'Escritorio en L'),
    66: ('escritorios', 'Escritorio Negro'),
    67: ('escritorios', 'Escritorio Largo'),
    68: ('mesas', 'Comedor de Madera'),
    69: ('sillas', 'Silla de Comedor'),
    70: ('mesas', 'Mesa para Exteriores')
}

html_cards = []

# Generate consistent numbers for items to simulate catalog codes
random.seed(42)

for i in range(71):
    cat, exact_name = items[i]
    product_name = exact_name + ' ' + str(random.randint(100, 999))
    
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

