---
layout: default
title: Apomorphine
parent: Solo predicción del modelo (L5)
nav_order: 61
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Apomorphine: nueva indicación predicha, Esquizofrenia (la predicción nº 1 del modelo es polimicrogiria perisi… (nivel de evidencia L5). Indicación original: Enfermedad de Parkinson (y síndromes parki…"
monitor_inn: "Apomorphine"
predicted_indications: ["polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "schizophrenia", "myopia X-linked", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited", "syndromic myopia", "hydranencephaly (disease)"]
---

# Apomorphine
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

## Apomorfina: De Enfermedad de Parkinson a Esquizofrenia
{: .text-alpha }

## Resumen en Una Frase

Apomorfina es un agonista dopaminérgico no ergolínico, utilizado originalmente para tratar la enfermedad de Parkinson (en particular los episodios "off" en fases avanzadas).
El modelo TxGNN predice que podría ser efectivo para **esquizofrenia** (la predicción con mayor respaldo bibliográfico entre las 10 candidatas), pero **no hay ensayos clínicos** y solo hay **20 publicaciones** de carácter mayoritariamente mecanístico, antiguas o preclínicas, cuya dirección es contraria a un uso terapéutico.

> Nota: la predicción nº 1 del modelo es "polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis" (puntaje 99,75 %), pero carece por completo de evidencia. Este informe se centra en esquizofrenia por ser la única candidata con literatura disponible; el resto se resume en una tabla al final.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Enfermedad de Parkinson (y síndromes parkinsonianos relacionados) |
| Nueva Indicación Predicha | Esquizofrenia (la predicción nº 1 del modelo es polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis) |
| Puntaje de Predicción TxGNN | 99,69 % (esquizofrenia); 99,75 % (polimicrogiria, nº 1) |
| Nivel de Evidencia | L4 (esquizofrenia); L5 (polimicrogiria) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información farmacológica conocida, apomorfina es un agonista dopaminérgico con afinidad por los receptores D1, D2, D3, D4 y D5, y también interactúa con receptores serotoninérgicos (5-HT1A, 5-HT2A, 5-HT2B, 5-HT2C), adrenérgicos α2 (A, B y C) y el canal TRPA1. Su eficacia en Parkinson está comprobada.

La relación con la esquizofrenia es la hipótesis dopaminérgica: ambas enfermedades implican alteraciones del sistema dopaminérgico. Sin embargo, la lógica terapéutica es opuesta. En esquizofrenia el tratamiento estándar se basa en antagonistas o agonistas parciales del receptor D2, mientras que un agonista pleno como la apomorfina cabría esperar que empeorase los síntomas positivos. La literatura revisada apunta a que apomorfina se ha usado como sonda de sensibilidad dopaminérgica y respuesta neuroendocrina, no como tratamiento.

Por tanto, la plausibilidad mecanística es débil y el puntaje alto del modelo parece reflejar proximidad en la red de conocimiento (ambas condiciones comparten dianas dopaminérgicas) más que un beneficio terapéutico real.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Se muestran las publicaciones más relevantes de las 20 identificadas para esquizofrenia (sin ECA entre ellas):

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6372737](https://pubmed.ncbi.nlm.nih.gov/6372737/) | 1984 | Estudio clínico | Arch Gen Psychiatry | Apomorfina a dosis baja (0,75 mg s.c.) vs. placebo en 25 varones esquizofrénicos: sin mejoría ni empeoramiento significativos de síntomas psicóticos ni discinesia tardía |
| [6718635](https://pubmed.ncbi.nlm.nih.gov/6718635/) | 1984 | Estudio clínico (pequeña escala) | Psychopharmacol Bull | Estudio de apomorfina en esquizofrenia (sin resumen disponible) |
| [6682989](https://pubmed.ncbi.nlm.nih.gov/6682989/) | 1983 | Estudio doble ciego | Prog Neuropsychopharmacol Biol Psychiatry | 12 pacientes crónicos: sin diferencia terapéutica global frente a placebo; mejoría en subescalas de ansiedad y depresión |
| [11394190](https://pubmed.ncbi.nlm.nih.gov/11394190/) | 2001 | Revisión/Comentario | J Psychiatry Neurosci | Hay poca o ninguna evidencia de que apomorfina induzca psicosis o exacerbe síntomas psicóticos a dosis que estimulan receptores postsinápticos |
| [1099172](https://pubmed.ncbi.nlm.nih.gov/1099172/) | 1975 | Observación clínica doble ciego | J Neurol Neurosurg Psychiatry | 40 varones, 14 días de apomorfina 1 mg: no aparecieron síntomas esquizofrénicos ni depresión; sin diferencias frente a placebo |
| [540209](https://pubmed.ncbi.nlm.nih.gov/540209/) | 1979 | Estudio neuroendocrino | Br J Psychiatry | Respuestas de GH y prolactina a apomorfina como herramienta de investigación en esquizofrenia |
| [12727131](https://pubmed.ncbi.nlm.nih.gov/12727131/) | 2003 | Estudio clínico | Psychoneuroendocrinology | Respuestas de PRL, ACTH y cortisol a apomorfina en 20 pacientes sin tratamiento |
| [30805732](https://pubmed.ncbi.nlm.nih.gov/30805732/) | 2019 | Revisión | J Neural Transm | Revisión de agonistas dopaminérgicos clásicos, incluida la apomorfina parenteral en Parkinson |
| [33571431](https://pubmed.ncbi.nlm.nih.gov/33571431/) | 2021 | Estudio estructural/mecanístico | Cell | Estructuras crio-EM de complejos de señalización de receptores D1 y D2 |
| [23761388](https://pubmed.ncbi.nlm.nih.gov/23761388/) | 2013 | Preclínico (animal) | J Psychopharmacol | Efecto de MK-801 y agonistas dopaminérgicos en respuesta apetitiva en ratas |

## Información de Mercado en España

Hay 16 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no figuran en los datos compilados. Se listan las 5 principales:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88979 | KYNMOBI 25 mg película sublingual | Película sublingual | No disponible |
| 85464 | APO-GO POD 5 mg/ml solución para perfusión en cartucho | Solución para perfusión en cartucho | No disponible |
| 79174 | DACEPTON 5 mg/ml solución para perfusión EFG | Solución inyectable y para perfusión | No disponible |
| 74400 | APO-GO 10 mg/ml solución inyectable o para perfusión en ampollas | Solución inyectable y para perfusión | No disponible |
| 63893 | APO-GO PEN 10 mg/ml solución inyectable | Solución inyectable en pluma precargada | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones señaladas en el grafo de conocimiento** (no proceden del texto del prospecto): atrofia multisistémica, síndrome de taquicardia postural ortostática, hipotensión ortostática, discinesia inducida por fármacos, síndrome de QT largo (incluido el familiar), torsades de pointes, enfermedad hepática, enfermedad de la vesícula biliar, trastorno psicótico, trastorno esquizofreniforme, trastorno esquizoafectivo, trastorno mental, deficiencia de potasio, abuso/dependencia de sustancias, enfermedad coronaria, insuficiencia renal, priapismo y trastorno cerebrovascular.
- **Interacciones farmacológicas**: se identificaron 13 interacciones farmacodinámicas con dianas (receptores 5-HT1A/2A/2B/2C, adrenérgicos α2A/2B/2C, dopaminérgicos D1–D5 y TRPA1). No se dispone de interacciones con otros fármacos clasificadas por nivel de gravedad.

Un aspecto crítico: el grafo señala como contraindicados el trastorno psicótico, el esquizofreniforme y el esquizoafectivo, lo que entra en conflicto directo con la indicación predicha. Para el resto de advertencias, consultar el prospecto.

## Otras Predicciones del Modelo (todas sin ensayos ni literatura)

| Rango | Enfermedad predicha | Puntaje TxGNN | Nivel | Valoración |
|------|------|------|------|------|
| 1 | Polimicrogiria perisilviana con hipoplasia cerebelosa y artrogriposis | 99,75 % | L5 | Sin vínculo mecanístico; probable artefacto de red |
| 2 | Trastorno congénito de la glicosilación con fucosilación defectuosa | 99,73 % | L5 | Sin justificación mecanística |
| 3 | Distrofia retiniana con o sin anomalías extraoculares | 99,71 % | L5 | Plausibilidad laxa (dopamina retiniana), sin respaldo |
| 4 | Enfermedad de Charcot-Marie-Tooth desmielinizante tipo 1G | 99,71 % | L5 | Sin vínculo mecanístico |
| 6 | Miopía ligada al X | 99,69 % | L5 | Racional débil; etiología genética |
| 7 | Encefalopatía atípica por glicina | 99,68 % | L5 | Sin vínculo mecanístico |
| 8 | Miopía 26 ligada al X, limitada a mujeres | 99,64 % | L5 | Especulativo |
| 9 | Miopía sindrómica | 99,60 % | L5 | Plausibilidad laxa, solo predicción |
| 10 | Hidranencefalia | 99,54 % | L5 | Sin vínculo plausible |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No existen ensayos clínicos y la literatura sobre esquizofrenia (nivel L4) es antigua, de pequeña escala o mecanística, sin mostrar beneficio terapéutico; además, el mecanismo agonista dopaminérgico choca con el tratamiento estándar y el grafo de conocimiento registra los trastornos psicóticos como contraindicación. El resto de predicciones son solo computacionales (L5).

**Para avanzar se necesita:**
- Datos del mecanismo de acción de apomorfina (consultar DrugBank).
- Advertencias y contraindicaciones del prospecto de la AEMPS, hoy no disponibles, lo que impide el cribado de seguridad.
- Textos de indicación aprobada de las autorizaciones españolas.
- Evidencia clínica directa que justifique reconsiderar la hipótesis; de lo contrario, descartar esquizofrenia y priorizar otras líneas.
- Evaluación de compatibilidad de vía de administración (actualmente pendiente).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

