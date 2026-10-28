---
layout: default
title: Povidone
parent: Solo predicción del modelo (L5)
nav_order: 652
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Povidone: nueva indicación predicha, Eritrodermia ictiosiforme congénita (nivel de evidencia L5). Indicación original: Síndrome del ojo seco / xeroftalmia"
monitor_inn: "povidone"
predicted_indications: ["congenital ichthyosiform erythroderma"]
---

# Povidone
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

## Povidona: De Síndrome del Ojo Seco a Eritrodermia Ictiosiforme Congénita
{: .text-alpha }

## Resumen en Una Frase

La povidona es un polímero hidrófilo utilizado como lubricante en colirios (lágrimas artificiales), originalmente indicado para el síndrome del ojo seco y la xeroftalmia.
El modelo TxGNN predice que podría ser efectiva para la **eritrodermia ictiosiforme congénita**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Síndrome del ojo seco / xeroftalmia |
| Nueva Indicación Predicha | Eritrodermia ictiosiforme congénita |
| Puntaje de Predicción TxGNN | 0.9911 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Autorizado pero no comercializado (registros: 5) |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de la povidona en los datos compilados para este informe. Según la información conocida, la povidona es un polímero hidrófilo empleado como lubricante y humectante en lágrimas artificiales y, en su forma de povidona yodada, como antiséptico tópico. Su eficacia en el ojo seco se asocia a su capacidad de retener agua y formar una película protectora sobre la superficie ocular.

Una hipótesis puramente especulativa es que esas mismas propiedades (formación de película y fijación de agua) podrían contribuir a hidratar la piel en una enfermedad caracterizada por descamación y alteración de la barrera cutánea. Esta hipótesis no ha sido probada.

La eritrodermia ictiosiforme congénita es un trastorno genético de la queratinización (por ejemplo, variantes en TGM1, ALOX12B, ALOXE3). Nada en los datos disponibles conecta la povidona con esas vías. El puntaje elevado de TxGNN (0.9911) es una predicción del modelo y no constituye evidencia clínica ni mecanística.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 61983 | OCULOTECT 50 mg/ml colirio en solución en envase unidosis (Alcon Healthcare S.A.) | Colirio en solución | No especificada en los datos |
| 61982 | OCULOTECT 50 mg/ml colirio en solución (Alcon Healthcare S.A.) | Colirio en solución | No especificada en los datos |
| 2943389 | OCULOTECT 50 mg/ml colirio en solución en envase unidosis (Alcon Portugal) | Colirio en solución en envase unidosis | No especificada en los datos |
| 1-21275 | OCULOTECT 50 mg/ml colirio en solución (Laboratoires Thea) | Colirio en solución | No especificada en los datos |
| 2630085 | OCULOTECT 50 mg/ml colirio en solución (Alcon Portugal) | Colirio en solución | No especificada en los datos |

La indicación original (síndrome del ojo seco / xeroftalmia) no proviene del texto de las autorizaciones; procede del modelo TxGNN (deep learning) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** epilepsia, enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia respiratoria, disociación auriculoventricular, bloqueo auriculoventricular y bloqueo cardíaco. Estas asociaciones deben interpretarse con cautela, ya que no están verificadas con el texto oficial de la ficha técnica.
- **Interacciones farmacológicas:** no se encontraron interacciones registradas en la consulta realizada.

Consultar el prospecto para la información de advertencias y contraindicaciones oficiales.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin un vínculo mecanístico documentado entre la povidona y la eritrodermia ictiosiforme congénita. Además, la formulación disponible en España es un colirio oftálmico, que no es compatible de forma evidente con una enfermedad cutánea.

**Para avanzar se necesita:**
- Datos del mecanismo de acción de la povidona (por ejemplo, consulta a DrugBank)
- Descarga y análisis del prospecto de AEMPS para advertencias y contraindicaciones oficiales
- Estudios preclínicos o revisión de la literatura que sustenten un posible efecto en trastornos de la queratinización
- Evaluación de la compatibilidad de vía de administración y formulación (el producto actual es oftálmico)
- Confirmación de las contraindicaciones señaladas por el grafo de conocimiento frente a fuentes oficiales
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

