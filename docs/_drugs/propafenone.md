---
layout: default
title: Propafenone
parent: Solo predicción del modelo (L5)
nav_order: 443
evidence_level: L5
indication_count: 8
---

# Propafenone
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

# Propafenona: De Arritmias Cardíacas a Trastorno Bipolar Maníaco

## Resumen en Una Frase

La propafenona es un antiarrítmico de clase Ic, utilizado en arritmias auriculares y ventriculares.
El modelo TxGNN predice que podría ser efectivo para **trastorno bipolar maníaco**, pero **no hay ensayos clínicos** y las **3 publicaciones** encontradas describen sobre todo efectos adversos (manía y psicosis), no beneficio terapéutico.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Arritmias auriculares y ventriculares (según Guide to Pharmacology; los registros de AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Trastorno bipolar maníaco |
| Puntaje de Predicción TxGNN | 99,80% |
| Nivel de Evidencia | L4 (según el Evidence Pack; no hay evidencia de beneficio) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 5 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, la propafenona actúa como antiarrítmico de clase Ic (bloqueo de canales de sodio) y presenta afinidad por los receptores β1 y β2 adrenérgicos y por el canal Kv1.5. Su eficacia en arritmias está establecida, pero no existe un vínculo mecanístico claro con el trastorno bipolar maníaco.

**Esta predicción no tiene una justificación terapéutica.** La literatura describe un caso de manía secundaria a propafenona y un cuadro psicótico por interacción con venlafaxina. Ambos son señales de efecto adverso, no de beneficio. El caso de 1985 sugirió, de forma solo especulativa, que su parecido químico con el bupropión podría implicar cierta actividad antidepresiva, lo que explicaría precisamente el riesgo de efectos afectivos.

El puntaje alto de TxGNN probablemente es un artefacto del grafo de conocimiento, que registra la asociación fármaco-enfermedad sin distinguir su dirección (efecto adverso frente a beneficio).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [32124390](https://pubmed.ncbi.nlm.nih.gov/32124390/) | 2020 | Revisión | Pharmacological Reports | Evalúa interacciones dañinas entre antipsicóticos y fármacos cardiovasculares en pacientes con trastorno bipolar o esquizofrenia y comorbilidad cardiovascular |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Caso clínico | International Journal of Psychiatry in Medicine | Psicosis orgánica por interacción venlafaxina-propafenona en un paciente con trastorno bipolar |
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Caso clínico | Journal of Clinical Psychiatry | Manía secundaria a propafenona; complicación no descrita previamente |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 55538 | RYTMONORM 150 mg comprimidos recubiertos | Comprimido recubierto | Teva B.V. |
| 55541 | RYTMONORM 300 mg comprimidos recubiertos | Comprimido recubierto | Teva B.V. |
| 58275 | RYTMONORM 3,5 mg/ml solución inyectable | Solución inyectable | Teva B.V. |
| 82298 | PROPAFENONA HIDROCLORURO ACCORD 150 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Accord Healthcare S.L.U. |
| 82299 | PROPAFENONA HIDROCLORURO ACCORD 300 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Accord Healthcare S.L.U. |

---

## Consideraciones de Seguridad

- **Señales de seguridad psiquiátrica (literatura)**: manía secundaria a propafenona (1985) y psicosis orgánica por interacción con venlafaxina (2001), ambas en pacientes con trastorno afectivo.

Para advertencias, contraindicaciones e interacciones farmacológicas, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia disponible para esta indicación apunta a un riesgo (manía y psicosis inducidas), no a un beneficio, y no hay ensayos clínicos ni mecanismo plausible. El puntaje TxGNN alto probablemente refleja un artefacto del grafo.

**Para avanzar se necesita:**
- Descartar formalmente que la asociación sea una señal de efecto adverso y no terapéutica; sin evidencia de beneficio, no se recomienda avanzar.
- Obtener las advertencias y contraindicaciones del prospecto de AEMPS y los datos de mecanismo de acción (DrugBank).
- Priorizar otras predicciones del mismo Evidence Pack con mejor respaldo. La **taquicardia ventricular polimórfica catecolaminérgica** tiene modelos preclínicos que muestran inhibición de RyR2 y un caso de tratamiento eficaz durante 35 años (L4). La **taquicardia ventricular incesante infantil** tiene series pediátricas (L3). En ambas habría que evaluar el riesgo proarrítmico de los antiarrítmicos 1C en cardiopatía estructural.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

