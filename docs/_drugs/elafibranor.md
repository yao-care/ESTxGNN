---
layout: default
title: Elafibranor
parent: Solo predicción del modelo (L5)
nav_order: 195
evidence_level: L5
indication_count: 1
---

# Elafibranor
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

# Elafibranor: De Indicación Original No Registrada a Amenorrea

## Resumen en Una Frase

Elafibranor es un agonista dual de PPAR-alfa/delta, comercializado en España como IQIRVO, aunque el registro disponible no incluye su indicación original.
El modelo TxGNN predice que podría ser efectivo para **amenorrea**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: la predicción se basa únicamente en el modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en el registro (el texto de indicación aprobada de la AEMPS está vacío) |
| Nueva Indicación Predicha | Amenorrea |
| Puntaje de Predicción TxGNN | 99,86 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El único respaldo es el puntaje muy alto de TxGNN (0,9986). La ruta del grafo de conocimiento que lo sustenta no está disponible, por lo que no se puede revisar qué relaciones llevaron a esa predicción.

Elafibranor es un agonista dual de PPAR-alfa/delta. Actualmente no se dispone de datos detallados sobre su mecanismo de acción ni de su indicación original en el registro, así que no se puede comparar con la nueva indicación. La señalización PPAR se relaciona de forma plausible con la regulación metabólica y endocrina del eje hipotálamo-hipófisis-ovario, pero esto es especulativo y ninguna evidencia directa con elafibranor en amenorrea lo respalda.

Además, la amenorrea es un síntoma con muchas causas posibles (hipotalámica, hipofisaria, ovárica, uterina o embarazo). Un vínculo mecanístico con un solo fármaco es poco probable si no se especifica el subtipo.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1241855001 | IQIRVO 80 MG comprimidos recubiertos con película (Ipsen Pharma) | Comprimido recubierto con película | No especificada en el registro |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto, pero es evidencia de nivel L5: no hay ensayos, no hay literatura y el mecanismo no se puede verificar. Tampoco hay datos de seguridad de la AEMPS, lo cual bloquea el cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones), que es el bloqueo actual.
- Completar el mecanismo de acción y la indicación original consultando DrugBank.
- Obtener la ruta del grafo de TxGNN que explica la predicción.
- Definir el subtipo de amenorrea al que se dirigiría la hipótesis.
- Buscar de forma dirigida ensayos y literatura sobre elafibranor/PPAR y función reproductiva.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

