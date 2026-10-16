---
layout: default
title: Cholecalciferol
parent: Solo predicción del modelo (L5)
nav_order: 177
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Cholecalciferol: nueva indicación predicha, Hipoparatiroidismo aislado familiar por secreción alterada de PTH (nivel de evidencia L5). Indicación original: Osteoporosis (según las indicaciones del gr…"
monitor_inn: "Cholecalciferol"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hypophosphatemic rickets", "renal osteodystrophy", "renal tubular acidosis"]
---

# Cholecalciferol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Colecalciferol: De Osteoporosis a Hipoparatiroidismo Aislado Familiar por Secreción Alterada de PTH

## Resumen en Una Frase

El colecalciferol (vitamina D3) se utiliza desde hace tiempo para tratar la osteoporosis y otros trastornos del metabolismo óseo y mineral, como el raquitismo, la osteomalacia y el déficit de vitamina D.
El modelo TxGNN predice que podría ser efectivo para el **hipoparatiroidismo aislado familiar por secreción alterada de PTH**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden específicamente esta predicción.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Osteoporosis (según las indicaciones del grafo de conocimiento TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Hipoparatiroidismo aislado familiar por secreción alterada de PTH |
| Puntaje de Predicción TxGNN | 99,79 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, el colecalciferol es un precursor (profármaco) de la vitamina D. Su eficacia en trastornos del metabolismo óseo y mineral está comprobada, y mecanísticamente podría ser aplicable a estados de déficit de PTH. Sus metabolitos activos aumentan la absorción intestinal de calcio, algo biológicamente plausible en estados deficientes de PTH.

El hipoparatiroidismo ya figura entre las indicaciones originales del colecalciferol en el grafo de conocimiento. La predicción es, por tanto, en gran parte una reformulación de una indicación de clase existente y no una evidencia nueva de reposicionamiento. Además, la forma familiar aislada por secreción alterada de PTH no cuenta con ensayos ni literatura específicos en los datos compilados.

Hay una limitación importante. El hipoparatiroidismo suele manejarse con análogos activos de la vitamina D (calcitriol, alfacalcidol), porque la conversión del colecalciferol a su forma activa depende de la PTH. Esto reduce el interés práctico del colecalciferol nativo en este contexto.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones vigentes, todas de monofármaco. No hay autorizaciones canceladas ni combinaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 86565 | DELCRIN 50.000 UI/2,5 ML SOLUCIÓN ORAL | Solución oral |
| 89921 | DITRALIA 25.000 UI PELÍCULAS BUCODISPERSABLES | Película bucodispersable |
| 82411 | THORENS 25.000 UI/2,5 ML SOLUCIÓN ORAL | Solución oral |
| 81395 | BENFEROL 400 UI CÁPSULAS BLANDAS | Cápsula blanda |
| 81820 | VIDESIL 25.000 UI SOLUCIÓN ORAL | Solución oral |

Las formas farmacéuticas disponibles en España son solución oral, gotas orales, cápsulas blandas y duras, comprimidos y películas bucodispersables.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): hipercalcemia, nefrocalcinosis, hiperparatiroidismo, trastornos del metabolismo del fósforo, sarcoidosis, enfermedad renal, enfermedad hepática y hepatobiliar, hipertensión, diabetes mellitus, fibrilación auricular, hiperoxaluria primaria, trastornos del metabolismo del hierro (hemocromatosis hereditaria, hemosiderosis), enfermedad de Wilson, hiperlipidemia, anemia falciforme, trastornos de la coagulación, y cáncer de mama femenino y de próstata, entre otros.
- **Interacciones farmacológicas**: solo se identificó una relación de tipo farmacológico, la del metabolito vitamina D3 con el receptor X farnesoide-β (estudio en ratón). No corresponde a una interacción clínica entre fármacos.

Consultar el prospecto para la información de seguridad completa, ya que no se dispone de las advertencias ni de las contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto en TxGNN, pero carece de ensayos clínicos y de literatura específica (L5). Además, se apoya sobre todo en una indicación de clase ya existente, y en la práctica se prefieren los análogos activos de la vitamina D.

**Para avanzar se necesita:**
- Datos del mecanismo de acción del colecalciferol.
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS.
- Evidencia clínica o de casos específica del hipoparatiroidismo aislado familiar, y comparación frente a calcitriol o alfacalcidol.

**Nota sobre otras predicciones del mismo fármaco:** la **osteodistrofia renal** tiene la evidencia más sólida (L2, Proceed with Guardrails). Cuenta con un ensayo de Fase 3 de estado desconocido (NCT00752401), una comparación completada frente a doxercalciferol (NCT00285467) y literatura de apoyo. Requeriría monitorizar calcio, fosfato y PTH, vigilar la hipercalcemia y la calcificación vascular, y reservar los análogos activos o calcimiméticos para los pacientes adecuados.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

