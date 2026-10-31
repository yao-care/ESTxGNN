---
layout: default
title: Leflunomide
parent: Solo predicción del modelo (L5)
nav_order: 458
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "Leflunomide"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Leflunomide: nueva indicación predicha, Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Leflunomide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

## Leflunomide: Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## Resumen en Una Frase

Leflunomida es un fármaco inmunomodulador utilizado originalmente para el tratamiento de la artritis reumatoide y la artritis psoriásica.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de braquidactilia-sindactilia**, una malformación congénita rara de las extremidades,
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde esta dirección (solo predicción computacional).

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Síndrome de braquidactilia-sindactilia (brachydactyly-syndactyly syndrome) |
| Puntaje de Predicción TxGNN | 0.9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 12) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, leflunomida inhibe la enzima dihidroorotato deshidrogenasa (DHODH, gen *DHODH*), lo que reduce la síntesis de pirimidinas en los linfocitos en proliferación. Esto explica su eficacia en enfermedades autoinmunes como la artritis reumatoide y la artritis psoriásica.

**No se ha establecido un vínculo mecanístico** entre esta inhibición y la fisiopatología del síndrome de braquidactilia-sindactilia, una malformación congénita del desarrollo de las extremidades. La similitud con las indicaciones originales no ha sido evaluada. El puntaje de 0,9993 es únicamente una predicción computacional, sin respaldo de ensayos clínicos ni literatura.

Además, leflunomida es teratogénica y tiene una advertencia de toxicidad embriofetal, por lo que cualquier hipótesis en un trastorno congénito del desarrollo requeriría una revisión toxicológica cuidadosa.

Cabe mencionar una segunda predicción de menor rango, el síndrome de microftalmia colobomatosa-displasia rizomélica (puntaje 0,9993), que tampoco tiene ensayos ni literatura y presenta las mismas limitaciones.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones vigentes (todas de principio activo único):

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 99118007 | ARAVA 20 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible en los datos |
| 09604005 | Leflunomide Zentiva 20 mg EFG | Comprimido recubierto con película | No disponible en los datos |
| 78115 | Leflunomida Tecnigen 20 mg EFG | Comprimido recubierto con película | No disponible en los datos |
| 85071 | Leflunomida Tillomed 20 mg EFG | Comprimido | No disponible en los datos |
| 74186 | Lefluartil 20 mg EFG | Comprimido recubierto con película | No disponible en los datos |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del prospecto): insuficiencia y enfermedad hepática, enfermedad renal, enfermedad de la vesícula biliar, hepatitis B y C crónicas, trombocitopenia, neutropenia (incluidas formas congénitas), agranulocitosis, pancitopenia, anemia, neuropatía periférica, enfermedad pulmonar intersticial, neumocistosis y aspergilosis.
- **Interacciones farmacológicas**: solo se identificó su diana farmacológica, la dihidroorotato deshidrogenasa (DHODH); no hay interacciones con otros fármacos documentadas.
- **Toxicidad embriofetal**: leflunomida es teratogénica, lo que es especialmente relevante para las indicaciones predichas, que son trastornos congénitos del desarrollo.

No se dispone de las advertencias y contraindicaciones del prospecto de la AEMPS; consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, sin vínculo mecanístico demostrado y con un perfil teratogénico que desaconseja avanzar sin una justificación sólida.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente un vacío de datos bloqueante
- Completar los datos del mecanismo de acción desde DrugBank
- Buscar una hipótesis mecanística que conecte la inhibición de DHODH con la biología del síndrome de braquidactilia-sindactilia
- Revisar la literatura y los modelos preclínicos pertinentes
- Realizar una evaluación toxicológica específica del riesgo embriofetal
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

