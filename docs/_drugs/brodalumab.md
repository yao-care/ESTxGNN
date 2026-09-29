---
layout: default
title: Brodalumab
parent: Solo predicción del modelo (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
---

# Brodalumab
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

# Brodalumab: De Psoriasis en Placas a Estrongiloidiasis

## Resumen en Una Frase

Brodalumab es un anticuerpo monoclonal que bloquea el receptor IL-17RA y se comercializa en España como KYNTHEUM. Su indicación original no figura en el texto de la autorización registrada; según la información general del fármaco, es la psoriasis en placas.
El modelo TxGNN predice que podría ser efectivo para **estrongiloidiasis**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es solo una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Psoriasis en placas (dato no incluido en el texto de la autorización; procede de información general del fármaco) |
| Nueva Indicación Predicha | Estrongiloidiasis |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, brodalumab bloquea el receptor IL-17RA, y la vía de IL-17 participa en la defensa de las mucosas frente a bacterias y hongos. Su eficacia se ha establecido en enfermedades inflamatorias mediadas por el sistema inmune, no en infecciones parasitarias.

Aquí la razonabilidad biológica es **débil**. La estrongiloidiasis es una infección por un helminto, y el bloqueo de IL-17RA no tiene un vínculo mecanístico claro con su tratamiento. Además, los biológicos inmunosupresores son un factor de riesgo reconocido de hiperinfección por *Strongyloides*, así que el efecto podría ir en sentido desfavorable.

El puntaje alto (99.84%) refleja probablemente la cercanía entre nodos en el grafo de conocimiento y no una señal biológica independiente. No hay estudios que la confirmen.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1161155001 | KYNTHEUM 210 MG SOLUCION INYECTABLE EN JERINGA PRECARGADA (Leo Pharma A/S) | Solución inyectable | No especificada en los datos disponibles |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni publicaciones. Además, el mecanismo de acción sugiere que el bloqueo de IL-17RA no aporta beneficio en una infección helmíntica y podría aumentar el riesgo de hiperinfección.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de la AEMPS (advertencias y contraindicaciones).
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una revisión específica del riesgo de hiperinfección por *Strongyloides* con biológicos inmunosupresores.
- Obtener evidencia preclínica o clínica antes de reconsiderar la indicación.

**Nota sobre otras predicciones:** el resto de las 10 principales predicciones (por ejemplo, enfermedad ocular y las neuritis ópticas) también quedan en *Hold*. Solo "enfermedad ocular" alcanza L4, apoyada en una revisión indirecta sobre IL-17 en enfermedades reumáticas sistémicas. Las neuritis ópticas comparten el mismo puntaje, así que probablemente representan una sola señal correlacionada.

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

