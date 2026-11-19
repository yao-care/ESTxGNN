---
layout: default
title: Relebactam
parent: Solo predicción del modelo (L5)
nav_order: 690
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-05
monitor_inn: "relebactam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
description: "Relebactam: nueva indicación predicha, Hiperamilasemia (hyperamylasemia) (nivel de evidencia L5). En España, autorizaciones de la AEMPS: 1 (comercializadas: 1)"
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

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Relebactam: Hiperamilasemia (hyperamylasemia)
{: .text-alpha }

## Resumen en Una Frase

Relebactam es un inhibidor de beta-lactamasas que se administra junto con imipenem/cilastatina, y originalmente se utiliza para tratar infecciones del tracto urinario y pielonefritis.
El modelo TxGNN predice que podría ser efectivo para **hiperamilasemia**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos locales |
| Nueva Indicación Predicha | Hiperamilasemia (hyperamylasemia) |
| Puntaje de Predicción TxGNN | 0.9922 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 1 de 1) |
| Número de Autorizaciones | 1 (comercializadas: 1) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Según ChEMBL (EMBL-EBI), el mecanismo de acción registrado para Relebactam es (traducción no oficial): «Inhibidor de la betalactamasa SHV-1; inhibidor de la betalactamasa bacteriana TEM; inhibidor de betalactamasas; inhibidor de la betalactamasa hidrolizante de carbapenémicos KPC» Texto original en inglés: "Beta-lactamase SHV-1 inhibitor; Bacterial beta-lactamase TEM inhibitor; Beta-lactamase inhibitor; Carbapenem-hydrolyzing beta-lactamase KPC inhibitor" ([ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605), CC BY-SA 3.0; consultado el 2026-11-19). Según la información conocida, relebactam es un inhibidor de beta-lactamasas de serina de clase A y C que se combina con imipenem/cilastatina para proteger al antibiótico de la degradación enzimática. Su utilidad en infecciones urinarias complicadas y pielonefritis procede de ese efecto adyuvante antibacteriano.

Sin embargo, **no se identifica un vínculo mecanístico creíble** con la hiperamilasemia. Relebactam no tiene acción conocida sobre el metabolismo ni el aclaramiento de la amilasa pancreática o salival. Además, la hiperamilasemia suele ser un hallazgo de laboratorio (pancreatitis, insuficiencia renal, enfermedad de glándulas salivales) más que una enfermedad tratable en sí misma, por lo que el fundamento de reposicionamiento es débil.

El puntaje elevado de TxGNN (0.9922) refleja una predicción del modelo TxGNN (aprendizaje profundo) y no está respaldado por estudios reales. Otras predicciones del modelo con puntajes similares, como el síndrome de hiperviscosidad policlonal (0.9922) y la analbuminemia congénita (0.9908), tampoco muestran un vínculo mecanístico plausible y también quedan en nivel L5.

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

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [ChEMBL CHEMBL3301605 (relebactam): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL3301605) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

