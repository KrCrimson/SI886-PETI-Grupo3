# -*- coding: utf-8 -*-
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os
import win32com.client

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
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

def format_cell_text(cell, text, bold=False, color="000000", size=9, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    run.font.bold = bold
    if color != "000000":
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        run.font.color.rgb = RGBColor(r, g, b)

def add_styled_paragraph(parent, text, style="First Paragraph", bold=False, space_after=6, space_before=2):
    p = parent.add_paragraph(style=style)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.font.bold = bold
    return p

def add_bullet(parent, text, bold_prefix="", space_after=3):
    p = parent.add_paragraph(style="First Paragraph")
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run("•  " + bold_prefix + " ")
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
    else:
        r_pre = p.add_run("•  ")
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10.5)
    r_txt = p.add_run(text)
    r_txt.font.name = "Calibri"
    r_txt.font.size = Pt(10.5)
    return p

def main():
    template_path = "SI886-PLANTILLA-TALLER (7).docx"
    output_docx = "SI886-S15-TALLER-Grupo3.docx"
    output_pdf = "SI886-S15-TALLER-Grupo3.pdf"

    # We load the original template
    doc = docx.Document(template_path)

    # 1. Carátula
    doc.paragraphs[11].text = '“Registro de riesgos del plan y matriz de comunicación — Sección 8 del PETI (Caso: Municipalidad Distrital de Alto Selva)”'
    doc.paragraphs[14].text = '“PLANEAMIENTO ESTRATÉGICO DE TI SEC. A”'
    doc.paragraphs[17].text = 'CHOQUEÑA CHOQUE MAURICIO ARIAN · 2023076799'
    doc.paragraphs[27].text = 'TACNA — PERÚ\n2026'

    # Remove the instruction page "Cómo se usa esta plantilla" (P50 to P57)
    for i in range(57, 49, -1):
        p = doc.paragraphs[i]
        p._element.getparent().remove(p._element)

    print(f"Template base cleaned. Paragraphs count: {len(doc.paragraphs)}")

    # Clear everything after Section 1.1 up to end, we will rebuild systematically
    # Let's locate Heading 1 "1. Información sobre el evento práctico"
    body = doc._element.body
    
    # We will build clean content under existing headings
    # Let's write a script that creates a fully populated new document cloning styles from template,
    # or clears and injects elements into the template.
    # Modifying the existing elements in place preserves exact headers and footers!
    print("Modifying document in place...")

if __name__ == "__main__":
    main()
