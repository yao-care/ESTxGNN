---
layout: default
title: Tetracycline
parent: Evidencia moderada (L3-L4)
nav_order: 786
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Tetracycline: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L4). Indicación original: Infección del tracto urinario (según el grafo de conocimiento"
---

# Tetracycline
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Tetraciclina: De Infección del Tracto Urinario a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Tetraciclina es un antibiótico de amplio espectro, originalmente utilizado para infecciones como las del tracto urinario, bronquitis, acné, neumonía y conjuntivitis.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
con **0 ensayos clínicos** y **1 publicación** (un reporte de caso indirecto) que actualmente respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la tetraciclina pertenece a la clase de las tetraciclinas, su eficacia en infecciones bacterianas, incluida la conjuntivitis, es conocida, y mecanísticamente podría ser aplicable a la queratoconjuntivitis epitelial punteada.

La relación con la indicación original es plausible: la tetraciclina ya se utiliza en conjuntivitis, y la queratitis epitelial punteada puede aparecer tras una conjuntivitis folicular por *Chlamydia trachomatis*. Por ello, su actividad antimicrobiana frente a Chlamydia constituye un vínculo razonable. Además, las tetraciclinas tienen propiedades antiinflamatorias e inhibidoras de metaloproteinasas de matriz (MMP) que podrían beneficiar la inflamación de la superficie ocular.

Sin embargo, la única literatura disponible es un reporte de 1992 sobre queratitis persistente después de una conjuntivitis por clamidia. Es evidencia indirecta y no demuestra beneficio terapéutico en esta condición.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Reporte de caso | Cornea | Dos casos de conjuntivitis folicular por *C. trachomatis* tratados con tetraciclina o doxiciclina oral; se resolvieron los folículos, pero después aparecieron lesiones epiteliales punteadas recurrentes y bilaterales en la córnea. No demuestra beneficio del tratamiento. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 25697 | TETRACICLINA ITALFARMACO | Comprimido recubierto con película | No disponible |
| 75095 | PYLERA 140 mg/125 mg/125 mg CÁPSULAS | Cápsula dura | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad renal, insuficiencia renal, uremia, glomerulonefritis, epilepsia, neutropenia, agranulocitosis, deficiencia de G6PD, gota, neuropatía periférica, enfermedades de la coagulación, colitis por *Clostridium difficile*, enterocolitis necrosante perinatal, diabetes mellitus, cetoacidosis diabética, fibrilación auricular, bloqueo auriculoventricular, síndrome de Adams-Stokes, insuficiencia respiratoria, entre otras.
- **Interacciones Farmacológicas**: se identificaron 308 interacciones. Entre las de nivel **Mayor** figuran isotretinoína, acitretina y ácido aminolevulínico. Entre las de nivel **Moderado** figuran etinilestradiol, amoxicilina, ampicilina, aminofilina, atovacuona, balsalazida, subcitrato de bismuto y potasio, hidróxido de aluminio, citrato de sodio y asparaginasa. Hay además interacciones de nivel Menor, como acetazolamida, hidroclorotiazida y amilorida.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya en un puntaje alto del modelo (99.58%), pero la única evidencia es un reporte de caso de 1992 que es indirecto y no demuestra eficacia. No hay ensayos clínicos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), que hoy es un vacío de datos bloqueante para el cribado de seguridad.
- Complementar los datos del mecanismo de acción (MOA).
- Revisar la literatura sobre el uso de tetraciclinas (orales o tópicas) en queratoconjuntivitis y queratitis epitelial punteada, con estudios clínicos específicos.
- Evaluar la compatibilidad de vía de administración (oral frente a oftálmica), aún pendiente.
- Definir un plan de seguridad que considere la elevada carga de interacciones y las contraindicaciones identificadas.

---

**Nota sobre otras indicaciones predichas:** el modelo también predijo rinosinusitis crónica (99.15%, L4; existen revisiones sistemáticas, pero sobre doxiciclina o la clase de antibióticos y no sobre tetraciclina), sinusitis etmoidal crónica (99.15%, L4) y neoplasia de senos paranasales (99.10%, L5, solo predicción del modelo). Ninguna cuenta con ensayos clínicos específicos de tetraciclina.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

