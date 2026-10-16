---
layout: default
title: Nimodipine
parent: Solo predicción del modelo (L5)
nav_order: 567
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Nimodipine: nueva indicación predicha, Hipercolesterolemia familiar homocigota (nivel de evidencia L5). Indicación original: Hemorragia subaracnoidea (según el grafo de conocimiento de TxGNN"
monitor_inn: "nimodipine"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Nimodipino: De Hemorragia Subaracnoidea a Hipercolesterolemia Familiar Homocigota

## Resumen en Una Frase

Nimodipino es un antagonista de los canales de calcio, originalmente utilizado para la hemorragia subaracnoidea (incluida la hemorragia subaracnoidea aneurismática).
El modelo TxGNN predice que podría ser efectivo para **hipercolesterolemia familiar homocigota**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Hemorragia subaracnoidea (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipercolesterolemia familiar homocigota |
| Puntaje de Predicción TxGNN | 99,29% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 7 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según el conocimiento farmacológico general, nimodipino es un bloqueador de los canales de calcio tipo L de la familia de las dihidropiridinas, con acción vasodilatadora preferente sobre la circulación cerebral. Esto explica su uso en la hemorragia subaracnoidea.

La hipercolesterolemia familiar homocigota se debe a defectos en la vía del receptor de LDL (genes LDLR, APOB, PCSK9, LDLRAP1). No existe un vínculo mecanístico directo respaldado por los datos disponibles. Algunos bloqueadores de los canales de calcio se han asociado, en estudios preclínicos, con efectos modestos sobre el manejo vascular de lípidos o la aterosclerosis, pero esta justificación es indirecta y especulativa, y no corrige la deficiencia subyacente del receptor de LDL.

El puntaje alto de TxGNN (0,993) es solo una predicción computacional y no sustituye a la evidencia experimental o clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 58644 | Nimodipino Remontal 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 62504 | Nimodipino Stada 30 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos compilados |
| 84780 | Nimodipino Stadafarma 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 58780 | Brainal 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |
| 58074 | Nimotop 30 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos compilados |

Hay 7 autorizaciones vigentes en total; también existen dos presentaciones en solución para perfusión (Nimotop 0,2 mg/ml, n.º 58075, y Nimodipino Altan 0,2 mg/ml EFG, n.º 67042).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar y trastornos hipotensivos.
- **Interacciones Farmacológicas**: se registran 147 interacciones. Entre las principales:
  - **Mayores**: claritromicina y dolasetrón.
  - **Moderadas**: bupropión, aprepitant, morfina, ácido acetilsalicílico, cimetidina, miconazol, sulfato de magnesio, canagliflozina, dapagliflozina, empagliflozina, dronabinol, nabilona, kanamicina, neomicina y sales de calcio (fosfato, acetato, carbonato y cloruro).
- El efecto hipotensor del nimodipino, junto con el elevado número de interacciones, exige especial atención en cualquier evaluación futura.
- Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (L5), sin ensayos clínicos ni literatura, y no existe un vínculo mecanístico directo con la deficiencia del receptor de LDL. Además, la información de seguridad del prospecto no está disponible.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y ensayos que respalden un vínculo mecanístico con la hipercolesterolemia familiar homocigota.
- Obtener evidencia preclínica que justifique el interés en esta indicación.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.

---

**Nota sobre la segunda predicción (rango 2):** la hipótesis de *síndrome nefrogénico de antidiuresis inapropiada* (puntaje 99,05%) también es de nivel L5, sin evidencia ni vínculo mecanístico respaldado, y con decisión **Hold**.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

