---
layout: default
title: Norgestimate
parent: Solo predicción del modelo (L5)
nav_order: 576
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "norgestimate"
predicted_indications: ["zinc, elevated plasma"]
description: "Norgestimate: nueva indicación predicha, Zinc plasmático elevado (zinc, elevated plasma) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Norgestimate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Norgestimate: Zinc plasmático elevado (zinc, elevated plasma)
{: .text-alpha }

## Resumen en Una Frase

Norgestimato es un progestágeno (profármaco cuyos metabolitos activos incluyen levonorgestrel y norelgestromina), habitualmente combinado con etinilestradiol, y su uso original está asociado al acné y a trastornos relacionados con la menopausia, como la osteoporosis posmenopáusica y la vaginitis atrófica.
El modelo TxGNN predice que podría ser efectivo para **zinc plasmático elevado**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Zinc plasmático elevado (zinc, elevated plasma) |
| Puntaje de Predicción TxGNN | 0.9906 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 1 de 3) |
| Número de Autorizaciones | 3 (vigentes: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, norgestimato es un progestágeno que se combina con etinilestradiol en anticonceptivos orales. Su indicación original es el acné, y mecanísticamente se desconoce si podría ser aplicable a la nueva indicación.

Como conocimiento general (no respaldado por los datos compilados para este informe), los esteroides sexuales y los anticonceptivos orales pueden modificar los niveles circulantes de oligoelementos, como zinc, cobre y ceruloplasmina. Esto sugeriría una posible relación biológica, pero no constituye un vínculo mecanístico demostrado.

Además, el zinc plasmático elevado es un hallazgo de laboratorio y no una enfermedad con una diana terapéutica clara, por lo que el significado clínico de cualquier intervención es incierto. El puntaje de 0,9906 proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| BE141215 | EDELSIN comprimidos (Janssen-Cilag) | Comprimido | No disponible en los datos compilados |
| 83379 | EDELSINE 0,250/0,035 MG comprimidos (Laboratorios Effik) | Comprimido | No disponible en los datos compilados |
| 84027 | LIBERELLE 0,25 MG/0,035 MG comprimidos EFG (Exeltis Healthcare) | Comprimido | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión, epilepsia, trastornos de ansiedad y neuróticos, distimia, porfiria, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, hiperglucemia, diabetes mellitus y cetoacidosis diabética, hipertrigliceridemia, hipercalcemia y nefrocalcinosis, hipotiroidismo, lupus eritematoso sistémico, asma, y carcinoma de mama femenino.
- **Interacciones farmacológicas**: se identificaron 38 interacciones. Entre las de nivel **mayor** figuran sugammadex, griseofulvina, bexaroteno, brigatinib, dabrafenib y encorafenib. Entre las de nivel moderado figuran metreleptina, miltefosina, adalimumab, anakinra, cladribina y enasidenib, entre otras (se muestra solo una parte de la lista).

No se dispone de advertencias ni contraindicaciones del prospecto; consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, sin mecanismo de acción documentado y con una indicación diana que es un hallazgo de laboratorio y no una enfermedad. Además, el perfil de contraindicaciones es amplio.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), requisito previo para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda de literatura sobre anticonceptivos orales/progestágenos y zinc plasmático.
- Definir si el zinc plasmático elevado constituye una indicación clínica con relevancia terapéutica.
- Evaluar la compatibilidad de vía de administración y la similitud con las indicaciones originales (actualmente pendientes).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

