import os
import shutil
import random

source_dir = 'carpetaconimgs(noaddongit)'
dest_dir = 'imgs/nuevas'

images = [f for f in os.listdir(source_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
images.sort()
catalog_images = images[9:]

categories = ['mesas', 'sillas', 'libreros', 'closets', 'cocina', 'bano', 'sala', 'escritorios', 'personalizados']

names = {
    'mesas': ['Mesa de Centro', 'Mesa de Comedor', 'Mesa Auxiliar', 'Mesa de Noche', 'Mesa Rustica', 'Mesa de Cristal'],
    'sillas': ['Silla de Comedor', 'Silla de Oficina', 'Sillon Individual', 'Silla Reclinable', 'Taburete', 'Silla Moderna'],
    'libreros': ['Librero de Pared', 'Estante Minimalista', 'Librero Clasico', 'Librero Industrial', 'Estante de Roble'],
    'closets': ['Closet Abierto', 'Armario de Melamina', 'Closet de Cedro', 'Armario Empotrado', 'Closet Moderno'],
    'cocina': ['Mueble de Cocina', 'Isla de Cocina', 'Alacena', 'Desayunador', 'Mueble Inferior'],
    'bano': ['Mueble de Lavabo', 'Gabinete de Baño', 'Estante para Baño', 'Mueble con Espejo'],
    'sala': ['Mueble para TV', 'Sofa Cama', 'Sofa 3 Plazas', 'Mesa de Sala', 'Seccional'],
    'escritorios': ['Escritorio Ejecutivo', 'Escritorio Minimalista', 'Mesa de Trabajo', 'Escritorio en L'],
    'personalizados': ['Mueble Especial', 'Diseño a Medida', 'Mueble Unico', 'Pieza Exclusiva']
}

html_cards = []

for i, img_file in enumerate(catalog_images):
    cat = categories[i % len(categories)]
    cat_names = names[cat]
    product_name = random.choice(cat_names) + ' ' + str(random.randint(100, 999))
    
    new_img_name = f'cat_{i:03d}.jpg'
    dst = f'imgs/nuevas/{new_img_name}'
    
    html = f'''
                <div class="col-md-4 col-sm-6 catalog-item" data-category="{cat}">
                    <div class="card card-custom h-100 text-center border-0 shadow-sm">
                        <img src="{dst}" class="card-img-top img-cover rounded-top" alt="{product_name}" style="height: 250px;">
                        <div class="card-body bg-blanco">
                            <h5 class="card-title text-primario fw-bold">{product_name}</h5>
                            <span class="product-label d-inline-block mt-2">{cat.capitalize()}</span>
                        </div>
                    </div>
                </div>'''
    html_cards.append(html)

cards_string = ''.join(html_cards)

with open('catalogo.html', 'r', encoding='utf-8') as f:
    catalogo_html = f.read()

start_marker = '<div class="row g-4" id="catalog-grid">'
end_marker = '</div>\n        </div>\n    </main>'

start_idx = catalogo_html.find(start_marker)
end_idx = catalogo_html.find('</main>', start_idx)

# We want to replace from start_idx + len(start_marker) to end_idx - 14 (which is before </div></div>)
# Actually, the easiest is to split the string
parts = catalogo_html.split('<div class="row g-4" id="catalog-grid">')
head = parts[0] + '<div class="row g-4" id="catalog-grid">'
tail = parts[1][parts[1].find('</main>') - 25:] # keep the closing divs

new_html = head + '\n' + cards_string + '\n' + '            </div>\n        </div>\n    </main>\n\n    <!-- Footer -->' + catalogo_html.split('<!-- Footer -->')[1]

with open('catalogo.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

