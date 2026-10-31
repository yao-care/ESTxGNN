---
layout: default
title: Cholecalciferol
parent: Solo predicción del modelo (L5)
nav_order: 177
evidence_level: L5
indication_count: 4
monitor_inn: "Cholecalciferol"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "renal osteodystrophy", "renal tubular acidosis"]
last_modified_at: 2026-10-31
description: "Cholecalciferol: nueva indicación predicha, Acromesomelic dysplasia, Campailla Martinelli type (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Cholecalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Cholecalciferol: Acromesomelic dysplasia, Campailla Martinelli type
{: .text-alpha }

## Resumen en Una Frase

Según los datos compilados para este informe, el colecalciferol (vitamina D3) tiene registradas en el grafo de conocimiento relaciones con osteoporosis, raquitismo, osteomalacia y deficiencia de vitamina D. El modelo TxGNN predice que podría ser efectivo para la **osteodistrofia renal**, con **2 ensayos clínicos** y **20 publicaciones** recuperados. Sin embargo, ningún estudio aborda directamente la osteodistrofia renal con desenlaces óseos, por lo que la evidencia se clasifica como L5.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Acromesomelic dysplasia, Campailla Martinelli type |
| Puntaje de Predicción TxGNN | 0.9978 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

Nota: la predicción mejor clasificada del modelo (displasia acromesomélica tipo Campailla-Martinelli, 0.9978) y la segunda (condrodisplasia craneofacial, 0.9975) carecen de ensayos y literatura y no tienen vínculo mecanístico plausible. Este informe se centra en la osteodistrofia renal, la primera predicción con evidencia clínica relacionada.

## ¿Por qué es Razonable esta Predicción?

No se dispone actualmente de datos detallados sobre el mecanismo de acción en las fuentes consultadas. Según la información conocida, el colecalciferol es un profármaco: se hidroxila en el hígado a 25-hidroxivitamina D y luego en el riñón a calcitriol, la forma activa que regula la absorción de calcio y fosfato y la producción de hormona paratiroidea.

En la enfermedad renal crónica, la hidroxilación renal está alterada y se acumulan fosfato y déficit de vitamina D, lo que provoca hiperparatiroidismo secundario y trastorno mineral y óseo (CKD-MBD), cuya expresión ósea es la osteodistrofia renal. Por ello existe plausibilidad biológica: reponer vitamina D nutricional puede elevar la 25(OH)D, reducir la PTH y favorecer la mineralización.

Aun así, la evidencia de mejora en desenlaces óseos duros (histología, fracturas) es limitada y mixta. Además, la indicación se solapa en gran medida con usos ya conocidos en deficiencia de vitamina D y osteomalacia, por lo que la novedad real es reducida.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00752401](https://clinicaltrials.gov/study/NCT00752401) | Fase 3 | Desconocido | 200 | Colecalciferol frente a placebo en receptores de trasplante renal con déficit de vitamina D; evalúa filtrado glomerular, creatinina, rechazos agudos e infecciones. Población trasplantada, no osteodistrofia |
| [NCT00285467](https://clinicaltrials.gov/study/NCT00285467) | N/A | Completado | 55 | Colecalciferol frente a doxercalciferol en hiperparatiroidismo secundario en ERC estadios 3-4; criterio sustituto (PTH), muestra pequeña |

Ninguno de los dos estudia directamente la osteodistrofia renal como enfermedad.

## Evidencia de Literatura

Se muestran las publicaciones más relevantes (de 20 recuperadas), priorizando estudios clínicos sobre revisiones.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34747516](https://pubmed.ncbi.nlm.nih.gov/34747516/) | 2022 | Análisis secundario de ECA | J Bone Miner Res | La suplementación con colecalciferol atenúa la pérdida ósea en receptores de trasplante renal recientes (193 pacientes aleatorizados) |
| [38397979](https://pubmed.ncbi.nlm.nih.gov/38397979/) | 2024 | Estudio clínico observacional | Biomedicines | Eficacia y seguridad de dosis altas de colecalciferol en pacientes en hemodiálisis con déficit de 25(OH)D |
| [39597015](https://pubmed.ncbi.nlm.nih.gov/39597015/) | 2024 | Estudio prospectivo observacional | Medicina (Kaunas) | Colecalciferol para alcanzar niveles altos de 25(OH)D en hemodiálisis; efecto sobre CKD-MBD |
| [35200136](https://pubmed.ncbi.nlm.nih.gov/35200136/) | 2022 | Estudio prospectivo controlado | Clin Nephrol | Efecto de esteroles de vitamina D sobre la histología ósea en pacientes prediálisis |
| [30274806](https://pubmed.ncbi.nlm.nih.gov/30274806/) | 2019 | Revisión | Nefrologia | Papel incierto de la vitamina D nativa en ERC prediálisis |
| [33922902](https://pubmed.ncbi.nlm.nih.gov/33922902/) | 2021 | Revisión | Nutrients | Efectos de la vitamina D sobre el hueso y el sistema cardiovascular en ERC y trasplante renal |
| [30297082](https://pubmed.ncbi.nlm.nih.gov/30297082/) | 2018 | Informe de taller de consenso | Am J Kidney Dis | Controversias sobre la vitamina D en ERC estadios 3-4 |
| [34626363](https://pubmed.ncbi.nlm.nih.gov/34626363/) | 2022 | Revisión | J Nephrol | Calcifediol de liberación prolongada para hiperparatiroidismo secundario en ERC 3-4 |
| [20671739](https://pubmed.ncbi.nlm.nih.gov/20671739/) | 2010 | Revisión | Kidney Int Suppl | Relación entre enfermedad ósea renal, vitamina D y mortalidad en ERC |
| [21947120](https://pubmed.ncbi.nlm.nih.gov/21947120/) | 2011 | Revisión | Nat Rev Nephrol | Trastornos minerales y óseos en niños con ERC |

## Información de Mercado en España

Los datos disponibles muestran al menos 20 autorizaciones de medicamentos de colecalciferol como principio activo único; la lista puede ser parcial. Los registros no incluyen texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 82411 | THORENS 25.000 UI/2,5 ML solución oral | Solución oral | No disponible |
| 81820 | VIDESIL 25.000 UI solución oral | Solución oral | No disponible |
| 89326 | COLECALCIFEROL ALTER 25.000 UI cápsulas duras | Cápsula dura | No disponible |
| 84727 | DELCRIN 10.000 UI/ML gotas orales en solución | Gotas orales en solución | No disponible |
| 81223 | BENFEROL MENSUAL 25.000 UI cápsulas blandas | Cápsula blanda | No disponible |


## Consideraciones de Seguridad

- **Relaciones de contraindicación registradas en el grafo de conocimiento** (no proceden del prospecto): hipercalcemia, nefrocalcinosis, trastornos del metabolismo del fósforo, hiperparatiroidismo, osteítis fibrosa, enfermedad renal, enfermedad hepática, sarcoidosis, hipertensión, diabetes mellitus, fibrilación auricular, hiperoxaluria primaria, enfermedad de Wilson y hemocromatosis hereditaria, entre otras.
- **Interacciones farmacológicas**: se registra una relación farmacológica con el receptor X farnesoide-β (Nr1h5, ratón), como metabolito; sin nivel de gravedad clínica asignado.
- **Señal de seguridad en la literatura**: un caso pediátrico de sobredosis de vitamina D3 por diagnóstico precipitado de raquitismo en acidosis tubular distal.

Es especialmente relevante la coexistencia de enfermedad renal, hiperfosfatemia e hipercalcemia en la población diana; se debe consultar el prospecto para las advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Ningún ensayo ni publicación estudia directamente la osteodistrofia renal como enfermedad: los ensayos se centran en receptores de trasplante y en hiperparatiroidismo secundario mediante criterios sustitutos. Por tanto, el nivel de evidencia es L5 pese al puntaje alto del modelo. Además, la indicación se solapa con usos ya conocidos de la vitamina D en el déficit y la osteomalacia.

**Para avanzar se necesita:**
- Revisar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente no disponible.
- Datos del mecanismo de acción desde DrugBank.
- Estudios controlados con desenlaces óseos directos (histomorfometría, fracturas) en pacientes con osteodistrofia renal.
- Plan de seguridad para el control de calcio, fósforo y PTH en ERC.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

