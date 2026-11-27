# EduForge Web

Sitio estático bilingüe de EduForge Studio. El español es el idioma inicial.
El contenido y las rutas se generan desde `build.py`. Los estilos, el selector de tema
y la galería están en `site/assets/`. Las imágenes del editor provienen de las
capturas de verificación de Studio.

## Desarrollo local

Desde este directorio, con Python 3.11 o posterior:

```powershell
python build.py
python -m http.server 8000 --bind 127.0.0.1 --directory site
```

Abre http://127.0.0.1:8000/. También puedes abrir `site/index.html` directamente.
Regenera las páginas al editar los textos y conserva los HTML generados en Git. Las guías bilingües viven en `guides.py`.

## Diseño

La identidad usa un fondo grafito, violeta como acento, tipografía del sistema y
una escala fluida. Los componentes comparten variables CSS para ambos temas.
La galería enlaza las capturas directamente cuando JavaScript está desactivado.
El tema usa la preferencia del sistema y guarda la selección en el navegador
cuando el almacenamiento local está disponible.

## Publicación

`site/` es la raíz publicable. En Cloudflare Pages puede configurarse como
directorio de salida. En GitHub Pages puede cargarse como artefacto mediante
Actions. Las rutas relativas admiten despliegue bajo un subdirectorio.

Las páginas de descargas consultan la API pública del canal
`hans-07/eduforge-releases` sin token. Los enlaces de instaladores aparecen
cuando una release pública incluye el EXE y su archivo SHA-256. El historial
completo de GitHub sigue accesible incluso si la API falla.
Confirma los canales de contacto y apoyo, y revisa los borradores legales antes
de publicar el sitio.
