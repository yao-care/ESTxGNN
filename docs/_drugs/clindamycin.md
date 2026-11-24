---
layout: default
title: Clindamycin
parent: Solo predicción del modelo (L5)
nav_order: 189
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
description: "Clindamycin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 16 (comercializadas: 13)"
---

# Clindamycin
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

## Clindamycin: Queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## Resumen en Una Frase

Clindamicina es un antibiótico utilizado originalmente para tratar infecciones bacterianas (estreptocócicas, estafilocócicas y por anaerobios), acné y vaginosis bacteriana.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada (punctate epithelial keratoconjunctivitis) |
| Puntaje de Predicción TxGNN | 0.9997 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 13 de 16; revocadas o suspendidas: 3) |
| Número de Autorizaciones | 16 (comercializadas: 13) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para Clindamycin (traducción no oficial): «La clindamicina inhibe la síntesis de proteínas bacterianas mediante su unión al ARN 23S de la subunidad 50S del ribosoma. La clindamicina es bacteriostática.» Texto original en inglés: "Clindamycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the ribosome. Clindamycin is bacteriostatic." ([DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a), versión del 2026-09-16; consultado el 2026-11-19). Según la información conocida, clindamicina es un antibiótico que inhibe la síntesis de proteínas bacterianas al actuar sobre la subunidad ribosomal 50S, y su eficacia en infecciones bacterianas cutáneas, respiratorias y ginecológicas está bien establecida.

La relación con la nueva indicación es débil. La queratoconjuntivitis epitelial punteada suele tener origen viral o inflamatorio, por lo que un antibacteriano no tiene un vínculo mecanístico claro, salvo que exista un componente bacteriano. El puntaje elevado proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

Por tanto, la predicción debe considerarse una hipótesis sin respaldo experimental. No se han recuperado estudios que evalúen clindamicina en esta enfermedad, y el uso oftálmico tópico de clindamicina no está establecido.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Predicciones Evaluadas

Para contexto, estas fueron las demás indicaciones predichas por el modelo, todas con decisión Hold:

<!-- review:begin es-lic-20261105-clindamycin-1 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Se muestran 5 de las 16 autorizaciones vigentes (los textos de indicación aprobada no están disponibles en los datos compilados)." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-clindamycin-1 -->

| Indicación Predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Queratitis por exposición | 0.9980 | L4 | Solo literatura indirecta (casos de queratitis por *S. aureus* y *B. cereus*); ningún estudio evalúa clindamicina |
| Enfermedad animal no humana | 0.9969 | L5 | Categoría no clínica; la literatura trata sobre *C. difficile*, y clindamicina es un factor de riesgo, no una opción terapéutica |
| Queratopatía neurotrófica | 0.9949 | L5 | Patología degenerativa no bacteriana; sin evidencia |
| Queratoconjuntivitis epidémica | 0.9949 | L5 | Causa adenoviral; la literatura es veterinaria (bovina) y no aplicable |
| Vaginitis atrófica posmenopáusica | 0.9903 | L5 | Causa por déficit estrogénico; el mecanismo no se transfiere |

## Información de Mercado en España

<!-- licenses:begin -->

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular | Estado |
|---------|------|------|------|------|
| 62911 | DALACIN 100 mg OVULOS | ÓVULO | Pfizer S.L. | Comercializada |
| 81565 | CLINDAMICINA QUALIGEN 300 MG CAPSULAS DURAS EFG | CÁPSULA DURA | Neuraxpharm Spain S.L.U. | Comercializada |
| 60034 | DALACIN 20 mg/g CREMA VAGINAL | CREMA VAGINAL | Pfizer S.L. | Comercializada |
| 81568 | CLINDAMICINA QUALIGEN 150 MG CAPSULAS DURAS EFG | CÁPSULA DURA | Neuraxpharm Spain S.L.U. | Comercializada |
| 63669 | CLINDAMICINA NORMON 600 mg/4 ml SOLUCION INYECTABLE EFG | SOLUCIÓN INYECTABLE | Laboratorios Normon S.A. | Comercializada |
| 58783 | DALACIN 300 mg CAPSULAS DURAS | CÁPSULA DURA | Pfizer S.L. | Comercializada |
| 66610 | ZINDACLIN 1% GEL | GEL | Industrial Farmaceutica Cantabria S.A. | Comercializada |
| 60361 | CLINWAS 10 MG/ML SOLUCIÓN PARA PULVERIZACIÓN CUTÁNEA | SOLUCIÓN CUTÁNEA | Chiesi España S.A.U. | Comercializada |
| 49152 | DALACIN 150 mg CAPSULAS DURAS | CÁPSULA DURA | Pfizer S.L. | Comercializada |
| 60362 | CLINWAS 10 MG/G GEL | GEL | Chiesi España S.A.U. | Comercializada |

Se muestran 10 de 16 autorizaciones con este principio activo en los datos de CIMA (AEMPS); primero las comercializadas.

<!-- licenses:end -->

Existen presentaciones orales, inyectables, vaginales y cutáneas (gel, solución y emulsión); no hay presentaciones oftálmicas.

<!-- review:begin es-lic-20261105-clindamycin-2 -->

> **Corrección de revisión (2026-11-24)**: Texto original: "Las 16 autorizaciones son de medicamentos con clindamicina como único principio activo, y todas están vigentes. Existen presentaciones orales, inyectables, vaginales y cutáneas (gel, solución y emulsión); no hay presentaciones oftálmicas." Eliminado: el número o el estado de comercialización de las autorizaciones no coincidía con los datos de CIMA (AEMPS) reconstruidos por principio activo el 2026-11-05. Las cifras actuales están en el Resumen rápido y en la tabla de Información de Mercado en España. Fuente: [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html).

<!-- review:end es-lic-20261105-clindamycin-2 -->

## Consideraciones de Seguridad

- **Contraindicaciones o enfermedades de precaución según el grafo de conocimiento** (no proviene del prospecto): insuficiencia hepática, enfermedad de Crohn, enfermedad inflamatoria intestinal, colitis ulcerosa, colitis por *Clostridium difficile*, enfermedad diarreica, enterocolitis necrosante perinatal, dermatitis (atópica y exfoliativa), quemadura solar y candidiasis vulvovaginal.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total. Las de nivel moderado incluyen balsalazida, claritromicina, ácido picosulfúrico, atapulgita y caolín. Otras (nivel desconocido) incluyen anfotericina B, ácido acetilsalicílico, amoxicilina, bupropión, pantoprazol, metformina, omeprazol, morfina y vancomicina, entre otros.
- **Señal de riesgo relevante**: clindamicina se asocia de forma conocida con colitis por *C. difficile*, lo que debe considerarse en cualquier uso nuevo, especialmente sistémico.

Para las advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y la patología (habitualmente viral o inflamatoria) no se corresponde con el mecanismo antibacteriano de clindamicina. Ninguna de las otras indicaciones predichas ofrece una alternativa más sólida.

**Para avanzar se necesita:**
- Datos de advertencias y contraindicaciones del prospecto de la AEMPS (carencia bloqueante para el cribado de seguridad).
- Datos detallados del mecanismo de acción.
- Evidencia de que existe un componente bacteriano en la queratoconjuntivitis epitelial punteada y estudios preclínicos o de series de casos con clindamicina.
- Evaluación de la vía de administración: no existe una formulación oftálmica comercializada en España.
- Revisión del perfil de riesgo (colitis por *C. difficile*, interacciones) si se avanzara con una vía sistémica.

<!-- review:begin log -->

## Registro de revisión

A continuación figura el registro de revisión de esta página: afirmaciones contrastadas con los datos oficiales que usa este sitio (AEMPS, CIMA). Las correcciones se limitan a afirmaciones factuales básicas; las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial).

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-24 | Eliminado: "Se muestran 5 de las 16 autorizaciones vigentes (los textos de indicación aprobada no están disponibles en los datos compilados)" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-24 | Eliminado: "Las 16 autorizaciones son de medicamentos con clindamicina como único principio activo, y todas están vigentes" | Corregido (revisado el 2026-11-24; la versión anterior se guarda en el registro) | [AEMPS: CIMA, Centro de Información online de Medicamentos](https://cima.aemps.es/cima/publico/home.html) |
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

