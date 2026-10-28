---
layout: default
title: Ethambutol
parent: Solo predicción del modelo (L5)
nav_order: 313
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "ethambutol"
predicted_indications: ["epiglottitis", "laryngitis", "meningococcal infection", "peritonitis", "infectious otitis media"]
description: "Ethambutol: nueva indicación predicha, Epiglotitis (epiglottitis) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Ethambutol
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

## Ethambutol: Epiglotitis (epiglottitis)
{: .text-alpha }

## Resumen en Una Frase

Etambutol es un antimicobacteriano utilizado originalmente para el tratamiento de la tuberculosis pulmonar.
El modelo TxGNN predice que podría ser efectivo para **epiglotitis**, pero sin ensayos clínicos y con solo **1 publicación** (una serie de casos de tuberculosis laríngea de 1989) que se relaciona de forma indirecta con esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Epiglotitis (epiglottitis) |
| Puntaje de Predicción TxGNN | 0.9990 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 2 de 2) |
| Número de Autorizaciones | 2 (vigentes: 2) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la fuente consultada. Según la farmacología general, el etambutol es un agente antimicobacteriano que inhibe las arabinosil transferasas (embB) y altera la síntesis del arabinogalactano de la pared celular de las micobacterias. Su eficacia en tuberculosis pulmonar está bien establecida.

La epiglotitis suele deberse a *Haemophilus influenzae* tipo b, estreptococos o *Staphylococcus aureus*, frente a los cuales el etambutol no tiene actividad conocida. El único vínculo es indirecto: la tuberculosis puede afectar a la laringe y estructuras adyacentes (la epiglotis es uno de los sitios afectados en la tuberculosis laríngea), y en ese caso el etambutol forma parte del régimen antituberculoso estándar.

Por tanto, la puntuación alta del modelo probablemente refleja la cercanía con la tuberculosis y no una nueva indicación real. Se trataría de la misma indicación antimicobacteriana aplicada a otra localización anatómica, no de un reposicionamiento genuino para la epiglotitis en general.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Serie de casos | The European Respiratory Journal | 41 casos de tuberculosis laríngea (1975-1985). Todos tenían tuberculosis pulmonar actual o previa. La epiglotis fue el segundo sitio más afectado tras las cuerdas vocales. Los pacientes recibieron habitualmente isoniazida, rifampicina y etambutol. |

La evidencia no aísla la contribución del etambutol y no corresponde a epiglotitis de causa no tuberculosa.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 44430 | Myambutol 400 mg comprimidos recubiertos | Comprimido recubierto | No disponible |
| 65904 | Rimstar comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto)**: enfermedad renal, piouréter, gota, retinopatía diabética, catarata diabética y neuritis óptica.
- **Interacciones Farmacológicas**: se identificaron 112 interacciones. Entre las de nivel moderado figuran metronidazol, ácido picosulfúrico, naltrexona, rosuvastatina, simvastatina, tinidazol e hidróxido de aluminio. Otras con nivel no clasificado incluyen clotrimazol, pantoprazol, morfina, omeprazol, lansoprazol, vancomicina, prednisona, nistatina, hidrocortisona, cloruro de potasio, sulfasalazina, prednisolona y ranitidina.

Las advertencias y contraindicaciones del prospecto de la AEMPS no estaban disponibles; consultar el prospecto para la información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción carece de ensayos clínicos y de un mecanismo plausible para las causas habituales de epiglotitis; la única evidencia es una serie de casos de tuberculosis laríngea, que corresponde a la indicación antituberculosa ya existente. El puntaje alto del modelo parece un artefacto de proximidad en la red con la tuberculosis.

**Para avanzar se necesita:**
- Obtener y revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Aclarar si el interés se limita a la epiglotitis tuberculosa (extensión de la indicación actual) o a otras causas, para las que no hay respaldo.
- Valorar con cautela el perfil de seguridad, en particular la neuritis óptica, la enfermedad renal y las interacciones.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

