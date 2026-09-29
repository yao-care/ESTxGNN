---
layout: default
title: Aprepitant
parent: Solo predicción del modelo (L5)
nav_order: 46
evidence_level: L5
indication_count: 10
---

# Aprepitant
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

# Aprepitant: De Antiemético Antagonista NK1 a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Aprepitant es un antagonista del receptor de neuroquinina 1 (NK1) comercializado en España en cápsulas duras y polvo para suspensión oral. Los datos de AEMPS recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción. Se trata de una hipótesis basada únicamente en el modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en los datos de AEMPS proporcionados (los textos de indicación están vacíos) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.97% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 13 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Aprepitant actúa como antagonista del receptor NK1, es decir, bloquea la señalización de la sustancia P. Los datos de DrugBank recibidos no incluyen una descripción detallada del mecanismo de acción, así que este resumen se basa en la clase farmacológica conocida.

El NSIAD es una enfermedad genética causada por variantes de ganancia de función del receptor V2 de la vasopresina (AVPR2). Esto provoca una antidiuresis inapropiada y una hiponatremia que no dependen de la vasopresina. No se conoce ninguna vía establecida que conecte la señalización sustancia P/NK1 con ese defecto, por lo que **el vínculo mecanístico es especulativo**.

El puntaje del modelo es muy alto (99.97%), pero no está respaldado por ningún ensayo clínico, estudio preclínico ni publicación. Debe interpretarse como una señal exploratoria del grafo de conocimiento y no como una recomendación terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 03262002 | EMEND 80 MG CÁPSULAS DURAS | Cápsula dura |
| 84275 | APREPITANT ACCORD 125 MG CÁPSULAS DURAS EFG | Cápsula dura |
| 84706 | ATANTO 125 MG CÁPSULAS DURAS EFG | Cápsula dura |
| 85689 | APREPITANT QILU 80 MG CÁPSULAS DURAS EFG | Cápsula dura |
| 103262011 | EMEND 125 MG POLVO PARA SUSPENSIÓN ORAL | Polvo para suspensión oral |

Se muestran 5 de las 13 autorizaciones registradas. Los datos recibidos no incluyen el texto de indicación aprobada.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada, y las advertencias y contraindicaciones del prospecto de AEMPS aún no se han incorporado.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (nivel L5), sin ensayos clínicos ni literatura específica de aprepitant, y con un vínculo mecanístico que los propios datos califican de especulativo. Además, falta la información de seguridad del prospecto, que es un vacío bloqueante para pasar a la siguiente etapa.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e interacciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Buscar evidencia preclínica o mecanística que relacione la señalización NK1/sustancia P con la función del receptor AVPR2 o con el manejo de la hiponatremia.
- Revisar otras predicciones del mismo fármaco con una hipótesis biológica algo más plausible, como la hemorragia subaracnoidea (neuroinflamación mediada por sustancia P). Ninguna cuenta hoy con evidencia clínica, y la literatura recuperada para la malformación con componente periodontal es solo coincidencia de palabras clave y no evalúa aprepitant.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

