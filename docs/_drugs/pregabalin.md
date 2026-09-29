---
layout: default
title: Pregabalin
parent: Solo predicción del modelo (L5)
nav_order: 438
evidence_level: L5
indication_count: 6
---

# Pregabalin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Pregabalina: De Indicación Original (no registrada en los datos) a Tendinitis

## Resumen en Una Frase

La pregabalina es un fármaco comercializado en España (Lyrica y genéricos), pero el paquete de evidencia no recoge el texto de sus indicaciones autorizadas.
El modelo TxGNN predice que podría ser efectiva para **tendinitis**, con **0 ensayos clínicos** y **6 publicaciones** recuperadas.
Ninguna de esas publicaciones evalúa la pregabalina como tratamiento de la tendinitis, por lo que la predicción sigue siendo solo del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Tendinitis |
| Puntaje de Predicción TxGNN | 99.71% |
| Nivel de Evidencia | L5 (el paquete asigna L4, pero la literatura no contiene estudios de pregabalina en tendinitis) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos consultada. Por farmacología general, y no por los datos aportados, la pregabalina se une a la subunidad alfa2-delta de los canales de calcio dependientes de voltaje. Esto reduce la liberación de neurotransmisores excitadores y puede aliviar el dolor de origen neuronal.

Ese mecanismo actúa sobre la transmisión del dolor, no sobre la patología del tendón (degeneración, inflamación o reparación del tejido). Por eso el vínculo mecanístico con la tendinitis es débil. En el mejor de los casos, la pregabalina podría servir como analgésico adyuvante, no como tratamiento de la enfermedad.

El puntaje de 99.71% indica una asociación en el grafo de conocimiento, no evidencia clínica. Los estudios más cercanos son de dolor postoperatorio tras reparación artroscópica del manguito rotador, una cirugía de tendón. Miden el control del dolor y el ahorro de opioides, no el tratamiento de la tendinitis.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | ECA | Arthroscopy | Compara pregabalina oral perioperatoria con el bloqueo interescalénico tras reparación artroscópica del manguito rotador. El título indica puntuaciones de dolor postoperatorio equivalentes. Es dolor postquirúrgico, no tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Cohorte retrospectiva | J Orthop Sci | Evalúa la eficacia analgésica de la pregabalina y su efecto ahorrador de opioides tras reparación del manguito rotador. El resumen disponible está truncado y no incluye resultados. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Reporte de caso/Revisión | Praxis | Discapacidad asociada a fluoroquinolonas tras ciprofloxacino, con tendinopatías entre los efectos adversos. No evalúa la pregabalina como tratamiento. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Reporte de caso | Pain Pract | Atrapamiento del nervio cutáneo femoral posterior tras un maratón, asociado a tendinitis de isquiotibiales. No es un estudio de pregabalina. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Comentario sobre el síndrome piriforme y su tratamiento con neurólisis ciática y liberación del tendón piriforme. No evalúa pregabalina. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclínico | Adv Pharmacol Pharm Sci | Un extracto de *Cissus quadrangularis* atenúa la neuropatía inducida por vincristina en ratas. No involucra pregabalina ni tendinitis. |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. El paquete no incluye el texto de las indicaciones aprobadas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 90014 | Pregabalina Normon 300 mg comprimidos EFG | Comprimido |
| 04279012IP | Lyrica 75 mg cápsulas duras | Cápsula dura |
| 104279015 | Lyrica 100 mg cápsulas duras | Cápsula dura |
| 80287 | Pregabalina Aurovitas 150 mg cápsulas duras EFG | Cápsula dura |
| 104279021 | Lyrica 200 mg cápsulas duras | Cápsula dura |

También existe una presentación de solución oral.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La consulta de interacciones farmacológicas no devolvió resultados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la literatura recuperada no estudia la pregabalina como tratamiento de la tendinitis. El mecanismo conocido solo justificaría un papel analgésico, y el puntaje alto de TxGNN no sustituye la evidencia clínica.

**Para avanzar se necesita:**
- Una búsqueda dirigida de estudios de pregabalina en tendinopatías, y de ensayos que midan dolor o función en tendinitis.
- Las indicaciones autorizadas y el perfil de seguridad, extraídos del prospecto de la AEMPS.
- Los datos de mecanismo de acción de DrugBank.
- Evaluar si el interés real es un uso analgésico adyuvante, y no un tratamiento de la enfermedad tendinosa.

**Nota:** la predicción de **trastorno de migraña** para este mismo fármaco tiene más respaldo (nivel L2, con ECAs pediátricos y revisiones sistemáticas). Conviene evaluarla por separado.

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

