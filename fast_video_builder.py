# -*- coding: utf-8 -*-
"""
Generador ultra-rápido de video MP4 usando ffmpeg nativo directo.
"""
import os
import subprocess
import imageio_ffmpeg
from PIL import Image
from gtts import gTTS
import matplotlib.pyplot as plt
import matplotlib.patches as patches

WORKSPACE = r"C:\Users\52477\Desktop\challengeAIbuilder"
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

def create_slide_1():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor('#0b0f19')
    ax.set_facecolor('#0b0f19')

    # Header Badges
    fig.text(0.5, 0.88, "PROGRAMA ORACLE NEXT EDUCATION (ONE) & ALURA LATAM", 
             fontsize=16, fontweight='bold', color='#94a3b8', ha='center', family='sans-serif')
    fig.text(0.5, 0.82, "CHALLENGE ONE G11 — AI FOR BUSINESS", 
             fontsize=22, fontweight='bold', color='#f59e0b', ha='center', family='sans-serif')

    # Main Title Box
    title_box = patches.FancyBboxPatch((0.12, 0.42), 0.76, 0.34, boxstyle="round,pad=0.02",
                                       fc='#1e293b', ec='#38bdf8', lw=3, transform=fig.transFigure)
    fig.patches.append(title_box)

    fig.text(0.5, 0.65, "CONSULTORÍA ESTRATÉGICA DE IA — TARANIS BLACK", 
             fontsize=26, fontweight='bold', color='#ffffff', ha='center', family='sans-serif')
    fig.text(0.5, 0.56, "RUTA 4: IA PARA FINANZAS Y OPERACIONES", 
             fontsize=20, fontweight='bold', color='#38bdf8', ha='center', family='sans-serif')
    fig.text(0.5, 0.47, "SIPOC  •  Ishikawa (6M)  •  Panel Financiero Inteligente  •  Simulador Predictivo Q1 2027", 
             fontsize=14, color='#cbd5e1', ha='center', family='sans-serif')

    # Presenter Information Box
    info_box = patches.FancyBboxPatch((0.20, 0.14), 0.60, 0.22, boxstyle="round,pad=0.015",
                                      fc='#111827', ec='#334155', lw=2, transform=fig.transFigure)
    fig.patches.append(info_box)

    fig.text(0.5, 0.28, "ESTUDIANTE / CONSULTOR LÍDER:", fontsize=12, fontweight='bold', color='#f59e0b', ha='center', family='sans-serif')
    fig.text(0.5, 0.22, "Francisco Israel Mesillas Hernández", fontsize=18, fontweight='bold', color='#ffffff', ha='center', family='sans-serif')
    fig.text(0.5, 0.17, "israel.mecillas@gmail.com  |  Cohorte G11  |  Noviembre 2026", fontsize=12, color='#94a3b8', ha='center', family='sans-serif')

    ax.axis('off')
    path = os.path.join(WORKSPACE, "slide1_raw.png")
    plt.savefig(path, bbox_inches='tight', facecolor=fig.get_facecolor(), dpi=100)
    plt.close()
    return standardize_image("slide1_raw.png", "slide1_1080p.jpg")

def create_slide_6():
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    fig.patch.set_facecolor('#0b0f19')
    ax.set_facecolor('#0b0f19')

    fig.text(0.5, 0.90, "TARANIS BLACK | CONCLUSIÓN EJECUTIVA Y RETORNO DE INVERSIÓN", 
             fontsize=22, fontweight='bold', color='#ffffff', ha='center', family='sans-serif')
    fig.text(0.5, 0.85, "Impacto Cuantitativo, Gobernanza Responsable y Resumen de Entrega (ONE G11)", 
             fontsize=14, color='#10b981', ha='center', family='sans-serif')

    kpis = [
        ("INVERSIÓN TOTAL AÑO 1", "USD 185,000", "Infraestructura, APIs y capacitación", "#38bdf8", 0.08),
        ("BENEFICIO ANUAL BRUTO", "USD 2,980,000", "Fletes, cancelaciones y morosidad", "#10b981", 0.30),
        ("ROI ESTIMADO FORMAL", "1,510.8%", "Beneficio neto: USD 2.79M", "#f59e0b", 0.52),
        ("PAYBACK ESTIMADO", "22 Días Hábiles", "0.74 meses de recuperación", "#a855f7", 0.74)
    ]
    for title, val, sub, col, x in kpis:
        c_box = patches.FancyBboxPatch((x, 0.52), 0.18, 0.26, boxstyle="round,pad=0.01",
                                       fc='#1e293b', ec=col, lw=2.5, transform=fig.transFigure)
        fig.patches.append(c_box)
        fig.text(x + 0.012, 0.71, title, fontsize=11, fontweight='bold', color='#94a3b8', family='sans-serif')
        fig.text(x + 0.012, 0.61, val, fontsize=20, fontweight='bold', color=col, family='sans-serif')
        fig.text(x + 0.012, 0.55, sub, fontsize=10, color='#cbd5e1', family='sans-serif')

    gov_box = patches.FancyBboxPatch((0.08, 0.12), 0.84, 0.34, boxstyle="round,pad=0.01",
                                     fc='#111827', ec='#334155', lw=2, transform=fig.transFigure)
    fig.patches.append(gov_box)

    fig.text(0.11, 0.39, "PILAR DE GOBERNANZA & SUPERVISIÓN HUMANA (HITL):", fontsize=13, fontweight='bold', color='#f59e0b', family='sans-serif')
    gov_bullets = (
        "• Human-in-the-Loop Obligatorio: Aprobación del Controller para pedidos de crédito >USD 50k y ajustes >USD 5,000.\n"
        "• Cumplimiento Normativo LGPD (Brasil): Enmascaramiento de datos personales (CPF) y política estricta de Zero Data Retention.\n"
        "• Reducción Operativa: El cierre mensual contable se reduce de 7 a 2 días hábiles, liberando 123 horas/mes por analista.\n"
        "• Repositorio Oficial y Documentos: GitHub IsraQuanDev/AI_Builder_Challenge_Finanzas-Operaciones"
    )
    fig.text(0.11, 0.18, gov_bullets, fontsize=12, color='#e2e8f0', family='sans-serif', linespacing=1.6)

    ax.axis('off')
    path = os.path.join(WORKSPACE, "slide6_raw.png")
    plt.savefig(path, bbox_inches='tight', facecolor=fig.get_facecolor(), dpi=100)
    plt.close()
    return standardize_image("slide6_raw.png", "slide6_1080p.jpg")

def standardize_image(src_filename, out_filename):
    src_path = os.path.join(WORKSPACE, src_filename)
    out_path = os.path.join(WORKSPACE, out_filename)
    canvas = Image.new("RGB", (1920, 1080), (11, 15, 25))
    if os.path.exists(src_path):
        img = Image.open(src_path)
        if img.mode in ('RGBA', 'LA'):
            bg = Image.new('RGB', img.size, (11, 15, 25))
            bg.paste(img, mask=img.split()[-1])
            img = bg
        else:
            img = img.convert('RGB')
        img.thumbnail((1880, 1040), Image.Resampling.LANCZOS)
        x = (1920 - img.width) // 2
        y = (1080 - img.height) // 2
        canvas.paste(img, (x, y))
    canvas.save(out_path, format="JPEG", quality=95)
    return out_path

def main():
    print("1. Generando diapositivas 1080p con dimensiones exactas...")
    s1 = create_slide_1()
    s2 = standardize_image("captura_dashboard_financiero.png", "slide2_1080p.jpg")
    s3 = standardize_image("matriz_sipoc_taranis_black.png", "slide3_1080p.jpg")
    s4 = standardize_image("diagrama_ishikawa_taranis_black.png", "slide4_1080p.jpg")
    s5 = standardize_image("matriz_esfuerzo_impacto_taranis_black.png", "slide5_1080p.jpg")
    s6 = create_slide_6()

    slides = [
        (s1, "slide1_audio.mp3",
         "Hola, qué tal comité evaluador de Oracle Next Education y Alura Latam. "
         "Mi nombre es Francisco Israel Mesillas Hernández, perteneciente a la cohorte G11 del programa ONE AI for Business. "
         "A continuación presento la consultoría estratégica de Inteligencia Artificial para la empresa simulada Taranis Black, "
         "enfocada en la Ruta 4: Finanzas y Operaciones."),

        (s2, "slide2_audio.mp3",
         "Iniciamos con el diagnóstico financiero. Taranis Black alcanzó ventas brutas por 48.5 millones de dólares, "
         "cumpliendo el 99.8 por ciento de la meta presupuestada. Sin embargo, su EBITDA colapsó un 41.4 por ciento, perdiendo más de 4 millones de dólares "
         "de margen operativo. La causa principal radica en fricciones operativas por conciliar manualmente tres hojas de cálculo y un ERP legado, "
         "desencadenando un sobrecosto de 1.36 millones en fletes urgentes y 1.25 millones en cancelaciones por lentitud."),

        (s3, "slide3_audio.mp3",
         "Al analizar el macroproceso de facturación y despacho con la matriz SIPOC, identificamos que de los cinco días hábiles de tiempo de ciclo total, "
         "el tiempo de procesamiento de valor agregado es de únicamente 65 minutos. Esto revela una eficiencia de flujo del 2.7 por ciento "
         "y un 97.3 por ciento de desperdicio burocrático y tiempos muertos."),

        (s4, "slide4_audio.mp3",
         "En el Diagrama de Ishikawa identificamos las causas raíz a través de las 6M: principalmente la retención de 48 horas en aprobación de crédito "
         "en la bandeja de gerencia, una tasa de error del 6.8 por ciento en la facturación manual, y la desincronización crítica de datos entre áreas."),

        (s5, "slide5_audio.mp3",
         "Para solucionar estos cuellos de botella, estructuramos una hoja de ruta con tres iniciativas de IA en nuestra Matriz de Esfuerzo por Impacto: "
         "Primero, un Quick Win en el Mes 1 con Ingesta Inteligente OCR para procesar pedidos en 3 minutos. "
         "Segundo, un Motor Predictivo de Scoring Crediticio en el Mes 2 para aprobar créditos en 15 minutos. "
         "Y tercero, un Conciliador Financiero Continuo en el Mes 3 para reducir el cierre contable mensual de 7 a 2 días hábiles."),

        (s6, "slide6_audio.mp3",
         "Garantizamos además una gobernanza estricta con supervisión humana obligatoria y cumplimiento de la ley LGPD de Brasil. "
         "Con una inversión total de 185 mil dólares, el proyecto captura 2.98 millones de beneficio anual, "
         "entregando un retorno de inversión superior al 1,500 por ciento y un periodo de recuperación de solo 22 días laborables. "
         "Muchas gracias por su atención y evaluación.")
    ]

    clip_files = []
    print("2. Generando audios TTS y clips de video...")
    for idx, (img_path, audio_name, text) in enumerate(slides, start=1):
        audio_path = os.path.join(WORKSPACE, audio_name)
        if not os.path.exists(audio_path):
            print(f"Generando TTS para Slide {idx}...")
            tts = gTTS(text=text, lang='es', slow=False)
            tts.save(audio_path)
        
        clip_path = os.path.join(WORKSPACE, f"part_{idx}.mp4")
        cmd = [
            FFMPEG, "-y",
            "-loop", "1",
            "-i", img_path,
            "-i", audio_path,
            "-vf", "scale=1920:1080,setsar=1",
            "-c:v", "libx264",
            "-tune", "stillimage",
            "-c:a", "aac",
            "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            "-r", "24",
            clip_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            print(f"Error generando part_{idx}: {res.stderr}")
        else:
            print(f"Clip {idx} listo ({os.path.getsize(clip_path)} bytes).")
        clip_files.append(clip_path)

    concat_list_path = os.path.join(WORKSPACE, "concat_list.txt")
    with open(concat_list_path, "w", encoding="utf-8") as f:
        for c in clip_files:
            f.write(f"file '{c.replace(os.sep, '/')}'\n")

    final_mp4 = os.path.join(WORKSPACE, "video_demostracion_taranis_black.mp4")
    print(f"3. Concatenando los 6 clips en video final: {final_mp4}...")
    cmd_concat = [
        FFMPEG, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        final_mp4
    ]
    res_concat = subprocess.run(cmd_concat, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if res_concat.returncode == 0:
        print(f"¡ÉXITO TOTAL! Video completo generado: {final_mp4}")
        size_mb = os.path.getsize(final_mp4) / (1024 * 1024)
        print(f"Tamaño final del MP4: {size_mb:.2f} MB")
    else:
        print(f"Error en concatenación: {res_concat.stderr}")

if __name__ == '__main__':
    main()
