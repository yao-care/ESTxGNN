---
layout: default
title: Granisetron
parent: Solo predicción del modelo (L5)
nav_order: 385
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Granisetron: nueva indicación predicha, Trastorno afectivo bipolar maníaco (manic bipolar affective disorder) (nivel de evidencia L5). Indicación original: No disponible en los datos de licencias de …"
monitor_inn: "granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Granisetrón: De Indicación Original No Registrada a Trastorno Bipolar Maníaco
{: .text-alpha }

## Resumen en Una Frase

Granisetrón es un antagonista selectivo de los receptores 5-HT3, comercializado en España en múltiples presentaciones (inyectable, comprimidos, perfusión y parche transdérmico). El texto de indicación aprobada no está disponible en los datos compilados para este informe.
El modelo TxGNN predice que podría ser efectivo para **trastorno afectivo bipolar maníaco**, pero **no existe ningún ensayo clínico ni publicación** que respalde esta dirección; se trata únicamente de una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de licencias de la AEMPS |
| Nueva Indicación Predicha | Trastorno afectivo bipolar maníaco (manic bipolar affective disorder) |
| Puntaje de Predicción TxGNN | 99,62% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 11 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Granisetrón es un antagonista selectivo del receptor 5-HT3 de serotonina. Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados; sin embargo, la clase de los antagonistas 5-HT3 es conocida por su uso en la prevención de náuseas y vómitos, y los productos en España (inyectables, comprimidos, parche) son coherentes con ese perfil.

La relación con el trastorno bipolar maníaco es **especulativa**. Se ha planteado que la modulación de 5-HT3 podría influir en la señalización dopaminérgica y serotoninérgica relacionada con la regulación del ánimo, pero no hay ensayos ni literatura que lo confirmen. La puntuación alta de TxGNN (99,62%) refleja únicamente una predicción basada en el grafo de conocimiento.

Cabe señalar que no se pudo establecer una similitud formal entre la indicación original y la nueva indicación, al no disponerse del texto de indicación aprobada.

### Otras indicaciones predichas (referencia)

| Rango | Indicación predicha | Puntaje TxGNN | Plausibilidad mecanística |
|---|------|------|------|
| 2 | Síndrome de Tourette | 99,52% | Hipotética (se han explorado otros 5-HT3 como ondansetrón en estudios pequeños) |
| 3 | Conjuntivitis contagiosa aguda | 99,49% | Sin vínculo plausible; probable artefacto del grafo |
| 4 | Angioedema | 99,36% | Débil (vías de histamina/bradicinina) |
| 5 | Urticaria alérgica | 99,32% | Especulativa (serotonina y mastocitos) |
| 6 | Síndrome nefrogénico de antidiuresis inapropiada | 99,32% | Sin vínculo aparente (mutaciones del receptor V2) |
| 7 | Tricotilomanía | 99,23% | Hipotética (espectro obsesivo-compulsivo) |
| 8 | Bronquitis | 99,18% | Sin fundamento mecanístico claro |
| 9 | Urticaria por frío | 99,10% | Especulativa |
| 10 | Conjuntivitis | 99,09% | Sin vínculo establecido |

Todas ellas tienen nivel de evidencia L5 y recomendación Hold.

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
| 59867 | KYTRIL 3MG/3ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 68225 | GRANISETRON ALTAN 1 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 71577 | GRANISETRON AUROVITAS SPAIN 1 mg COMPRIMIDOS RECUBIERTOS CON PELÍCULA EFG | Comprimido recubierto con película | No disponible |
| 61803 | KYTRIL 1MG/1ML SOLUCIÓN INYECTABLE | Solución inyectable | No disponible |
| 60204 | KYTRIL 1 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible |

Se muestran 5 de las 11 autorizaciones vigentes (todas de monofármaco). El resto incluye presentaciones en solución para perfusión, concentrado para solución inyectable y el parche transdérmico SANCUSO 3,1 mg/24 h.

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proviene del texto del prospecto)**: síndrome de QT largo, síndrome de QT largo familiar, deficiencia de potasio, paro cardíaco súbito y enfermedad de la conducción cardíaca. En conjunto, indican un riesgo de prolongación del QT y de arritmias.
- **Interacciones Farmacológicas**: se identificaron 461 interacciones en total. Entre las principales de nivel **Mayor**: fentanilo, dextrometorfano, tramadol, alfentanilo, almotriptán, sumatriptán, amiodarona, amisulprida, amitriptilina y anagrelida. Varias se relacionan con prolongación del QT o con riesgo de síndrome serotoninérgico. Entre las de nivel **Moderado**: abametapir, abiraterona, dihidrocodeína, codeína, famotidina, formoterol, adenosina, salbutamol, alfuzosina y propofol.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para trastorno bipolar maníaco se basa solo en el modelo (nivel L5), sin ensayos clínicos ni literatura, y con un vínculo mecanístico especulativo. Además, el perfil de riesgo cardíaco (QT) y las numerosas interacciones mayores exigirían cautela en una población que a menudo usa antipsicóticos y antidepresivos.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente sin datos.
- Completar los datos del mecanismo de acción.
- Realizar una revisión sistemática de literatura preclínica y clínica sobre antagonistas 5-HT3 en trastorno bipolar y manía.
- Evaluar la compatibilidad de vías de administración y la similitud con la indicación original.
- Evaluar el riesgo de prolongación del QT y de interacciones con estabilizadores del ánimo y antipsicóticos antes de plantear cualquier estudio.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

