---
layout: default
title: Enoxaparin
parent: Solo predicción del modelo (L5)
nav_order: 290
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
monitor_inn: "enoxaparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive"]
description: "Enoxaparin: nueva indicación predicha, Trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency… (nivel de evidencia L5). Indicación original: No cons…"
---

# Enoxaparin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

## Enoxaparin: Trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive)
{: .text-alpha }

## Resumen en Una Frase

Enoxaparina es una heparina de bajo peso molecular, utilizada originalmente en indicaciones como la embolia pulmonar, la coagulación intravascular diseminada y la púrpura fulminante.
El modelo TxGNN predice que podría ser efectivo para **trombofilia por deficiencia de proteína C, autosómica recesiva**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección: se trata solo de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Trombofilia por deficiencia de proteína C, autosómica recesiva (thrombophilia due to protein C deficiency, autosomal recessive) |
| Puntaje de Predicción TxGNN | 0.9958 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 14) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Los datos compilados no incluyen una descripción detallada del mecanismo de acción registrado. Según el conocimiento general, la enoxaparina es una heparina de bajo peso molecular que potencia la antitrombina III e inhibe principalmente el factor Xa y, en menor medida, la trombina.

La deficiencia grave (homocigota) de proteína C elimina una vía anticoagulante natural, lo que provoca una generación descontrolada de trombina, púrpura fulminante neonatal y trombosis venosa recurrente. La enoxaparina podría compensar parcialmente este defecto mediante la inhibición de la coagulación dependiente de antitrombina. Además, comparte fisiopatología con indicaciones ya conocidas del fármaco (púrpura fulminante, púrpura fulminante adquirida y CID), todas ellas con trombosis microvascular impulsada por trombina.

El puntaje elevado de TxGNN refleja esta cercanía en la red de conocimiento, pero no constituye evidencia clínica. El tratamiento estándar de la deficiencia grave congénita se basa en concentrado de proteína C o plasma fresco congelado, con anticoagulación (heparina/HBPM o antagonistas de la vitamina K) como complemento o terapia a largo plazo. Cualquier uso de enoxaparina en este contexto debe verificarse en la literatura, ya que los datos aportados no lo respaldan.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes (todas de medicamentos con un solo principio activo). El texto de indicación aprobada no está disponible en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62470 | Clexane 6.000 UI (60 mg)/0,6 ml | Solución inyectable en jeringa precargada | No disponible |
| 82494 | Enoxaparina Rovi 6.000 UI (60 mg)/0,6 ml | Solución inyectable en jeringa precargada | No disponible |
| 82497 | Crusia 10.000 UI (100 mg)/1 ml | Solución inyectable en jeringa precargada | No disponible |
| 83293 | Hepaxane 2.000 UI (20 mg)/0,2 ml | Solución inyectable en jeringa precargada | No disponible |
| 1161132007 | Inhixa 8.000 UI (80 mg)/0,8 ml | Solución inyectable | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): insuficiencia hepática, enfermedades hematológicas, trombocitopenia (incluida la trombocitopenia inducida por heparina), trastornos de la coagulación, hemofilia, osteoporosis (incluida la posmenopáusica), colitis ulcerosa y enfermedad inflamatoria intestinal, úlcera péptica activa, enfermedad de las vías biliares, ictericia obstructiva, arteriosclerosis obliterante, déficit de antitrombina III, enfermedades de la retina (retinitis, retinopatía diabética e hipertensiva, catarata diabética), endocarditis infecciosa (incluida la subaguda bacteriana), hemorragia intracraneal e intracerebral, desprendimiento de placenta, trombastenia de Glanzmann y defectos plaquetarios cualitativos.
- **Interacciones farmacológicas**: se identificaron 174 interacciones en total; se muestran las principales de nivel mayor entre las 20 primeras revisadas:
  - Ácido acetilsalicílico
  - Ibuprofeno
  - Ketorolaco
  - Alteplasa
  - Abciximab
  - Acalabrutinib
  - Deferasirox
  - Trastuzumab emtansina
  - Ibritumomab tiuxetán
  - Tositumomab (con y sin I-131)

  Además hay interacciones moderadas, por ejemplo con fenfluramina, dexfenfluramina, sibutramina, aliskireno, sugammadex y yoduros radiactivos (I-123 e I-131).

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero se encuentra en nivel L5: no hay ensayos clínicos ni literatura que la respalden, y faltan los datos del mecanismo de acción y las advertencias oficiales del prospecto. Además, el tratamiento estándar de esta enfermedad ya se basa en otras terapias (concentrado de proteína C).

**Para avanzar se necesita:**
- Revisión sistemática de la literatura sobre el uso de HBPM en deficiencia grave de proteína C
- Datos del mecanismo de acción desde DrugBank
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS (necesarias antes del cribado de seguridad)
- Textos de indicaciones aprobadas de las autorizaciones españolas
- Evaluación de compatibilidad de vías de administración y del perfil de riesgo hemorrágico en población neonatal/pediátrica
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

