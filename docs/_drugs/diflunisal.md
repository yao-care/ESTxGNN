---
layout: default
title: Diflunisal
parent: Solo predicción del modelo (L5)
nav_order: 249
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Diflunisal: nueva indicación predicha, Displasia acromesomélica, tipo Hunter-Thompson (nivel de evidencia L5). Indicación original: Artritis reumatoide (según el grafo de conocimiento"
monitor_inn: "DIFLUNISAL"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "spondyloarthropathy, susceptibility to", "myosclerosis", "ankylosing spondylitis", "brachyolmia", "hypermobility of coccyx", "rheumatoid vasculitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "inflammatory spondylopathy"]
---

# Diflunisal
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Diflunisal: De Artritis Reumatoide a Displasia Acromesomélica tipo Hunter-Thompson

## Resumen en Una Frase

Diflunisal es un antiinflamatorio no esteroideo (AINE), utilizado originalmente en artritis reumatoide, artrosis y otras artropatías.
El modelo TxGNN predice que podría ser efectivo para **displasia acromesomélica tipo Hunter-Thompson**, una displasia esquelética genética muy rara, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Artritis reumatoide (según el grafo de conocimiento; la autorización española no incluye texto de indicación) |
| Nueva Indicación Predicha | Displasia acromesomélica, tipo Hunter-Thompson |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Por su clase, diflunisal es un AINE derivado del ácido salicílico que inhibe la ciclooxigenasa y reduce la síntesis de prostaglandinas. Su eficacia como antiinflamatorio y analgésico en enfermedades reumáticas es conocida.

La displasia acromesomélica tipo Hunter-Thompson es un trastorno esquelético hereditario raro, asociado al gen *GDF5* (CDMP1). No es una enfermedad de origen inflamatorio, y no se identifica un vínculo plausible con la inhibición de la COX. El puntaje elevado probablemente refleja la cercanía en el grafo de conocimiento con términos musculoesqueléticos (artropatía, artrosis) y no una justificación farmacológica.

Por tanto, esta predicción debe considerarse una señal estadística del modelo sin respaldo mecanístico ni clínico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1251929001 | ATTROGY 250 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

La autorización es de tipo monofármaco, está vigente y su titular es Purpose Pharma International AB.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): hipertensión y trastornos hipertensivos, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, úlcera péptica (incluida la activa), trastornos de la coagulación, infarto de miocardio y trombosis coronaria, enfermedad cardiovascular y cardiopatía, hemoglobinopatías y piouréter.
- **Interacciones farmacológicas**: se identificaron 100 interacciones, y las 20 primeras listadas son de nivel moderado. Las principales son:
  - Corticoides: hidrocortisona, triamcinolona, dexametasona, betametasona y budesonida.
  - Antidiabéticos: metformina, clorpropamida, glimepirida y varias insulinas (aspart, degludec, detemir y glargina).
  - Salicilatos y aminosalicilatos: ácido acetilsalicílico, mesalazina y balsalazida.
  - Laxantes y soluciones de preparación intestinal, además de sales de potasio: ácido picosulfúrico, polietilenglicol con electrolitos, sulfato de sodio, citrato de potasio y bicarbonato de potasio.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura. Además, la enfermedad es un trastorno genético esquelético sin componente inflamatorio, por lo que no hay un vínculo mecanístico plausible con un AINE.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis biológica que conecte diflunisal con la vía de *GDF5*/BMP.
- Evidencia preclínica o clínica específica de esta enfermedad; hoy no hay ninguna.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS, ya que no están disponibles en los datos compilados.
- Considerar otras predicciones del mismo análisis con más respaldo. La **espondilitis anquilosante** (puntaje 99.98%, nivel L3) cuenta con un estudio doble ciego aleatorizado de 1986 que compara diflunisal con fenilbutazona en 38 pacientes (PMID 3524970). Es una evidencia antigua y de pequeña escala, y su novedad es limitada porque diflunisal ya se usa en patologías reumáticas inflamatorias.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

