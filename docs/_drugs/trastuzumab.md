---
layout: default
title: Trastuzumab
parent: Solo predicción del modelo (L5)
nav_order: 540
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: Nueva Indicación Predicha en Subtipo de Carcinoma de Mama Tipo «Normal-like»

## Resumen en Una Frase

Trastuzumab es un anticuerpo monoclonal dirigido contra HER2, comercializado en España como biosimilares en polvo para perfusión. Los registros de la AEMPS recibidos no incluyen el texto de la indicación original.
El modelo TxGNN predice que podría ser efectivo para el **subtipo de carcinoma de mama tipo «normal-like»**. Hay **12 ensayos clínicos** y **1 publicación** asociados, pero ninguno demuestra beneficio específico en este subtipo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Subtipo de carcinoma de mama tipo «normal-like» |
| Puntaje de Predicción TxGNN | 99,90 % |
| Nivel de Evidencia | L3 (el paquete de datos asignó L2; ver nota abajo) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

> **Nota sobre el nivel de evidencia:** el paquete asignó L2, pero ningún ensayo aportado es un ECA de Fase 2/3 completado en este subtipo. El único estudio publicado es una cohorte observacional. Por eso lo clasifico como L3.

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de datos. Según la información conocida, trastuzumab es un anticuerpo monoclonal anti-HER2. Bloquea la señalización de HER2 y puede mediar citotoxicidad celular dependiente de anticuerpos (ADCC). Mecanísticamente podría ser aplicable al cáncer de mama, pero solo cuando el tumor depende de HER2.

Aquí está el problema. El beneficio de trastuzumab depende del estado de HER2, no de la etiqueta del subtipo intrínseco. La etiqueta «normal-like» es ambigua y se solapa poco con la enfermedad enriquecida en HER2.

El puntaje TxGNN muy alto probablemente refleja la relación general del fármaco con el carcinoma de mama, no un mecanismo específico de este subtipo. Como los campos de indicación original y de mecanismo de acción están vacíos, no se pudo contrastar el solapamiento con la indicación autorizada.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04759248](https://clinicaltrials.gov/study/NCT04759248) | Fase 2 | Activo, sin reclutar | 55 | Atezolizumab + trastuzumab + vinorelbina en cáncer de mama HER2+ con RE negativo o subtipo PAM50 no luminal. Es el más cercano a un subtipo no luminal; sin resultados. |
| [NCT05582499](https://clinicaltrials.gov/study/NCT05582499) | Fase 2 | Reclutando | 716 | Plataforma de terapia neoadyuvante de precisión (FASCINATE-N). Relevante para anti-HER2, sin resultados por subtipo. |
| [NCT06328387](https://clinicaltrials.gov/study/NCT06328387) | Fase 1/2 | Desconocido | 120 | Hidroxicloroquina + conjugado anticuerpo-fármaco en cáncer de mama avanzado. Estudio temprano de combinación. |
| [NCT06585969](https://clinicaltrials.gov/study/NCT06585969) | Fase 3 | Retirado | 0 | Trastuzumab deruxtecán frente a inhibidores de CDK4/6 en cáncer de mama no luminal A, HER2-bajo. No aporta evidencia; además evalúa otro fármaco. |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Fase 3 | Activo, sin reclutar | 720 | Paclitaxel semanal ± carboplatino neoadyuvante en cáncer de mama triple negativo. La contribución de trastuzumab no está confirmada. |
| [NCT01796197](https://clinicaltrials.gov/study/NCT01796197) | Fase 2 | Completado | 23 | Paclitaxel + trastuzumab + pertuzumab preoperatorio en cáncer de mama inflamatorio HER2+. Brazo único. |
| [NCT06348134](https://clinicaltrials.gov/study/NCT06348134) | Fase 2 | Reclutando | 74 | Tratamiento anti-HER2 neoadyuvante/adyuvante en mujeres nigerianas con cáncer de mama HER2+. |
| [NCT05659056](https://clinicaltrials.gov/study/NCT05659056) | Fase 2 | Reclutando | 65 | Pirotinib + trastuzumab + Abraxane neoadyuvante en enfermedad enriquecida en HER2. |
| [NCT05900206](https://clinicaltrials.gov/study/NCT05900206) | Fase 2 | Reclutando | 370 | ARIADNE: trastuzumab deruxtecán frente a tratamiento preoperatorio estándar en HER2+. |
| [NCT04750122](https://clinicaltrials.gov/study/NCT04750122) | Fase 1/2 | Reclutando | 46 | Neoadyuvancia guiada por cribado de fármacos en agregados celulares derivados del paciente, en HER2+ precoz. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [19466513](https://pubmed.ncbi.nlm.nih.gov/19466513/) | 2009 | Cohorte | Breast Cancer (Tokyo) | Características morfológicas y citopatológicas del carcinoma de mama de subtipo basal-like. Describe los subtipos moleculares, pero no evalúa trastuzumab ni el subtipo «normal-like». |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 1171241001 | Ontruzant 150 mg | Polvo para concentrado para solución para perfusión | Samsung Bioepis NL B.V. |
| 1171241002 | Ontruzant 420 mg | Polvo para concentrado para solución para perfusión | Samsung Bioepis NL B.V. |
| 1181281001 | Kanjinti 150 mg | Polvo para concentrado para solución para perfusión | Amgen Europe B.V. |
| 1181295002 | Trazimera 420 mg | Polvo para concentrado para solución para perfusión | Pfizer Europe MA EEIG |
| 1171257001 | Herzuma 150 mg | Polvo para concentrado para solución para perfusión | Celltrion Healthcare Hungary Kft. |

Los registros recibidos no incluyen el texto de las indicaciones aprobadas.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-HER2) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Función cardíaca (uno de los ensayos aportados, NCT01436604, estudia la toxicidad cardíaca de trastuzumab); resto según el prospecto |
| Protección en Manejo | Consultar el prospecto y la normativa local de manejo de medicamentos citotóxicos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
- El puntaje TxGNN es muy alto, pero ningún ensayo ni publicación aportado demuestra beneficio de trastuzumab en el subtipo «normal-like». El beneficio depende de HER2, no del subtipo.
- Los datos de seguridad de la AEMPS faltan (carencia bloqueante).

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), un requisito bloqueante.
- Obtener las indicaciones autorizadas y el mecanismo de acción (DrugBank) para contrastar el solapamiento con la indicación original.
- Definir si «normal-like» se refiere a tumores con HER2 confirmado. Si no, la predicción carece de base clínica.
- Como alternativa dentro del mismo paquete, revisar las predicciones de cáncer de mama con receptor de progesterona positivo o negativo y de luminal A/B. Tienen más ensayos de Fase 2 y ECA, pero solo se sostienen en tumores HER2-positivos confirmados.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

