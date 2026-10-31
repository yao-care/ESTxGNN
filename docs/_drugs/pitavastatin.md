---
layout: default
title: Pitavastatin
parent: Solo predicción del modelo (L5)
nav_order: 645
evidence_level: L5
indication_count: 4
monitor_inn: "pitavastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "feline acquired immunodeficiency syndrome"]
last_modified_at: 2026-10-31
description: "Pitavastatin: nueva indicación predicha, Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) (nivel de evidencia L5). Indicación origi…"
---

# Pitavastatin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

## Pitavastatin: Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency)
{: .text-alpha }

## Resumen en Una Frase

Pitavastatina es una estatina que, según la relación registrada en el grafo de conocimiento, se asocia con la hiperlipidemia familiar combinada.
El modelo TxGNN predice que podría ser efectiva para la **deficiencia de la proteína de transferencia de ésteres de colesterol (CETP)**,
pero **no hay ensayos clínicos ni publicaciones** que respalden actualmente esta dirección, por lo que es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Deficiencia de la proteína de transferencia de ésteres de colesterol (cholesterol-ester transfer protein deficiency) |
| Puntaje de Predicción TxGNN | 0.9998 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (registros vigentes: al menos 13) |
| Número de Autorizaciones | al menos 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la pitavastatina pertenece a la clase de las estatinas (inhibidores de la HMG-CoA reductasa), que reducen el colesterol LDL.

La deficiencia de CETP es un trastorno del metabolismo de las lipoproteínas, típicamente con colesterol HDL elevado. El puntaje tan alto del modelo probablemente refleja que ambas condiciones comparten la vía del metabolismo lipídico en la red de conocimiento.

Sin embargo, la deficiencia de CETP normalmente no es una condición que requiera tratamiento para reducir el LDL, por lo que la justificación clínica es débil. No hay estudios que respalden la hipótesis, y debe considerarse una señal computacional sin confirmación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

La lista de autorizaciones puede ser parcial. Los registros no incluyen texto de indicación aprobada. A continuación se muestran 5 autorizaciones vigentes:

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 73040 | ALIPZA 4 mg comprimidos recubiertos con película (Kowa Pharmaceutical Europe) | Comprimido recubierto con película |
| 84894 | Pitavastatina Alter 1 mg EFG (Laboratorios Alter) | Comprimido recubierto con película |
| 84955 | Pitavastatina Kern Pharma 4 mg EFG (Kern Pharma) | Comprimido recubierto con película |
| 85211 | Pitavastatina Normon 1 mg EFG (Laboratorios Normon) | Comprimido recubierto con película |
| 84951 | Pitavastatina Pensa 2 mg EFG (Towa Pharmaceutical) | Comprimido recubierto con película |

## Consideraciones de Seguridad

- **Contraindicaciones y condiciones de riesgo (relaciones registradas en el grafo de conocimiento, no texto del prospecto)**: enfermedad hepática, enfermedad de la vesícula biliar, hipotiroidismo (incluidos mixedema e hipotiroidismo congénito), miopatía y enfermedades musculares, parálisis periódica familiar, rabdomiólisis, función renal alterada, trastornos hipotensivos, fascitis nodular y lesiones.
- **Interacciones farmacológicas**: se registraron 86 interacciones y se dispone del detalle de 20.
  - **Mayor**: eritromicina.
  - **Moderadas (entre otras)**: rosuvastatina, simvastatina, cobicistat, eltrombopag, cloroquina, hidroxicloroquina, metronidazol, naltrexona, eluxadolina, disulfiram y etanol.
  - **Menores**: warfarina y dicumarol.

Para las advertencias del prospecto, consultar el prospecto oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje muy alto, pero no está respaldada por ningún ensayo ni publicación sobre esta enfermedad (nivel L5). Además, la deficiencia de CETP normalmente no requiere tratamiento hipolipemiante.

**Para avanzar se necesita:**
- Estudios preclínicos o clínicos que evalúen directamente la pitavastatina en la deficiencia de CETP.
- Una justificación clínica de la necesidad terapéutica (beneficio esperado en una condición con HDL elevado).
- Datos del mecanismo de acción y de las advertencias y contraindicaciones del prospecto.

**Nota:** entre las otras predicciones del modelo, la relacionada con el VIH sí tiene evidencia sólida (ensayo REPRIEVE, publicado en NEJM 2023). Esa evidencia se refiere a la prevención de enfermedad cardiovascular en personas con VIH, no al tratamiento de la infección, y no respalda la indicación evaluada en este informe.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

