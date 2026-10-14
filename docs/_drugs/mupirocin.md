---
layout: default
title: Mupirocin
parent: Solo predicción del modelo (L5)
nav_order: 546
evidence_level: L5
indication_count: 2
---

# Mupirocin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Mupirocina: De Impétigo a Empiema Pleural

## Resumen en Una Frase

Mupirocina es un antibiótico tópico, originalmente utilizado para el tratamiento del impétigo y del impétigo ampolloso.
El modelo TxGNN predice que podría ser efectivo para **empiema pleural**,
pero actualmente **no hay ensayos clínicos ni publicaciones** en los datos compilados que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Impétigo (las autorizaciones de AEMPS no incluyen texto de indicación; se usa la indicación original del grafo de conocimiento) |
| Nueva Indicación Predicha | Empiema pleural |
| Puntaje de Predicción TxGNN | 99,49% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según el conocimiento farmacológico general (no verificado con los datos aportados), mupirocina inhibe la isoleucil-tRNA sintetasa bacteriana y es activa principalmente frente a cocos grampositivos como *Staphylococcus aureus* (incluido SARM) y *Streptococcus pyogenes*.

Estos microorganismos son causas frecuentes tanto de infecciones cutáneas como el impétigo (la indicación original) y del empiema pleural, lo que ofrece una base antibacteriana teórica para la predicción.

Sin embargo, existe una barrera importante: mupirocina solo está formulada para uso tópico (cutáneo y nasal). No tiene formulación sistémica y no hay datos que respalden concentraciones adecuadas en el espacio pleural. Además, el empiema requiere drenaje y antibióticos sistémicos. La incompatibilidad de la vía de administración es el principal obstáculo para su traslación clínica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59531 | BACTROBAN NASAL 20 mg/g POMADA NASAL | Pomada nasal | No disponible en los datos |
| 58987 | PLASIMINE 20 mg/g POMADA | Pomada | No disponible en los datos |
| 58868 | BACTROBAN 20 mg/g pomada | Pomada | No disponible en los datos |
| 75862 | MUPIROCINA ISDIN 20 mg/g POMADA | Pomada | No disponible en los datos |
| 84009 | MUPIROCINA INFECTOPHARM 20 MG/G POMADA | Pomada | No disponible en los datos |

Se muestran 5 de las 8 autorizaciones vigentes (todas de principio activo único).

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento, no del prospecto)**: dermatitis.
- **Interacciones Farmacológicas**: se identificaron 118 interacciones potenciales, todas con nivel de gravedad no clasificado ("Desconocido"). Entre ellas figuran calcitriol, clotrimazol, morfina, metformina, pantoprazol, omeprazol, vancomicina, triamcinolona, prednisona y simvastatina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L5), sin ensayos clínicos ni literatura de respaldo. Además, mupirocina solo existe en formulaciones tópicas, incompatibles con el tratamiento del empiema pleural, que exige drenaje y antibioterapia sistémica.

**Para avanzar se necesita:**
- Datos del mecanismo de acción verificados (p. ej., desde DrugBank)
- Prospecto de AEMPS con advertencias y contraindicaciones oficiales
- Evaluación de compatibilidad de vía de administración y de la penetración en el espacio pleural
- Estudios preclínicos o clínicos que respalden la actividad en empiema pleural
- Clasificación de la gravedad de las interacciones farmacológicas

---

*Nota: también se predijo la queratoconjuntivitis epitelial punteada (puntaje TxGNN 99,10%, L5, Hold). Mupirocina solo podría ser relevante en el subconjunto de origen estafilocócico, carece de actividad antiviral, no está aprobada para uso oftálmico y no hay ensayos ni literatura que la respalden.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

