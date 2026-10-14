---
layout: default
title: Bevacizumab
parent: Solo predicción del modelo (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Bevacizumab
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

# Bevacizumab: De Cáncer de Peritoneo a Neoplasia de Epiglotis

## Resumen en Una Frase

Bevacizumab es un anticuerpo monoclonal que bloquea el factor de crecimiento endotelial vascular A (VEGF-A). Se utiliza en oncología, con indicaciones originales como el cáncer de peritoneo y ovario, el cáncer de mama, el cáncer colorrectal metastásico y el glioblastoma.
El modelo TxGNN predice que podría ser efectivo para **neoplasia de epiglotis**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta indicación concreta; solo existe la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de peritoneo (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Neoplasia de epiglotis |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Los datos compilados para este informe no incluyen una descripción detallada del mecanismo de acción. Según la información conocida, bevacizumab se une al VEGF-A y reduce la formación de nuevos vasos sanguíneos (angiogénesis) que los tumores necesitan para crecer.

Las indicaciones originales son tumores sólidos muy dependientes de la vascularización, como el cáncer de peritoneo, ovario, mama, colon y glioblastoma. Los tumores de cabeza y cuello también pueden depender de la angiogénesis. Por eso es plausible que bloquear el VEGF-A limite el crecimiento de una neoplasia de epiglotis.

Esta plausibilidad es solo teórica. No se aportó ningún ensayo ni publicación sobre esta indicación, y la similitud formal con las indicaciones originales aún no se ha evaluado. La predicción debe considerarse una hipótesis sin respaldo clínico directo.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Hay 13 autorizaciones vigentes, todas de medicamento único y ninguna cancelada. Todas son concentrado para solución para perfusión (25 mg/ml). Los textos de indicación aprobada no estaban disponibles en los datos compilados, por lo que no se incluyen.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 04300002IP | Avastin 25 mg/ml | Concentrado para solución para perfusión | Roche Registration GmbH |
| 04300001 | Avastin 25 mg/ml | Concentrado para solución para perfusión | Roche Registration GmbH |
| 1201454001 | Aybintio 25 mg/ml | Concentrado para solución para perfusión | Samsung Bioepis NL B.V. |
| 1181344002 | Zirabev 25 mg/ml | Concentrado para solución para perfusión | Pfizer Europe MA EEIG |
| 1201509001 | Alymsys 25 mg/ml | Concentrado para solución para perfusión | mAbxience Research S.L. |

Las otras 8 autorizaciones corresponden a Equidacent, Zirabev (segunda autorización), Mvasi (dos autorizaciones), Avastin (04300002), Abevmy, Vegzelma y Oyavas, es decir, el medicamento de referencia y varios biosimilares.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida (anticuerpo monoclonal anti-VEGF-A); no es un citotóxico convencional |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

No se dispone de advertencias principales ni contraindicaciones del prospecto en los datos compilados. Consultar el prospecto para esa información.

**Interacciones Farmacológicas:** se identificaron 22 interacciones (20 detalladas en los datos compilados), según la base DDInter.

- **Mayores:** deferiprona, samario (153Sm) lexidronam, panitumumab, sunitinib y talidomida.
- **Moderadas:**
  - Bifosfonatos: ácido alendrónico, risedrónico, etidrónico, pamidrónico, tiludrónico e ibandronato.
  - Factores estimulantes de colonias y afines: filgrastim, pegfilgrastim, sargramostim y palifermina.
  - Radiofármacos: estroncio-89, radio-223 y fosfato de sodio monobásico (P32).
  - Otros: idelalisib y romosozumab.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación se apoya solo en el puntaje del modelo (99.90%), sin ensayos clínicos ni literatura (nivel L5). Tampoco hay datos de seguridad del prospecto ni mecanismo de acción detallado, por lo que no es posible avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS.
- Documentar el mecanismo de acción detallado.
- Revisar la literatura y los registros de ensayos específicos de tumores de laringe y epiglotis, incluidos los estudios en cáncer de cabeza y cuello.
- Evaluar la similitud con las indicaciones originales y la compatibilidad de la vía de administración (actualmente solo perfusión intravenosa).

**Nota sobre otras predicciones:** entre las predicciones del mismo modelo, la **neoplasia quística** (que corresponde a tumores epiteliales de ovario) tiene evidencia mucho más sólida (nivel L1). Incluye un ensayo de Fase 3 (NCT00565851, n=1052) y una revisión sistemática. Merece una evaluación independiente como candidata prioritaria.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

