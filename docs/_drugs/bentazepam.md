---
layout: default
title: Bentazepam
parent: Solo predicción del modelo (L5)
nav_order: 69
evidence_level: L5
indication_count: 7
---

# Bentazepam
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

# Bentazepam: De Ansiedad (indicación inferida) a Insomnio

## Resumen en Una Frase

Bentazepam es una benzodiazepina de tipo tienodiazepina, comercializada en España como ansiolítico. La ficha de autorización no incluye el texto de la indicación, así que la indicación original se infiere de la literatura.
El modelo TxGNN predice que podría ser efectivo para **insomnio**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en la autorización de AEMPS. La literatura la describe como ansiolítico para trastornos de ansiedad (inferido) |
| Nueva Indicación Predicha | Insomnio |
| Puntaje de Predicción TxGNN | 99,95% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción de bentazepam. Según la información conocida, es una benzodiazepina, su uso como ansiolítico está documentado en España, y mecanísticamente podría ser aplicable al insomnio. Como el resto de su clase, probablemente modula de forma alostérica positiva el receptor GABA-A, lo que produce efectos sedantes e hipnóticos. Esto es una inferencia de clase y no está verificado para este compuesto.

La relación entre la indicación original y la nueva es estrecha. La ansiedad y el insomnio comparten circuitos GABAérgicos, y muchas benzodiazepinas se usan para ambos. Por eso el puntaje alto de TxGNN es biológicamente plausible. Sin embargo, no se suministró ningún estudio de bentazepam en insomnio.

Conviene tratar esta predicción con cautela. Es probable que la ansiedad sea el uso ya establecido y que la ausencia de indicación original en los datos sea una laguna, no un reposicionamiento real.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para insomnio.

Como contexto, la predicción de **ansiedad** (rank 6, puntaje 99,37%, nivel L3) sí cuenta con literatura. Es observacional y centrada en seguridad y farmacocinética, sin ECAs:

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [1983365](https://pubmed.ncbi.nlm.nih.gov/1983365/) | 1990 | Cohorte (farmacovigilancia) | Rev Med Univ Navarra | 1.046 pacientes psiquiátricos ambulatorios. Estudio con potencia para detectar efectos >5% como sequedad de boca, somnolencia, astenia, molestias gástricas y estreñimiento. La coprescripción más frecuente fue con antidepresivos |
| [10961721](https://pubmed.ncbi.nlm.nih.gov/10961721/) | 2000 | Reporte de casos | Dig Dis Sci | Tres pacientes con aumento persistente de transaminasas tras semanas de tratamiento. Se resolvió al retirar el fármaco. Hepatotoxicidad idiosincrática poco común |
| [2565591](https://pubmed.ncbi.nlm.nih.gov/2565591/) | 1989 | Reporte de caso | Rev Esp Anestesiol Reanim | Intoxicación mixta (bentazepam, clordiazepóxido e imipramina) con coma e insuficiencia respiratoria, revertida con flumazenilo |
| [2893777](https://pubmed.ncbi.nlm.nih.gov/2893777/) | 1987 | Simulación farmacocinética | Int J Clin Pharmacol Ther Toxicol | Simulación de niveles plasmáticos con 25 mg por vía oral cada 8, 12 y 24 h durante 5 días |
| [2877954](https://pubmed.ncbi.nlm.nih.gov/2877954/) | 1986 | Estudio farmacocinético | Int J Clin Pharmacol Ther Toxicol | Tiadipona 25 mg en 10 voluntarios sanos, modelo monocompartimental. Debe verificarse la identidad con bentazepam |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 55464 | TIADIPONA (Mylan Ire Healthcare Limited) | Comprimido | No disponible en los datos |

---

## Consideraciones de Seguridad

No hay datos de advertencias ni contraindicaciones del prospecto de AEMPS, y no se encontraron interacciones farmacológicas registradas. La literatura aporta las siguientes señales:

- **Hepatotoxicidad**: casos de lesión hepática crónica (aumento persistente de transaminasas) con resolución tras la retirada. Es especialmente relevante para alcohol y sustancias, poblaciones con alta prevalencia de hepatopatía.
- **Efectos adversos frecuentes en farmacovigilancia**: sequedad de boca, somnolencia, astenia, molestias gástricas, estreñimiento y náuseas.
- **Sobredosis**: un caso de intoxicación mixta grave, con reversión mediante flumazenilo.
- **Riesgo de clase**: dependencia y uso indebido, comunes a las benzodiazepinas. Es una inferencia de clase, sin datos específicos de bentazepam.

Consultar el prospecto para la información de seguridad completa.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Para insomnio solo existe la predicción del modelo (L5), sin ensayos ni literatura específica. Además, la señal de hepatotoxicidad y el riesgo de dependencia exigen cautela antes de invertir en esta dirección.

Las otras predicciones también están en Hold y en L5:
- Delirio por abstinencia alcohólica
- Abuso de alucinógenos, barbitúricos y antidepresivos
- Trastorno del sueño (inicio y mantenimiento)

Los puntajes idénticos (0,99484) de las tres predicciones de abuso sugieren un artefacto del grafo.

**Para avanzar se necesita:**
- Obtener la ficha técnica de AEMPS (advertencias, contraindicaciones e indicación autorizada), pendiente de descarga y análisis.
- Confirmar el mecanismo de acción en DrugBank.
- Verificar la indicación original y la identidad entre tiadipona y bentazepam.
- Buscar ensayos o estudios de bentazepam en insomnio.
- Plan de vigilancia hepática y evaluación del riesgo de dependencia.

*Los resultados son solo para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

