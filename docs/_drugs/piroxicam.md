---
layout: default
title: Piroxicam
parent: 僅模型預測 (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
---

# Piroxicam
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

# Piroxicam: De Artritis Reumatoide (Adultos) a Artritis Idiopática Juvenil

## Nota sobre la selección de indicación

TxGNN generó 10 indicaciones predichas para este fármaco. Las 9 primeras por puntaje (rank 205-1281) son síndromes genéticos raros de displasia esquelética/ocular o inmunodeficiencia (p. ej. *colobomatous microphthalmia-rhizomelic dysplasia*, *brachydactyly-syndactyly syndrome*, *WHIM syndrome*) sin ningún ensayo clínico, literatura ni vínculo mecanístico con la inhibición de COX-1/COX-2 — nivel de evidencia L5, recomendación "Hold" en todos los casos. La única indicación con evidencia real es **Artritis Idiopática Juvenil (AIJ)** (rank 10), por lo que este informe se centra en ella.

---

## Resumen en Una Frase

Piroxicam es un antiinflamatorio no esteroideo (AINE) de la clase oxicam, utilizado tradicionalmente en adultos para artritis reumatoide, osteoartritis y espondilitis anquilosante. El modelo TxGNN predice que también podría ser eficaz en la **Artritis Idiopática Juvenil**, respaldado por **13 publicaciones** (incluyendo 2 ensayos aleatorizados con piroxicam directamente en artritis juvenil), aunque actualmente no hay ensayos clínicos activos registrados en ClinicalTrials.gov o ICTRP.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Antiinflamatorio no esteroideo (AINE) — artritis reumatoide, osteoartritis, espondilitis anquilosante (uso general en adultos) |
| Nueva Indicación Predicha | Artritis Idiopática Juvenil (AIJ) |
| Puntaje de Predicción TxGNN | 99.93% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Taiwán | ✗ No comercializado (未上市) |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

---

## Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de evidencia consultada. Según la información conocida, piroxicam es un AINE de la clase oxicam que inhibe la ciclooxigenasa (COX-1/COX-2), reduciendo la síntesis de prostaglandinas responsables de la inflamación, el dolor y la tumefacción articular.

La AIJ comparte con las artropatías inflamatorias del adulto (artritis reumatoide) el mismo componente fisiopatológico central: sinovitis mediada por prostaglandinas. Esto hace que el mecanismo de acción de piroxicam sea directamente trasladable, y de hecho existen ensayos clínicos históricos que evaluaron piroxicam específicamente en población pediátrica con artritis crónica/reumatoide juvenil, no solo una extrapolación teórica del modelo.

Dicho esto, piroxicam tiene una semivida de eliminación prolongada (~50 horas) y un perfil de riesgo gastrointestinal y cutáneo mayor que otros AINEs, motivo por el cual las guías pediátricas actuales lo consideran un fármaco de segunda línea frente a opciones de semivida más corta. La evidencia respalda el mecanismo, pero no lo posiciona como primera opción terapéutica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados en ClinicalTrials.gov o ICTRP para esta indicación. La evidencia clínica disponible proviene de ensayos aleatorizados publicados históricamente (ver sección de Literatura).

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2957205](https://pubmed.ncbi.nlm.nih.gov/2957205/) | 1987 | ECA | European Journal of Rheumatology and Inflammation | Piroxicam vs. naproxen en 26 niños con artritis reumatoide juvenil (3-25 años); reducción significativa de articulaciones dolorosas e inflamadas |
| [3510686](https://pubmed.ncbi.nlm.nih.gov/3510686/) | 1986 | ECA | British Journal of Rheumatology | Estudio multicéntrico doble ciego cruzado (8 semanas, 47 niños de 5-16 años) comparando piroxicam vs. naproxen en artritis crónica juvenil; sin diferencia significativa entre tratamientos |
| [38680254](https://pubmed.ncbi.nlm.nih.gov/38680254/) | 2024 | Revisión (metaanálisis en red) | World Journal of Clinical Cases | Metaanálisis en red de distintos AINEs (incluye piroxicam) para artritis idiopática juvenil; aún sin método óptimo establecido |
| [33632948](https://pubmed.ncbi.nlm.nih.gov/33632948/) | 2021 | Revisión (sistemática) | Indian Pediatrics | Revisión sistemática y metaanálisis en red de eficacia y seguridad comparada de 9 AINEs en AIJ |
| [1782984](https://pubmed.ncbi.nlm.nih.gov/1782984/) | 1991 | Estudio farmacocinético | European Journal of Clinical Pharmacology | Farmacocinética en estado estacionario de piroxicam (0.4 mg/kg/día) en 10 niños con enfermedad reumática; semivida media 32.6 h |
| [9890680](https://pubmed.ncbi.nlm.nih.gov/9890680/) | 1998 | Revisión | Clinical Rheumatology | Toxicidad a largo plazo de fármacos antirreumáticos/antiinflamatorios (incluye AINEs) en 117 niños seguidos ~8.6 años |
| [7797387](https://pubmed.ncbi.nlm.nih.gov/7797387/) | 1994 | Cohorte | International Ophthalmology | Frecuencia de iridociclitis crónica en artritis crónica juvenil pauciarticular ANA-positiva (contexto de manejo de AIJ, no piroxicam específico) |
| [2185374](https://pubmed.ncbi.nlm.nih.gov/2185374/) | 1990 | Revisión | Kinderärztliche Praxis | Aspectos actuales de la farmacoterapia de la artritis crónica juvenil, menciona piroxicam entre las opciones |
| [15456329](https://pubmed.ncbi.nlm.nih.gov/15456329/) | 2004 | Revisión | Drugs | Perfil terapéutico y de seguridad de nabumetona en artrosis y artritis reumatoide (contexto comparativo de AINEs) |
| [21175420](https://pubmed.ncbi.nlm.nih.gov/21175420/) | 2010 | Revisión | Critical Reviews in Therapeutic Drug Carrier Systems | Sistemas de microencapsulación como vía de administración novedosa de AINEs en artritis, incluida AIJ |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. Los datos de advertencias, contraindicaciones e interacciones farmacológicas de TFDA aún no han sido incorporados a esta evaluación (brecha bloqueante — ver Próximos Pasos).

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Existe evidencia clínica directa de nivel L1 (dos ECAs históricos con piroxicam en artritis juvenil, más revisiones sistemáticas recientes de AINEs en AIJ) que respalda mecanística y clínicamente la predicción. Sin embargo, el fármaco no está comercializado actualmente en Taiwán, y la brecha de datos de seguridad de TFDA (advertencias/contraindicaciones) es de severidad "Blocking" — impide iniciar la evaluación de seguridad inicial (S1) requerida antes de avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto/etiquetado de TFDA (advertencias, contraindicaciones) — brecha bloqueante DG001
- Confirmar el mecanismo de acción vía DrugBank — brecha DG002
- Evaluar el perfil de seguridad pediátrico frente a AINEs de semivida más corta, dado el riesgo gastrointestinal/cutáneo conocido de piroxicam en niños
- Definir vía regulatoria para comercialización en Taiwán, dado que actualmente no hay ninguna autorización vigente
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

