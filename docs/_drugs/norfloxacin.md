---
layout: default
title: Norfloxacin
parent: Solo predicción del modelo (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Norfloxacin: nueva indicación predicha, Síndrome de hiperviscosidad policlonal (nivel de evidencia L5). Indicación original: Infecciones del tracto urinario (según las indicaciones originales de…"
---

# Norfloxacin
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

# Norfloxacino: De Infecciones Bacterianas (Urinarias y Gastrointestinales) a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Norfloxacino es una fluoroquinolona antibacteriana, utilizada originalmente para tratar infecciones como las del tracto urinario, la disentería, la fiebre tifoidea y la bronquitis.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de hiperviscosidad policlonal**, pero **no existen ensayos clínicos ni publicaciones** que respalden esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones del tracto urinario (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.70% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, norfloxacino es una fluoroquinolona que inhibe la ADN girasa y la topoisomerasa IV bacterianas, y su eficacia en infecciones bacterianas está bien establecida.

Sin embargo, **no se identifica un vínculo mecanístico plausible** con el síndrome de hiperviscosidad policlonal. El norfloxacino no tiene efecto conocido sobre los niveles de proteínas séricas ni sobre la viscosidad sanguínea. El puntaje alto de TxGNN (99.70%) refleja una predicción basada en el grafo de conocimiento, sin respaldo clínico ni bibliográfico, y debe interpretarse como una hipótesis no sustentada.

Cabe señalar que otras predicciones del modelo con el mismo perfil (hiperamilasemia, analbuminemia congénita, incompatibilidad de grupo sanguíneo, esclerodermia difusa) tampoco cuentan con vínculo mecanístico ni evidencia. Las únicas con plausibilidad indirecta son la queratoconjuntivitis epitelial punteada y la peste septicémica (ambas nivel L4, "pregunta de investigación"), aunque con evidencia limitada y sin datos específicos de norfloxacino en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 56901 | Norfloxacino Qualigen 400 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 62622 | Norfloxacino Sandoz 400 mg comprimidos EFG | Comprimido recubierto | No disponible |
| 68627 | Norfloxacino Cinfa 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |
| 63159 | Norfloxacino Normon 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto | No disponible |
| 63202 | Norfloxacino Stada 400 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | No disponible |

Nota: se muestran 5 de las 9 autorizaciones vigentes (todas de principio activo único). Entre las no listadas figura Chibroxin 3 mg/ml colirio en solución (Laboratorios Thea), de uso oftálmico.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, insuficiencia hepática, enfermedad hepática y cirrosis, enfermedad renal, epilepsia, trastornos psiquiátricos (ansiedad, psicosis, esquizoafectivo, trastorno distímico, entre otros), trombocitopenia, anemia, diabetes mellitus y cetoacidosis diabética, déficit de potasio, neuropatía periférica, tendinitis y otras afecciones tendinosas, y rabdomiólisis.
- **Interacciones farmacológicas**: se identificaron 100 interacciones en total; entre las principales de nivel **mayor** figuran hidrocortisona, dexametasona, betametasona, triamcinolona (corticosteroides, con mayor riesgo de lesión tendinosa), bupropión y clorpropamida. Entre las de nivel moderado destacan antidiabéticos (metformina, pioglitazona, acarbosa, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico y sales de calcio.
- Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para el síndrome de hiperviscosidad policlonal se basa únicamente en el modelo (nivel L5), sin ensayos, sin literatura y sin vínculo mecanístico plausible. Además, el perfil de seguridad es relevante (QT, tendones, SNC, hepático y renal).

**Para avanzar se necesita:**
- Un fundamento mecanístico creíble que relacione norfloxacino con la hiperviscosidad sérica (actualmente inexistente).
- Datos del mecanismo de acción y de advertencias/contraindicaciones del prospecto de la AEMPS.
- Si se desea explorar alternativas, priorizar como preguntas de investigación la queratoconjuntivitis epitelial punteada (vía oftálmica, con Chibroxin como formulación existente) y la peste septicémica, teniendo en cuenta que para esta última serían preferibles fluoroquinolonas de mayor exposición sistémica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

