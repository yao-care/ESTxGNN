---
layout: default
title: Mepyramine
parent: Evidencia moderada (L3-L4)
nav_order: 505
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Mepyramine: nueva indicación predicha, Urticaria alérgica (nivel de evidencia L4). Indicación original: Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común…"
monitor_inn: "mepyramine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis"]
---

# Mepyramine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Mepiramina: De Rinitis Alérgica y Urticaria a Urticaria Alérgica

## Resumen en Una Frase

La mepiramina es un antihistamínico de primera generación, utilizado originalmente para cuadros alérgicos y de vías respiratorias altas como la rinitis alérgica, la urticaria y el angioedema.
El modelo TxGNN predice que podría ser efectiva para **urticaria alérgica**,
pero actualmente **no hay ensayos clínicos** y solo **4 publicaciones** indirectas (preclínicas y una veterinaria) respaldan esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica, rinitis vasomotora, faringitis, resfriado común, urticaria, angioedema, entre otras (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99,92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, la mepiramina es un antagonista clásico del receptor H1 de histamina de primera generación. Su eficacia en cuadros alérgicos mediados por histamina es conocida, y mecanísticamente es aplicable a la urticaria alérgica.

La urticaria alérgica es un proceso mediado por histamina, liberada por la degranulación de los mastocitos y que actúa sobre el receptor H1. Por ello, el ajuste mecanístico es sólido. Sin embargo, la urticaria y el angioedema ya figuran entre las indicaciones originales del fármaco, de modo que esto es esencialmente un uso dentro de indicación (o muy cercano a ella) y no un reposicionamiento genuino. El puntaje tan alto del modelo (0,999) probablemente refleja esa superposición.

Las demás predicciones del modelo siguen un patrón similar: enfermedad de la cavidad nasal (99,74%), laringofaringitis aguda (99,72%) y urticaria por frío (99,70%). Todas se solapan con indicaciones ya existentes y cuentan con evidencia aún más limitada.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21033572](https://pubmed.ncbi.nlm.nih.gov/21033572/) | 2010 | Estudio clínico veterinario (aleatorizado, con placebo) | Polish Journal of Veterinary Sciences | En 27 perros con angioedema, el maleato de mepiramina podría ser útil frente a placebo |
| [34758144](https://pubmed.ncbi.nlm.nih.gov/34758144/) | 2021 | Preclínico/mecanístico | FASEB Journal | La mepiramina bloquea directamente canales de sodio de nociceptores, con efecto analgésico tópico |
| [18222495](https://pubmed.ncbi.nlm.nih.gov/18222495/) | 2008 | Preclínico | Neuropharmacology | La mepiramina inhibe el canal KCNQ/M y despolariza neuronas de rata, lo que explicaría la toxicidad neuronal en sobredosis |
| [29371669](https://pubmed.ncbi.nlm.nih.gov/29371669/) | 2018 | Preclínico | Scientific Reports | Desarrollo de sondas fluorescentes para estudiar la cinética de unión al receptor H1 en células vivas |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 54500 | FLUIDASA 3 mg/ml SOLUCIÓN INYECTABLE | Solución inyectable | No disponible en los datos |
| 54498 | FLUIDASA 5 mg/ml SOLUCIÓN ORAL | Solución oral | No disponible en los datos |
| 54499 | FLUIDASA 20 mg/ml GOTAS ORALES EN SOLUCIÓN | Gotas orales en solución | No disponible en los datos |
| 55465 | FLUIDASA 150 mg CÁPSULAS DURAS | Cápsula dura | No disponible en los datos |

Las cuatro autorizaciones están vigentes, son de monofármaco y pertenecen a Teofarma S.R.L.

## Consideraciones de Seguridad

- **Contraindicaciones asociadas en el grafo de conocimiento** (no proceden del prospecto): hipertensión, insuficiencia hepática, epilepsia, EPOC, enfermedad renal, pancreatitis, hipotiroidismo, úlcera péptica, enfermedad inflamatoria intestinal, diabetes mellitus y cetoacidosis diabética, hiperplasia benigna de próstata, enfermedad coronaria e infarto de miocardio, abuso de sustancias, rabdomiólisis, hemoglobinopatías y colitis por *Clostridium difficile*, entre otras.
- **Interacciones farmacológicas**: se registraron 382 interacciones. Las de nivel **mayor** incluyen **cloruro de potasio** y **citrato de potasio**. Las de nivel **moderado** incluyen anticolinérgicos (atropina, escopolamina, hiosciamina, glicopirronio, diciclomina, propantelina, trospio), opioides (morfina, opio, loperamida), metoclopramida, dronabinol y eluxadolina, principalmente por efectos aditivos anticolinérgicos o depresores del sistema nervioso central.
- La literatura revisada recoge que la sobredosis de mepiramina puede causar somnolencia, convulsiones y coma.

Las advertencias y contraindicaciones del prospecto de la AEMPS no están disponibles; consultar el prospecto para la información de seguridad oficial.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es mecanísticamente razonable, pero se solapa con indicaciones ya existentes y carece de ensayos clínicos en humanos. La evidencia disponible (L4) es indirecta: estudios preclínicos y un estudio veterinario. Además, falta la información de seguridad del prospecto.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de la AEMPS (advertencias, contraindicaciones e indicaciones autorizadas), que es un requisito previo para el cribado de seguridad.
- Confirmar si la urticaria alérgica ya está cubierta por las indicaciones autorizadas, ya que podría no tratarse de una indicación nueva.
- Completar los datos de mecanismo de acción desde DrugBank.
- Buscar ensayos clínicos o estudios observacionales en humanos con mepiramina en urticaria.
- Comparar con antihistamínicos de segunda generación, preferidos por las guías por su menor sedación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

