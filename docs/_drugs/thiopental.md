---
layout: default
title: Thiopental
parent: Solo predicción del modelo (L5)
nav_order: 791
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Thiopental: nueva indicación predicha, Tricotilomanía (nivel de evidencia L5). Indicación original: Epilepsia…"
monitor_inn: "thiopental"
predicted_indications: ["trichotillomania", "Prinzmetal angina", "migraine disorder", "Tourette syndrome", "migraine with brainstem aura", "obsolete bundle branch block", "substance abuse/dependence", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Thiopental
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Tiopental: De Epilepsia a Tricotilomanía

## Resumen en Una Frase

Tiopental es un barbitúrico de acción ultracorta, comercializado en España como polvo para solución inyectable, y cuyas indicaciones originales en el grafo de conocimiento son la epilepsia, el pseudotumor cerebral y la hipertensión intracraneal.
El modelo TxGNN predice que podría ser efectivo para **tricotilomanía**, pero no hay **ningún ensayo clínico** ni **ninguna publicación** que respalde esta dirección: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Epilepsia, pseudotumor cerebral e hipertensión intracraneal (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Tricotilomanía |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tiopental es un barbitúrico que potencia la inhibición mediada por el receptor GABA-A y actúa como depresor del sistema nervioso central. Su eficacia en cuadros convulsivos y en el control de la presión intracraneal es la base de sus indicaciones originales.

Para la tricotilomanía, sin embargo, **no se identifica un fundamento mecanístico plausible**. Este trastorno se trata con terapia conductual (reversión de hábito) y con fármacos que actúan sobre vías serotoninérgicas, glutamatérgicas o dopaminérgicas, no con depresores GABAérgicos. El puntaje elevado de TxGNN es una predicción basada solo en la estructura del grafo, sin respaldo clínico ni bibliográfico.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 49591 | TIOBARBITAL B. BRAUN 0,5 G POLVO PARA SOLUCION INYECTABLE | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |
| 18329 | TIOBARBITAL B. BRAUN 1 G POLVO PARA SOLUCION INYECTABLE | Polvo y disolvente para solución inyectable | No disponible en los datos compilados |

## Consideraciones de Seguridad

- **Contraindicaciones sugeridas por el grafo de conocimiento** (no provienen del texto del prospecto): enfermedad renal e insuficiencia renal, uremia, enfermedad hepática, enfermedad de la vesícula biliar, asma (intrínseca y alérgica), trastornos hipotensivos, anemia, insuficiencia suprarrenal (incluida la enfermedad de Addison y la hiperplasia suprarrenal congénita), miastenia gravis y enfermedades de la unión neuromuscular, porfiria (variegata y aguda intermitente), mixedema e hipotiroidismo.
- **Interacciones farmacológicas**: se registraron 45 interacciones. Las de nivel **mayor** son:
  - **Etanol**
  - **Warfarina**

  Entre las de nivel moderado figuran morfina, codeína, hidrocodona, dextrometorfano, doxiciclina, dronabinol, nabilona, cetirizina, carbinoxamina, clemastina, nitisinona, azul de metileno y yoduro I-123/I-131. Entre las menores figuran piridoxina, cimetidina, sulfasalazina y prometazina. La mayoría de las combinaciones con depresores del SNC implican efecto sedante aditivo.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para tricotilomanía no tiene ensayos clínicos ni literatura, carece de fundamento mecanístico plausible y el perfil de un anestésico barbitúrico inyectable resulta poco compatible con un trastorno crónico del control de impulsos. No hay base para avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) y del texto de indicaciones y de seguridad del prospecto de la AEMPS.
- Evidencia preclínica o clínica que vincule la modulación GABAérgica con la tricotilomanía.
- Evaluación de la viabilidad de la vía de administración (solo existe formulación inyectable) y del perfil riesgo-beneficio.

**Otras predicciones revisadas (todas en Hold):**
- **Epilepsia del lóbulo frontal** (L4) y **epilepsia de ausencia** (L4): la literatura es indirecta (pruebas diagnósticas con tiopental, casos clínicos, estado epiléptico refractario). Además, son cercanas a la indicación ya existente, por lo que no constituyen un verdadero reposicionamiento. En la epilepsia de ausencia, el mecanismo podría incluso ser desfavorable.
- **Abuso/dependencia de sustancias** (L4): la literatura trata de tolerancia y abstinencia a barbitúricos; el tiopental tiene riesgo de abuso, por lo que un uso terapéutico sería potencialmente dañino.
- **Angina de Prinzmetal, migraña (incluida con aura de tronco encefálico), síndrome de Tourette, bloqueo de rama (término obsoleto) y síndrome nefrogénico de antidiuresis inapropiada** (L5): sin fundamento mecanístico ni evidencia pertinente; los pocos artículos recuperados no evalúan tiopental como tratamiento.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

