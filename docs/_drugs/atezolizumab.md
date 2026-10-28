---
layout: default
title: Atezolizumab
parent: Solo predicción del modelo (L5)
nav_order: 74
evidence_level: L5
indication_count: 6
monitor_inn: "ATEZOLIZUMAB"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-28
description: "Atezolizumab: nueva indicación predicha, Adenocarcinoma del ligamento uterino (nivel de evidencia L5). Indicación original: Carcinoma de células transicionales"
---

# Atezolizumab
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

## Atezolizumab: De Carcinoma de Células Transicionales a Adenocarcinoma del Ligamento Uterino
{: .text-alpha }

## Resumen en Una Frase

Atezolizumab es un anticuerpo monoclonal que, según el grafo de conocimiento utilizado por el modelo, tiene registrada una relación con el **carcinoma de células transicionales**. El modelo TxGNN predice que podría ser efectivo para el **adenocarcinoma del ligamento uterino**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Carcinoma de células transicionales (relación registrada en el grafo de conocimiento; los registros de autorización locales no incluyen texto de indicación) |
| Nueva Indicación Predicha | Adenocarcinoma del ligamento uterino |
| Puntaje de Predicción TxGNN | 0,9993 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: 8 de 11) |
| Número de Autorizaciones | 11 (vigentes: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la información compilada para este informe. Según el conocimiento general, atezolizumab bloquea la proteína PD-L1 y puede restablecer la actividad antitumoral de los linfocitos T. Esa es su base para el uso en carcinoma de células transicionales.

La predicción para el adenocarcinoma del ligamento uterino solo podría apoyarse, de forma indirecta, en la expresión de PD-L1 que se observa en otros adenocarcinomas ginecológicos. Esta hipótesis **no está respaldada por datos directos** en la información compilada. La relación entre la indicación original (tumor urotelial) y la nueva (tumor ginecológico glandular) es por tanto especulativa. Se trata de una predicción del modelo que requiere validación.

**Nota complementaria:** entre las demás predicciones del modelo, el carcinoma endocervical (puntaje 0,9992) sí cuenta con estudios relacionados. Incluyen un ensayo de Fase 2 completado de atezolizumab con bevacizumab en cáncer de cuello uterino recurrente (NCT02921269, 11 pacientes) y un ensayo de Fase 1 completado con quimiorradioterapia (NCT03738228, 40 pacientes). Estos estudios no analizan directamente el adenocarcinoma del ligamento uterino, por lo que no se usan para determinar el nivel de evidencia de esta predicción.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 11 autorizaciones. Los registros no incluyen texto de indicación aprobada, por lo que no se puede indicar para qué usos están autorizados los productos.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1171220001 | Tecentriq 1200 mg | Concentrado para solución para perfusión |
| 1171220001IP3 | Tecentriq 1200 mg | Concentrado para solución para perfusión |
| 1171220002 | Tecentriq 840 mg | Concentrado para solución para perfusión |
| 1171220002IP1 | Tecentriq 840 mg | Concentrado para solución para perfusión |
| 1171220003 | Tecentriq 1875 mg | Solución inyectable |

Titular: Roche Registration GmbH.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Inmunoterapia (anticuerpo anti-PD-L1), no citotóxico convencional |
| Riesgo de Mielosupresión | Bajo en general; consultar las advertencias y precauciones del prospecto |
| Clasificación de Emetogenicidad | Baja |
| Items de Monitoreo | Hemograma, función hepática y renal, función tiroidea y glucemia (por posibles reacciones inmunomediadas) |
| Protección en Manejo | Consultar las advertencias y precauciones del prospecto y los protocolos del centro para manejo de medicamentos oncológicos |

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 75 interacciones potenciales. Las principales son:
  - **Mayores:** adalimumab, baricitinib y la vacuna BCG de microorganismos vivos (cepa Tice).
  - **Moderadas:** corticosteroides (hidrocortisona, prednisona, prednisolona, dexametasona, metilprednisolona, betametasona, budesonida, triamcinolona, deflazacort), azatioprina, alemtuzumab, anakinra, alefacept, roflumilast y varias vacunas (toxoide tetánico, ántrax, adenovirus tipo 4).

Para advertencias y contraindicaciones, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción alcanza un puntaje alto (0,9993), pero no existe ningún ensayo clínico ni publicación que estudie directamente el adenocarcinoma del ligamento uterino, por lo que el nivel de evidencia es L5. Además, el mecanismo de acción no está documentado en los datos compilados.

**Para avanzar se necesita:**
- Datos de mecanismo de acción y de expresión de PD-L1 en adenocarcinoma del ligamento uterino.
- Revisión sistemática de la literatura sobre esta histología, incluyendo series y reportes de caso.
- Obtención y análisis del prospecto de la AEMPS (advertencias y contraindicaciones).
- Valoración de la evidencia en cáncer cervical como posible vía de extrapolación, con evaluación de su aplicabilidad a esta entidad.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

