---
layout: default
title: Trastuzumab
parent: Evidencia alta (L1-L2)
nav_order: 815
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Trastuzumab: nueva indicación predicha, Cáncer de mama con receptor de progesterona positivo (predicción de m… (nivel de evidencia L1). Indicación original: Carcinoma de mama HER2 positivo"
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "progesterone-receptor negative breast cancer", "breast tumor luminal A or B", "malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
---

# Trastuzumab
{: .fs-9 }

Nivel de evidencia: **L1** | Indicaciones predichas: **10** 
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

# Trastuzumab: De Carcinoma de Mama HER2 Positivo a Carcinoma de Mama con Receptor de Progesterona Positivo

## Resumen en Una Frase

Trastuzumab es un anticuerpo monoclonal dirigido contra HER2, utilizado originalmente para el tratamiento del carcinoma de mama HER2 positivo.
El modelo TxGNN predice que podría ser efectivo para el **cáncer de mama con receptor de progesterona positivo**, con **12 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección.
Cabe aclarar que se trata de una estratificación por subtipo dentro de una indicación ya aprobada, y no de un reposicionamiento verdaderamente nuevo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de mama HER2 positivo |
| Nueva Indicación Predicha | Cáncer de mama con receptor de progesterona positivo (predicción de mayor rango: subtipo "normal breast-like", ver nota) |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Proceed with Guardrails |

**Nota:** la primera predicción de la lista (subtipo de mama "normal breast-like", puntaje 99.90%, nivel L4) tiene solo un ensayo, que evalúa un fármaco distinto (trastuzumab rezetecán, un conjugado anticuerpo-fármaco), y no tiene fundamento mecanístico directo, por lo que se recomienda **Hold**. Este informe se centra en la predicción de cáncer de mama con receptor de progesterona positivo (mismo puntaje, 99.90%), que es la primera con evidencia sustancial (L1).

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, trastuzumab se une al dominio extracelular de HER2, bloquea su señalización y media citotoxicidad celular dependiente de anticuerpos (ADCC). Su eficacia en el cáncer de mama HER2 positivo está comprobada.

En tumores con receptor de progesterona positivo, el beneficio depende de la coexpresión de HER2. La interacción (crosstalk) entre HER2 y los receptores hormonales es un mecanismo de resistencia conocido, y la combinación con terapia endocrina o inhibidores de CDK4/6 cuenta con respaldo.

Por tanto, esta predicción se solapa con la indicación ya aprobada: es una estratificación por subtipo y no una indicación novedosa. El beneficio se limita a pacientes HER2 positivas. La predicción de cáncer de mama con receptor de progesterona negativo (99.90%) sigue la misma lógica, ya que la acción de trastuzumab es independiente del estado del receptor de progesterona.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Fase 3 | Completado | 3270 | Quimioterapia adyuvante con o sin trastuzumab en cáncer de mama invasivo con ganglios positivos o alto riesgo |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Fase 3 | Completado | 517 | QL1209/pertuzumab con docetaxel y trastuzumab en cáncer de mama HER2 positivo, ER/PR negativo |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Fase 2 | Completado | 92 | Quimioterapia neoadyuvante con o sin trastuzumab |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Fase 2 | Completado | 50 | Quimioterapia neoadyuvante en cáncer de mama HER2 positivo resecable |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Fase 2 | Completado | 36 | Cabozantinib solo o con trastuzumab en metástasis cerebrales |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Fase 2 | Completado | 33 | Letrozol más trastuzumab en cáncer de mama metastásico ErbB2 positivo con receptores hormonales positivos |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Fase 2 | Desconocido | 34 | Palbociclib, trastuzumab, pirotinib y fulvestrant en metástasis cerebrales ER/PR+, HER2+ |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Fase 2 | Reclutando | 30 | Neratinib y terapia endocrina con trastuzumab preoperatorio en ER+, HER2+ |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Fase 1 | Completado | 37 | Everolimus, letrozol y trastuzumab en cáncer avanzado con receptores hormonales y HER2 positivos |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Fase 3 | Retirado | 0 | Trastuzumab con o sin tamoxifeno; sin inscripción, no aporta evidencia |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | ECA (fase 2) | Lancet Oncol | monarcHER: abemaciclib más trastuzumab con o sin fulvestrant frente a quimioterapia más trastuzumab en cáncer avanzado HR+/HER2+ |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | ECA (fase 2) | Ann Oncol | WSG-ADAPT: desescalada neoadyuvante con trastuzumab y pertuzumab ± paclitaxel |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | ECA (fase 3) | Lancet Oncol | ExteNET: neratinib tras terapia adyuvante basada en trastuzumab |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Ensayo fase 2 | Lancet Oncol | NeoSphere: análisis a 5 años de pertuzumab y trastuzumab neoadyuvantes |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Metaanálisis | Lancet | Efecto de quimioterapia y terapia hormonal en cáncer de mama precoz sobre recurrencia y supervivencia a 15 años |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Cohorte | Theranostics | Perfiles moleculares y respuesta a trastuzumab en cáncer triple positivo (ER+/PR+/HER2+) |
| [33726508](https://pubmed.ncbi.nlm.nih.gov/33726508/) | 2021 | Revisión | Future Oncol | Tendencias actuales en el tratamiento del cáncer HR+/HER2+ |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Revisión | Nat Rev Clin Oncol | Cáncer de mama HER2 y receptor hormonal positivo: bloqueo de la diana correcta |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | Fase 2a | Lancet Oncol | Zanidatamab con palbociclib y fulvestrant en cáncer HR+/HER2+ metastásico |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Revisión | Breast | Implicaciones clínicas de los subtipos moleculares intrínsecos del cáncer de mama |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171241001 | Ontruzant 150 mg | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 1181281001 | Kanjinti 150 mg | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 1181295002 | Trazimera 420 mg | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 1171257001 | Herzuma 150 mg | Polvo para concentrado para solución para perfusión | No disponible en los datos compilados |
| 100145002 | Herceptin 600 mg | Solución inyectable | No disponible en los datos compilados |

Se registran 17 autorizaciones vigentes en total (incluyen biosimilares como Ontruzant, Kanjinti, Trazimera, Herzuma, Ogivri y Zercepac, además del original Herceptin).

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2) |
| Riesgo de Mielosupresión | Bajo como agente único; puede aumentar al combinarse con quimioterapia |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Función cardíaca (fracción de eyección del ventrículo izquierdo), hemograma, función hepática y renal |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

La literatura compilada también señala la cardiotoxicidad como aspecto relevante de seguimiento (PMID 17687157, 27038641).

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: se identificaron 94 interacciones; entre las de nivel **Mayor** figuran deferiprona, samario (153Sm) lexidronam, adalimumab y baricitinib. Entre las de nivel moderado destacan warfarina, paclitaxel, zidovudina, azatioprina, alemtuzumab y anakinra.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
La evidencia es sólida (L1): hay ensayos de fase 3 completados (como NCT01275677 con 3270 pacientes) y varios ECA en poblaciones HR+/HER2+. Sin embargo, la predicción coincide con la indicación ya aprobada y el beneficio se restringe a pacientes HER2 positivas, por lo que se trata de una estratificación y no de un reposicionamiento novedoso. Las predicciones de subtipo "normal breast-like" y las de tumores raros (L5) deben quedar en **Hold**.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS (hueco de datos bloqueante para el cribado de seguridad)
- Completar los datos del mecanismo de acción desde DrugBank
- Confirmar los textos de indicación aprobada de las autorizaciones españolas
- Definir un plan de monitoreo cardíaco y restringir el uso a pacientes con HER2 positivo confirmado
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

