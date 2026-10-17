---
layout: default
title: Catumaxomab
parent: Solo predicción del modelo (L5)
nav_order: 153
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Catumaxomab: nueva indicación predicha, Retinopatía diabética no proliferativa grave (nivel de evidencia L5). Indicación original: No disponible en los textos de autorización de la AEMPS (según infor…"
monitor_inn: "CATUMAXOMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "drug-induced osteoporosis", "diabetic retinopathy"]
---

# Catumaxomab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Catumaxomab: De Ascitis Maligna a Retinopatía Diabética No Proliferativa Grave

## Resumen en Una Frase

Catumaxomab es un anticuerpo biespecífico trifuncional (EpCAM x CD3) comercializado en España, cuya indicación original no figura en los datos de autorización compilados para este informe. El modelo TxGNN predice que podría ser efectivo para la **retinopatía diabética no proliferativa grave**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los textos de autorización de la AEMPS (según información farmacológica de referencia: ascitis maligna asociada a cánceres EpCAM positivos) |
| Nueva Indicación Predicha | Retinopatía diabética no proliferativa grave |
| Puntaje de Predicción TxGNN | 99,64 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Catumaxomab es un anticuerpo biespecífico trifuncional que se une a EpCAM (presente en células tumorales epiteliales) y a CD3ε (en linfocitos T). Además, mediante su región Fc recluta células accesorias, dirigiendo la destrucción inmunitaria hacia las células tumorales. No se dispone de datos detallados del mecanismo de acción en la información compilada; lo anterior procede de la anotación farmacológica de su diana principal (CD3E).

**La predicción no cuenta con un vínculo mecanístico respaldado por los datos.** La retinopatía diabética es una enfermedad microvascular, dependiente de VEGF e inflamatoria, y no una neoplasia que exprese EpCAM. Las terapias establecidas actúan sobre VEGF, la inflamación y el control glucémico y vascular, vías con las que catumaxomab no se alinea. El puntaje elevado (0,996) refleja un patrón del grafo de conocimiento, no evidencia biológica.

Las otras dos predicciones del modelo (osteoporosis inducida por fármacos, 99,58 %, y retinopatía diabética general, 99,47 %) tampoco tienen respaldo clínico ni bibliográfico. La retinopatía diabética es la categoría general de la primera indicación, por lo que probablemente comparten patrones de embedding y no constituyen señales biológicas independientes. Además, la activación de linfocitos T implicaría riesgos de inflamación ocular y síndrome de liberación de citocinas.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241826001 | KORJUNY 10 microgramos concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 1241826002 | KORJUNY 50 microgramos concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 09512001 | REMOVAB 10 microgramos concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |
| 09512002 | REMOVAB 50 microgramos concentrado para solución para perfusión | Concentrado para solución para perfusión | No disponible en los datos |

Las cuatro autorizaciones están vigentes. KORJUNY corresponde a Atnahs Pharma Netherlands y REMOVAB a Fresenius Biotech. Según la información farmacológica de referencia, la autorización europea para la ascitis maligna en cánceres EpCAM positivos se retiró en 2017 por motivos comerciales y se reautorizó a principios de 2025.

---

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo biespecífico EpCAM x CD3; código ATC L01XC09) |
| Riesgo de Mielosupresión | Consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Consultar las advertencias y precauciones del prospecto |
| Items de Monitoreo | Consultar las advertencias y precauciones del prospecto; por su mecanismo, vigilar signos de liberación de citocinas |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: la consulta se completó y registró una única entrada, correspondiente a la diana farmacológica CD3ε (no a un fármaco concomitante), sin nivel de gravedad asignado. No se identificaron interacciones con otros fármacos.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las tres indicaciones predichas se basan solo en el modelo (nivel L5), sin ensayos ni publicaciones, y carecen de un vínculo mecanístico plausible con un anticuerpo dirigido a EpCAM y CD3. Además, no se dispone de la información de seguridad del prospecto, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es un bloqueo actual.
- Obtener datos detallados del mecanismo de acción desde DrugBank.
- Confirmar la indicación original autorizada en España.
- Estudios preclínicos que demuestren una base biológica para la retinopatía diabética, incluida la evaluación de la seguridad ocular y del riesgo de liberación de citocinas.
- Evaluar la compatibilidad de vías de administración (la forma actual es perfusión; una indicación oftálmica requeriría otra estrategia).
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

