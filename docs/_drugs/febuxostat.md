---
layout: default
title: Febuxostat
parent: Evidencia moderada (L3-L4)
nav_order: 227
evidence_level: L4
indication_count: 3
---

# Febuxostat
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Febuxostat: De Hiperuricemia/Gota a Hipouricemia Renal

## Resumen en Una Frase

Febuxostat es un inhibidor selectivo no purínico de la xantina oxidorreductasa (XOR) que reduce el ácido úrico en sangre. Su uso conocido es la hiperuricemia y la gota, aunque los registros de AEMPS del paquete de evidencia no incluyen el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para **hipouricemia renal**, pero solo hay **1 ensayo clínico** (con relevancia baja) y **2 publicaciones** (una revisión narrativa y un reporte de caso), por lo que la predicción es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los registros de AEMPS del paquete de evidencia (uso conocido: hiperuricemia/gota) |
| Nueva Indicación Predicha | Hipouricemia renal |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Febuxostat inhibe la xantina oxidorreductasa, enzima que produce ácido úrico. Por eso reduce el urato sérico. No se dispone de datos detallados de mecanismo de acción en DrugBank para este paquete, pero la naturaleza del fármaco como inhibidor de XOR es conocida.

La hipouricemia renal es lo contrario de la indicación original. Es un estado de urato bajo causado por una reabsorción renal defectuosa (por ejemplo, alteraciones de URAT1/GLUT9). El alto puntaje de TxGNN probablemente refleja cercanía en el grafo del metabolismo del urato y no una adecuación terapéutica real.

La única hipótesis mecanística es que inhibir la XOR podría reducir las especies reactivas de oxígeno y el estrés del catabolismo de purinas en la lesión renal aguda inducida por el ejercicio (EIAKI), una complicación conocida de esta condición. Reducir aún más el urato podría ser contraproducente, y no hay datos clínicos que respalden un beneficio.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Desconocido | 100 | Estudio prospectivo controlado sobre el efecto del control del ácido úrico en la recurrencia de cálculos y la función renal en pacientes con litiasis e hiperuricemia. Relevancia baja (grado C): no se puede verificar su relación con la hipouricemia renal. |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Revisión narrativa | Clinical Rheumatology | Actualización sobre hipouricemia (urato sérico < 2 mg/dL) y sus causas, dirigida al reumatólogo. No evalúa febuxostat como tratamiento. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Reporte de caso / hipótesis | Internal Medicine | Futbolista japonés de 16 años con hipouricemia renal familiar (mutaciones en URAT1) y EIAKI recurrente. La hidratación no bastó como profilaxis y se planteó febuxostat. El resumen disponible está truncado y no permite confirmar el resultado. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 83214 | Febuxostat Kern Pharma 120 mg EFG | Comprimido recubierto con película | Kern Pharma S.L. |
| 83910 | Febuxostat Combix 120 mg EFG | Comprimido recubierto con película | Laboratorios Combix S.L.U. |
| 08447014IP | Adenuric 80 mg | Comprimido recubierto con película | Menarini International Operations Luxembourg S.A. |
| 83229 | Uxaton 80 mg EFG | Comprimido recubierto con película | Uxa Farma S.A. |
| 83769 | Gotaric 80 mg EFG | Comprimido recubierto con película | Especialidades Farmacéuticas Centrum S.A. |

Se muestran 5 de las 20 autorizaciones. Los registros no incluyen el texto de indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Desde el punto de vista mecanístico, el análisis del paquete advierte que reducir aún más el urato en una condición ya hipouricémica podría ser contraproducente.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es de nivel L4: solo hay una revisión narrativa, un reporte de caso con resultado no confirmado y un ensayo de relevancia baja. Además, la hipouricemia renal ya es un estado de urato bajo, por lo que el alto puntaje de TxGNN parece reflejar proximidad en el grafo y no un ajuste terapéutico.

**Para avanzar se necesita:**
- Revisar el texto completo del reporte de caso (PMID 36754409) para confirmar si febuxostat previno la EIAKI
- Verificar en el registro completo si NCT04398251 tiene alguna relación con la hipouricemia renal
- Descargar y analizar la ficha técnica de AEMPS (advertencias y contraindicaciones)
- Obtener datos de mecanismo de acción desde DrugBank
- Evaluar el riesgo de reducir aún más el urato sérico en estos pacientes

**Otras predicciones del modelo (para seguimiento, con nivel L4):**
- Deficiencia parcial de HPRT (puntaje 99.98%)
- Síndrome de Lesch-Nyhan (puntaje 99.68%)

Ambas se apoyan solo en reportes de caso y series pequeñas. Su mecanismo es más plausible que el de la hipouricemia renal, porque en ellas el urato está elevado. Habría que vigilar el riesgo de cálculos de xantina, y en Lesch-Nyhan el beneficio se limitaría al componente metabólico.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

