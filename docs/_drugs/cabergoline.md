---
layout: default
title: Cabergoline
parent: Evidencia moderada (L3-L4)
nav_order: 91
evidence_level: L4
indication_count: 5
---

# Cabergoline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Cabergolina: De Trastornos Hiperprolactinémicos a Adenocarcinoma de Hipófisis

## Resumen en Una Frase

Cabergolina es un agonista dopaminérgico que se utiliza para tratar trastornos hiperprolactinémicos y la enfermedad de Parkinson (según la ficha farmacológica; los textos de indicación de la AEMPS no vienen en los datos).
El modelo TxGNN predice que podría ser efectiva para **adenocarcinoma de hipófisis**,
pero actualmente hay **0 ensayos clínicos** y solo **3 publicaciones**, todas reportes de caso, y solo una guarda relación directa con el tema.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos hiperprolactinémicos y enfermedad de Parkinson (fuente: ficha farmacológica; la AEMPS no aporta texto de indicación) |
| Nueva Indicación Predicha | Adenocarcinoma de hipófisis |
| Puntaje de Predicción TxGNN | 99,06% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, cabergolina es un agonista de los receptores de dopamina D2, con actividad adicional sobre receptores serotoninérgicos (5-HT) y adrenérgicos. Su eficacia en la hiperprolactinemia está comprobada.

Mecanísticamente, la activación del receptor D2 suprime la secreción de prolactina y puede reducir el tamaño de tumores hipofisarios que expresan D2. Por eso el vínculo con tumores de hipófisis es plausible.

Sin embargo, la literatura de respaldo es solo de nivel de caso y no aborda el carcinoma hipofisario verdadero. La puntuación alta de TxGNN debe leerse como una señal de investigación, no como prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para esta indicación exacta.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Reporte de caso | Endocr Pract | Respuesta de la corticotropina al tratamiento prolongado con octreotida o cabergolina en una paciente con secreción ectópica de corticotropina tras adrenalectomía |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Reporte de caso | Medicine | Neoplasia endocrina múltiple con curso atípico y una variante del gen MEN1 de significado incierto |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Reporte de caso | Rev Esp Enferm Dig | Linfangiectasias duodenales como primer signo de adenocarcinoma de páncreas en una paciente con adenoma hipofisario tratada con cabergolina (poco relevante para la indicación) |

## Información de Mercado en España

Solo se listan 5 de las 6 autorizaciones, porque los datos recibidos incluyen únicamente esas. El texto de indicación aprobada no está disponible en los datos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 64408 | SOGILEN 1 mg COMPRIMIDOS (Pfizer S.L.) | Comprimido |
| 64409 | SOGILEN 2 mg COMPRIMIDOS (Pfizer S.L.) | Comprimido |
| 69669 | CABERGOLINA TEVA 0,5 mg COMPRIMIDOS EFG (Teva Pharma S.L.U.) | Comprimido |
| 69686 | CABERGOLINA TEVA 2 mg COMPRIMIDOS EFG (Teva Pharma S.L.U.) | Comprimido |
| 69687 | CABERGOLINA TEVA 1 mg COMPRIMIDOS EFG (Teva Pharma S.L.U.) | Comprimido |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta no devolvió interacciones fármaco-fármaco. Devolvió 15 dianas farmacológicas de cabergolina (perfil de afinidad por receptores, no interacciones clínicas):
  - Dopamina: D1, D2, D3, D4 y D5.
  - Serotonina: 5-HT1A, 1B, 1D, 2A, 2B y 2C.
  - Adrenérgicos: α1A, α2A, α2B y α2C.
- **Señales de la literatura recopilada**: para otras indicaciones predichas, el paquete señala valvulopatía cardíaca (asociada a la actividad sobre 5-HT2B), trastornos del control de impulsos y un caso de glaucoma de ángulo cerrado bilateral. Estos riesgos justifican monitoreo si se usa en dosis altas o de forma prolongada.

Para advertencias y contraindicaciones formales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene una puntuación TxGNN alta y un mecanismo plausible (agonismo D2). Pero no hay ensayos clínicos y la literatura consiste en tres reportes de caso, de los cuales solo uno es cercano al tema. Ninguno aborda el carcinoma hipofisario verdadero.

**Para avanzar se necesita:**
- Casos y estudios específicos de carcinoma hipofisario (no adenoma), con confirmación del subtipo tumoral y de la expresión de D2.
- Los datos de mecanismo de acción y el prospecto de la AEMPS (advertencias y contraindicaciones), que faltan actualmente. La falta del prospecto bloquea el cribado de seguridad.
- Un plan de monitoreo ecocardiográfico de valvulopatía si se contempla uso prolongado o en dosis altas.

**Nota:** la predicción vecina "cáncer de hipófisis" (rango 3, puntaje 99,04%) tiene mucha más evidencia. Incluye ensayos de Fase 3 en adenoma no funcionante y en tumor corticotropo, además de una revisión sistemática con metaanálisis. Su evaluación del paquete es L2 con "Proceed with Guardrails", aunque la evidencia corresponde a adenoma y no a carcinoma metastásico. Conviene priorizar esa vía para el análisis de reposicionamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

