---
layout: default
title: Elafibranor
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 1
---

# Elafibranor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Elafibranor: De Farmaco en Investigacion a Amenorrea (Predicha)

## Resumen en Una Frase

Elafibranor es un agonista dual PPARα/δ que actualmente no tiene indicacion aprobada ni presencia en el mercado espanol.
El modelo TxGNN predice que podria ser efectivo para **Amenorrea**, con una puntuacion de **99.86%**,
pero por ahora **no existen ensayos clinicos ni publicaciones** que respalden directamente esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Sin indicacion aprobada registrada (farmaco no comercializado) |
| Nueva Indicacion Predicha | Amenorrea |
| Puntaje de Prediccion TxGNN | 99.86% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion de elafibranor en esta fuente. Segun la informacion disponible, se trata de un agonista dual PPARα/δ, un compuesto que no tiene indicacion oficial aprobada y que aun no ha llegado al mercado.

La via PPARα/δ esta relacionada principalmente con el metabolismo lipidico, la sensibilidad a la insulina y la inflamacion hepatica, sin una conexion mecanistica directa y conocida con el eje hipotalamo-hipofisis-ovario (eje HPO) o la regulacion del ciclo menstrual. La puntuacion elevada de TxGNN podria reflejar rutas de asociacion indirecta dentro del grafo de conocimiento (por ejemplo, nodos compartidos con metabolismo lipidico, sindrome de ovario poliquistico o resistencia a la insulina), en lugar de un efecto farmacologico directo sobre la amenorrea.

Tambien debe considerarse una hipotesis alternativa: la senal alta podria corresponder a un posible efecto adverso sobre el eje reproductivo (mas que a un beneficio terapeutico) que el modelo esta clasificando erroneamente como asociacion de tratamiento. Esta ambiguedad refuerza la necesidad de verificacion mecanistica adicional antes de avanzar.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Consideraciones de Seguridad

No hay informacion de seguridad disponible en las fuentes consultadas (ficha tecnica/TFDA, base de interacciones). Al no estar comercializado en Espana, tampoco existe prospecto local de referencia.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La puntuacion de TxGNN es alta, pero no esta respaldada por ningun ensayo clinico ni publicacion (nivel de evidencia L5), no hay confirmacion del mecanismo de accion, y la via PPARα/δ no tiene una relacion mecanistica directa conocida con el eje HPO o el ciclo menstrual. No puede descartarse que la senal refleje un efecto adverso reproductivo en lugar de un beneficio terapeutico.

**Para avanzar se necesita:**
- Confirmar el mecanismo de accion (MOA) mediante consulta a DrugBank u otra fuente farmacologica
- Obtener advertencias y contraindicaciones oficiales (ficha tecnica/regulador), actualmente bloqueante para la evaluacion de seguridad
- Estudios preclinicos o mecanisticos que evaluen el efecto de elafibranor sobre el eje HPO o el ciclo menstrual
- Aclarar si la senal de TxGNN corresponde a un efecto terapeutico o a una senal de seguridad reproductiva mal clasificada
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

