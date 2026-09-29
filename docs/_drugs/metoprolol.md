---
layout: default
title: Metoprolol
parent: Solo predicción del modelo (L5)
nav_order: 350
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

# Metoprolol: De Indicación Original No Registrada a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Metoprolol es un betabloqueante cardioselectivo (beta-1) comercializado en España. El Evidence Pack no registra su indicación original aprobada.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**,
pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada (los textos de indicación aprobada de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99.91% (posición 2065 en el ranking del modelo) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Metoprolol es un betabloqueante beta-1, y mecanísticamente podría ser aplicable a la hipertensión maligna con daño renal.

El bloqueo beta-1 reduce la frecuencia cardíaca, el gasto cardíaco y la liberación de renina. Por eso es plausible un efecto reductor de la presión arterial, y la supresión de renina es relevante en la hipertensión de origen renal.

Esta razonabilidad es solo una hipótesis. La hipertensión maligna se maneja normalmente con fármacos intravenosos de dosis titulable. No se aportó ningún ensayo ni publicación que estudie metoprolol en esta condición, y la similitud con la indicación original no pudo evaluarse. El puntaje alto del modelo debe leerse como una señal de exploración, no como una prueba de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Hay 6 autorizaciones en total. Se listan las 5 principales incluidas en el Evidence Pack. Ninguna tiene texto de indicación aprobada registrado.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 82000 | Metoprolol Aurovitas 100 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 61506 | Beloken Retard 95 mg comprimidos de liberación prolongada | Comprimido de liberación prolongada |
| 54503 | Lopresor 100 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 56989 | Beloken 1 mg/ml solución inyectable | Solución inyectable |
| 55748 | Beloken 100 mg comprimidos | Comprimido |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Nota: el modelo también señala, para otras indicaciones predichas, una posible preocupación de seguridad del ventrículo derecho con el bloqueo beta en hipertensión pulmonar. No hay datos de seguridad específicos para la indicación evaluada aquí.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos ni literatura. Además, el manejo estándar de la hipertensión maligna usa fármacos intravenosos titulables, por lo que no hay base para avanzar.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de la AEMPS (advertencias y contraindicaciones), un vacío de datos bloqueante.
- Obtener el mecanismo de acción desde DrugBank (DB00264).
- Hacer una búsqueda bibliográfica dirigida de metoprolol en hipertensión maligna y nefroesclerosis hipertensiva.
- Evaluar la compatibilidad de vías de administración (la solución inyectable existe en España, pero se necesita analizar su idoneidad).

**Otras predicciones del mismo fármaco con más respaldo (para revisión separada):**
- Infarto de miocardio septal: L3, con estudios clínicos cuyo diseño no está confirmado.
- Cor pulmonale crónico: L4, con evidencia indirecta en poblaciones con EPOC, insuficiencia cardíaca e infarto. El ensayo de Fase 3 NCT02587351 terminó de forma anticipada sin mostrar beneficio.

*Los resultados son solo de referencia para investigación y no constituyen consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

