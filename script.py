import os
import shutil
import random

source_dir = 'carpetaconimgs(noaddongit)'
dest_dir = 'imgs/nuevas'
os.makedirs(dest_dir, exist_ok=True)

images = [f for f in os.listdir(source_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
images.sort()

# Take first 9 for index carousels
carousel_names = [
    'carrusel_artesanal_1.jpg', 'carrusel_artesanal_2.jpg', 'carrusel_artesanal_3.jpg',
    'carrusel_extravagante_1.jpg', 'carrusel_extravagante_2.jpg', 'carrusel_extravagante_3.jpg',
    'carrusel_moderno_1.jpg', 'carrusel_moderno_2.jpg', 'carrusel_moderno_3.jpg'
]

for i in range(9):
    if i < len(images):
        src = os.path.join(source_dir, images[i])
        dst = os.path.join(dest_dir, carousel_names[i])
        shutil.copy2(src, dst)

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = index_html.replace('imgs/mueblesestiloartesanal.png', 'imgs/nuevas/carrusel_artesanal_1.jpg', 1)
index_html = index_html.replace('imgs/mueblesestiloartesanal.png', 'imgs/nuevas/carrusel_artesanal_2.jpg', 1)
index_html = index_html.replace('imgs/mueblesestiloartesanal.png', 'imgs/nuevas/carrusel_artesanal_3.jpg', 1)

index_html = index_html.replace('imgs/mueblesestiloextravagante.png', 'imgs/nuevas/carrusel_extravagante_1.jpg', 1)
index_html = index_html.replace('imgs/mueblesestiloextravagante.png', 'imgs/nuevas/carrusel_extravagante_2.jpg', 1)
index_html = index_html.replace('imgs/mueblesestiloextravagante.png', 'imgs/nuevas/carrusel_extravagante_3.jpg', 1)

index_html = index_html.replace('imgs/mueblesestilomoderno.png', 'imgs/nuevas/carrusel_moderno_1.jpg', 1)
index_html = index_html.replace('imgs/mueblesestilomoderno.png', 'imgs/nuevas/carrusel_moderno_2.jpg', 1)
index_html = index_html.replace('imgs/mueblesestilomoderno.png', 'imgs/nuevas/carrusel_moderno_3.jpg', 1)

index_html = index_html.replace('filter: grayscale(30%);', '')
index_html = index_html.replace('filter: grayscale(60%);', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Now handle the rest of the images for the catalog
catalog_images = images[9:]

categories = ['mesas', 'sillas', 'libreros', 'closets', 'cocina', 'bano', 'sala', 'escritorios', 'personalizados']

names = {
    'mesas': ['Mesa de Centro', 'Mesa de Comedor', 'Mesa Auxiliar', 'Mesa de Noche', 'Mesa Rústica', 'Mesa de Cristal'],
    'sillas': ['Silla de Comedor', 'Silla de Oficina', 'Sillón Individual', 'Silla Reclinable', 'Taburete', 'Silla Moderna'],
    'libreros': ['Librero de Pared', 'Estante Minimalista', 'Librero Clásico', 'Librero Industrial', 'Estante de Roble'],
    'closets': ['Closet Abierto', 'Armario de Melamina', 'Closet de Cedro', 'Armario Empotrado', 'Closet Moderno'],
    'cocina': ['Mueble de Cocina', 'Isla de Cocina', 'Alacena', 'Desayunador', 'Mueble Inferior'],
    'bano': ['Mueble de Lavabo', 'Gabinete de Baño', 'Estante para Baño', 'Mueble con Espejo'],
    'sala': ['Mueble para TV', 'Sofá Cama', 'Sofá 3 Plazas', 'Mesa de Sala', 'Seccional'],
    'escritorios': ['Escritorio Ejecutivo', 'Escritorio Minimalista', 'Mesa de Trabajo', 'Escritorio en L'],
    'personalizados': ['Mueble Especial', 'Diseño a Medida', 'Mueble Único', 'Pieza Exclusiva']
}

html_cards = []

for i, img_file in enumerate(catalog_images):
    cat = categories[i % len(categories)]
    cat_names = names[cat]
    product_name = random.choice(cat_names) + ' ' + str(random.randint(100, 999))
    
    new_img_name = f'cat_{i:03d}.jpg'
    src = os.path.join(source_dir, img_file)
    dst = os.path.join(dest_dir, new_img_name)
    shutil.copy2(src, dst)
    
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
end_marker = '</div>\n            </div>\n        </main>'
# Find positions
start_idx = catalogo_html.find(start_marker)
# Find the exact end of the grid, which is just before </main>
end_idx = catalogo_html.find('</main>', start_idx) - 27

new_html = catalogo_html[:start_idx + len(start_marker)] + '\\n' + cards_string + '\\n            ' + catalogo_html[end_idx:]

with open('catalogo.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Processed 9 images for index and {len(catalog_images)} images for catalog.")

