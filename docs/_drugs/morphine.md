---
layout: default
title: Morphine
parent: Solo predicción del modelo (L5)
nav_order: 543
evidence_level: L5
indication_count: 10
---

# Morphine
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

# Morfina: De Enfermedad Diarreica a Síndrome de Piernas Inquietas

## Resumen en Una Frase

La morfina es un analgésico opioide agonista de los receptores mu, delta y kappa. En el grafo de conocimiento utilizado por el modelo figura asociada a la enfermedad diarreica, y en España se comercializa para el dolor intenso.
El modelo TxGNN genera varias predicciones; la que cuenta con más respaldo es el **síndrome de piernas inquietas** (predicción n.º 4 por puntaje, con **1 ensayo clínico** de Fase 1 y **19 publicaciones**). La predicción de mayor puntaje, el **síndrome de dolor miofascial**, tiene solo evidencia indirecta y nivel L4.

> **Nota metodológica:** la indicación de mayor puntaje del modelo es el síndrome de dolor miofascial (99,75 %), pero no existe ningún estudio que muestre que la morfina lo trate, y los opioides no se recomiendan a largo plazo en esa condición. Por ello, este informe se centra en el síndrome de piernas inquietas, que tiene la evidencia más sólida entre las diez candidatas, y resume las demás al final de la sección de conclusiones.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad diarreica (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de piernas inquietas (puntaje más alto del modelo: síndrome de dolor miofascial) |
| Puntaje de Predicción TxGNN | 99,47 % (síndrome de piernas inquietas); 99,75 % (dolor miofascial) |
| Nivel de Evidencia | L3 (síndrome de piernas inquietas) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails (solo síndrome de piernas inquietas refractario); Hold para el resto |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, la morfina es un agonista de los receptores opioides mu (OPRM1), delta (OPRD1) y kappa (OPRK1), y se utiliza en el tratamiento del dolor intenso. Su relación con la enfermedad diarreica (indicación original según el grafo) se explica por el efecto opioide sobre la motilidad intestinal.

En el síndrome de piernas inquietas, los opioides modulan las vías dopaminérgicas y sensitivas implicadas en la enfermedad. Se emplean clínicamente en casos refractarios, es decir, cuando los agonistas dopaminérgicos o los ligandos alfa-2-delta no funcionan, causan aumento paradójico de síntomas (aumentación) o producen efectos adversos. La literatura incluye revisiones, un registro nacional de opioides con seguimiento a 1, 2 y 5 años, y varios reportes de morfina intratecal en dosis bajas para casos graves.

La evidencia es mayormente observacional y se refiere a los opioides como clase, no a la morfina específicamente. Además, existen riesgos de dependencia, escalada de dosis y aparición de síntomas de piernas inquietas al suspender el opioide, por lo que su uso se limitaría a casos refractarios bajo supervisión especializada.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01476124](https://clinicaltrials.gov/study/NCT01476124) | Fase 1 | Completado | 18 | Estudio cruzado doble ciego en voluntarios sanos sobre farmacocinética y tolerabilidad de gabapentina enacarbil y morfina, solos y combinados. No evalúa eficacia en síndrome de piernas inquietas; relevancia solo indirecta. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [41543123](https://pubmed.ncbi.nlm.nih.gov/41543123/) | 2026 | Cohorte | Sleep | Resultados a 5 años del Registro Nacional de Opioides en SPI: efectividad y estabilidad de dosis en pacientes con aumentación por agonistas dopaminérgicos |
| [36697248](https://pubmed.ncbi.nlm.nih.gov/36697248/) | 2023 | Cohorte | Neurology | Seguridad a largo plazo, estabilidad de dosis y eficacia de opioides a 2 años en el registro nacional |
| [32918469](https://pubmed.ncbi.nlm.nih.gov/32918469/) | 2021 | Cohorte | Sleep | Datos basales y a 1 año del registro de opioides en dosis bajas para SPI refractario |
| [27964861](https://pubmed.ncbi.nlm.nih.gov/27964861/) | 2017 | Revisión | Sleep Medicine | Los agonistas opioides alivian síntomas sensitivos y motores del SPI y mejoran el sueño; mecanismo aún especulativo |
| [27310338](https://pubmed.ncbi.nlm.nih.gov/27310338/) | 2016 | Revisión | Expert Opin Drug Metab Toxicol | Aspectos farmacológicos y clínicos de los opioides en SPI grave |
| [39106456](https://pubmed.ncbi.nlm.nih.gov/39106456/) | 2024 | Reporte de caso | Pain | Infusión intratecal prolongada de morfina en dosis bajas que alivia el SPI grave sin inducir tolerancia |
| [31883387](https://pubmed.ncbi.nlm.nih.gov/31883387/) | 2020 | Estudio retrospectivo | Acta Neurol Scand | Eficacia y complicaciones de la bomba implantable de morfina intratecal en SPI refractario |
| [31133964](https://pubmed.ncbi.nlm.nih.gov/31133964/) | 2019 | Reporte de caso | Front Neurol | Mejoría del SPI durante el tratamiento del dolor oncológico con morfina y fentanilo |
| [36692170](https://pubmed.ncbi.nlm.nih.gov/36692170/) | 2023 | Reporte de caso | J Clin Sleep Med | Aparición de SPI durante la retirada supervisada de opioides |
| [29304922](https://pubmed.ncbi.nlm.nih.gov/29304922/) | 2018 | Revisión | Mayo Clin Proc | Uso apropiado de opioides en SPI refractario, donde son pilar del tratamiento |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61909 | MST Continus 200 mg | Comprimido de liberación prolongada | No disponible |
| 59655 | Sevredol 20 mg | Comprimido recubierto con película | No disponible |
| 86588 | Morfina Sun 2 mg/ml | Solución para perfusión en jeringa precargada | No disponible |
| 42221 | Morfina B. Braun 10 mg/ml | Solución inyectable | No disponible |
| 62040 | Oramorph 20 mg/ml | Solución oral | No disponible |

Hay 20 autorizaciones vigentes en total, todas de monofármaco, ninguna cancelada.

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del prospecto): hipertensión, hipotensión ortostática, síndrome de QT largo y torsades de pointes, insuficiencia hepática y enfermedad hepática, enfermedad renal, epilepsia, enfermedad pulmonar obstructiva crónica, úlcera gástrica, pancreatitis, enfermedad de la vesícula biliar, hipotiroidismo, trastornos de ansiedad, trastornos psicóticos y mentales, y deficiencia de potasio.
- **Interacciones farmacológicas:** los datos disponibles describen únicamente la unión a los receptores opioides delta, kappa y mu, sin interacciones medicamentosas clínicas.
- En el contexto del síndrome de piernas inquietas, la literatura destaca los riesgos de dependencia, escalada de dosis y síntomas de piernas inquietas al retirar el opioide.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails** (solo síndrome de piernas inquietas refractario); **Hold** para las demás indicaciones predichas.

**Justificación:**
El síndrome de piernas inquietas cuenta con evidencia observacional consistente (registro nacional a 5 años, revisiones y reportes de morfina intratecal), pero no hay ensayos de eficacia de Fase 2/3 y la evidencia se refiere principalmente a opioides como clase (nivel L3). Las otras nueve predicciones tienen nivel L4–L5, con evidencia indirecta o nula. Algunas, como migraña, tricotilomanía o TDAH, presentan argumentos mecanísticos o de riesgo en contra.

**Resumen de otras predicciones (todas Hold):**
- Dolor miofascial (L4): evidencia indirecta; los opioides no se recomiendan a largo plazo.
- Trastorno bipolar maníaco, síndrome de Tourette, TDAH inatento, tricotilomanía, metahemoglobinemia, migraña con aura de tronco encefálico y trastorno específico del desarrollo (L5): sin respaldo clínico.
- Migraña (L4): las guías desaconsejan los opioides por cefalea por abuso de medicación e hiperalgesia inducida.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones oficiales del prospecto de la AEMPS (dato bloqueante pendiente).
- Completar los datos del mecanismo de acción desde DrugBank.
- Ensayos controlados aleatorizados de morfina específicamente en síndrome de piernas inquietas refractario.
- Definir criterios de selección (refractariedad, aumentación), plan de vigilancia de dependencia y escalada de dosis, y supervisión por especialista.
- Evaluar la compatibilidad de vías de administración (oral frente a intratecal), aún sin determinar.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

