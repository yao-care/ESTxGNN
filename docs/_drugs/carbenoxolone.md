---
layout: default
title: Carbenoxolone
parent: Solo predicción del modelo (L5)
nav_order: 144
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
monitor_inn: "carbenoxolone"
predicted_indications: ["non-syndromic esophageal malformation", "vitamin deficiency disorder", "biotin metabolic disease", "filariasis", "bile duct disease", "bile duct neoplasm", "tinea nigra"]
description: "Carbenoxolone: nueva indicación predicha, Malformación esofágica no sindrómica (non-syndromic esophageal malformation) (nivel de evidencia L5). Indicación original: No consta en los datos locales"
---

# Carbenoxolone
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

## Carbenoxolone: Malformación esofágica no sindrómica (non-syndromic esophageal malformation)
{: .text-alpha }

## Resumen en Una Frase

Carbenoxolona es un fármaco mucoprotector antiulceroso, utilizado originalmente para la enfermedad ulcerosa péptica, la úlcera esofágica y las enfermedades del esófago.
El modelo TxGNN predice que podría ser efectivo para **malformación esofágica no sindrómica**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Malformación esofágica no sindrómica (non-syndromic esophageal malformation) |
| Puntaje de Predicción TxGNN | 1.0000 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado (registros anulados: 1 de 1) |
| Número de Autorizaciones | 1 (vigentes: 0) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción del fármaco en los datos compilados para este informe. Según la información conocida, la carbenoxolona es un derivado del ácido glicirretínico con acción mucoprotectora antiulcerosa, y se le describe también como inhibidor de uniones comunicantes (gap junctions) y de la 11-beta-hidroxiesteroide deshidrogenasa.

El puntaje muy alto proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, como las indicaciones esofágicas ya aprobadas (úlcera esofágica y enfermedad esofágica), no evidencia biológica. Sin embargo, una malformación esofágica no sindrómica es un defecto estructural congénito, y ninguna de las acciones conocidas de la carbenoxolona permite plausiblemente corregirlo.

Por tanto, no es posible construir un fundamento mecanístico sólido. La predicción debe considerarse una hipótesis generada por el modelo, sin respaldo biológico o clínico demostrado.

## Informe de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 44352 | SANODIN 20 mg/g POMADA BUCAL | Pomada bucal | No disponible en los datos compilados |

Titular: Laboratorios Ern S.A. Autorización vigente, de tipo monofármaco.

## Consideraciones de Seguridad

- **Interacciones Farmacológicas**: no se encontraron interacciones registradas en la consulta realizada.
- No hay contraindicaciones derivadas del grafo de conocimiento.

Consultar el prospecto para información de seguridad adicional (advertencias y contraindicaciones). Como aspecto teórico, la carbenoxolona se asocia a efectos de tipo mineralocorticoide (retención de sodio, hipopotasemia, hipertensión) que deberían valorarse en cualquier nuevo uso.

## Otras Predicciones Evaluadas

Todas con nivel de evidencia L5, sin ensayos ni literatura, y recomendación Hold:

| Posición | Indicación Predicha | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Trastorno por deficiencia de vitaminas | 0,9997 | Sin vínculo mecanístico evidente |
| 3 | Enfermedad metabólica de la biotina | 0,9997 | Sin intersección con vías conocidas del fármaco |
| 4 | Filariasis | 0,9994 | Sin actividad antifilárica documentada |
| 5 | Enfermedad de las vías biliares | 0,9954 | Vínculo indirecto por cercanía gastrointestinal; preocupaciones de seguridad |
| 6 | Neoplasia de las vías biliares | 0,9948 | Fundamento preclínico muy especulativo |
| 7 | Tiña negra | 0,9922 | Sin mecanismo antifúngico establecido |

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en un puntaje alto del modelo, sin ensayos clínicos, literatura ni mecanismo plausible, y la formulación disponible en España (pomada bucal) no tiene una relación evidente con una malformación congénita.

**Para avanzar se necesita:**
- Obtener el mecanismo de acción desde DrugBank.
- Descargar y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicación autorizada).
- Realizar una revisión sistemática de la literatura y de registros de ensayos.
- Evaluar la compatibilidad de la vía de administración con la nueva indicación.
- Valorar si alguna de las otras predicciones (por ejemplo, enfermedades de las vías biliares) tiene un fundamento más defendible.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

