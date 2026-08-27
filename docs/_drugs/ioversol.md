---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 10
---

# Ioversol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Ioversol: De Agente de Contraste Radiológico a Osteoartritis (Susceptibilidad)

## Resumen en Una Frase

Ioversol es un agente de contraste yodado no iónico utilizado exclusivamente para diagnóstico por imagen (radiografía, angiografía, TC), sin indicación terapéutica registrada. El modelo TxGNN predice una asociación con **"osteoarthritis susceptibility"** (susceptibilidad/predisposición a osteoartritis) con una puntuación muy alta, pero esta predicción **no cuenta actualmente con ningún ensayo clínico ni publicación científica que la respalde**.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Agente de contraste radiológico (uso diagnóstico, sin indicación terapéutica) |
| Nueva Indicación Predicha | Osteoarthritis susceptibility (susceptibilidad a osteoartritis) |
| Puntaje de Predicción TxGNN | 99.67% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de Ioversol en la base de evidencia consultada. Según la información conocida, Ioversol es un medio de contraste yodado no iónico usado en procedimientos de imagen diagnóstica; no tiene un mecanismo farmacológico terapéutico descrito, por lo que no existe un fundamento mecanístico plausible que conecte su uso con la osteoartritis.

Adicionalmente, "osteoarthritis susceptibility" es un fenotipo de **predisposición/susceptibilidad genética**, no una enfermedad activa tratable — este tipo de indicación no suele ser un objetivo clínicamente accionable para reposicionamiento farmacológico.

Es relevante notar que, para la indicación relacionada de rango 2 ("osteoarthritis", puntuación 99.63%), la evidencia disponible en la base de datos corresponde en realidad a ensayos con **Lipiodol** (aceite yodado usado en embolización arterial terapéutica), no con Ioversol. Esto sugiere que la alta puntuación del modelo TxGNN podría derivar de una confusión de entidades en el grafo de conocimiento (ambos son compuestos yodados), más que de una relación mecanística real. Para la indicación de rango 1 aquí evaluada no existe siquiera esa evidencia indirecta: cero ensayos clínicos y cero publicaciones.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La puntuación de predicción de TxGNN es alta, pero no existe ningún ensayo clínico ni publicación que respalde la asociación entre Ioversol y osteoartritis/susceptibilidad a osteoartritis. Ioversol es un agente de contraste sin mecanismo terapéutico conocido, y el fenotipo predicho (susceptibilidad genética) no es un objetivo clínico directamente tratable.

**Para avanzar se necesita:**
- Datos del mecanismo de acción (MOA) de Ioversol y evaluación de si existe alguna plausibilidad farmacológica real
- Verificación de si la señal del modelo se debe a confusión de entidades con Lipiodol (aceite yodado) en el grafo de conocimiento, dado el patrón observado en la indicación relacionada "osteoarthritis"
- Datos del prospecto de la AEMPS (advertencias, contraindicaciones, interacciones), actualmente pendientes (gap bloqueante DG001)
- Ioversol no está comercializado en España (0 autorizaciones), lo que limita la viabilidad práctica de cualquier desarrollo de reposicionamiento en este mercado
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

