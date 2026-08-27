---
layout: default
title: Levonorgestrel
parent: 僅模型預測 (L5)
nav_order: 166
evidence_level: L5
indication_count: 6
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Levonorgestrel: De Anticoncepción Hormonal a Acné

## Resumen en Una Frase

Levonorgestrel es un progestágeno de segunda generación empleado en anticoncepción hormonal (sistemas intrauterinos, implantes subdérmicos y anticonceptivos orales combinados). El modelo TxGNN predice que podría ser efectivo para **Acné**, con **5 ensayos clínicos** y **20 publicaciones** identificadas, aunque la evidencia mecanística disponible apunta en una dirección contraria a la esperada para esta indicación.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Anticoncepción hormonal (sistema intrauterino, implante subdérmico, anticonceptivo oral combinado) |
| Nueva Indicación Predicha | Acné |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción verificados (dato pendiente de DrugBank). Según la información conocida a partir de la literatura recopilada, levonorgestrel es un progestágeno con **actividad androgénica relativamente alta**, utilizado en sistemas de liberación intrauterina, implantes subdérmicos y anticonceptivos orales combinados; su eficacia anticonceptiva está ampliamente demostrada.

Sin embargo, la relación entre la indicación original y la nueva indicación predicha presenta una **contradicción mecanística relevante**: el acné vulgar se asocia a exceso de actividad androgénica en la unidad pilosebácea, y el tratamiento hormonal del acné se basa habitualmente en progestágenos **antiandrogénicos** (acetato de ciproterona, drospirenona, acetato de clormadinona) combinados con estrógeno para suprimir el andrógeno ovárico. Levonorgestrel pertenece al grupo opuesto de progestágenos androgénicos, por lo que mecanísticamente podría, en teoría, agravar el acné en lugar de mejorarlo.

No obstante, la literatura identificada matiza este punto: al menos un ensayo aleatorizado controlado con placebo (PMID 12196750) mostró que la combinación etinilestradiol/levonorgestrel (20/100 mcg) mejoró el acné moderado, probablemente porque el componente estrogénico aumenta la SHBG y reduce la testosterona libre pese al perfil androgénico del levonorgestrel. Otros estudios comparativos (PMID 15025547) indican que combinaciones con progestágenos antiandrogénicos son superiores a la combinación con levonorgestrel para tratar el acné. En conjunto, la puntuación alta de TxGNN podría reflejar asociaciones indirectas en el grafo de conocimiento (comorbilidad anticoncepción-dermatología) más que un mecanismo terapéutico directo, y debe tratarse como una señal que requiere verificación cuidadosa antes de avanzar.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | Terminado | 44 | Sistema intrauterino de levonorgestrel (Mirena) para prevención de cáncer de endometrio en mujeres con IMC>35; no evalúa acné (relevancia baja). |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | Completado | 101.498 | Cohorte de seguridad comparando anticonceptivo con nomegestrol/estradiol frente a anticonceptivos combinados con levonorgestrel; no evalúa acné (relevancia baja). |
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | Completado | 131 | Anticonceptivo oral continuo + doxiciclina para reducir sangrado irregular; la doxiciclina se usa comúnmente en acné, pero el ensayo no confirma el uso de levonorgestrel ni evalúa acné como objetivo primario (relevancia moderada). |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Fase 2 | Completado | 100 | Implante subdérmico de gestrinona para dolor pélvico por endometriosis; no relacionado con acné (relevancia baja). |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Fase 2 | Desconocido | 60 | Tratamiento conservador de fertilidad para hiperplasia endometrial atípica (Mirena vs. megestrol); no relacionado con acné (relevancia baja). |

**Nota:** Ninguno de los ensayos identificados evalúa directamente levonorgestrel como tratamiento del acné; la relevancia general es baja a moderada.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | ECA | J Am Acad Dermatol | Anticonceptivo oral de dosis baja con etinilestradiol/levonorgestrel (20/100 mcg) mejoró el acné moderado frente a placebo en ensayo controlado. |
| [10717776](https://pubmed.ncbi.nlm.nih.gov/10717776/) | 1999 | ECA | Contraception | Estudio multicéntrico aleatorizado que compara marcadores androgénicos y acné entre levonorgestrel y otro progestágeno en anticonceptivos de dosis baja. |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | Revisión | Drugs | Etinilestradiol/acetato de clormadinona fue significativamente más eficaz que etinilestradiol/levonorgestrel en el tratamiento del acné papulopustuloso leve a moderado. |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Revisión | Am J Clin Dermatol | Revisión sobre beneficios dermatológicos de combinaciones antiandrogénicas en acné, hirsutismo y alopecia por hiperandrogenemia. |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Revisión | J Womens Health | Compara drospirenona con acetato de medroxiprogesterona, levonorgestrel y progesterona micronizada; destaca menor incidencia de acné con drospirenona. |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Revisión | Am J Med | Revisión sobre la androgenicidad de los progestágenos, base mecanística de por qué levonorgestrel tiene mayor actividad androgénica que otros progestágenos. |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Aunque la puntuación TxGNN es muy alta (99.88%), la evidencia disponible es contradictoria: no existen ensayos clínicos que evalúen levonorgestrel en monoterapia para acné, y la literatura sugiere que su perfil androgénico va en dirección opuesta a la esperada, con progestágenos antiandrogénicos mostrando mejor eficacia que las combinaciones con levonorgestrel. Además, el fármaco no está comercializado en España (0 autorizaciones) y faltan datos regulatorios básicos (ficha técnica/prospecto), lo que impide iniciar la evaluación de seguridad S1.

**Para avanzar se necesita:**
- Datos verificados de mecanismo de acción (MOA) desde DrugBank (brecha de datos de severidad Alta)
- Ficha técnica/prospecto con advertencias y contraindicaciones (brecha de datos de severidad Bloqueante — impide la evaluación S1)
- Aclarar si la formulación relevante es levonorgestrel en monoterapia o en combinación con etinilestradiol, dado que la única evidencia positiva proviene de combinaciones EE/LNG
- Los otros 5 candidatos predichos (síndrome de Worth, osteoporosis asociada al embarazo, vitreorretinopatía inflamatoria neovascular autosómica dominante, adenosis apocrina y adenosis de conductos romos de mama) presentan nivel de evidencia L5, sin ensayos ni literatura de respaldo, y con racionales mecanísticos débiles o contradictorios — no se recomienda avanzar con ninguno sin evidencia adicional
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

