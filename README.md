# KeydaWeb

Proyecto web para "Muebles Keyda", un catálogo interactivo con diseño responsivo e identidad visual cálida y artesanal.

## Descripción
Este proyecto es la interfaz frontend para Muebles Keyda, donde se exhibe el catálogo de productos (mesas, sillas, libreros, closets, cocina, baño, sala, escritorios y personalizados), información sobre la empresa, formularios de cotización y contacto, y una sección para la descarga de su Sistema de Gestión.

## Tecnologías Utilizadas
- **HTML5:** Estructura semántica de las páginas.
- **CSS3:** Estilos personalizados, variables CSS para la identidad visual y adaptabilidad.
- **JavaScript Vanilla:** Lógica para filtros del catálogo y validación de formularios.
- **Bootstrap 5:** Framework CSS para cuadrículas y componentes adaptables.

## Estructura del Proyecto
```
KeydaWeb/
├── index.html          # Página principal
├── catalogo.html       # Catálogo de productos con filtros
├── servicios.html      # Servicios ofrecidos
├── nosotros.html       # Historia y valores
├── galeria.html        # Galería de proyectos
├── cotizaciones.html   # Formulario de cotizaciones
├── descarga.html       # Descarga del sistema y requisitos
├── contacto.html       # Información de contacto y mapa
├── css/
│   └── styles.css      # Hoja de estilos personalizados
├── js/
│   └── main.js         # Scripts de interacción y validación
└── imgs/               # Imágenes y recursos gráficos
```

## Funcionalidades Implementadas
- **Navegación completa:** Menú funcional que enlaza las 8 páginas principales.
- **Catálogo Dinámico:** Filtrado de productos por categoría utilizando JavaScript sin necesidad de recargar la página.
- **Validación de Formularios:** Validaciones HTML5 y JS personalizadas en Cotizaciones y Contacto (simula el envío a través de `mailto:` dado que el proyecto es exclusivamente estático).
- **Diseño Responsivo:** Completamente adaptable a móviles, tablets y pantallas grandes (Mobile-First).
- **Mapa interactivo:** Ubicación real incrustada en la página de Contacto mediante un Iframe de Google Maps.
- **Identidad Visual Consistente:** Paleta de colores aplicada a lo largo de todo el sitio usando variables CSS.

## Recursos Pendientes (A proveer por el equipo técnico)
En la página de **Descarga**, los siguientes archivos no se encuentran en el proyecto y los enlaces están deshabilitados temporalmente:
- `Instalador del Sistema de Gestión (.exe)`
- `Manual del Usuario (.pdf)`
- `Manual Técnico (.pdf)`
- `Especificaciones Técnicas exactas del equipo requerido`

## Ejecución Local
Al ser un proyecto de tipo sitio web estático puro, solo necesitas un navegador web:
1. Clona el repositorio en tu máquina local.
2. Abre el archivo `index.html` haciendo doble clic sobre él o arrastrándolo a tu navegador de preferencia.
3. Puedes navegar usando los enlaces en la barra de navegación superior.

## Despliegue en Vercel
El proyecto está optimizado y preparado para un despliegue automático con Vercel.
1. Crea una cuenta en [Vercel](https://vercel.com).
2. Conecta Vercel con tu repositorio de GitHub donde se encuentra este proyecto.
3. Importa el proyecto.
4. El framework preset puede dejarse como `Other` y no requiere comandos de Build (Build Command: vacío) o Output Directory (Output Directory: vacío / predeterminado al root).
5. Vercel te dará una URL en vivo (ej. `muebles-keyda.vercel.app`) donde el sitio estará completamente operativo.
