---
layout: default
title: Lenograstim
parent: Solo predicción del modelo (L5)
nav_order: 310
evidence_level: L5
indication_count: 4
---

# Lenograstim
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Lenograstim: De G-CSF (factor estimulante de colonias de granulocitos) a Trastorno de Liberación Primaria Plaquetaria

## Resumen en Una Frase

Lenograstim es un factor estimulante de colonias de granulocitos (G-CSF) recombinante, comercializado en España como Granocyte. Los registros disponibles no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de liberación primaria de las plaquetas**, pero la evidencia real es muy débil: hay **13 ensayos clínicos** vinculados, todos de baja relevancia (centrados en trasplante de progenitores hematopoyéticos), y **ninguna publicación** que respalde esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Trastorno de liberación primaria de las plaquetas |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 (solo predicción del modelo; los ensayos vinculados no estudian esta indicación) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados en el paquete de evidencia. Según la información conocida, lenograstim es un G-CSF recombinante que actúa sobre el receptor de G-CSF, impulsa la proliferación del linaje de neutrófilos y moviliza células madre hematopoyéticas.

Sin embargo, **no existe un vínculo mecanístico establecido** con la liberación plaquetaria (secreción de gránulos). El puntaje alto de TxGNN (0.999) es únicamente una salida del grafo de conocimiento. Los 13 ensayos asociados parecen haberse emparejado por el contexto de trasplante de progenitores hematopoyéticos (TPH), no por trastornos de la función plaquetaria.

Por ello, la plausibilidad biológica de esta predicción es baja y debe tratarse como una hipótesis sin respaldo clínico.

---

## Evidencia de Ensayos Clínicos

Ningún ensayo estudia trastornos plaquetarios. Todos se evaluaron como de relevancia baja (grado C) o pendiente de evaluación. Se muestran 10 de los 13 ensayos vinculados.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00281879](https://clinicaltrials.gov/study/NCT00281879) | Fase 2 | Terminado | 200 | Trasplante de células madre de donante no emparentado en neoplasias hematológicas; lenograstim, como mucho, es soporte |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Fase 3 | Reclutando | 156 | Mejor terapia disponible vs. trasplante autólogo en esclerosis múltiple resistente al tratamiento |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Fase 2 | Reclutando | 358 | Protocolo de plataforma de profilaxis de EICH con ciclofosfamida postrasplante |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Fase 1/2 | Completado | 147 | Trasplante alogénico no mieloablativo con busulfán, fludarabina e irradiación corporal total |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Fase 1 | Retirado | 0 | Médula ósea criopreservada de donante HLA no compatible; sin participantes, sin valor probatorio |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Fase 2 | Completado | 160 | Ganciclovir/valganciclovir para prevenir reactivación de CMV en lesión pulmonar aguda |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Fase 2 | Completado | 60 | Piloto de trasplante alogénico/singénico en sarcomas pediátricos de alto riesgo |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Fase 2 | Terminado | 49 | Dapansutrilo oral en COVID-19 moderado con síndrome de liberación de citocinas temprano |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Fase 1/2 | Reclutando | 260 | Búsqueda de la dosis mínima eficaz de ciclofosfamida postrasplante |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Fase 2 | Completado | 9 | Piloto de linfodepleción intensificada y trasplante autólogo en lupus eritematoso sistémico grave |

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Los registros no incluyen el texto de la indicación aprobada de ninguna de las dos autorizaciones. Ambas pertenecen a Italfarmaco S.A.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 60672 | Granocyte 13 millones de UI | Polvo y disolvente para solución inyectable o perfusión |
| 60211 | Granocyte 34 millones de UI | Polvo y disolvente para solución inyectable o perfusión |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. La búsqueda de interacciones farmacológicas no devolvió resultados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el grafo de conocimiento. No hay vínculo mecanístico entre la señalización de G-CSF y la liberación plaquetaria, y ningún ensayo ni publicación estudia esta indicación. Las otras predicciones del modelo (tromboastenia de Glanzmann, pseudo-enfermedad de von Willebrand y retinopatía diabética no proliferativa grave) tampoco tienen evidencia y quedan igualmente en espera.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS para obtener advertencias, contraindicaciones y el texto de la indicación aprobada (hoy es un bloqueo para el cribado de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Realizar una revisión de literatura preclínica o de mecanismo que justifique un vínculo entre G-CSF y la función plaquetaria.
- Reevaluar la relevancia de los ensayos que siguen pendientes de clasificación (NCT00923364, NCT01503918, NCT00354172).

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier uso.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

