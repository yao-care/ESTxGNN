---
layout: default
title: Diclofenac
parent: Solo predicción del modelo (L5)
nav_order: 247
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
monitor_inn: "Diclofenac"
predicted_indications: ["hypotrichosis simplex of the scalp", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "brachyolmia", "brachyolmia-amelogenesis imperfecta syndrome", "congenital hypotrichosis milia", "myosclerosis", "diffuse alopecia areata", "juvenile idiopathic arthritis", "WHIM syndrome"]
description: "Diclofenac: nueva indicación predicha, Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Diclofenac
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

## Diclofenac: Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp)
{: .text-alpha }

## Resumen en Una Frase

Diclofenaco es un antiinflamatorio no esteroideo (AINE) utilizado originalmente para tratar enfermedades articulares como la artritis reumatoide y la artrosis, así como lesiones cutáneas como la queratosis actínica.
El modelo TxGNN predice que podría ser efectivo para **hipotricosis simple del cuero cabelludo**,
pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hipotricosis simple del cuero cabelludo (hypotrichosis simplex of the scalp) |
| Puntaje de Predicción TxGNN | 0.9969 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada. Según lo conocido, el diclofenaco es un AINE que inhibe las ciclooxigenasas COX-1 y COX-2 y reduce la síntesis de prostaglandinas. Su eficacia en la inflamación y el dolor articular está bien establecida. Los datos farmacológicos compilados también lo asocian con otras dianas, como PPARγ, TRPM3, ASIC3 y el transportador de aminoácidos PAT1.

La relación entre la indicación original y la nueva es débil. La hipotricosis simple del cuero cabelludo es un trastorno folicular de origen genético y monogénico (por ejemplo, variantes en CDSN, APCDD1 o RPL21). Las vías de las prostaglandinas influyen en el ciclo del cabello, pero inhibir la COX no corregiría un defecto genético de este tipo.

Por tanto, el puntaje alto del modelo parece reflejar una relación en la red de conocimiento y no un fundamento terapéutico plausible. Se debe interpretar con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes. Todas son de principio activo único y ninguna está cancelada. Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 74119 | Diclofenaco Kern Pharma 11,6 mg/g gel | Gel |
| 62000 | Diclofenaco Pensa 50 mg comprimidos gastrorresistentes EFG | Comprimido |
| 62024 | Voltaren Retard 75 mg comprimidos de liberación modificada | Comprimido de liberación modificada |
| 57589 | Diclofenaco Llorens 75 mg solución inyectable EFG | Solución inyectable |
| 61866 | Diclofenaco Alter 50 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente |

## Consideraciones de Seguridad

- **Contraindicaciones (según el grafo de conocimiento, no el prospecto):**
  - Cardiovasculares: hipertensión, insuficiencia cardíaca congestiva, infarto de miocardio, ictus y enfermedad cerebrovascular.
  - Hepáticas: insuficiencia hepática, hepatopatía y lesión hepática inducida por fármacos.
  - Digestivas: úlcera péptica activa y enfermedad inflamatoria intestinal.
  - Respiratorias: asma.
  - Otras: trastornos de la coagulación, anemia, hemoglobinopatías, diabetes y cetoacidosis diabética, enfermedad de la vesícula biliar, abuso o dependencia de sustancias y queratitis.
- **Dianas farmacológicas relevantes:** COX-1 y COX-2 (mecanismo principal), PPARγ, TRPM3, ASIC3 y PAT1. Estos datos describen la farmacología del fármaco y no son interacciones medicamentosas clínicas.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para hipotricosis simple del cuero cabelludo tiene nivel de evidencia L5: no hay ensayos ni literatura, y no existe un vínculo mecanístico plausible entre la inhibición de la COX y un defecto genético folicular.

Entre las 10 principales predicciones, solo la **artritis idiopática juvenil** (puntaje 0.9925) cuenta con literatura de apoyo (nivel L3). Esa literatura consiste en estudios pediátricos pequeños y antiguos con diclofenaco, como un estudio abierto de 1983 y un cruzado de 1988, además de revisiones. En la práctica esto es una extensión del uso habitual de los AINE y no un reposicionamiento novedoso. Podría evaluarse como una línea de investigación independiente.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA) y un análisis mecanístico que vincule la COX o las prostaglandinas con la biología del folículo piloso.
- Estudios preclínicos o revisión de literatura que respalden la hipótesis; actualmente no existen.
- Advertencias y contraindicaciones del prospecto de la AEMPS para completar la evaluación de seguridad.
- Si se prioriza una indicación alternativa (por ejemplo, artritis idiopática juvenil), una revisión sistemática de la evidencia pediátrica y un análisis de seguridad gastrointestinal, renal y hepática.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

