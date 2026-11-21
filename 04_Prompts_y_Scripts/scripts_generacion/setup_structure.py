# -*- coding: utf-8 -*-
"""
Script integral para estructurar y poblar el repositorio GitHub
IsraQuanDev/AI_Builder_Challenge_Finanzas-Operaciones con carpetas profesionales,
análisis técnicos exhaustivos, evidencias, dashboard y documentación de entrega.
Estudiante: Francisco Israel Mesillas Hernández
"""
import os
import shutil

REPO_ROOT = r"C:\Users\52477\Desktop\challengeAIbuilder"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# 1. Definición de Carpetas
DIR_ESTRATEGIA = os.path.join(REPO_ROOT, "01_Estrategia_Ruta0_Corporativa")
DIR_LEAN = os.path.join(REPO_ROOT, "02_Diagnostico_Lean_Operaciones")
DIR_FINANZAS = os.path.join(REPO_ROOT, "03_Panel_Financiero_y_Predictivo")
DIR_PROMPTS = os.path.join(REPO_ROOT, "04_Prompts_y_Scripts")
DIR_SCRIPTS = os.path.join(DIR_PROMPTS, "scripts_generacion")
DIR_EVIDENCIAS = os.path.join(REPO_ROOT, "05_Evidencias_y_Entrega_Alura")

for d in [DIR_ESTRATEGIA, DIR_LEAN, DIR_FINANZAS, DIR_PROMPTS, DIR_SCRIPTS, DIR_EVIDENCIAS]:
    ensure_dir(d)

# Mover scripts de generación a 04_Prompts_y_Scripts/scripts_generacion
for script_name in ["generate_docs.py", "generate_html_dashboard.py", "generate_markdown_report.py"]:
    src = os.path.join(REPO_ROOT, script_name)
    dst = os.path.join(DIR_SCRIPTS, script_name)
    if os.path.exists(src):
        shutil.copy2(src, dst)

# Copiar dashboard_financiero_taranis_black.html a 03_Panel_Financiero_y_Predictivo
src_dash = os.path.join(REPO_ROOT, "dashboard_financiero_taranis_black.html")
dst_dash = os.path.join(DIR_FINANZAS, "dashboard_financiero_taranis_black.html")
if os.path.exists(src_dash):
    shutil.copy2(src_dash, dst_dash)

print("Carpetas base creadas y archivos distribuidos.")
