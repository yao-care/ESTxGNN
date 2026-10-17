---
layout: default
title: Clindamycin
parent: Solo predicción del modelo (L5)
nav_order: 189
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Clindamycin: nueva indicación predicha, Queratoconjuntivitis epitelial punteada (nivel de evidencia L5). Indicación original: Acné, infecciones estreptocócicas y estafilocócicas…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis"]
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

# Clindamicina: De Acné e Infecciones Bacterianas a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Clindamicina es un antibiótico utilizado originalmente para tratar infecciones bacterianas (estreptocócicas, estafilocócicas y por anaerobios), acné y vaginosis bacteriana.
El modelo TxGNN predice que podría ser efectivo para **queratoconjuntivitis epitelial punteada**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Acné, infecciones estreptocócicas y estafilocócicas, infecciones por bacterias anaerobias, vaginosis bacteriana (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 16 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, clindamicina es un antibiótico que inhibe la síntesis de proteínas bacterianas al actuar sobre la subunidad ribosomal 50S, y su eficacia en infecciones bacterianas cutáneas, respiratorias y ginecológicas está bien establecida.

La relación con la nueva indicación es débil. La queratoconjuntivitis epitelial punteada suele tener origen viral o inflamatorio, por lo que un antibacteriano no tiene un vínculo mecanístico claro, salvo que exista un componente bacteriano. El puntaje elevado probablemente refleja la proximidad en el grafo con infecciones oculares bacterianas, y no un mecanismo validado.

Por tanto, la predicción debe considerarse una hipótesis sin respaldo experimental. No se han recuperado estudios que evalúen clindamicina en esta enfermedad, y el uso oftálmico tópico de clindamicina no está establecido.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Otras Predicciones Evaluadas

Para contexto, estas fueron las demás indicaciones predichas por el modelo, todas con decisión Hold:

| Indicación Predicha | Puntaje TxGNN | Nivel | Observación |
|------|------|------|------|
| Queratitis por exposición | 99.80% | L4 | Solo literatura indirecta (casos de queratitis por *S. aureus* y *B. cereus*); ningún estudio evalúa clindamicina |
| Enfermedad animal no humana | 99.69% | L5 | Categoría no clínica; la literatura trata sobre *C. difficile*, y clindamicina es un factor de riesgo, no una opción terapéutica |
| Queratopatía neurotrófica | 99.49% | L5 | Patología degenerativa no bacteriana; sin evidencia |
| Queratoconjuntivitis epidémica | 99.49% | L5 | Causa adenoviral; la literatura es veterinaria (bovina) y no aplicable |
| Vaginitis atrófica posmenopáusica | 99.03% | L5 | Causa por déficit estrogénico; el mecanismo no se transfiere |

## Información de Mercado en España

Se muestran 5 de las 16 autorizaciones vigentes (los textos de indicación aprobada no están disponibles en los datos compilados).

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62911 | Dalacin 100 mg óvulos | Óvulo | No disponible |
| 81565 | Clindamicina Qualigen 300 mg cápsulas duras EFG | Cápsula dura | No disponible |
| 60034 | Dalacin 20 mg/g crema vaginal | Crema vaginal | No disponible |
| 63669 | Clindamicina Normon 600 mg/4 ml solución inyectable EFG | Solución inyectable | No disponible |
| 66610 | Zindaclin 1% gel | Gel | No disponible |

Las 16 autorizaciones son de medicamentos con clindamicina como único principio activo, y todas están vigentes. Existen presentaciones orales, inyectables, vaginales y cutáneas (gel, solución y emulsión); no hay presentaciones oftálmicas.

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
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

