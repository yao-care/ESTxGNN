---
layout: default
title: Paroxetine
parent: Solo predicción del modelo (L5)
nav_order: 409
evidence_level: L5
indication_count: 1
---

# Paroxetine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **1** 
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

# Paroxetina: De Trastorno Depresivo Mayor a Síndrome de Ohdo y variantes

## Resumen en Una Frase

> Paroxetina es un inhibidor selectivo de la recaptación de serotonina (ISRS), utilizado originalmente para el tratamiento del trastorno depresivo mayor y otros trastornos de ansiedad.
> El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Ohdo y variantes**,
> pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección: es solo una predicción computacional.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastorno depresivo mayor (según datos farmacológicos; los textos de autorización de AEMPS no incluyen indicación) |
| Nueva Indicación Predicha | Síndrome de Ohdo y variantes |
| Puntaje de Predicción TxGNN | 99.11% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, paroxetina es un ISRS cuyo objetivo principal es el transportador de serotonina (SERT, gen SLC6A4). También figura como ligando del receptor purinérgico P2X4 (gen P2RX4). Su eficacia en depresión, trastorno obsesivo compulsivo, trastorno de pánico, ansiedad social, ansiedad generalizada, estrés postraumático y trastorno disfórico premenstrual está comprobada.

El Síndrome de Ohdo y sus variantes (incluido el tipo Say-Barber-Biesecker-Young-Simpson) son trastornos congénitos raros. Cursan con discapacidad intelectual, blefarofimosis y, con frecuencia, hipotiroidismo. Suelen atribuirse a variantes del gen KAT6B, una histona acetiltransferasa. Con los datos disponibles **no se puede verificar ninguna vía** que conecte paroxetina con la biología de KAT6B o de la regulación de la cromatina.

Cualquier vínculo, por ejemplo un efecto indirecto serotoninérgico o del neurodesarrollo, sería especulativo. El único respaldo es el puntaje alto del grafo de conocimiento de TxGNN (0.991), que es una predicción computacional y no evidencia clínica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 89018 | Paroxetina Normon 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Sin texto de indicación registrado |
| 69921 | Paroxetina Qualigen 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Sin texto de indicación registrado |
| 89502 | Paroxetina Teva-Ratio 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Sin texto de indicación registrado |
| 68050 | Paroxetina Aristo 20 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Sin texto de indicación registrado |
| 76029 | Paroxetina Stada 10 mg comprimidos EFG | Comprimido | Sin texto de indicación registrado |

---

## Consideraciones de Seguridad

- **Dianas farmacológicas registradas** (no son interacciones fármaco-fármaco): SERT (SLC6A4) y P2X4 (P2RX4), ambas humanas.
- **Precaución de teratogenicidad**: paroxetina tiene advertencias de teratogenicidad en el primer trimestre del embarazo. Es una razón adicional de cautela en un trastorno del desarrollo congénito. Es una consideración de seguridad, no evidencia a favor ni en contra de la eficacia.

Consultar el prospecto para información completa de advertencias y contraindicaciones.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos, literatura ni un vínculo mecanístico verificable con la biología de KAT6B. Además, la precaución de teratogenicidad complica cualquier uso en un contexto de trastorno congénito.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), necesario para el cribado de seguridad.
- Obtener datos del mecanismo de acción desde DrugBank para analizar el vínculo mecanístico.
- Buscar estudios preclínicos o de mecanismo que relacionen paroxetina con KAT6B o la regulación de la cromatina.
- Evaluar la viabilidad de vía de administración y población objetivo, hoy pendientes.
- Revisar la relación beneficio-riesgo, dada la teratogenicidad, antes de cualquier avance.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

