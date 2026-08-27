---
layout: default
title: Loprazolam
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 1
---

# Loprazolam
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

# Loprazolam: De No Comercializado en España a Insomnio (Trastorno de Inicio y Mantenimiento del Sueño)

## Resumen en Una Frase

Loprazolam es una benzodiazepina hipnótica que actualmente **no está comercializada en España**, sin indicación original registrada localmente.
El modelo TxGNN predice que sería efectivo para **Trastorno de Inicio y Mantenimiento del Sueño (Insomnio)**,
con **0 ensayos clínicos registrados** pero **20 publicaciones**, varias de ellas ensayos clínicos aleatorizados históricos, que respaldan esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible — sin licencias registradas en España (fármaco no comercializado) |
| Nueva Indicación Predicha | Trastorno de Inicio y Mantenimiento del Sueño (Insomnio) |
| Puntaje de Predicción TxGNN | 99.84% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

---

## ¿Por qué es Razonable esta Predicción?

Loprazolam es una benzodiazepina del tipo nitrobenzodiazepina (imidazobenzodiazepina) que actúa sobre el sitio de unión a benzodiazepinas del receptor GABA-A, potenciando la neurotransmisión inhibitoria mediada por GABA. Este mecanismo es el mismo que sustenta el efecto sedante/hipnótico característico de toda la clase de las benzodiazepinas.

A diferencia de un reposicionamiento clásico hacia un mecanismo no relacionado, en este caso la indicación predicha por TxGNN (insomnio) coincide con el uso histórico ya documentado del fármaco: loprazolam ha estado en uso clínico en mercados como el Reino Unido y Francia para el tratamiento del insomnio agudo y crónico desde la década de 1980. Por tanto, la predicción del modelo no representa tanto una hipótesis novedosa de reposicionamiento, sino la confirmación farmacológica de una indicación ya establecida fuera de España, donde el producto actualmente no está comercializado.

Esto también explica por qué existe abundante literatura clínica —incluyendo múltiples ensayos controlados aleatorizados doble ciego— pero ningún ensayo clínico registrado activo: la evidencia proviene mayoritariamente de estudios de las décadas de 1980-1990 que establecieron la eficacia del fármaco frente a placebo y frente a otros hipnóticos comparadores (nitrazepam, temazepam, triazolam, flurazepam).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6141896](https://pubmed.ncbi.nlm.nih.gov/6141896/) | 1983 | ECA | Current Medical Research and Opinion | Doble ciego en 40 pacientes con insomnio ansioso; loprazolam 1 mg superior a placebo |
| [6147285](https://pubmed.ncbi.nlm.nih.gov/6147285/) | 1984 | ECA | J Int Med Res | Estudio multicéntrico (190 pacientes) comparando loprazolam vs nitrazepam; eficacia similar |
| [6142463](https://pubmed.ncbi.nlm.nih.gov/6142463/) | 1983 | ECA | Pharmatherapeutica | Ensayo aleatorizado doble ciego en 40 ancianos; loprazolam y nitrazepam mejoraron el sueño significativamente |
| [6141114](https://pubmed.ncbi.nlm.nih.gov/6141114/) | 1984 | ECA | J Int Med Res | Estudio multicéntrico (197 pacientes) en atención primaria comparando loprazolam, temazepam y placebo |
| [2569239](https://pubmed.ncbi.nlm.nih.gov/2569239/) | 1989 | ECA | Thérapie | Cruzado doble ciego (67 pacientes) comparando triazolam 0.25 mg vs loprazolam 1 mg en insomnio común |
| [8771595](https://pubmed.ncbi.nlm.nih.gov/8771595/) | 1996 | ECA | Prog Neuropsychopharmacol Biol Psychiatry | Cruzado doble ciego (67 pacientes) con evaluación de preferencia del paciente; ambos fármacos mejoraron la calidad del sueño |
| [6132929](https://pubmed.ncbi.nlm.nih.gov/6132929/) | 1983 | ECA | Journal of Clinical Pharmacology | Dosis única doble ciego (60 pacientes); loprazolam 0.5-1 mg comparable a flurazepam 15 mg, superior a placebo |
| [2874007](https://pubmed.ncbi.nlm.nih.gov/2874007/) | 1986 | Revisión | Drugs | Revisión farmacodinámica/farmacocinética; vida media 7-8h, ventaja sobre hipnóticos de acción más larga |
| [15252823](https://pubmed.ncbi.nlm.nih.gov/15252823/) | 2004 | Revisión sistemática (meta-análisis) | Human Psychopharmacology | Compara fármacos Z frente a benzodiazepinas (incluye loprazolam) autorizadas en el Reino Unido para insomnio a corto plazo |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Revisión | BMJ Clinical Evidence | Revisión sobre insomnio en el anciano; hasta 40% de prevalencia en adultos |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El mecanismo (agonismo GABA-A) y la evidencia clínica histórica —múltiples ensayos aleatorizados doble ciego frente a placebo y comparadores— respaldan sólidamente la eficacia de loprazolam en insomnio. Sin embargo, faltan datos regulatorios locales (advertencias, contraindicaciones, interacciones) y el producto no está comercializado en España, lo que impide cerrar la evaluación de seguridad sin guardrails adicionales.

**Para avanzar se necesita:**
- Ficha técnica/prospecto oficial con advertencias y contraindicaciones
- Datos de interacciones farmacológicas (DDI) documentados
- Confirmar la vía regulatoria para introducir el producto al mercado español, dado que actualmente no tiene autorizaciones registradas
- Evaluar riesgo de dependencia/abuso y pautas de uso en población anciana, señalada en la literatura como grupo de mayor riesgo de efectos residuales (sedación diurna, caídas)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

