---
layout: default
title: Lormetazepam
parent: Solo predicción del modelo (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Lormetazepam
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

# Lormetazepam: Predicción de Insomnio (indicación ya establecida en el mercado)

## Resumen en Una Frase

Lormetazepam es una benzodiacepina de acción corta, comercializada en España como hipnótico sedante.
El modelo TxGNN predice que podría ser eficaz para **insomnio**, que en la práctica es una indicación ya establecida y no un reposicionamiento en sentido estricto.
Hay **3 ensayos clínicos** y **4 publicaciones** vinculados a esta predicción, con un ensayo de Fase 3 completado frente a un comparador.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,98% |
| Nivel de Evidencia | L2 (ver nota) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Proceed with Guardrails |

**Nota sobre el nivel de evidencia:** el Evidence Pack asigna L1. Con las reglas de este informe solo hay un ECA de Fase 3 completado (NCT00679900), ya que NCT00788515 fue terminado con 33 participantes. Por eso se asigna L2. Los registros de AEMPS no traen el texto de indicación aprobada, así que no se puede citar una indicación original desde esa fuente.

---

## ¿Por qué es Razonable esta Predicción?

Lormetazepam potencia la señalización del receptor GABA-A, lo que produce efectos sedantes e hipnóticos. Los datos de mecanismo de acción de DrugBank no están disponibles. Esta descripción proviene de la justificación mecanística del Evidence Pack y del conocimiento general de la clase.

El insomnio es el uso comercial establecido del fármaco. La predicción del modelo coincide con la práctica clínica real, por lo que funciona como confirmación y no como una nueva hipótesis terapéutica. Esa coherencia respalda la fiabilidad del puntaje, pero no aporta un hallazgo novedoso.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00679900](https://clinicaltrials.gov/study/NCT00679900) | Fase 3 | Completado | 283 | Eplivanserina 5 mg vs lormetazepam 1 mg durante 4 semanas en insomnio primario crónico con dificultad de mantenimiento del sueño. Evalúa somnolencia residual matutina, seguridad, insomnio de rebote y síntomas de abstinencia. Lormetazepam es el comparador activo. |
| [NCT00788515](https://clinicaltrials.gov/study/NCT00788515) | Fase 3 | Terminado | 33 | Volinanserina 2 mg vs lormetazepam 1 mg, mismo diseño de 4 semanas. Terminado con solo 33 participantes, por lo que tiene poca potencia y aporta poco. |
| [NCT06473415](https://clinicaltrials.gov/study/NCT06473415) | N/A | Reclutando | 50 | Efecto de la infusión continua de lormetazepam sobre el EEG y la calidad del sueño en pacientes críticos en UCI. Sin resultados todavía. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | Ensayo clínico comparativo | J Int Med Res | Lormetazepam 1 mg vs diazepam 5 mg durante 7 días en 100 pacientes ambulatorios con trastornos del sueño. Lormetazepam fue significativamente mejor en reducir el tiempo para dormirse y en prolongar el sueño continuo (p < 0,05). |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Revisión | Acta Psychiatr Scand Suppl | Uso clínico de los hipnóticos. Defiende disponer de varias benzodiacepinas con distinta farmacocinética y farmacodinamia según el patrón de insomnio. |
| [2873832](https://pubmed.ncbi.nlm.nih.gov/2873832/) | 1986 | Estudio clínico no controlado | Br J Clin Pract | Transferencia de usuarios crónicos de nitrazepam con insomnio a lormetazepam. Sin resumen disponible. |
| [11215344](https://pubmed.ncbi.nlm.nih.gov/11215344/) | 2001 | Revisión | MMW Fortschr Med | Un antidepresivo como alternativa a las benzodiacepinas para dormir. Sin resumen disponible. |

La evidencia bibliográfica es antigua (1981-2001) y limitada. Solo un estudio es comparativo controlado.

---

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. El registro no incluye texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 89877 | Lormetazepam Alter 2 mg comprimidos EFG | Comprimido | Laboratorios Alter S.A. |
| 63332 | Noctamid 2,5 mg/ml gotas orales en solución | Gotas orales en solución | Teofarma S.R.L. |
| 75732 | Lormetazepam Stada 1 mg comprimidos EFG | Comprimido | Laboratorio Stada S.L. |
| 88831 | Lormetazepam Tecnigen 1 mg comprimidos EFG | Comprimido | Tecnimede España Industria Farmacéutica S.A. |
| 73584 | Lormetazepam Kern Pharma 1 mg comprimidos EFG | Comprimido | Kern Pharma S.L. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se recuperaron advertencias, contraindicaciones ni interacciones farmacológicas.

---

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El insomnio es una indicación ya establecida de lormetazepam, con un ECA de Fase 3 completado y estudios comparativos clásicos. La predicción es coherente, pero aporta poca novedad. Debe avanzar con salvaguardas por el riesgo de dependencia y tolerancia, el deterioro psicomotor al día siguiente, la cautela en personas mayores y con alcohol u otros depresores del SNC.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS para obtener advertencias y contraindicaciones.
- Completar los datos de mecanismo de acción desde DrugBank.
- Confirmar el texto de indicación aprobada en los registros de AEMPS.

**Otras predicciones del modelo (no evaluadas en detalle):**
- Ansiedad y trastorno de ansiedad tienen evidencia L3, con solo estudios indirectos (sedación en UCI, farmacovigilancia). Quedan como pregunta de investigación.
- Delirium por abstinencia alcohólica es plausible por la clase farmacológica, pero no tiene evidencia y queda en espera.
- Abuso de alucinógenos, barbitúricos y antidepresivos, síndrome de cauda equina y tortícolis paroxística benigna de la infancia probablemente son artefactos del grafo, sin respaldo terapéutico. Todos quedan en espera.
- "Trastorno del sueño, inicio y mantenimiento" es casi sinónimo de insomnio y conviene fusionarlo con esa entrada.

*Los resultados de este informe son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

