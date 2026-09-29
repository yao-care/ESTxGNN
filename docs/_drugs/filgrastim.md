---
layout: default
title: Filgrastim
parent: Solo predicción del modelo (L5)
nav_order: 232
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: De Indicación Original No Registrada a Trastorno de Liberación Primaria de las Plaquetas

## Resumen en Una Frase

Filgrastim es un factor estimulante de colonias de granulocitos (G-CSF). En los registros de AEMPS analizados no consta el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de liberación primaria de las plaquetas**,
con **14 ensayos clínicos** y **1 publicación** vinculados. Ninguno estudia directamente esa enfermedad, por lo que la predicción no tiene respaldo clínico real.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (las autorizaciones de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas |
| Puntaje de Predicción TxGNN | 99.998% |
| Nivel de Evidencia | L4 (solo evidencia indirecta) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Filgrastim actúa sobre el receptor de G-CSF. Impulsa la proliferación del linaje de neutrófilos y la movilización de células madre hematopoyéticas. No se conoce ningún mecanismo por el que afecte la liberación de gránulos plaquetarios ni la función de las plaquetas.

La relación con la nueva indicación es sobre todo de vecindad en el grafo de conocimiento. Los 14 ensayos vinculados son en su mayoría trasplantes de progenitores hematopoyéticos o profilaxis de la enfermedad de injerto contra huésped (EICH), donde el G-CSF es, como mucho, un agente de apoyo o movilización. Todos fueron clasificados con relevancia baja (grado C). El puntaje tan alto (0.99998) probablemente es un artefacto de proximidad en el grafo y no una señal de eficacia.

Las otras nueve indicaciones predichas tampoco tienen respaldo mecanístico. Incluyen pseudo-enfermedad de von Willebrand, trombastenia de Glanzmann, síndrome de Scott y trombocitopenia aloinmune fetal y neonatal. Ninguna tiene ensayos ni literatura directamente relacionados.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Terminado | 200 | Trasplante de progenitores de donante no emparentado en neoplasias hematológicas. No estudia trastornos plaquetarios. |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Fase 2 | Completado | 64 | Trasplante autólogo con selección CD34+ frente a sin selección en linfoma de células del manto y linfoma B difuso de células grandes. El G-CSF es a lo sumo un componente de movilización. |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fase 3 | Reclutando | 156 | ECA de trasplante autólogo frente a mejor terapia disponible en esclerosis múltiple resistente. No se puede aislar la contribución de filgrastim. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Reclutando | 358 | Protocolo de plataforma de profilaxis de EICH con ciclofosfamida postrasplante. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fase 1/2 | Completado | 147 | Trasplante alogénico no mieloablativo con busulfán, fludarabina e irradiación corporal total. |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Fase 1 | Retirado | 0 | Médula ósea criopreservada de donante no emparentado con HLA discordante. Sin participantes ni datos. |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Fase 2 | Completado | 160 | Ganciclovir/valganciclovir para prevenir la reactivación de CMV en lesión pulmonar aguda. Filgrastim no es la intervención. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completado | 60 | Piloto de trasplante alogénico/singénico en sarcomas pediátricos de alto riesgo. Relación solo indirecta. |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Fase 2 | Terminado | 49 | Dapansutrilo oral en COVID-19 moderado con síndrome de liberación de citocinas. Sin relación con filgrastim. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Reclutando | 260 | Búsqueda de dosis mínima eficaz de ciclofosfamida postrasplante como profilaxis de EICH. |

Se muestran 10 de los 14 ensayos vinculados. Ninguno evalúa un trastorno de liberación plaquetaria.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohorte | Frontiers in Immunology | La movilización de células madre de sangre periférica con G-CSF en donantes sanos moviliza de forma preferente subpoblaciones de linfocitos. Es un estudio sobre el trasplante, no sobre trastornos plaquetarios. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 08495003 | ZARZIO 30 MU/0,5 ml SOL. INY. O PARA PERFUSION EN JERINGA PRECARGADA | Solución inyectable y para perfusión en jeringa precargada |
| 110631007 | NIVESTIM 48 MU/0,5 ml SOLUCION INYECTABLE O PARA PERFUSION | Solución inyectable y para perfusión |
| 110631001 | NIVESTIM 12 MU/0,2 ml SOLUCION INYECTABLE O PARA PERFUSION | Solución inyectable y para perfusión |
| 08495005 | ZARZIO 48 MU/0,5 ml SOL. INY. O PARA PERFUSION EN JERINGA PRECARGADA | Solución inyectable y para perfusión en jeringa precargada |
| 114946004 | Accofil 48 MU/0,5 ml solución inyectable y para perfusión en jeringa precargada | Solución inyectable y para perfusión en jeringa precargada |

Hay 20 autorizaciones en total; se muestran 5. Los titulares son Sandoz GmbH, Pfizer Europe MA EEIG y Accord Healthcare S.L.U.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existe evidencia clínica ni mecanismo plausible que vincule filgrastim con el trastorno de liberación primaria de las plaquetas. El puntaje alto de TxGNN parece reflejar cercanía en el grafo, y los ensayos asociados son de trasplante y oncología donde el G-CSF es solo apoyo.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), necesario antes de cualquier cribado de seguridad.
- Obtener el texto de las indicaciones aprobadas y los datos del mecanismo de acción desde DrugBank.
- Encontrar estudios preclínicos o clínicos que muestren un efecto de G-CSF sobre la función plaquetaria. Sin ellos, la predicción debería permanecer en Hold.
- Considerar otras predicciones del mismo fármaco solo si aparece evidencia directa, ya que ninguna la tiene por ahora.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

