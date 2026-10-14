---
layout: default
title: Pilocarpine
parent: Solo predicción del modelo (L5)
nav_order: 636
evidence_level: L5
indication_count: 1
---

# Pilocarpine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Pilocarpina: De Glaucoma de Ángulo Abierto a Glaucoma Hereditario Primario

## Resumen en Una Frase

Pilocarpina es un agonista muscarínico utilizado originalmente para el tratamiento del glaucoma de ángulo abierto y la hipertensión ocular.
El modelo TxGNN predice que podría ser efectivo para **glaucoma hereditario primario**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Glaucoma de ángulo abierto e hipertensión ocular |
| Nueva Indicación Predicha | Glaucoma hereditario primario |
| Puntaje de Predicción TxGNN | 99,83% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la farmacología conocida y los datos de dianas, la pilocarpina actúa como agonista de los receptores muscarínicos (M1 a M5). A través del receptor M3, contrae el músculo ciliar y aumenta la salida del humor acuoso por la malla trabecular, lo que reduce la presión intraocular. Este mecanismo explica su uso en glaucoma de ángulo abierto e hipertensión ocular.

El glaucoma hereditario primario también implica una alteración en la salida del humor acuoso, por lo que, mecanísticamente, un fármaco que mejora ese drenaje podría ser aplicable. Sin embargo, este vínculo se infiere de la farmacología general y no de los datos aportados.

Conviene ser prudente: los glaucomas hereditarios (por ejemplo, congénitos o juveniles, con variantes en genes como MYOC o CYP1B1) suelen implicar anomalías del desarrollo de la malla trabecular o del ángulo, por lo que la eficacia de un mióstico podría ser limitada. Además, el perfil de seguridad en población pediátrica requeriría una evaluación independiente. El puntaje de 99,83% es solo una predicción computacional.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88757 | PILOCARPINA APOTHEKE 5 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película | No especificada en los datos |
| 61835 | SALAGEN 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en los datos |
| 10955 | COLIRCUSI PILOCARPINA 20 mg/ml colirio en solución | Colirio en solución | No especificada en los datos |

Nota: las tres autorizaciones están vigentes y son de principio activo único. La formulación oftálmica (colirio) es relevante para la indicación predicha, mientras que los comprimidos orales corresponden a otros usos (como la xerostomía, según la información farmacológica disponible). La compatibilidad de vías de administración para la nueva indicación está pendiente de evaluación.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: el grafo de conocimiento asocia la pilocarpina con enfermedades en las que podría estar contraindicada, entre ellas:
  - Oculares: glaucoma de ángulo cerrado, queratitis, queratoconjuntivitis, iritis, iridociclitis, uveítis y desprendimiento de retina.
  - Respiratorias: asma, enfermedad pulmonar obstructiva crónica (EPOC) y enfermedad bronquial.
  - Biliares y hepáticas: colelitiasis, colecistitis, coledocolitiasis, enfermedad de las vías biliares, ictericia obstructiva e insuficiencia hepática.
  - Renales: nefrolitiasis y nefropatía aguda por uratos.
- **Interacciones y farmacología**: la pilocarpina se une a los receptores muscarínicos M1, M2, M3, M4 y M5 humanos. Esto sugiere posibles efectos colinérgicos sistémicos y posibles interacciones con fármacos anticolinérgicos o colinérgicos, aunque los datos compilados no detallan interacciones con otros medicamentos.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles en los datos compilados; consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden, y faltan datos de seguridad del prospecto. Aunque el mecanismo es plausible, los glaucomas hereditarios suelen tener anomalías del ángulo que podrían limitar la eficacia de un mióstico.

**Para avanzar se necesita:**
- Obtener y analizar las advertencias y contraindicaciones del prospecto de la AEMPS (bloqueante para el cribado de seguridad).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda sistemática de literatura y ensayos clínicos sobre pilocarpina en glaucomas hereditarios (congénito, juvenil).
- Evaluar la seguridad pediátrica y la compatibilidad de la vía de administración (colirio) con la nueva indicación.
- Analizar la relevancia de las contraindicaciones del grafo de conocimiento, en particular las oculares, frente a la población diana.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

