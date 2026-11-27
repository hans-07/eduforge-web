"""Bilingual Studio guides for the public website."""

SLUGS = ("", "primer-proyecto", "diseno", "bloques", "datos", "exportar", "preferencias")
PHOTOS = {1: "library.png", 2: "design.png", 3: "tutorial-conectar.png", 4: "campus-demo.png"}
GUIDES = {
    "es": (
        ("Documentación", "De tu primer proyecto a una aplicación lista para compartir.",
         (("Empieza aquí", "Crea una aplicación pequeña para registrar materiales. Las guías recorren el lienzo, los eventos, las tablas y la exportación en el mismo orden en que los usarás.", ()),
          ("Cómo se organiza Studio", "Diseño define la interfaz. Lógica conecta eventos con acciones. Datos contiene las tablas del proyecto. Probar ejecuta la pantalla activa en una vista previa aislada.", ()),
          ("Practica dentro del editor", "En Biblioteca, abre Tutoriales para seguir las indicaciones en la interfaz. Campus Reserva permite ver una aplicación completa y editar una copia.", ()))),
        ("Crea tu primer proyecto", "Construye la pantalla de un registro de materiales y guarda un respaldo.",
         (("Crea la pantalla", "", ("Pulsa Nuevo proyecto y escribe Registro de materiales.", "En Diseño, añade un Título, un Campo y un Botón. Cambia el texto del botón a Guardar.", "Pulsa Probar y comprueba que el campo admite texto.")),
          ("Guarda un punto de partida", "Studio guarda las ediciones automáticamente. Usa Copia de seguridad para descargar el archivo JSON del proyecto. Abre la copia desde Biblioteca con Importar proyecto.", ()))),
        ("Diseño de interfaces", "Coloca componentes, ajusta propiedades y comprueba la interfaz en distintos tamaños.",
         (("Elige el lienzo", "", ("En Tipo de pantalla, selecciona Móvil para una interfaz vertical o Escritorio para una pantalla ancha.", "Selecciona un componente desde el lienzo o desde Capas. Usa el inspector para editar posición, tamaño y texto.")),
          ("Adapta la interfaz", "Configura los anclajes desde Propiedades y revisa la visibilidad por ancho. Prueba la app en una ventana estrecha y en otra amplia. El tamaño del lienzo sirve de referencia para el diseño.", ()),
          ("Usa imágenes locales", "Añade Imagen, selecciona el componente y usa Subir imagen. La imagen queda incorporada al proyecto. Comprueba su aspecto con Contener y Cubrir.", ()))),
        ("Eventos y bloques", "Conecta el botón Guardar con una acción y verifica que se ejecuta.",
         (("Crea el evento", "", ("Selecciona el botón Guardar y pulsa Editar lógica.", "Selecciona el evento Al presionar de ese botón.", "Arrastra Mostrar mensaje desde Interfaz y conéctalo debajo del bloque del evento.")),
          ("Comprueba el flujo", "Escribe Material registrado como mensaje de prueba. Pulsa Probar y luego Guardar en la app. Si no se ejecuta, comprueba que el bloque esté unido al evento del botón correcto.", ()),
          ("Añade una condición", "Usa Si / si no para elegir qué acciones ejecutar según una condición. Conecta las acciones de cada caso a su rama.", ()))),
        ("Tablas y archivos CSV", "Organiza filas y columnas y conecta los datos con tu interfaz.",
         (("Crea una tabla", "", ("En Datos, pulsa Crear tabla.", "Asigna un nombre y escribe los encabezados separados por comas. Por ejemplo, material,cantidad.", "En Diseño puedes mostrar esa tabla con el componente Tabla y elegirla en Propiedades.")),
          ("Inserta desde un botón", "Agrega Insertar fila al evento. Conecta un bloque Valor de columna por cada encabezado y mantén el orden de la tabla. Prueba con datos ficticios.", ()),
          ("Intercambia CSV", "Antes de importar un CSV en una tabla existente, comprueba que sus encabezados coincidan. Los cambios de datos durante Probar se descartan al cerrar la vista previa.", ()))),
        ("Prueba y exporta", "Valida la aplicación antes de compartirla como HTML o ejecutable para Windows.",
         (("Verifica el recorrido", "", ("Abre Probar y ejecuta el flujo de la pantalla activa.", "Comprueba también la navegación hacia las demás páginas y el comportamiento de los botones.", "Guarda una copia JSON si quieres seguir editando.")),
          ("Elige un formato", "En Exportar aplicación, elige HTML independiente para abrir el archivo en un navegador compatible o Windows (.exe, 64 bits) para compartir un ejecutable que usa el navegador del equipo.", ()),
          ("Revisa la exportación", "Abre el archivo exportado. La ejecución comienza en la primera página del proyecto, así que comprueba el flujo desde allí.", ()))),
        ("Tema e idioma", "Personaliza la interfaz de Studio desde la biblioteca.",
         (("Tema", "Claro y Oscuro fijan la apariencia de Studio. Sistema sigue la preferencia del equipo. El lienzo conserva los colores que elegiste para tu aplicación.", ()),
          ("Idioma", "Selecciona Español o English en la biblioteca. Studio recarga la interfaz y guarda la preferencia en esa instalación. Los nombres, textos y datos de tus proyectos conservan su idioma original.", ()))),
    ),
    "en": (
        ("Documentation", "Go from your first project to an app you can share.",
         (("Start here", "Build a small app that tracks materials. The guides cover the canvas, events, tables, and export in the order you will use them.", ()),
          ("How Studio is organized", "Design defines the interface. Logic connects events to actions. Data holds project tables. Test runs the active screen in an isolated preview.", ()),
          ("Practice in the editor", "Open Tutorials in the library to follow instructions in the interface. Campus Reserva lets you explore a full app and edit a copy.", ()))),
        ("Create your first project", "Build a materials tracker screen and save a backup.",
         (("Create the screen", "", ("Choose New project and enter Materials tracker.", "In Design, add a Heading, an Input, and a Button. Change the button text to Save.", "Choose Test and check that you can type in the input.")),
          ("Save a starting point", "Studio saves your edits automatically. Use Backup to download the project JSON. Open the backup from the library using Import project.", ()))),
        ("Design interfaces", "Place components, adjust properties, and check the interface at different sizes.",
         (("Choose a canvas", "", ("Under Screen preset, select Mobile for a portrait interface or Desktop for a wide screen.", "Select a component on the canvas or in Layers. Use the inspector to edit its position, size, and text.")),
          ("Adapt the interface", "Set anchors in Properties and review visibility by screen width. Try the app in both a narrow and a wide window. The canvas size is the design reference.", ()),
          ("Use local images", "Add an Image, select the component, and choose Upload image. The image is embedded in the project. Compare the Contain and Cover options.", ()))),
        ("Events and blocks", "Connect the Save button to an action and verify that it runs.",
         (("Create the event", "", ("Select the Save button and choose Edit logic.", "Select that button's On click event.", "Drag Show message from Interface and connect it below the event block.")),
          ("Check the flow", "Enter Material recorded as your test message. Choose Test and click Save in your app. If nothing happens, check that the block is attached to the correct button event.", ()),
          ("Add a condition", "Use If / else to choose which actions run based on a condition. Connect the actions for each case to its branch.", ()))),
        ("Tables and CSV files", "Organize rows and columns and connect your data to the interface.",
         (("Create a table", "", ("In Data, choose Create table.", "Name the table and enter comma-separated headers such as material,quantity.", "In Design, add a Table component and select that table in Properties.")),
          ("Insert from a button", "Attach Insert row to the event. Connect one Column value block for each header in table order. Try it with sample data.", ()),
          ("Exchange CSV files", "Before importing a CSV into an existing table, check that the headers match. Data changes made during Test are discarded when you close the preview.", ()))),
        ("Test and export", "Validate your app before sharing an HTML file or Windows executable.",
         (("Verify the workflow", "", ("Choose Test and work through the active screen.", "Check navigation to other pages and the behavior of each button.", "Save a JSON backup if you want to keep editing.")),
          ("Choose a format", "Under Export app, choose Standalone HTML to open the file in a compatible browser, or Windows (.exe, 64-bit) to share an executable that uses the system browser.", ()),
          ("Check the exported app", "Open the exported file. It starts on the first project page, so verify the entire workflow from there.", ()))),
        ("Theme and language", "Customize the Studio interface from the project library.",
         (("Theme", "Light and Dark set Studio's appearance. System follows your device's preference. Your canvas keeps the colors you chose for your app.", ()),
          ("Language", "Select Español or English in the library. Studio reloads the interface and remembers your choice for that installation. Names, text, and data in your projects keep their original language.", ()))),
    ),
}

def read_lessons(language):
    from pathlib import Path

    file = Path(__file__).with_name(f"lessons-{language}.txt")
    lessons = {}
    for line in file.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip():
            continue
        slug, title, description, content = line.split("|", 3)
        sections = []
        for item in content.split("||"):
            label, text = item.split(": ", 1)
            sections.append((label, "", tuple(text.split(" / "))) if label in {"Ejercicio", "Exercise"} else (label, text, ()))
        lessons[slug] = (title, description, tuple(sections))
    return lessons


for language in GUIDES:
    lessons = read_lessons(language)
    if language == "es":
        extra_slugs = tuple(lessons)
    elif tuple(lessons) != extra_slugs:
        raise ValueError("Las rutas de las guías deben coincidir en ambos idiomas.")
    GUIDES[language] += tuple(lessons.values())

SLUGS += extra_slugs


def export_studio(destination):
    import json
    from pathlib import Path

    data = {"slugs": SLUGS, "guides": GUIDES}
    Path(destination).write_text(
        "export const handbook = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    import argparse

    options = argparse.ArgumentParser()
    options.add_argument("--studio", required=True)
    export_studio(options.parse_args().studio)
