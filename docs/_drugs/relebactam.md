---
layout: default
title: Relebactam
parent: Solo predicción del modelo (L5)
nav_order: 690
evidence_level: L5
indication_count: 3
---

# Relebactam
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Relebactam: De Infección del Tracto Urinario a Hiperamilasemia

## Resumen en Una Frase

Relebactam es un inhibidor de beta-lactamasas que se administra junto con imipenem/cilastatina, y originalmente se utiliza para tratar infecciones del tracto urinario y pielonefritis.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección del tracto urinario y pielonefritis (según el grafo de conocimiento; el texto de indicación autorizado en España no está disponible) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.22% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, relebactam es un inhibidor de beta-lactamasas de serina de clase A y C que se combina con imipenem/cilastatina para proteger al antibiótico de la degradación enzimática. Su utilidad en infecciones urinarias complicadas y pielonefritis procede de ese efecto adyuvante antibacteriano.

Sin embargo, **no se identifica un vínculo mecanístico creíble** con la hiperamilasemia. Relebactam no tiene acción conocida sobre el metabolismo ni el aclaramiento de la amilasa pancreática o salival. Además, la hiperamilasemia suele ser un hallazgo de laboratorio (pancreatitis, insuficiencia renal, enfermedad de glándulas salivales) más que una enfermedad tratable en sí misma, por lo que el fundamento de reposicionamiento es débil.

El puntaje elevado de TxGNN (99.22%) refleja una predicción basada en el grafo de conocimiento y no está respaldado por estudios reales. Otras predicciones del modelo con puntajes similares, como el síndrome de hiperviscosidad policlonal (99.22%) y la analbuminemia congénita (99.08%), tampoco muestran un vínculo mecanístico plausible y también quedan en nivel L5.

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
| 1191420001 | RECARBRIO 500 mg/500 mg/250 mg polvo para solución para perfusión | Polvo para solución para perfusión | No disponible en los datos compilados |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en los datos compilados.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible. Además, la hiperamilasemia es principalmente un hallazgo de laboratorio, lo que debilita el fundamento terapéutico.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) del fármaco
- Revisión del prospecto de la AEMPS (advertencias y contraindicaciones), imprescindible antes de cualquier cribado de seguridad
- Evidencia preclínica o clínica que sustente un vínculo biológico con la hiperamilasemia
- Evaluación de la compatibilidad de vía de administración (el fármaco solo está disponible como perfusión intravenosa) y de la similitud con la indicación original
- Considerar priorizar otras indicaciones con mejor sustento biológico, ya que las tres predicciones principales carecen de evidencia
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

