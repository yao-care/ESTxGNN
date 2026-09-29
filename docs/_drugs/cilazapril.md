---
layout: default
title: Cilazapril
parent: Solo predicción del modelo (L5)
nav_order: 127
evidence_level: L5
indication_count: 4
---

# Cilazapril
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Cilazapril: De Inhibidor de la ECA Antihipertensivo a Hipertensión Pulmonar de Mecanismo Multifactorial No Aclarado

## Resumen en Una Frase

Cilazapril es un inhibidor de la enzima convertidora de angiotensina (IECA), comercializado en España como antihipertensivo bajo la marca INOCAR.
El modelo TxGNN predice que podría ser efectivo para **hipertensión pulmonar de mecanismo multifactorial no aclarado**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: es solo una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Hipertensión pulmonar de mecanismo multifactorial no aclarado |
| Puntaje de Predicción TxGNN | 99,20 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado. Según la información conocida, cilazapril es un IECA: bloquea la conversión de angiotensina I en angiotensina II, un potente vasoconstrictor. En teoría, reducir la angiotensina II podría disminuir la vasoconstricción y el remodelado vascular pulmonar.

Esa relación con la indicación original es, sin embargo, débil. La hipertensión pulmonar de mecanismo multifactorial no aclarado es una categoría heterogénea, y los IECA no son una terapia establecida para ella. El puntaje alto de TxGNN (99,20 %) refleja una inferencia computacional, probablemente por el efecto de clase antihipertensiva, y no una prueba de eficacia.

Otras predicciones del modelo para este fármaco tampoco tienen respaldo clínico:
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia (99,20 %):** se recuperaron 20 publicaciones, pero tratan la biología de la hipoxia en general. Ninguna estudia cilazapril ni otro IECA, y ninguna aborda el tratamiento de la hipertensión pulmonar. Además, los vasodilatadores sistémicos pueden empeorar la relación ventilación-perfusión.
- **Enfermedad renal hipertensiva maligna (99,12 %):** el mecanismo es plausible, pero es una urgencia hipertensiva que suele manejarse con fármacos parenterales titulables.
- **Hipertensión renovascular maligna (99,12 %):** el mecanismo es plausible, pero los IECA pueden reducir bruscamente la filtración glomerular en estenosis bilateral de arteria renal o de riñón único, lo que es una preocupación de seguridad importante.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la indicación principal.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 59330 | INOCAR 1 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |
| 59329 | INOCAR 2,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |
| 59328 | INOCAR 5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No especificada en el registro |

Titular: Mylan Ire Healthcare Limited.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura pertinente. El mecanismo es especulativo para una categoría heterogénea, y los IECA no son terapia establecida en hipertensión pulmonar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un dato bloqueante para cualquier evaluación de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la literatura específica sobre IECA en hipertensión pulmonar y buscar estudios preclínicos o clínicos con cilazapril.
- Si se considera otra indicación predicha, evaluar antes la seguridad renal y el potasio, en especial en estenosis de arteria renal.

*Este resultado es solo para fines de investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

