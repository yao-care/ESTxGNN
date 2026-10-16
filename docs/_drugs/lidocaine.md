---
layout: default
title: Lidocaine
parent: Solo predicción del modelo (L5)
nav_order: 470
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lidocaine: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Dermatitis…"
monitor_inn: "Lidocaine"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "papillary conjunctivitis", "rosacea conjunctivitis", "exposure keratitis", "atopic conjunctivitis", "conjunctival disorder", "nephrotic syndrome", "non-human animal disease", "tinea corporis", "sporadic idiopathic steroid-resistant nephrotic syndrome"]
---

# Lidocaine
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

# Lidocaína: De Dermatitis y Neuralgia a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

La lidocaína es un anestésico local bloqueador de canales de sodio, utilizado originalmente en anestesia local y regional, y en el alivio del dolor y del picor (por ejemplo, neuralgia postherpética y afecciones dermatológicas).
El modelo TxGNN predice que podría ser efectiva para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Dermatitis, neuralgia y neuralgia postherpética (según el grafo de conocimiento; los textos de indicación autorizados no están disponibles) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la lidocaína bloquea los canales de sodio dependientes de voltaje (Nav1.2, Nav1.4, Nav1.5, Nav1.7 y Nav1.8 figuran entre sus dianas farmacológicas), lo que reduce la transmisión de señales dolorosas por las fibras nerviosas sensitivas. Ya se utiliza en forma de gel oftálmico (Ophtesic) como anestésico de superficie ocular.

La relación con la nueva indicación es débil. Las indicaciones originales son sobre todo de control sintomático del dolor y del picor, y la queratoconjuntivitis epitelial punteada es una afección inflamatoria o lesiva de la superficie ocular. Un posible beneficio se limitaría al alivio sintomático del dolor, sin modificar la enfermedad.

Hay además una señal de cautela: los anestésicos tópicos pueden **perjudicar la cicatrización del epitelio corneal**, y su uso crónico se asocia a queratopatía. Por ello, la predicción es plausible solo como analgesia sintomática, no como tratamiento de la enfermedad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para queratoconjuntivitis epitelial punteada.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

*Nota sobre otras predicciones:* entre las demás indicaciones predichas, la mejor respaldada es "trastorno conjuntival" (L4), con un ensayo de Fase 4 completado ([NCT05978687](https://clinicaltrials.gov/study/NCT05978687), 41 participantes, gel de lidocaína Ophtesic frente a inyección subconjuntival en la escisión de pterigión). Se trata de anestesia durante el procedimiento, no de tratamiento de la enfermedad. La conjuntivitis atópica (L4) solo cuenta con evidencia mecanística indirecta (PMID 37819721 y 8039024). El resto de predicciones son L5.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 44793 | Lidocaína B. Braun 10 mg/ml solución inyectable | Solución inyectable | No disponible en los datos |
| 83397 | Verira 700 mg apósito adhesivo medicamentoso | Apósito adhesivo medicamentoso | No disponible en los datos |
| 83733 | Lidocaína Aguettant 10 mg/ml en jeringa precargada | Solución inyectable en jeringa precargada | No disponible en los datos |
| 84450 | Ophtesic 20 mg/g gel oftálmico en envase unidosis | Gel oftálmico | No disponible en los datos |
| 79538 | Dynexan 20 mg/g gel bucal | Gel bucal | No disponible en los datos |

Se muestran 5 de las 20 autorizaciones vigentes (todas de monofármaco). Entre ellas hay presentaciones inyectables, apósitos, cremas, pulverizador cutáneo, gel bucal, crema vaginal y gel oftálmico.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión, insuficiencia hepática, enfermedad hepática y cirrosis, epilepsia, enfermedad renal, enfermedad de la vesícula biliar, insuficiencia suprarrenal (enfermedad de Addison), hipotiroidismo, glaucoma de ángulo abierto, queratitis por herpes simple, infección por varicela zóster, dermatitis atópica, osteoporosis, trastornos psicóticos y mentales, infecciones fúngicas (dermatofitosis), déficit de potasio y gastritis, entre otras.
- **Señales de seguridad en la literatura recuperada:**
  - Efectos secundarios neuropsiquiátricos y cardiológicos con lidocaína intravenosa en cefalea refractoria (PMID 19250287).
  - Un caso de metahemoglobinemia grave en un niño con síndrome nefrótico por uso simultáneo de lidocaína tópica, benzocaína y cotrimoxazol (PMID 41995267).
  - Convulsiones en macacos tras administrar ceftriaxona disuelta en lidocaína al 1% (PMID 19858165).
  - Menor unión a proteínas plasmáticas de la lidocaína en enfermedad renal (PMID 7037263).
- **Interacciones farmacológicas:** los datos corresponden a dianas farmacológicas (canales de sodio Nav1.2, 1.4, 1.5, 1.7 y 1.8), no a interacciones con otros fármacos.

Para la información de seguridad completa, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (L5), sin ensayos ni literatura para la queratoconjuntivitis epitelial punteada. Además, los anestésicos tópicos pueden retrasar la cicatrización corneal, lo que va en contra de un uso terapéutico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto de la AEMPS (actualmente sin datos).
- Estudios preclínicos o clínicos que evalúen la lidocaína en la queratoconjuntivitis epitelial punteada, incluyendo su efecto sobre la cicatrización del epitelio corneal.
- Evaluación de la compatibilidad de vía de administración: el gel oftálmico existente (Ophtesic) es el único formato relevante.
- Valorar si el interés real se limita al alivio sintomático del dolor ocular, para lo cual ya existen anestésicos oftálmicos.
- Priorizar, si se desea explorar la vía oftálmica, las predicciones con evidencia indirecta (conjuntivitis atópica y trastorno conjuntival) como preguntas de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

