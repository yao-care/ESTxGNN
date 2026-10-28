---
layout: default
title: Triprolidine
parent: Solo predicción del modelo (L5)
nav_order: 830
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "triprolidine"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
description: "Triprolidine: nueva indicación predicha, Nasal cavity disease (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Triprolidine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

## Triprolidine: Nasal cavity disease
{: .text-alpha }

## Resumen en Una Frase

Triprolidina es un antihistamínico H1 de primera generación, utilizado originalmente para tratar la rinitis alérgica, el resfriado común y otros cuadros alérgicos y de vías respiratorias altas.
Actualmente no hay **ensayos clínicos** registrados y solo se dispone de **2 publicaciones** con relevancia indirecta o limitada.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Nasal cavity disease |
| Puntaje de Predicción TxGNN | 0.9983 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 3) |
| Número de Autorizaciones | 3 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la triprolidina es un antagonista de los receptores H1 de primera generación. En la urticaria alérgica, la liberación de histamina por los mastocitos provoca el habón y el eritema, por lo que el bloqueo H1 es mecanísticamente coherente.

La relación con las indicaciones originales es muy estrecha: la urticaria y el angioedema ya figuran entre sus indicaciones conocidas, junto con la rinitis alérgica, la conjuntivitis atópica y la dermatografismo familiar.

Conviene tener en cuenta que, para otras predicciones del modelo (urticaria por frío, enfermedad de la cavidad nasal, faringitis, laringofaringitis aguda, dermatitis atópica recalcitrante y respuesta de IgE atópica), la evidencia es indirecta o inexistente (nivel L4–L5), y todas quedan en "Hold".

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2568212](https://pubmed.ncbi.nlm.nih.gov/2568212/) | 1989 | Revisión | Clinical Pharmacy | Revisa los antihistamínicos H1 no sedantes (terfenadina, astemizol, loratadina, acrivastina); la acrivastina es un metabolito derivado de la triprolidina. Evidencia indirecta. |
| [14283425](https://pubmed.ncbi.nlm.nih.gov/14283425/) | 1965 | Estudio experimental | British Journal of Dermatology | Respuesta de la piel a la radiación ultravioleta con triprolidina; no trata directamente la urticaria. |

**Evidencia relacionada con otras predicciones (indirecta):**

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | ECA cruzado doble ciego | Dermatologica | En 18 pacientes con urticaria por frío, acrivastina (derivado de la triprolidina) y ciproheptadina redujeron los habones frente a placebo, con mayor efecto de la acrivastina. No evalúa triprolidina. |
| [6377256](https://pubmed.ncbi.nlm.nih.gov/6377256/) | 1984 | ECA doble ciego | Pediatric Infectious Disease | 142 niños con nasofaringitis purulenta; cefalexina sola o combinada con pseudoefedrina/triprolidina frente a placebo. No establece eficacia en faringitis. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 52677 | INISTON EXPECTORANTE Y DESCONGESTIVO JARABE | Jarabe | No disponible |
| 38249 | INISTON TOS Y CONGESTION JARABE | Jarabe | No disponible |
| 72689 | CINFATOS DESCONGESTIVO SOLUCION ORAL | Solución oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión, epilepsia, enfermedad renal, enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar, hipotiroidismo, úlcera péptica, enfermedad inflamatoria intestinal, diabetes mellitus y cetoacidosis diabética, hiperplasia prostática benigna, enfermedad coronaria, infarto de miocardio, aterosclerosis, hipertensión ocular, enfermedades de la conducción cardíaca, parada cardíaca súbita, entre otras.
- **Interacciones farmacológicas**: se identificaron 290 interacciones. Las de gravedad **mayor** incluyen cloruro de potasio y citrato de potasio. Las de gravedad **moderada** incluyen principalmente anticolinérgicos y depresores del SNC: atropina, escopolamina, hiosciamina, glicopirronio, diciclomina, loperamida, morfina, metoclopramida, dronabinol y nabilona.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de alta puntuación, pero casi no aporta novedad, ya que la urticaria y el angioedema ya son indicaciones conocidas. No existen ensayos clínicos ni literatura directa con triprolidina, y los antihistamínicos de segunda generación son hoy el tratamiento estándar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), lo cual es un requisito bloqueante para el cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura específica de triprolidina en urticaria.
- Definir si existe un valor diferencial frente a los antihistamínicos de segunda generación.
- Evaluar el perfil de seguridad dadas las numerosas contraindicaciones del grafo y las interacciones anticolinérgicas.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

