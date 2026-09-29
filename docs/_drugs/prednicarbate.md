---
layout: default
title: Prednicarbate
parent: Solo predicción del modelo (L5)
nav_order: 435
evidence_level: L5
indication_count: 7
---

# Prednicarbate
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Prednicarbato: De Corticoide Tópico a Queratosis Folicular Invertida Vulvar

## Resumen en Una Frase

Prednicarbato es un glucocorticoide de uso tópico, comercializado en España en pomada, crema y solución cutánea. El paquete de evidencia no incluye el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **queratosis folicular invertida vulvar**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una predicción puramente computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones (clase: corticoide tópico) |
| Nueva Indicación Predicha | Queratosis folicular invertida vulvar |
| Puntaje de Predicción TxGNN | 99,88 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Por conocimiento de clase (no proviene del paquete de evidencia), el prednicarbato es un glucocorticoide tópico de potencia media, con acción antiinflamatoria e inmunosupresora local. Su uso está establecido en dermatosis inflamatorias.

La queratosis folicular invertida es una lesión folicular benigna que normalmente se trata con escisión, no con fármacos. Por eso no hay un vínculo mecanístico claro con un antiinflamatorio tópico. El puntaje alto del modelo (99,88 %) no equivale a respaldo clínico. Es probable que refleje la similitud del fármaco con otros corticoides en el grafo de conocimiento, más que una razón biológica específica.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se listan 5 de las 8 autorizaciones. El paquete de evidencia no incluye el texto de la indicación aprobada para ninguna de ellas.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 60371 | PEITEL 2,5 MG/G UNGUENTO | Pomada |
| 60370 | PEITEL 2,5 MG/G POMADA | Pomada |
| 60372 | PEITEL 2,5 MG/G CREMA | Crema |
| 60458 | BATMEN 2,5 MG/G CREMA | Crema |
| 60459 | BATMEN SOLUCION | Solución cutánea |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es solo del modelo (L5), sin ensayos ni literatura. Además, la lesión es benigna y de manejo quirúrgico, y no hay un mecanismo plausible que justifique un tratamiento tópico con corticoide.

**Otras predicciones del modelo:**
Las variantes de liquen plano, con el mismo puntaje TxGNN de 99,64 %, tienen un fundamento mecanístico más coherente. Son dermatosis inflamatorias mediadas por linfocitos T y responden a corticoides tópicos. Se clasifican como "Research Question".
- **Liquen plano anular atrófico:** hay un único artículo (PMID 35001397, 2022), probablemente un caso o imagen clínica. No se ha verificado que involucre al prednicarbato, por lo que la evidencia es L4 e indirecta.
- **Liquen plano hipertrófico y penfigoide liquenoide:** una potencia media podría ser insuficiente.
- **Sensibilización a metacrilato de 2-hidroxietilo y linfoma cutáneo primario de células B:** ambos en Hold. Un corticoide, como mucho, aliviaría síntomas y no trataría la enfermedad.

**Para avanzar se necesita:**
- Prospecto de la AEMPS para completar la revisión de seguridad (advertencias y contraindicaciones), actualmente un bloqueo
- Mecanismo de acción desde DrugBank
- Texto de la indicación aprobada en las autorizaciones españolas
- Revisión bibliográfica dirigida sobre prednicarbato en liquen plano
- Comprobación de compatibilidad de vía y formulación con la localización de la lesión
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

