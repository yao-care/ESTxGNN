---
layout: default
title: Riluzole
parent: Solo predicción del modelo (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Riluzole: nueva indicación predicha, Polimicrogiria parieto-occipital parasagital bilateral (nivel de evidencia L5). Indicación original: Esclerosis lateral amiotrófica (según el grafo de conocimiento"
---

# Riluzole
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

# Riluzol: De Esclerosis Lateral Amiotrófica a Polimicrogiria Parieto-Occipital Parasagital Bilateral

## Resumen en Una Frase

Riluzol es un fármaco originalmente utilizado para el tratamiento de la esclerosis lateral amiotrófica (ELA).
El modelo TxGNN predice que podría ser efectivo para **polimicrogiria parieto-occipital parasagital bilateral**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Esclerosis lateral amiotrófica (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Polimicrogiria parieto-occipital parasagital bilateral |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, el riluzol modula la transmisión glutamatérgica (inhibición de la liberación de glutamato y bloqueo de canales de sodio), y su eficacia en la ELA, donde la excitotoxicidad por glutamato es un mecanismo patogénico relevante, está establecida.

Sin embargo, **no se ha establecido un vínculo mecanístico** entre esta acción y la polimicrogiria parieto-occipital parasagital bilateral, una malformación del desarrollo cortical. El elevado puntaje de TxGNN es solo una predicción del modelo, sin ensayos ni literatura de apoyo. Por ello, esta predicción debe considerarse con mucha cautela.

### Otras predicciones del modelo (contexto)

Entre las 10 principales predicciones, algunas tienen una plausibilidad biológica mayor por su cercanía a la indicación original, aunque todas carecen de ensayos clínicos en los datos compilados:

| Posición | Enfermedad predicha | Puntaje TxGNN | Nivel | Comentario |
|---|---|---|---|---|
| 3 | Síndrome de motoneurona inferior de inicio en la edad adulta tardía | 99.99% | L5 | Trastorno de motoneurona; plausible, solo inferencial |
| 6 | Amiotrofia monomélica | 99.99% | L5 | Evolución habitualmente benigna y autolimitada |
| 7 | Síndrome de Mills | 99.98% | L5 | Variante del espectro de enfermedad de motoneurona |
| 8 | ELA, susceptibilidad a | 99.98% | L4 | Reetiquetado de la indicación existente, no un reposicionamiento real |
| 10 | ELA tipo 22 | 99.98% | L5 | Subtipo genético de ELA; plausible por extensión |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación predicha principal.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88570 | EMYLIF 50 mg película bucodispersable | Película bucodispersable | No disponible en los datos |
| 78243 | TEGLUTIK 5 mg/ml suspensión oral | Suspensión oral | No disponible en los datos |
| 75131 | RILUZOL PMCS 50 mg comprimido recubierto con película EFG | Comprimido recubierto con película | No disponible en los datos |
| 96010001 | RILUTEK 50 mg comprimidos recubiertos con película | Comprimido recubierto | No disponible en los datos |
| 75015 | RILUZOL SUN 50 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible en los datos |

Hay una autorización adicional (RILUZOL AUROVITAS 50 mg, n.º 75160) hasta completar las 6 vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones / condiciones de riesgo según el grafo de conocimiento** (no proceden del texto del prospecto): neutropenia, agranulocitosis, abuso/dependencia de sustancias, hiperbilirrubinemia (incluida la hereditaria), síndrome de Gilbert, enfermedad pulmonar intersticial y daño hepático inducido por fármacos.
- **Interacciones farmacológicas**: se identificaron 44 interacciones en total. Entre las principales de nivel moderado figuran: ácido obeticólico, naltrexona, deferasirox, osilodrostat, anagrelida, asparaginasa de *E. coli*, brentuximab vedotina, clofarabina, metotrexato y epirrubicina. Entre las de nivel menor: omeprazol, cafeína, teofilina y aminofilina.
- Otros datos relevantes: en la literatura recuperada se señala que aproximadamente el 50% de los pacientes con ELA tratados con riluzol oral presentan elevación de ALT por encima del límite superior normal (8% por encima de 3×LSN y 2% por encima de 5×LSN), por lo que es necesaria la vigilancia de la función hepática.

Para las advertencias principales y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (polimicrogiria parieto-occipital parasagital bilateral) carece de ensayos clínicos, literatura y vínculo mecanístico plausible; la evidencia es solo de nivel L5 (predicción del modelo). El perfil de seguridad del riluzol, con riesgo hepático y hematológico, exige un fundamento más sólido antes de avanzar.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del riluzol desde DrugBank
- Prospecto de la AEMPS con advertencias y contraindicaciones oficiales (brecha de datos bloqueante para el cribado de seguridad)
- Estudios preclínicos que justifiquen un papel de la modulación glutamatérgica en esta malformación cortical
- Considerar priorizar las predicciones cercanas a la ELA (síndrome de motoneurona inferior, síndrome de Mills, ELA tipo 22), que tienen mayor plausibilidad biológica y podrían abordarse como preguntas de investigación
- Compatibilidad de vías de administración y similitud con la indicación original, actualmente pendientes de evaluar
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

