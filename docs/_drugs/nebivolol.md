---
layout: default
title: Nebivolol
parent: Solo predicción del modelo (L5)
nav_order: 372
evidence_level: L5
indication_count: 5
---

# Nebivolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Nebivolol: De Hipertensión Arterial a Hipertensión Renovascular Maligna

## Resumen en Una Frase

Nebivolol es un bloqueador beta-1 selectivo comercializado en España; según conocimiento farmacológico general se utiliza en hipertensión arterial, ya que los textos de indicación de las autorizaciones suministradas están vacíos.
El modelo TxGNN predice que podría ser efectivo para **hipertensión renovascular maligna**, con un puntaje alto (99,4 %).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta indicación, por lo que es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS suministrados (uso general conocido: hipertensión arterial) |
| Nueva Indicación Predicha | Hipertensión renovascular maligna |
| Puntaje de Predicción TxGNN | 99,42 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

No se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según el conocimiento farmacológico general (no procede de los datos suministrados), nebivolol es un bloqueador beta-1 selectivo con vasodilatación dependiente del endotelio mediada por óxido nítrico. Esto ofrece un vínculo plausible con la reducción de la presión arterial.

La hipertensión renovascular maligna se debe sobre todo a la activación del sistema renina-angiotensina y a la estenosis de la arteria renal. En ese contexto, el bloqueo beta sería, como mucho, un tratamiento complementario. Además, el modelo no aporta ensayos ni literatura que respalden el vínculo, por lo que la predicción debe leerse con cautela.

Se predijeron otras cuatro indicaciones, todas de nivel L5 y con puntajes entre 99,1 % y 99,4 %:
- Enfermedad renal hipertensiva maligna.
- Hipertensión pulmonar de mecanismo multifactorial poco claro.
- Hipertensión pulmonar por enfermedad pulmonar o hipoxia.
- Síndrome de Braddock.

Las dos primeras tienen exactamente el mismo puntaje, lo que sugiere que provienen del mismo entorno del grafo y no son evidencia independiente. En hipertensión pulmonar, la clase de los bloqueadores beta tiene antecedentes que exigen cautela.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

*Nota:* las 20 publicaciones recuperadas para la hipertensión pulmonar por hipoxia (otra indicación predicha) tratan de biología general de la hipoxia. Ninguna menciona nebivolol, por lo que no constituyen evidencia específica del fármaco.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 73926 | Nebivolol Cinfa 5 mg comprimidos EFG | Comprimido | Laboratorios Cinfa S.A. |
| 71271 | Nebivolol Pensa 5 mg comprimidos EFG | Comprimido | Towa Pharmaceutical S.A. |
| 2346204042012IP | Lobivon 5 mg comprimidos | Comprimido | Menarini International Operations Luxembourg S.A. |
| 83604 | Insucor 10 mg comprimidos | Comprimido | Glenmark Arzneimittel GmbH |
| 70928 | Nebivolol Normon 5 mg comprimidos EFG | Comprimido | Laboratorios Normon S.A. |

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no estaban disponibles en los datos suministrados.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo (nivel L5, sin ensayos ni literatura) y el vínculo mecanístico es débil. La hipertensión renovascular maligna se trata con estrategias establecidas, y el bloqueo beta sería como mucho complementario.

**Para avanzar se necesita:**
- Obtener advertencias y contraindicaciones de la ficha técnica de AEMPS, ya que la falta de estos datos impide el cribado de seguridad.
- Obtener el mecanismo de acción desde DrugBank.
- Realizar una búsqueda bibliográfica específica de nebivolol en hipertensión renovascular y maligna.
- Confirmar el papel de nebivolol frente a los tratamientos estándar, incluido el bloqueo del sistema renina-angiotensina.
- Evaluar si las predicciones con puntajes idénticos aportan evidencia independiente.

*Este informe es solo para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

