---
layout: default
title: Chlortetracycline
parent: Solo predicción del modelo (L5)
nav_order: 175
evidence_level: L5
indication_count: 8
---

# Chlortetracycline
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
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

# Clortetraciclina: De Tracoma a Vasculitis Postinfecciosa

## Resumen en Una Frase

La clortetraciclina es un antibiótico del grupo de las tetraciclinas, utilizado originalmente en el tratamiento del tracoma, la ornitosis y la oftalmía neonatal.
El modelo TxGNN predice que podría ser efectivo para **vasculitis postinfecciosa**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección: se trata de una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Tracoma, ornitosis y oftalmía neonatal (según el grafo de conocimiento de TxGNN; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Vasculitis postinfecciosa |
| Puntaje de Predicción TxGNN | 99,82% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, la clortetraciclina pertenece a la clase de las tetraciclinas, su actividad antibacteriana en infecciones oculares como el tracoma está establecida, y mecanísticamente podría ser aplicable a cuadros inflamatorios o infecciosos relacionados.

Las tetraciclinas tienen un posible efecto antiinflamatorio y de inhibición de metaloproteinasas de matriz, que teóricamente podría modular una vasculitis de origen inmunomediado. Además, el fármaco podría actuar sobre una infección bacteriana desencadenante.

Sin embargo, no existen ensayos ni literatura que apoyen este vínculo, y el mecanismo de acción original no está disponible. Una puntuación alta del modelo sin datos de apoyo no es suficiente para avanzar.

### Otras predicciones del modelo (todas de nivel L5, salvo la última)

| Enfermedad predicha | Puntaje TxGNN | Nivel | Comentario |
|------|------|------|------|
| Trastorno post-bacteriano | 99,82% | L5 | Categoría amplia e inespecífica; las secuelas suelen ser inmunomediadas |
| Síndrome postinfeccioso | 99,81% | L5 | Término genérico con patología heterogénea |
| Estenosis uretral infecciosa | 99,81% | L5 | Condición fibrótica y estructural; los antibióticos no revertirían una estenosis establecida |
| Otitis externa | 99,79% | L5 | Mecanismo antibacteriano plausible, pero ya existen terapias tópicas establecidas |
| Miocardiopatía de Chagas | 99,78% | L5 | Beneficio antiinflamatorio o antiparasitario especulativo |
| Síndrome hemolítico urémico asociado a infección | 99,78% | L5 | **Alerta de seguridad**: en el SHU por toxina Shiga el uso de antibióticos puede aumentar la liberación de toxina |
| Infestación parasitaria del párpado | 99,04% | L4 | Evidencia solo indirecta (ver más abajo) |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Para la indicación principal (vasculitis postinfecciosa), actualmente no hay literatura relacionada disponible.

Para la predicción de menor rango (infestación parasitaria del párpado) existe una única publicación, que no evalúa clortetraciclina:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21955627](https://pubmed.ncbi.nlm.nih.gov/21955627/) | 2012 | Estudio clínico | Cornea | Evalúa el ungüento de aceite de árbol de té al 5% para el picor ocular asociado a demodicosis ocular; no aporta datos del fármaco, solo apoya el contexto de la enfermedad |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 17503 | DERMOSA AUREOMICINA 10 MG/G POMADA | Pomada | No disponible |
| 17890 | DERMOSA AUREOMICINA 30 MG/G POMADA | Pomada | No disponible |
| 13909 | OFTALMOLOSA CUSI AUREOMICINA 5 mg/g POMADA OFTÁLMICA | Pomada oftálmica | No disponible |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Como señal de precaución derivada del análisis de las predicciones: en el síndrome hemolítico urémico asociado a infección por toxina Shiga, el uso de antibióticos suele ser motivo de preocupación, por lo que esa indicación requeriría una evaluación de seguridad específica. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos clínicos ni literatura que la respalden, y sin datos del mecanismo de acción ni de seguridad del prospecto. Una puntuación alta sin datos de apoyo no basta para avanzar.

**Para avanzar se necesita:**
- Obtener las advertencias y contraindicaciones del prospecto de la AEMPS (bloqueante para el cribado de seguridad)
- Completar los datos del mecanismo de acción
- Realizar una búsqueda de literatura y ensayos específicos para vasculitis postinfecciosa
- Evaluar la compatibilidad de vía de administración: las presentaciones comercializadas son tópicas (pomada y pomada oftálmica), lo que puede limitar su utilidad en enfermedades sistémicas
- Aclarar la similitud entre la indicación original y la nueva
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

