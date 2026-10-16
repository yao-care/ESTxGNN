---
layout: default
title: Bupivacaine
parent: Solo predicción del modelo (L5)
nav_order: 124
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Bupivacaine: nueva indicación predicha, Acrodermatitis crónica atrófica (nivel de evidencia L5). Indicación original: Dermatitis (según el grafo de conocimiento TxGNN"
---

# Bupivacaine
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

# Bupivacaína: De Dermatitis a Acrodermatitis Crónica Atrófica

## Resumen en Una Frase

Bupivacaína es un anestésico local de tipo amida, cuya indicación original registrada en el grafo de conocimiento es la dermatitis.
El modelo TxGNN predice que podría ser efectivo para **acrodermatitis crónica atrófica**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis (según el grafo de conocimiento TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Acrodermatitis crónica atrófica |
| Puntaje de Predicción TxGNN | 99.23% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 10 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este fármaco. Según la información conocida, bupivacaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje. Los datos farmacológicos compilados también muestran interacción con canales de potasio (Kir3.2, Kv1.5, Kv4.3) y con el canal de sodio cardíaco Nav1.5. No se encontraron datos públicos de afinidad que confirmen plenamente su mecanismo en canales de sodio humanos.

La acrodermatitis crónica atrófica es la manifestación cutánea tardía de la infección por *Borrelia* (borreliosis de Lyme) y se trata con antibióticos. Un anestésico local no tiene acción antimicrobiana ni modificadora de la enfermedad conocida en este contexto.

La puntuación alta de TxGNN (0.992) parece derivarse de la proximidad en el grafo con el nodo «dermatitis», no de una base biológica. **No se establece un vínculo mecanístico creíble**, por lo que la predicción debe considerarse con mucha cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 57109 | Bupivacaína Physan 2,5 mg/ml solución inyectable | Solución inyectable | No disponible |
| 58023 | Bupivacaína Physan 7,5 mg/ml solución inyectable | Solución inyectable | No disponible |
| 81695 | Bupivacaína Accord 2,5 mg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 81696 | Bupivacaína Accord 5 mg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 62412 | Bupivacaína B. Braun 2,5 mg/ml solución inyectable | Solución inyectable | No disponible |

Se muestran 5 de las 10 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del prospecto)**: el grafo TxGNN asocia bupivacaína con contraindicación en diversas enfermedades, entre ellas: hipertensión, insuficiencia hepática, enfermedad renal, epilepsia, EPOC, insuficiencia respiratoria, infarto de miocardio, enfermedad coronaria, parada cardíaca súbita, enfermedades de la conducción cardíaca, fibrilación auricular, hipotensión, diabetes mellitus, cetoacidosis diabética, hipotiroidismo, glaucoma de ángulo cerrado, hiperplasia prostática benigna, enfermedad inflamatoria intestinal, hemoglobinopatías y abuso o dependencia de sustancias.
- **Interacciones farmacológicas (datos farmacológicos de dianas)**: se identificaron 4 interacciones con dianas moleculares: Nav1.5 (canal de sodio cardíaco humano), Kv1.5 (humano), Kv4.3 (ratón) y Kir3.2. Son interacciones con dianas, no con otros fármacos, y su relevancia clínica no está cuantificada.
- **Señales de seguridad específicas de las indicaciones predichas**: la exposición sistémica a bupivacaína conlleva riesgo de cardiotoxicidad y de depresión respiratoria, y se describe miotoxicidad, lo cual preocupa en enfermedades musculares inflamatorias y en población pediátrica.

No se dispone de advertencias ni contraindicaciones del prospecto de la AEMPS; consultar el prospecto para esta información.

## Otras Predicciones Evaluadas

| Indicación Predicha | Puntaje TxGNN | Nivel de Evidencia | Decisión |
|------|------|------|------|
| Dermatomiositis neonatal | 99.15% | L5 | Hold |
| Enfermedad pulmonar intersticial secundaria infantil asociada a enfermedad del tejido conectivo | 99.11% | L5 | Hold |
| Dermatomiositis amiopática | 99.03% | L5 | Hold |

Ninguna cuenta con ensayos clínicos ni literatura, y en ninguna se identifica un vínculo mecanístico creíble. Como mucho, bupivacaína podría tener un papel sintomático o procedimental (control del dolor), que no constituye una justificación de reposicionamiento.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa exclusivamente en el modelo TxGNN (nivel L5), sin ensayos clínicos ni literatura, y sin vínculo mecanístico plausible entre un anestésico local y una infección por *Borrelia* con manifestación cutánea crónica.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción detallado desde DrugBank
- Descargar y analizar el prospecto de la AEMPS para disponer de advertencias y contraindicaciones oficiales, y de los textos de indicación aprobada
- Realizar una búsqueda de literatura y de registros de ensayos que confirmen o descarten cualquier asociación
- Si se persiguiera algún uso, evaluar la compatibilidad de vías de administración (hoy solo hay solución inyectable) y el perfil de seguridad cardíaca y respiratoria
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

