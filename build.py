from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent / "site"
SCREENSHOTS = ("design.png", "blocks.png", "campus-demo.png")
PAGES = ("inicio", "descargas", "tutoriales", "sobre", "apoyar", "soporte", "legal")
NAV = {
    "es": ("Inicio", "Descargas", "Tutoriales", "Sobre EduForge", "Apoyar", "Soporte", "Legal"),
    "en": ("Home", "Downloads", "Tutorials", "About", "Support the project", "Help", "Legal"),
}
HOME = {
    "es": {
        "title": "Crea software.<br><em>Aprende construyendo.</em>",
        "intro": "Diseña interfaces, conecta bloques y convierte tus ideas en aplicaciones funcionales. Un estudio visual gratuito para estudiantes de cualquier carrera.",
        "download": "Ir a descargas", "learn": "Explorar tutoriales", "skip": "Ir al contenido",
        "values": ("Gratis", "Funciona offline", "Sin cuenta"),
        "tabs": ("Diseño", "Lógica", "Campus Reserva"),
        "captions": ("Lienzo de diseño e inspector de EduForge Studio", "Editor de eventos y bloques de EduForge Studio", "Campus Reserva en la vista previa de EduForge Studio"),
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
        "download": "View downloads", "learn": "Explore tutorials", "skip": "Skip to content",
        "values": ("Free", "Works offline", "No account required"),
        "tabs": ("Design", "Logic", "Campus Reserva"),
        "captions": ("EduForge Studio design canvas and inspector", "EduForge Studio event and block editor", "Campus Reserva running in EduForge Studio preview"),
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
            ("Versión estable", "Aún no hay una versión estable pública disponible. La versión documentada en el proyecto es 0.4.0."),
            ("Compatibilidad documentada", "La edición de escritorio y el lanzador portátil se preparan para Windows de 64 bits. La edición HTML se abre en Edge o Chrome. Los requisitos mínimos de memoria y almacenamiento están pendientes de verificación."),
            ("Instalación", "Cuando se publique el instalador oficial, ejecútalo en Windows de 64 bits. Para la edición HTML, abre el archivo oficial directamente en Edge o Chrome."),
            ("Verificación SHA-256", "En Windows, ejecuta Get-FileHash -Algorithm SHA256 -LiteralPath 'archivo.exe' en PowerShell. Compara el resultado con la suma publicada para ese archivo."),
            ("Historial", "Las fechas, tamaños, sumas y notas aparecerán cuando haya una publicación oficial."))),
        ("Aprende con un proyecto", "Sigue el flujo de trabajo de Studio con una práctica pequeña.", (
            ("Crea tu primer proyecto", "En Biblioteca, crea un proyecto o abre Campus Reserva y elige Editar una copia. Exporta una copia de seguridad en JSON para guardar tu avance."),
            ("Diseña una pantalla", "En Diseño, elige un tamaño de lienzo y agrega un campo y un botón. Selecciona cada componente para ajustar su posición y apariencia en el inspector."),
            ("Conecta un evento", "En Lógica, selecciona el evento del botón y conecta una acción debajo del encabezado. Pulsa Probar para ejecutar la pantalla y revisar los bloques ejecutados."),
            ("Trabaja con datos", "En Datos, crea una tabla o importa un CSV. En Lógica, conecta un bloque Valor de columna por cada valor de la fila y respeta el orden de los encabezados."),
            ("Exporta y prueba", "Genera un HTML independiente o un ejecutable Windows de 64 bits. Abre la exportación y comprueba la navegación desde la primera página."),
            ("Ideas por carrera", "Usa una tabla para registrar materiales en ingeniería, organiza fichas de lectura en humanidades o practica con un inventario en administración."))),
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
            ("Stable version", "A public stable release is not yet available. The project documents version 0.4.0."),
            ("Documented compatibility", "The desktop edition and portable launcher target 64-bit Windows. The HTML edition opens in Edge or Chrome. Minimum memory and storage requirements are awaiting verification."),
            ("Installation", "Once the official installer is published, run it on 64-bit Windows. For the HTML edition, open the official file directly in Edge or Chrome."),
            ("SHA-256 verification", "On Windows, run Get-FileHash -Algorithm SHA256 -LiteralPath 'file.exe' in PowerShell. Compare the result with the published checksum for that file."),
            ("Release history", "Dates, file sizes, checksums, and release notes will appear when an official release is available."))),
        ("Learn with a project", "Follow the Studio workflow with a small exercise.", (
            ("Create your first project", "In the Library, create a project or open Campus Reserva and choose Edit a copy. Export a JSON backup to save your progress."),
            ("Design a screen", "In Design, choose a canvas size and add a field and a button. Select each component to adjust its position and appearance in the inspector."),
            ("Connect an event", "In Logic, select the button event and connect an action below its header. Choose Test to run the screen and check which blocks ran."),
            ("Work with data", "In Data, create a table or import a CSV. In Logic, connect one Column value block for each row value in header order."),
            ("Export and test", "Generate a standalone HTML file or a 64-bit Windows executable. Open the export and check navigation from the first page."),
            ("Ideas by field", "Track materials in engineering, organize reading notes in the humanities, or practice with an inventory in business studies."))),
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
        <img src="{base}assets/campus-demo.png" alt="{copy['captions'][2]}" width="1440" height="900" loading="lazy">
      </section>
      <section class="classroom"><h2>{copy['classroom']}</h2><p>{copy['class_text']}</p></section>"""


def render(lang, index, base):
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
    if index == 0:
        body = home(lang, base)
        intro = copy["intro"]
    else:
        heading, intro, sections = CONTENT[lang][index - 1]
        rows = "".join(f'<section><h2>{label}</h2><p>{description}</p></section>' for label, description in sections)
        body = f'<article class="reading"><h1>{heading}</h1><p class="intro">{intro}</p>{rows}</article>'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(intro)}">
<title>{title}</title>
<link rel="icon" href="{base}assets/eduforge-logo.webp">
<link rel="stylesheet" href="{base}assets/style.css">
<script src="{base}assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">{copy['skip']}</a>
<header class="header"><div class="shell">
<a class="brand" href="{base + url(lang, 'inicio')}"><img src="{base}assets/eduforge-logo.webp" width="36" height="36" alt=""><span>EduForge<span class="brand-studio"> Studio</span></span></a>
<nav aria-label="EduForge Studio">{nav}<a hreflang="{other}" lang="{other}" href="{base + url(other, page)}">{copy['language']}</a>
<button class="theme" type="button" aria-label="{copy['theme']}" title="{copy['theme']}" hidden><span aria-hidden="true">◐</span></button></nav>
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

