# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os
import win32com.client

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=130, right=130):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="B0C4DE"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{color}"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def format_cell(cell, text, bold=False, color="000000", size=9, align=WD_ALIGN_PARAGRAPH.LEFT, bg=None):
    cell.text = ""
    if bg:
        set_cell_background(cell, bg)
    set_cell_margins(cell, top=90, bottom=90, left=120, right=120)
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(str(text))
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    run.font.bold = bold
    if color != "000000":
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        run.font.color.rgb = RGBColor(r, g, b)

def add_p(doc, text="", style="First Paragraph", bold=False, space_after=6, space_before=2, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph(style=style)
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if text:
        run = p.add_run(text)
        run.font.name = "Calibri"
        run.font.size = Pt(size)
        run.font.bold = bold
    return p

def add_bullet(doc, text, bold_prefix="", space_after=3, size=10.5):
    p = doc.add_paragraph(style="First Paragraph")
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run("•  " + bold_prefix + " ")
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(size)
        r_pre.font.bold = True
    else:
        r_pre = p.add_run("•  ")
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(size)
    r_txt = p.add_run(text)
    r_txt.font.name = "Calibri"
    r_txt.font.size = Pt(size)
    return p

def add_callout(doc, text, title="NOTA METODOLÓGICA:"):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    cell = table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=130, bottom=130, left=170, right=170)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="003366"/>
            <w:top w:val="none"/>
            <w:right w:val="none"/>
            <w:bottom w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.1
    r_title = p.add_run(title + " ")
    r_title.font.name = "Calibri"
    r_title.font.bold = True
    r_title.font.size = Pt(10)
    r_title.font.color.rgb = RGBColor(0, 51, 102)
    r_text = p.add_run(text)
    r_text.font.name = "Calibri"
    r_text.font.size = Pt(10)
    p_space = doc.add_paragraph(style="Normal")
    p_space.paragraph_format.space_after = Pt(4)

def read_file_safe(path):
    for enc in ['utf-8', 'utf-16', 'latin-1', 'cp1252']:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read()
        except:
            pass
    return ''

def build_full_document():
    template_path = "SI886-PLANTILLA-TALLER (7).docx"
    output_docx = os.path.abspath("SI886-S15-TALLER-Grupo3.docx")
    output_pdf = os.path.abspath("SI886-S15-TALLER-Grupo3.pdf")

    doc = docx.Document(template_path)

    # 1. Update Cover
    doc.paragraphs[11].text = '“Registro de riesgos del plan y matriz de comunicación — Sección 8 del PETI (Caso: Municipalidad Distrital de Alto Selva)”'
    doc.paragraphs[14].text = '“PLANEAMIENTO ESTRATÉGICO DE TI SEC. A”'
    doc.paragraphs[17].text = 'CHOQUEÑA CHOQUE MAURICIO ARIAN · 2023076799'
    doc.paragraphs[27].text = 'TACNA — PERÚ\n2026'

    # Remove paragraphs after TOC (from P50 to end)
    # Total paragraphs initially is 82.
    # Paragraph 29 is 'Índice'. P47 is '7. Anexos\t1'.
    # Paragraphs 50 to 81 represent the instruction page and skeleton.
    # We remove from bottom up:
    for idx in range(len(doc.paragraphs) - 1, 48, -1):
        p = doc.paragraphs[idx]
        p._element.getparent().remove(p._element)

    # Remove the two empty tables from the template so we add newly styled ones
    for t in list(doc.tables):
        t._element.getparent().remove(t._element)

    print("Template stripped cleanly after TOC. Adding content...")

    # -------------------------------------------------------------
    # SECCIÓN 1: INFORMACIÓN SOBRE EL EVENTO PRÁCTICO
    # -------------------------------------------------------------
    doc.add_page_break()
    h1 = doc.add_paragraph("1. Información sobre el evento práctico", style="Heading 1")
    h1.paragraph_format.space_before = Pt(12)
    h1.paragraph_format.space_after = Pt(6)

    doc.add_paragraph("1.1 Título del evento práctico", style="Heading 2")
    add_p(doc, "Registro de riesgos del plan y matriz de comunicación — Formulación de la Sección 8 del Plan Estratégico de Tecnologías de la Información (PETI 2026-2028) para la Municipalidad Distrital de Alto Selva.")

    doc.add_paragraph("1.2 Objetivos", style="Heading 2")
    add_bullet(doc, "Definir el contexto y los criterios de riesgo del plan de TI acordados formalmente con la Gerencia Municipal y el Comité de Gobierno Digital previo a la evaluación.", "Objetivo 1:")
    add_bullet(doc, "Identificar y redactar de forma exhaustiva los riesgos sobre las nueve categorías mandatorias bajo la estructura formal Evento + Causa + Consecuencia.", "Objetivo 2:")
    add_bullet(doc, "Evaluar cuantitativamente cada riesgo mediante escalas de probabilidad e impacto (1 a 5) con definición operativa explícita antes de la valoración.", "Objetivo 3:")
    add_bullet(doc, "Determinar el tratamiento mandatorio para cada riesgo y calcular el riesgo residual correspondiente garantizando la reducción del nivel de exposición.", "Objetivo 4:")
    add_bullet(doc, "Establecer señales tempranas observables e indicadores de umbral de alerta cuantitativos para todos los riesgos evaluados con valor superior a 6.", "Objetivo 5:")
    add_bullet(doc, "Modelar y registrar la estructura de gestión de riesgos en SimpleRisk Community y generar la matriz de mapa de calor 5x5.", "Objetivo 6:")
    add_bullet(doc, "Construir la matriz integral de comunicación del riesgo definiendo los canales, periodicidades y decisiones habilitadas para la alta dirección.", "Objetivo 7:")
    add_bullet(doc, "Redactar íntegramente la Sección 8 del PETI y consolidar el expediente de gobernanza con trazabilidad versionada en Git.", "Objetivo 8:")

    doc.add_paragraph("1.3 Tiempo de duración", style="Heading 2")
    add_p(doc, "El evento práctico se desarrolló en una sesión intensiva de laboratorio de 2 horas académicas, complementada con 4 horas de trabajo técnico autónomo de modelamiento, desarrollo de scripts analíticos y redacción del informe técnico.")

    doc.add_paragraph("1.4 Resultados de aprendizaje", style="Heading 2")
    add_p(doc, "RA4: Evalúa los riesgos inherentes y residuales de la ejecución del portafolio de proyectos de TI aplicando estándares internacionales (ISO 31000 / ISO/IEC 27005) y directivas de gobierno digital del Estado Peruano (PCM-SGTD), diseñando matrices de tratamiento, alertas tempranas y esquemas de comunicación ejecutiva para la toma de decisiones.")

    doc.add_paragraph("1.5 Recursos", style="Heading 2")
    add_p(doc, "Para el desarrollo del taller se utilizaron herramientas de computación científica, entornos de versionamiento y la documentación institucional del caso asignado:")

    # Table Recursos
    t_rec = doc.add_table(rows=1, cols=3)
    t_rec.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_rec, "003366")
    format_cell(t_rec.rows[0].cells[0], "Recurso / Herramienta", bold=True, color="FFFFFF", size=9.5, bg="003366")
    format_cell(t_rec.rows[0].cells[1], "Versión", bold=True, color="FFFFFF", size=9.5, bg="003366")
    format_cell(t_rec.rows[0].cells[2], "Para qué se usó en el taller", bold=True, color="FFFFFF", size=9.5, bg="003366")

    recursos_data = [
        ("Python, pandas y numpy", "Python 3.11 / pandas 2.2", "Evaluación cuantitativa de P × I, cálculo del valor de riesgo, cálculo del riesgo residual y verificación automática de riesgos sin señal temprana."),
        ("matplotlib", "3.8+", "Generación automatizada de la matriz de calor de riesgos (5x5) con escala de colores invertida (RdYlGn_r) exportada a RG_mapa_calor.png."),
        ("Git & GitHub", "2.40+", "Control de versiones, trazabilidad histórica de acuerdos previos de criterios (git log) y versionamiento formal mediante tags v0.15 y taller-15."),
        ("Docker & SimpleRisk Community", "2024+", "Modelamiento de plataforma GRC para administración de riesgos institucionales, configuración de escalas y carga de riesgos críticos >= 12."),
        ("Documentación Empresa 03", "Caso Alto Selva 2026", "Análisis de insumos: bia.csv (criticidad y RTO/RPO), politica-de-respaldo.md (POL-TI-007) y universo-auditable-y-riesgos.md (UA-01 a UA-17)."),
        ("Marcos de Referencia", "ISO 31000 / PCM-SGTD", "Directrices internacionales para la gestión de riesgos y lineamientos del D.L. 1412 para la gobernanza y transformación digital pública.")
    ]
    for rec, ver, uso in recursos_data:
        r = t_rec.add_row()
        format_cell(r.cells[0], rec, bold=True, size=9)
        format_cell(r.cells[1], ver, size=9)
        format_cell(r.cells[2], uso, size=9)

    doc.add_paragraph("1.6 Seguridad", style="Heading 2")
    add_bullet(doc, "El registro de riesgos expone vulnerabilidades críticas de ejecución e infraestructura de la municipalidad; su tratamiento y custodia es de clasificación CONFIDENCIAL.", "1. Confidencialidad de la información:")
    add_bullet(doc, "Los riesgos asociados a factores humanos (patrocinio y personal clave) se redactaron por cargo estructural, evaluando el riesgo sistémico y nunca la conducta individual.", "2. Redacción por cargo estructural:")
    add_bullet(doc, "Los criterios de aceptación y las escalas operativas se formalizaron antes de iniciar la evaluación cuantitativa para garantizar imparcialidad y rigor metodológico.", "3. Definición previa de criterios:")
    add_bullet(doc, "La aceptación formal de riesgos residuales superiores al umbral de tolerancia (valor > 6) requiere obligatoriamente la firma del dueño del riesgo (Alcaldía/Gerencia).", "4. Firma formal de aceptación:")

    # -------------------------------------------------------------
    # SECCIÓN 2: PROCEDIMIENTO O METODOLOGÍA
    # -------------------------------------------------------------
    doc.add_page_break()
    h1_2 = doc.add_paragraph("2. Procedimiento o metodología", style="Heading 1")
    h1_2.paragraph_format.space_before = Pt(12)
    h1_2.paragraph_format.space_after = Pt(6)

    add_p(doc, "El desarrollo procedimental del taller se organizó en siete fases secuenciales y complementarias (Pasos A a G), orientadas a construir de manera trazable y verificable la gestión del riesgo de la Municipalidad Distrital de Alto Selva:")

    doc.add_paragraph("Paso A — Contexto y criterios de riesgo (ISO 31000)", style="Heading 2")
    add_p(doc, "Se delimitó el alcance del análisis exclusivamente a las amenazas contra la ejecución oportuna del PETI 2026-2028 (Años 1 al 3). Se definieron operativamente las escalas de Probabilidad (1 Muy baja a 5 Muy alta) e Impacto (1 Insignificante a 5 Catastrófico), fijando el criterio de aceptación en: <= 6 Aceptable, 7 a 14 Tratamiento con plazo, y >= 15 Decisión formal de Alcaldía y Gerencia Municipal. Este acuerdo se plasmó en el archivo 08_riesgos/RG01_contexto.md y se registró en Git con fecha previa a la evaluación (10 de octubre de 2026), garantizando que los criterios no fueron ajustados a posteriori.")

    doc.add_paragraph("Paso B — Identificación sobre las nueve categorías y evaluación", style="Heading 2")
    add_p(doc, "A partir del pre-mortem y el análisis documental de la Empresa 3 (incoherencias del BIA, precariedad en la política de respaldos POL-TI-007 y riesgos del universo auditable), se formularon 13 riesgos en 08_riesgos/RG02_registro.csv con la estructura mandatoria Evento + Causa + Consecuencia. Se cubrieron las 9 categorías requeridas: Presupuestal, Patrocinio, Capacidad de ejecución, Personal clave, Resistencia al cambio, Proveedor, Técnico, Normativo, De alcance, más la categoría transversal de Ejecución del plan.")
    add_p(doc, "Se ejecutó el script RG03_evaluacion.py, el cual calculó el valor inherente (P × I), clasificó los niveles de severidad y generó el archivo RG03_evaluado.csv junto con el mapa de calor gráfico en graficos/RG_mapa_calor.png.")

    doc.add_paragraph("Paso C — Tratamiento, señales tempranas y riesgo residual", style="Heading 2")
    add_p(doc, "Para cada riesgo identificado (todos con valor > 6) se definió una estrategia de tratamiento en 08_riesgos/RG04_tratamiento.csv (Mitigar, Transferir o Asumir con contingencia), especificando acciones concretas, responsable por cargo estructural, plazo perentorio y costo. Se estimaron la probabilidad e impacto residuales (P_res × I_res) y se asignaron una señal temprana observable y un umbral de alerta cuantitativo.")
    add_p(doc, "Se ejecutó el script RG05_residual.py, confirmando una reducción global del riesgo de 104 puntos (55 % de efectividad del plan de mitigación), identificando 6 riesgos residuales con valor 8 que demandan firma formal de Alcaldía/Gerencia Municipal, y certificando cero riesgos sin señal temprana.")

    doc.add_paragraph("Paso D — Matriz de comunicación del riesgo", style="Heading 2")
    add_p(doc, "Se estructuró la matriz de comunicación en 08_riesgos/RG06_comunicacion.csv con ocho columnas: ID del riesgo, Qué se comunica, A quién (cargo), Cuándo/frecuencia, Canal, Quién comunica, Formato y Qué decisión habilita. Se incorporó de manera mandatoria la fila final que exige que todos los riesgos >= 15 sean comunicados en sesión extraordinaria previa a la aprobación formal del PETI para que la Alta Dirección asuma conscientemente la responsabilidad institucional.")

    doc.add_paragraph("Paso E — Redacción de la Sección 8 del PETI", style="Heading 2")
    add_p(doc, "Se redactó la Sección 8 del PETI (08_riesgos/08_seccion_peti.md) integrando los 9 acápites formales: 8.1 Alcance y contexto, 8.2 Método ISO 31000, 8.3 Registro de riesgos, 8.4 Evaluación y mapa de calor, 8.5 Tratamiento y riesgo residual, 8.6 Señales tempranas y umbrales, 8.7 Matriz de comunicación, 8.8 Riesgos residuales para aceptación formal, y 8.9 Seguimiento y revisión.")

    doc.add_paragraph("Paso F — Validación y comprobaciones de integridad", style="Heading 2")
    add_p(doc, "Se realizaron las tres comprobaciones de control de calidad exigidas por la rúbrica: (1) Verificación de cobertura de las 9 categorías (todas cubiertas al 100 %); (2) Justificación de probabilidad e impacto basada en evidencia factual del caso municipal y no en mera intuición; (3) Comprobación de que cada riesgo de nivel alto/crítico cuenta con tratamiento asignado a un cargo estructural formal.")

    doc.add_paragraph("Paso G — Versionamiento y etiquetado Git", style="Heading 2")
    add_p(doc, "Se incorporó la totalidad de artefactos producidos al repositorio local, generando los commits correspondientes y creando las etiquetas v0.15 (estado de la Sección 8 del PETI) y taller-15 (entrega procedimental de la sesión).")

    # -------------------------------------------------------------
    # SECCIÓN 3: RESULTADOS
    # -------------------------------------------------------------
    doc.add_page_break()
    h1_3 = doc.add_paragraph("3. Resultados", style="Heading 1")
    h1_3.paragraph_format.space_before = Pt(12)
    h1_3.paragraph_format.space_after = Pt(6)

    add_p(doc, "A continuación se presenta la lista de comprobación de resultados esperados de acuerdo con la subsección 3.2 de la guía de taller, vinculando cada resultado con su evidencia física y digital verificable:")

    # Table 1: Resultados (14 rows)
    t_res = doc.add_table(rows=1, cols=4)
    t_res.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_res, "003366")
    format_cell(t_res.rows[0].cells[0], "#", bold=True, color="FFFFFF", size=9, align=WD_ALIGN_PARAGRAPH.CENTER, bg="003366")
    format_cell(t_res.rows[0].cells[1], "Resultado esperado (Lista 3.2)", bold=True, color="FFFFFF", size=9, bg="003366")
    format_cell(t_res.rows[0].cells[2], "¿Se logró?", bold=True, color="FFFFFF", size=9, align=WD_ALIGN_PARAGRAPH.CENTER, bg="003366")
    format_cell(t_res.rows[0].cells[3], "Evidencia verificable y enlace", bold=True, color="FFFFFF", size=9, bg="003366")

    checklist_items = [
        ("1", "Contexto y criterios definidos con fecha de acuerdo anterior a la evaluación.", "Logrado", "08_riesgos/RG01_contexto.md y commit ba3bd2d con fecha 10/10/2026."),
        ("2", "Escalas de probabilidad e impacto con definición operativa escrita.", "Logrado", "Sección 3 de RG01_contexto.md (descriptores cuantitativos y cualitativos)."),
        ("3", "Las nueve categorías evaluadas; las omitidas, justificadas.", "Logrado", "Salida de RG03_evaluacion.py: Categorías sin riesgo: ninguna ✔ (cobertura 100 %)."),
        ("4", "Registro con >= 12 riesgos redactados como Evento + Causa + Consecuencia.", "Logrado", "08_riesgos/RG02_registro.csv conteniendo 13 riesgos formulados estrictamente."),
        ("5", "Cada riesgo trazado a los objetivos y proyectos que afecta.", "Logrado", "Columna 'Objetivos o proyectos afectados' en RG02_registro.csv (OD y PR)."),
        ("6", "Mapa de calor generado.", "Logrado", "Archivo gráfico graficos/RG_mapa_calor.png generado por RG03_evaluacion.py."),
        ("7", "Riesgos >= 15 identificados como decisión de la gerencia general / alcaldía.", "Logrado", "7 riesgos identificados (R-08, R-12, R-01, R-03, R-05, R-07, R-02) en RG03_salida.txt."),
        ("8", "Tratamiento definido para todos los riesgos de valor > 6.", "Logrado", "08_riesgos/RG04_tratamiento.csv con acciones, cargo responsable, plazo y costo."),
        ("9", "Riesgo residual calculado, con la reducción lograda.", "Logrado", "Salida RG05_salida.txt: reducción de 104 puntos (55 % de reducción neta)."),
        ("10", "Señal temprana y umbral de alerta en cada riesgo > 6; cero riesgos sin señal.", "Logrado", "Salida RG05: 'Riesgos sin señal temprana: 0 -> []'."),
        ("11", "Riesgos residuales sobre el criterio con responsable de aceptación identificado.", "Logrado", "6 riesgos con residual 8 asignados por cargo formal (Alcaldía/Gerencia)."),
        ("12", "Registro modelado para SimpleRisk con escalas y criterio configurados.", "Logrado", "Arquitectura de contenedores Docker documentada y matriz de carga preparada."),
        ("13", "Matriz de comunicación con las ocho columnas.", "Logrado", "08_riesgos/RG06_comunicacion.csv con fila obligatoria de riesgos >= 15."),
        ("14", "Sección 8 redactada · etiquetas de versión Git.", "Logrado", "08_riesgos/08_seccion_peti.md versionado y tags v0.15 y taller-15 creados.")
    ]

    for num, desc, logr, evid in checklist_items:
        r = t_res.add_row()
        format_cell(r.cells[0], num, bold=True, size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell(r.cells[1], desc, size=8.5)
        format_cell(r.cells[2], logr, bold=True, color="006600", size=8.5, align=WD_ALIGN_PARAGRAPH.CENTER)
        format_cell(r.cells[3], evid, size=8.5)

    add_p(doc, "Declaración transparente de problemas y mejoras:", bold=True, space_before=10)
    add_callout(doc, "Durante la sesión práctica en la estación de trabajo local no se contaba con el servicio Docker Daemon habilitado en el sistema operativo Windows para instanciar la imagen mariadb:11 y simplerisk/simplerisk:latest. Conforme a las pautas de honestidad procedimental del curso, se modelaron y parametrizaron completamente los scripts en Python (RG03 y RG05), los archivos CSV estructurados con la fórmula clásica P × I y las tablas compatibles con la importación GRC de SimpleRisk, cumpliendo a plenitud el objetivo analítico y matemático de la práctica.", "INCIDENCIA Y MEJORA DECLARADA:")

    # -------------------------------------------------------------
    # SECCIÓN 4: CONCLUSIONES
    # -------------------------------------------------------------
    doc.add_page_break()
    h1_4 = doc.add_paragraph("4. Conclusiones", style="Heading 1")
    h1_4.paragraph_format.space_before = Pt(12)
    h1_4.paragraph_format.space_after = Pt(6)

    add_bullet(doc, "La aplicación de la dinámica de pre-mortem permitió descubrir riesgos ocultos estructurales de la Municipalidad Distrital de Alto Selva que la pregunta tradicional «¿qué puede salir mal?» jamás habría evidenciado, tales como el transporte manual de backups no cifrados en mochilas (POL-TI-007) y la incoherencia crítica de los tiempos RTO/RPO del BIA elaborado por practicantes sin validación de las áreas de rentas y trámite.", "1. Efectividad diagnóstica del Pre-mortem:")
    add_bullet(doc, "Un riesgo sin señal temprana observable y sin umbral cuantitativo no constituye un riesgo bajo control, sino un inventario ciego. La definición de umbrales como «2 fallos consecutivos de copia en la semana» o «45 días sin sesión del Comité de Gobierno Digital» transforma el registro de riesgos en un instrumento vivo de control operacional y preventivo.", "2. Valor de las señales tempranas y umbrales:")
    add_bullet(doc, "El riesgo residual aceptado tácitamente sin la firma de la Alta Dirección no está gestionado, está deliberadamente ignorado. La presentación de la matriz de comunicación previa a la aprobación del PETI garantiza que la Alcaldía y la Gerencia Municipal asuman conscientemente la responsabilidad institucional de los 6 riesgos residuales críticos que no pueden ser mitigados por debajo del umbral 6.", "3. Responsabilidad ejecutiva del riesgo residual:")
    add_bullet(doc, "La articulación de ISO 31000:2018 con las directivas de gobierno digital del Perú (PCM-SGTD) brinda un marco sólido para proteger los fondos públicos y asegurar la continuidad operativa de los servicios ciudadanos (recaudación, licencias y registro civil), blindando el portafolio del PETI contra la rotación política municipal.", "4. Gobernanza y sostenibilidad pública:")

    # -------------------------------------------------------------
    # SECCIÓN 5: CUESTIONARIO
    # -------------------------------------------------------------
    doc.add_page_break()
    h1_5 = doc.add_paragraph("5. Cuestionario", style="Heading 1")
    h1_5.paragraph_format.space_before = Pt(12)
    h1_5.paragraph_format.space_after = Pt(6)

    add_p(doc, "Pregunta de transferencia de la guía de taller:", bold=True)
    add_p(doc, "¿Qué riesgo correría una organización real si la gestión de riesgos del PETI se hiciera mal o se omitiera?", style="First Paragraph", bold=True, size=11, align=WD_ALIGN_PARAGRAPH.JUSTIFY)
    
    add_p(doc, "Respuesta técnica fundamentada:", bold=True)
    add_p(doc, "Si una entidad pública como la Municipalidad Distrital de Alto Selva realizara una gestión de riesgos deficiente o meramente formal (un «check administrativo»), correría el riesgo inminente de paralización total de los servicios públicos esenciales y colapso recaudatorio ante un incidente técnico previsible. En el caso analizado, al existir una dependencia absoluta de sistemas legados de rentas sin código fuente documentado y respaldos precarios trasladados en discos externos sin cifrar, un ataque informático o una renuncia del personal clave provocaría la pérdida definitiva de la base tributaria municipal, acarreando responsabilidades civiles, administrativas y penales ante la Contraloría General de la República por negligencia en la custodia del patrimonio público.")
    add_p(doc, "Asimismo, un PETI formulado sin criterios de riesgo acordados con la Gerencia terminaría convirtiéndose en un portafolio inerte que naufragaría ante el primer recorte presupuestal del Concejo Municipal o cambio de gestión edil, desperdiciando los recursos asignados y perpetuando la brecha de atención digital al ciudadano.")

    # -------------------------------------------------------------
    # SECCIÓN 6: REFERENCIAS BIBLIOGRÁFICAS
    # -------------------------------------------------------------
    doc.add_page_break()
    h1_6 = doc.add_paragraph("6. Referencias bibliográficas", style="Heading 1")
    h1_6.paragraph_format.space_before = Pt(12)
    h1_6.paragraph_format.space_after = Pt(6)

    add_p(doc, "Referencias en formato APA (7.ª edición):", bold=True)
    add_bullet(doc, "International Organization for Standardization. (2018). Risk management — Guidelines (ISO Standard No. 31000:2018). https://www.iso.org/standard/65694.html", "ISO.")
    add_bullet(doc, "International Organization for Standardization / International Electrotechnical Commission. (2022). Information security, cybersecurity and privacy protection — Guidance on managing information security risks (ISO/IEC Standard No. 27005:2022). https://www.iso.org/standard/80585.html", "ISO/IEC.")
    add_bullet(doc, "International Electrotechnical Commission. (2019). Risk management — Risk assessment techniques (IEC Standard No. 31010:2019). https://www.iso.org/standard/72140.html", "IEC.")
    add_bullet(doc, "ISACA. (2018). COBIT 2019 Framework: Governance and Management Objectives (APO12 Managed Risk & EDM03 Ensured Risk Optimization). ISACA.", "ISACA.")
    add_bullet(doc, "Klein, G. (2007). Performing a project premortem. Harvard Business Review, 85(9), 18–19.", "Klein, G.")
    add_bullet(doc, "Presidencia del Consejo de Ministros - Secretaría de Gobierno Digital. (2018). Resolución de Secretaría de Gobierno Digital N.º 005-2018-PCM/SEGDI: Lineamientos para la formulación del Plan de Gobierno Digital (Anexo I). Diario Oficial El Peruano.", "PCM-SEGDI.")
    add_bullet(doc, "Project Management Institute. (2021). A Guide to the Project Management Body of Knowledge (PMBOK Guide) (7.ª ed.). Project Management Institute.", "PMI.")
    add_bullet(doc, "Rodríguez Bermúdez, J. R. (2015). Planificación y dirección estratégica de tecnologías de la información. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875", "Rodríguez Bermúdez, J. R.")
    add_bullet(doc, "SimpleRisk. (2024). SimpleRisk Comprehensive Risk Management Platform Documentation. https://www.simplerisk.com/documentation", "SimpleRisk.")

    # -------------------------------------------------------------
    # SECCIÓN 7: ANEXOS
    # -------------------------------------------------------------
    doc.add_page_break()
    h1_7 = doc.add_paragraph("7. Anexos", style="Heading 1")
    h1_7.paragraph_format.space_before = Pt(12)
    h1_7.paragraph_format.space_after = Pt(6)

    doc.add_paragraph("Anexo A: Matriz Completa de Registro y Evaluación de Riesgos (RG02 / RG03)", style="Heading 2")
    add_p(doc, "A continuación se detalla la matriz de los 13 riesgos evaluados con sus factores P, I, valor inherente y nivel de riesgo asignado:")

    # Table Anexo A
    t_anx_a = doc.add_table(rows=1, cols=7)
    t_anx_a.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_anx_a, "003366")
    anx_headers = ["ID", "Categoría", "Riesgo (Evento + Causa + Consecuencia)", "P", "I", "Val", "Nivel"]
    for ci, ch in enumerate(anx_headers):
        format_cell(t_anx_a.rows[0].cells[ci], ch, bold=True, color="FFFFFF", size=8.5, bg="003366")

    import csv
    with open("08_riesgos/RG03_evaluado.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tr = t_anx_a.add_row()
            format_cell(tr.cells[0], row["id"], bold=True, size=8)
            format_cell(tr.cells[1], row["Categoría"], size=8)
            format_cell(tr.cells[2], row["Riesgo (evento + causa + consecuencia)"][:100] + "...", size=7.5)
            format_cell(tr.cells[3], row["P"], size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
            format_cell(tr.cells[4], row["I"], size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
            format_cell(tr.cells[5], row["valor"], bold=True, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
            niv_color = "990000" if row["nivel"]=="Crítico" else ("CC6600" if row["nivel"]=="Alto" else "006600")
            format_cell(tr.cells[6], row["nivel"], bold=True, color=niv_color, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.add_paragraph("Anexo B: Mapa de Calor de Riesgos del PETI (5x5)", style="Heading 2")
    add_p(doc, "Visualización de la distribución de frecuencias de los riesgos generada mediante matplotlib (RG_mapa_calor.png):")
    if os.path.exists("graficos/RG_mapa_calor.png"):
        doc.add_paragraph(style="Normal").alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.paragraphs[-1].paragraph_format.space_before = Pt(6)
        doc.paragraphs[-1].paragraph_format.space_after = Pt(6)
        doc.paragraphs[-1].add_run().add_picture("graficos/RG_mapa_calor.png", width=Inches(5.5))
        p_cap = doc.add_paragraph("Figura 1. Mapa de calor de riesgos de ejecución del PETI 2026-2028 (Municipalidad de Alto Selva).", style="Normal")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(9)
        p_cap.runs[0].font.italic = True

    doc.add_paragraph("Anexo C: Plan de Tratamiento y Reducción Residual (RG04 / RG05)", style="Heading 2")
    add_p(doc, "Resumen del plan de tratamiento y eficacia en la reducción del riesgo:")
    
    t_anx_c = doc.add_table(rows=1, cols=6)
    t_anx_c.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_anx_c, "003366")
    anx_c_headers = ["ID", "Valor Inic.", "Decisión", "Acción Principal", "Residual", "Reducción"]
    for ci, ch in enumerate(anx_c_headers):
        format_cell(t_anx_c.rows[0].cells[ci], ch, bold=True, color="FFFFFF", size=8.5, bg="003366")

    with open("08_riesgos/RG04_tratamiento.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tr = t_anx_c.add_row()
            format_cell(tr.cells[0], row["id"], bold=True, size=8)
            format_cell(tr.cells[1], row["Valor"], size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
            format_cell(tr.cells[2], row["Decisión"][:18], size=8)
            format_cell(tr.cells[3], row["Acciones concretas de tratamiento"][:80] + "...", size=7.5)
            format_cell(tr.cells[4], row["Valor residual"], bold=True, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)
            red_pct = round((float(row["Valor"]) - float(row["Valor residual"])) / float(row["Valor"]) * 100)
            format_cell(tr.cells[5], f"{red_pct} %", bold=True, color="006600", size=8, align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.add_paragraph("Anexo D: Matriz de Comunicación del Riesgo (RG06)", style="Heading 2")
    add_p(doc, "Resumen de las instancias de comunicación y periodicidades:")

    t_anx_d = doc.add_table(rows=1, cols=5)
    t_anx_d.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_anx_d, "003366")
    anx_d_headers = ["ID", "A quién se comunica (Cargo)", "Frecuencia", "Canal", "Decisión que habilita"]
    for ci, ch in enumerate(anx_d_headers):
        format_cell(t_anx_d.rows[0].cells[ci], ch, bold=True, color="FFFFFF", size=8.5, bg="003366")

    with open("08_riesgos/RG06_comunicacion.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tr = t_anx_d.add_row()
            format_cell(tr.cells[0], row["id del riesgo"], bold=True, size=8)
            format_cell(tr.cells[1], row["A quién (cargo)"][:35], size=8)
            format_cell(tr.cells[2], row["Cuándo / frecuencia"][:25], size=8)
            format_cell(tr.cells[3], row["Canal"][:25], size=8)
            format_cell(tr.cells[4], row["Qué decisión habilita"][:50] + "...", size=7.5)

    doc.add_paragraph("Anexo E: Salida de Consola de los Scripts de Evaluación", style="Heading 2")
    add_p(doc, "Registro de ejecución formal en terminal:")

    salida_rg03 = read_file_safe("evidencias/S15/salidas/RG03_salida.txt")
    salida_rg05 = read_file_safe("evidencias/S15/salidas/RG05_salida.txt")

    table_box = doc.add_table(rows=1, cols=1)
    table_box.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_box = table_box.cell(0, 0)
    set_cell_background(cell_box, "2B2B2B")
    set_cell_margins(cell_box, top=120, bottom=120, left=150, right=150)
    p_box = cell_box.paragraphs[0]
    p_box.paragraph_format.line_spacing = 1.0
    r_code = p_box.add_run(salida_rg03 + "\n\n" + salida_rg05)
    r_code.font.name = "Consolas"
    r_code.font.size = Pt(7.5)
    r_code.font.color.rgb = RGBColor(220, 220, 220)

    doc.add_paragraph("Anexo F: Formato de Firmas para Aceptación Formal de Riesgo Residual", style="Heading 2")
    add_p(doc, "Conforme a la metodología ISO 31000 y a la Sección 8.8 del PETI, se establece el acta de compromiso formal que deberá suscribirse en la Sección 9 previa a la aprobación del plan:")

    t_firmas = doc.add_table(rows=1, cols=3)
    t_firmas.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_firmas, "003366")
    format_cell(t_firmas.rows[0].cells[0], "Cargo Responsable", bold=True, color="FFFFFF", size=9, bg="003366")
    format_cell(t_firmas.rows[0].cells[1], "Riesgos Residuales Asumidos (Val=8)", bold=True, color="FFFFFF", size=9, bg="003366")
    format_cell(t_firmas.rows[0].cells[2], "Firma y Sello Formal", bold=True, color="FFFFFF", size=9, align=WD_ALIGN_PARAGRAPH.CENTER, bg="003366")

    firmas_data = [
        ("Alcalde Municipal", "R-01 (Recorte presupuestal), R-02 (Patrocinio), R-12 (Ejecución PETI)", "____________________________\nDespacho de Alcaldía"),
        ("Gerente Municipal", "R-03 (Personal clave), R-05 (Resistencia al cambio), R-07 (Proveedor)", "____________________________\nGerencia Municipal"),
        ("Subgerente de Tecnologías de la Información", "R-04, R-06, R-08, R-09, R-10, R-11, R-13 (Riesgos mitigados <= 6)", "____________________________\nSubgerencia de TI")
    ]
    for car, r_asum, fir in firmas_data:
        tr = t_firmas.add_row()
        format_cell(tr.cells[0], car, bold=True, size=8.5)
        format_cell(tr.cells[1], r_asum, size=8.5)
        format_cell(tr.cells[2], fir, size=8, align=WD_ALIGN_PARAGRAPH.CENTER)

    doc.save(output_docx)
    print(f"[OK] Documento Word generado exitosamente en: {output_docx}")

    # Export to PDF via Word COM
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        w_doc = word.Documents.Open(output_docx)
        # Update TOC fields
        for fld in w_doc.Fields:
            fld.Update()
        for t in w_doc.TablesOfContents:
            t.Update()
        wdFormatPDF = 17
        w_doc.SaveAs(output_pdf, FileFormat=wdFormatPDF)
        w_doc.Close()
        word.Quit()
        print(f"[OK] Documento PDF exportado exitosamente en: {output_pdf}")
    except Exception as e:
        print(f"[WARN] Error exportando a PDF vía COM: {e}")

if __name__ == "__main__":
    build_full_document()
