---
layout: default
title: Maraviroc
parent: Solo predicción del modelo (L5)
nav_order: 494
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Maraviroc: nueva indicación predicha, Neoplasia endocrina múltiple (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "MARAVIROC"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

## Maraviroc: De Indicación Original (no especificada en los datos) a Neoplasia Endocrina Múltiple
{: .text-alpha }

## Resumen en Una Frase

Maraviroc es un antagonista del receptor CCR5 comercializado en España (Celsentri y genéricos). Los datos compilados para este informe no incluyen el texto de su indicación autorizada.
El modelo TxGNN predice que podría ser efectivo para **neoplasia endocrina múltiple**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Neoplasia endocrina múltiple |
| Puntaje de Predicción TxGNN | 0.9982 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 6 de 6) |
| Número de Autorizaciones | 6 (comercializadas: 6) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen información detallada sobre el mecanismo de acción. Según la información conocida, maraviroc es un antagonista del receptor de quimiocinas CCR5. La señalización CCR5/CCL5 se ha relacionado con la biología de algunos tumores.

Sin embargo, no existe un vínculo mecanístico establecido entre el bloqueo de CCR5 y los síndromes de neoplasia endocrina múltiple (asociados a MEN1 o RET). No se dispone de ensayos clínicos ni de literatura sobre esta asociación, por lo que la similitud con la indicación original no se ha podido evaluar.

El puntaje alto de TxGNN (0.9982) es solo una predicción computacional y no sustituye a evidencia experimental o clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Otras Predicciones Evaluadas (Contexto)

Para esta misma molécula, el modelo generó otras predicciones. Ninguna supera el nivel L4 de evidencia:

| Posición | Indicación Predicha | Puntaje TxGNN | Nivel | Evidencia disponible |
|------|------|------|------|------|
| 2 | Acné | 0.9976 | L5 | Ninguna |
| 3 | Linfoma cutáneo primario de células T | 0.9972 | L5 | Una revisión sobre ACKR1 (PMID 37006247), sin evidencia clínica de maraviroc |
| 4 | Lupus eritematoso sistémico pediátrico | 0.9971 | L5 | Ninguna |
| 5 | Linfoma cutáneo primario no Hodgkin de células T | 0.9950 | L5 | Misma revisión sobre ACKR1 |
| 6 | Linfoma cutáneo primario de células B | 0.9938 | L5 | Ninguna |
| 7 | Candidiasis | 0.9928 | L5 | Revisión de efectos adversos de la terapia antirretroviral (PMID 21671545); no respalda un uso antifúngico |
| 8 | Deficiencia del componente 4a del complemento | 0.9924 | L5 | Ninguna |
| 9 | Infección por citomegalovirus | 0.9923 | L4 | Estudio de cohorte en pacientes con VIH (PMID 25397464), asociación indirecta |
| 10 | Carcinoma de mama HER2 positivo | 0.9922 | L4 | Estudio preclínico sobre CCL5 y resistencia a trastuzumab (PMID 32404410) |

De todas ellas, el carcinoma de mama HER2 positivo es la que cuenta con un racional mecanístico más plausible: el CCL5 señaliza a través de CCR5, por lo que su bloqueo con maraviroc podría ayudar a superar la resistencia a trastuzumab. La evidencia es preclínica e indirecta, y se considera una pregunta de investigación.

---

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 07418008 | CELSENTRI 300 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viiv Healthcare B.V. | Comercializada |
| 89844 | MARAVIROC WAYMADE 150 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Waymade B.V. | Comercializada |
| 89505 | MARAVIROC TARBIS 300 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |
| 07418003 | CELSENTRI 150 MG COMPRIMIDOS RECUBIERTOS CON PELICULA | COMPRIMIDO RECUBIERTO CON PELÍCULA | Viiv Healthcare B.V. | Comercializada |
| 89845 | MARAVIROC WAYMADE 300 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Waymade B.V. | Comercializada |
| 89504 | MARAVIROC TARBIS 150 MG COMPRIMIDOS RECUBIERTOS CON PELICULA EFG | COMPRIMIDO RECUBIERTO CON PELÍCULA | Tarbis Farma S.L. | Comercializada |

Se muestran las 6 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Existe una sexta autorización vigente (89504, Maraviroc Tarbis 150 mg EFG). Las 6 autorizaciones son de monofármaco y están vigentes.

<!-- review:begin es-lic-20261124-maraviroc-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Existe una sexta autorización vigente (89504, Maraviroc Tarbis 150 mg EFG), no listada arriba por el límite de cinco." Eliminado: el texto decía que esta autorización no figura en la tabla por un límite de cinco filas. La tabla de Información de Mercado en España se genera desde el 2026-11-24 por programa a partir de los datos de CIMA (AEMPS) y la incluye. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261124-maraviroc-1 -->

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: el grafo de conocimiento del modelo asocia maraviroc con enfermedades como hipotensión ortostática, taquicardia postural ortostática, atrofia multisistémica, enfermedad renal (incluida la crónica y terminal), enfermedad hepática, lesión hepática inducida por fármacos, infección crónica por virus de la hepatitis B y C, enfermedad coronaria, infarto de miocardio, isquemia miocárdica, enfermedad de la vesícula biliar y hemoglobinopatías. Deben verificarse con el prospecto oficial.
- **Interacciones farmacológicas**: se identificaron 93 interacciones. Entre ellas destaca una de nivel **Mayor** con **claritromicina**. Las de nivel moderado incluyen aprepitant, dexametasona, cimetidina, eliglustat, naltrexona, clotrimazol, miconazol, rolapitant, cobicistat, deferasibox, diazóxido, fentolamina, prometazina, epoprostenol y fostamatinib, entre otras.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para neoplasia endocrina múltiple se basa solo en el modelo (L5), sin ensayos clínicos, literatura ni vínculo mecanístico establecido. No hay base para avanzar en esta indicación en el estado actual de los datos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones), actualmente un bloqueo para la evaluación de seguridad
- Completar los datos del mecanismo de acción desde DrugBank
- Estudios preclínicos que justifiquen un vínculo entre CCR5 y los síndromes MEN
- Considerar priorizar la línea de carcinoma de mama HER2 positivo (L4, racional CCL5/CCR5) como hipótesis de investigación más sólida
- Evaluar el perfil de seguridad hepático, cardiovascular y de interacciones (en particular inhibidores potentes de CYP3A4 como claritromicina) para cualquier nueva población

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: «no listada arriba por el límite de cinco» | Corregido | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

