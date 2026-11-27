from pathlib import Path
from html import escape

from guides import GUIDES, PHOTOS, SLUGS

ROOT = Path(__file__).resolve().parent / "site"
SCREENSHOTS = ("design.png", "blocks.png", "blocks-dark.png", "campus-demo.png")
PAGES = ("inicio", "descargas", "tutoriales", "sobre", "apoyar", "soporte", "legal")
NAV = {
    "es": ("Inicio", "Descargas", "Documentación", "Sobre EduForge", "Apoyar", "Soporte", "Legal"),
    "en": ("Home", "Downloads", "Docs", "About", "Support the project", "Help", "Legal"),
}
HOME = {
    "es": {
        "title": "Crea software.<br><em>Aprende construyendo.</em>",
        "intro": "Diseña interfaces, conecta bloques y convierte tus ideas en aplicaciones funcionales. Un estudio visual gratuito para estudiantes de cualquier carrera.",
        "download": "Ir a descargas", "learn": "Leer la documentación", "skip": "Ir al contenido",
        "values": ("Gratis", "Funciona offline", "Sin cuenta"),
        "tabs": ("Diseño", "Lógica", "Modo oscuro", "Campus Reserva"),
        "captions": ("Lienzo de diseño e inspector de EduForge Studio", "Editor de eventos y bloques de EduForge Studio", "Editor de bloques en inglés con modo oscuro y un proyecto de inventario de ejemplo", "Campus Reserva en la vista previa de EduForge Studio"),
        "flow": "De la idea a la aplicación",
        "features": (("Diseña en el lienzo", "Añade campos, botones e imágenes. Organiza las capas y ajusta la interfaz desde el inspector."),
                     ("Conecta bloques", "Define eventos y acciones, trabaja con tablas y prueba el resultado desde el editor."),
                     ("Exporta tu aplicación", "Genera HTML independiente o un ejecutable de 64 bits para Windows.")),
        "demo": "Explora Campus Reserva",
        "demo_text": "Abre el ejemplo incluido y elige Editar una copia. Puedes probar el formulario, registrar una reserva e intercambiar datos con CSV.",
        "classroom": "En el aula", "class_text": "Como estudiante, puedes convertir un problema de tu carrera en un prototipo. Como docente, puedes partir de una práctica guiada y revisar el diseño, la lógica y los datos del proyecto.",
        "theme": "Cambiar tema", "language": "English",
    },
    "en": {
        "title": "Build software.<br><em>Learn by doing.</em>",
        "intro": "Design interfaces, connect blocks, and turn your ideas into working apps. A free visual studio for students in any field.",
        "download": "View downloads", "learn": "Read the docs", "skip": "Skip to content",
        "values": ("Free", "Works offline", "No account required"),
        "tabs": ("Design", "Logic", "Dark mode", "Campus Reserva"),
        "captions": ("EduForge Studio design canvas and inspector", "EduForge Studio event and block editor", "English block editor in dark mode with a sample inventory project", "Campus Reserva running in EduForge Studio preview"),
        "flow": "From idea to app",
        "features": (("Design on the canvas", "Add fields, buttons, and images. Arrange layers and adjust your interface in the inspector."),
                     ("Connect blocks", "Define events and actions, work with tables, and test the result in the editor."),
                     ("Export your app", "Generate a standalone HTML file or a 64-bit Windows executable.")),
        "demo": "Explore Campus Reserva",
        "demo_text": "Open the included example and choose Edit a copy. Try the form, record a reservation, and exchange data using CSV.",
        "classroom": "In the classroom", "class_text": "Students can turn a problem from their field into a prototype. Teachers can start with a guided exercise and review the project's design, logic, and data.",
        "theme": "Toggle theme", "language": "Español",
    },
}
CONTENT = {
    "es": (
        ("Estado de publicación", "Consulta aquí las versiones oficiales de EduForge Studio.", (
            ("Compatibilidad documentada", "La edición de escritorio y el lanzador portátil se preparan para Windows de 64 bits. La edición HTML se abre en Edge o Chrome. Los requisitos mínimos de memoria y almacenamiento están pendientes de verificación."),
            ("Instalación", "Descarga el instalador desde el historial oficial y ejecútalo en Windows de 64 bits. Para la edición HTML, abre el archivo oficial directamente en Edge o Chrome."),
            ("Verificación SHA-256", "En Windows, ejecuta Get-FileHash -Algorithm SHA256 -LiteralPath 'archivo.exe' en PowerShell. Compara el resultado con la suma publicada para ese archivo."),
        )),
        None,  # Documentation has its own chapter content.
        ("Sobre EduForge", "Una herramienta gratuita para aprender desarrollo de software haciendo proyectos.", (
            ("Misión", "Acercar la creación de software a estudiantes de cualquier carrera con un entorno visual que funciona offline."),
            ("Visión", "Facilitar que más estudiantes puedan diseñar, probar y compartir aplicaciones creadas como parte de su aprendizaje."),
            ("El proyecto", "EduForge Studio reúne un diseñador de interfaces, un editor de bloques y herramientas de exportación. El equipo mantiene privado el código fuente del editor. La reseña del fundador está pendiente de confirmar."))),
        ("Apoyar el proyecto", "EduForge Studio se plantea financiar mediante aportes voluntarios y posibles patrocinios.", (
            ("Cómo se usarían los aportes", "Los aportes podrían cubrir mantenimiento, pruebas y distribución. Esta página podrá publicar actualizaciones sobre su uso cuando exista un canal habilitado."),
            ("Aportes y patrocinadores", "Los enlaces de aportes y el espacio de patrocinadores se habilitarán cuando existan canales oficiales confirmados."))),
        ("Contacto y soporte", "Encuentra respuestas o prepara un reporte para el equipo.", (
            ("¿Puedo trabajar offline?", "El editor y los ejemplos incluidos funcionan offline. Los recursos HTTPS que agregues a un proyecto necesitan conexión."),
            ("¿Cómo hago una copia?", "Abre Biblioteca y usa Copia de seguridad para descargar el proyecto en JSON."),
            ("Errores y sugerencias", "Para un error, incluye versión, sistema operativo, pasos y resultado esperado. Para una sugerencia, explica la tarea que quieres resolver. El canal público está pendiente de confirmación."),
            ("Divulgación responsable", "Cuando esté disponible el canal de seguridad, reporta las vulnerabilidades en privado. Incluye la versión, el impacto y los pasos necesarios para entender el problema. Omite datos personales y credenciales."))),
        ("Documentación legal", "Borradores pendientes de revisión antes de la publicación.", (
            ("Aviso legal y copyright", "Pendiente de revisar la identificación del responsable, la titularidad de contenidos y los avisos de copyright aplicables."),
            ("Licencia de usuario final y condiciones", "La propuesta contempla el uso gratuito de Studio. Los permisos de redistribución y las condiciones de uso se definirán en la versión revisada."),
            ("Privacidad", "El editor guarda proyectos localmente según la edición. Los recursos remotos que elijas pueden implicar conexiones con terceros. El texto definitivo deberá describir los datos tratados por cada canal oficial."),
            ("Licencias de terceros", "EduForge Studio utiliza Blockly, Tauri y otras dependencias. El inventario definitivo deberá corresponder a los componentes de cada compilación distribuida."))),
    ),
    "en": (
        ("Release status", "Find official EduForge Studio releases here.", (

            ("Documented compatibility", "The desktop edition and portable launcher target 64-bit Windows. The HTML edition opens in Edge or Chrome. Minimum memory and storage requirements are awaiting verification."),
            ("Installation", "Download the installer from the official release history and run it on 64-bit Windows. For the HTML edition, open the official file directly in Edge or Chrome."),
            ("SHA-256 verification", "On Windows, run Get-FileHash -Algorithm SHA256 -LiteralPath 'file.exe' in PowerShell. Compare the result with the published checksum for that file."),
        )),
        None,  # Documentation has its own chapter content.
        ("About EduForge", "A free tool for learning software development through projects.", (
            ("Mission", "Make software creation accessible to students in any field through a visual environment that works offline."),
            ("Vision", "Help more students design, test, and share apps they create as part of their studies."),
            ("The project", "EduForge Studio brings together an interface designer, a block editor, and export tools. The editor's source code is private. The founder biography is awaiting confirmation."))),
        ("Support the project", "EduForge Studio plans to rely on voluntary contributions and potential sponsorships.", (
            ("How contributions could be used", "Contributions could cover maintenance, testing, and distribution. This page can publish updates on their use once an official channel is available."),
            ("Contributions and sponsors", "Contribution links and sponsor information will be added when official channels are confirmed."))),
        ("Contact and help", "Find answers or prepare a report for the team.", (
            ("Can I work offline?", "The editor and bundled examples work offline. HTTPS resources you add to a project require a connection."),
            ("How do I make a backup?", "Open the Library and choose Backup to download the project as JSON."),
            ("Bugs and suggestions", "For a bug, include the version, operating system, steps, and expected result. For a suggestion, describe the task you want to accomplish. A public channel is awaiting confirmation."),
            ("Responsible disclosure", "When a security channel is available, report vulnerabilities privately. Include the version, impact, and steps needed to understand the issue. Omit personal data and credentials."))),
        ("Legal documentation", "Drafts awaiting review before publication.", (
            ("Legal notice and copyright", "The responsible party, ownership of content, and applicable copyright notices are pending review."),
            ("End-user license and terms", "The proposal allows free use of Studio. Redistribution permissions and terms of use will be defined in the reviewed version."),
            ("Privacy", "The editor stores projects locally depending on the edition. Remote resources you choose can connect to third parties. The final text should describe the data handled by each official channel."),
            ("Third-party licenses", "EduForge Studio uses Blockly, Tauri, and other dependencies. The final inventory must match the components in each distributed build."))),
    ),
}


def url(lang, page):
    prefix = "en/" if lang == "en" else ""
    return prefix + ("" if page == "inicio" else page + "/") + "index.html"


def home(lang, base):
    copy = HOME[lang]
    links = "".join(f'<li>{value}</li>' for value in copy["values"])
    # Visible links also work with scripting disabled.
    controls = "".join(
        f'<a class="view" href="{base}assets/{file}" data-caption="{escape(caption)}"'
        f'{" aria-current=true" if i == 0 else ""}>{label}</a>'
        for i, (file, caption, label) in enumerate(zip(SCREENSHOTS, copy["captions"], copy["tabs"]))
    )
    features = "".join(f'<li><h3>{title}</h3><p>{description}</p></li>' for title, description in copy["features"])
    return f"""
      <section class="hero">
        <h1>{copy['title']}</h1>
        <p>{copy['intro']}</p>
        <div class="actions"><a class="primary" href="{base + url(lang, 'descargas')}">{copy['download']}</a>
        <a class="secondary" href="{base + url(lang, 'tutoriales')}">{copy['learn']}</a></div>
        <ul class="values">{links}</ul>
      </section>
      <figure class="studio" data-gallery>
        <div class="studio-bar"><strong>EduForge Studio</strong><div class="views">{controls}</div></div>
        <img data-screenshot src="{base}assets/design.png" alt="{copy['captions'][0]}" width="1440" height="900" fetchpriority="high">
        <figcaption aria-live="polite">{copy['captions'][0]}</figcaption>
      </figure>
      <section class="workflow"><h2>{copy['flow']}</h2><ul>{features}</ul></section>
      <section class="demo"><div><h2>{copy['demo']}</h2><p>{copy['demo_text']}</p>
        <a class="secondary" href="{base + url(lang, 'tutoriales')}">{copy['learn']}</a></div>
        <img src="{base}assets/campus-demo.png" alt="{copy['captions'][-1]}" width="1440" height="900" loading="lazy">
      </section>
      <section class="classroom"><h2>{copy['classroom']}</h2><p>{copy['class_text']}</p></section>"""


RELEASE_COPY = {
    "es": (
        "Versiones publicadas", "Ver el historial completo en GitHub",
        "No hay un instalador estable con SHA-256 disponible.",
        "No se pudo consultar GitHub. Revisa el historial oficial.",
        "Último instalador estable:",
    ),
    "en": (
        "Published releases", "View the full history on GitHub",
        "No stable installer with a SHA-256 checksum is available.",
        "GitHub could not be reached. Check the official history.",
        "Latest stable installer:",
    ),
}


def releases(lang):
    title, link, empty, unavailable, stable = RELEASE_COPY[lang]
    return f"""<section data-releases data-empty="{empty}" data-unavailable="{unavailable}" data-stable="{stable}">
      <h2>{title}</h2>
      <p role="status"></p>
      <ul hidden></ul>
      <p><a href="https://github.com/hans-07/eduforge-releases/releases">{link}</a></p>
    </section>"""


def guide_url(lang, slug):
    parent = url(lang, "tutoriales").removesuffix("index.html")
    return parent + (slug + "/" if slug else "") + "index.html"


def documentation(lang, base, slug):
    guides = GUIDES[lang]
    index = SLUGS.index(slug)
    heading, intro, sections = guides[index]
    sidebar, contents, more = (
        ("Guías de Studio", "En esta página", ("Anterior", "Siguiente")) if lang == "es"
        else ("Studio guides", "On this page", ("Previous", "Next"))
    )
    search_label, empty = (
        ("Buscar en la documentación", "No se encontraron guías.") if lang == "es"
        else ("Search documentation", "No matching guides.")
    )
    links = []
    for i, (key, (title, description, chapters)) in enumerate(zip(SLUGS, guides)):
        search_text = [title, description]
        for label, prose, steps in chapters:
            search_text.extend((label, prose, *steps))
        active = ' aria-current="page"' if i == index else ""
        links.append(
            f'<a data-guide="{escape(" ".join(search_text))}" '
            f'href="{base + guide_url(lang, key)}"{active}>{escape(title)}</a>'
        )
    toc, article = [], []
    for i, (label, copy, steps) in enumerate(sections, 1):
        anchor = f"section-{i}"
        toc.append(f'<a href="#{anchor}">{escape(label)}</a>')
        prose = f"<p>{escape(copy)}</p>" if copy else ""
        if steps:
            prose += "<ol>" + "".join(f"<li>{escape(step)}</li>" for step in steps) + "</ol>"
        article.append(f'<section><h2 id="{anchor}">{escape(label)}</h2>{prose}</section>')
    image = ""
    if index in PHOTOS:
        alt = {
            "es": ("Biblioteca de proyectos de EduForge Studio", "Lienzo y propiedades del editor", "Tutorial de conexión de bloques", "Vista previa de Campus Reserva"),
            "en": ("EduForge Studio project library", "Editor canvas and inspector", "Guided block connection exercise", "Campus Reserva preview"),
        }[lang][index - 1]
        image = f'<figure class="doc-shot"><a href="{base}assets/{PHOTOS[index]}"><img src="{base}assets/{PHOTOS[index]}" alt="{alt}" width="1440" height="900" loading="lazy"></a><figcaption>{alt}</figcaption></figure>'
    neighbors = "".join(
        f'<a href="{base + guide_url(lang, SLUGS[neighbor])}"><span>{label}</span>{escape(guides[neighbor][0])}</a>'
        for neighbor, label in zip((index - 1, index + 1), more) if 0 <= neighbor < len(guides)
    )
    body = f'''<div class="docs">
      <aside class="docs-side"><nav aria-label="{sidebar}"><strong>{sidebar}</strong>
      <input class="doc-search" type="search" placeholder="{search_label}" aria-label="{search_label}" hidden>
      <p class="doc-search-status" role="status" hidden>{empty}</p>{"".join(links)}</nav></aside>
      <article class="doc-article"><h1>{heading}</h1><p class="intro">{intro}</p>
      {article[0]}{image}{"".join(article[1:])}
      <nav class="doc-next" aria-label="{sidebar}">{neighbors}</nav></article>
      <aside class="docs-toc"><nav aria-label="{contents}"><strong>{contents}</strong>{"".join(toc)}</nav></aside>
    </div>'''
    return heading, intro, body


def render(lang, index, base, slug=""):
    copy = HOME[lang]
    names = NAV[lang]
    other = "en" if lang == "es" else "es"
    page = PAGES[index]
    title = "EduForge Studio" if index == 0 else f"{names[index]} · EduForge Studio"
    nav = "".join(
        f'<a href="{base + url(lang, key)}"{" aria-current=page" if i == index else ""}>{names[i]}</a>'
        for i, key in enumerate(PAGES[1:3], 1)
    )
    foot = "".join(f'<a href="{base + url(lang, key)}">{name}</a>' for key, name in zip(PAGES[3:], names[3:]))
    release_script = ""
    if index == 0:
        body = home(lang, base)
        intro = copy["intro"]
    elif page == "tutoriales":
        heading, intro, body = documentation(lang, base, slug)
        title = f"{heading} · EduForge Studio"
    else:
        heading, intro, sections = CONTENT[lang][index - 1]
        rows = "".join(f'<section><h2>{label}</h2><p>{description}</p></section>' for label, description in sections)
        if page == "descargas":
            rows = releases(lang) + rows
            release_script = f'\n<script src="{base}assets/releases.js" defer></script>'
        body = f'<article class="reading"><h1>{heading}</h1><p class="intro">{intro}</p>{rows}</article>'
    alternate = guide_url(other, slug) if page == "tutoriales" else url(other, page)
    theme_options = ("Sistema", "Claro", "Oscuro") if lang == "es" else ("System", "Light", "Dark")
    theme_menu = "".join(f'<option value="{key}">{label}</option>' for key, label in zip(("system", "light", "dark"), theme_options))
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(intro)}">
<title>{title}</title>
<link rel="icon" href="{base}assets/eduforge-logo.webp">
<link rel="stylesheet" href="{base}assets/style.css">
<script src="{base}assets/site.js" defer></script>{release_script}
</head>
<body>
<a class="skip" href="#main">{copy['skip']}</a>
<header class="header"><div class="shell">
<a class="brand" href="{base + url(lang, 'inicio')}"><img src="{base}assets/eduforge-logo.webp" width="36" height="36" alt=""><span>EduForge<span class="brand-studio"> Studio</span></span></a>
<nav aria-label="EduForge Studio">{nav}<a hreflang="{other}" lang="{other}" href="{base + alternate}">{copy['language']}</a>
<select class="theme" aria-label="{copy['theme']}" hidden>{theme_menu}</select></nav>
</div></header>
<main class="shell" id="main">{body}
</main>
<footer><div class="shell"><a class="footer-brand" href="{base + url(lang, 'inicio')}">EduForge Studio</a><nav aria-label="{names[3]}">{foot}</nav></div></footer>
</body>
</html>
"""


if __name__ == "__main__":
    for language in NAV:
        for index, page in enumerate(PAGES):
            path = ROOT / url(language, page)
            path.parent.mkdir(parents=True, exist_ok=True)
            base = "../" * len(path.parent.relative_to(ROOT).parts)
            path.write_text(render(language, index, base), encoding="utf-8")


        for slug in SLUGS[1:]:
            path = ROOT / guide_url(language, slug)
            path.parent.mkdir(parents=True, exist_ok=True)
            base = "../" * len(path.parent.relative_to(ROOT).parts)
            path.write_text(render(language, PAGES.index("tutoriales"), base, slug), encoding="utf-8")
