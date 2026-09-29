---
layout: default
title: Colchicine
parent: Evidencia moderada (L3-L4)
nav_order: 145
evidence_level: L4
indication_count: 3
---

# Colchicine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **3** 
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

# Colchicina: De Gota a Malaria por Plasmodium falciparum

## Resumen en Una Frase

La colchicina es un alcaloide oral, utilizado sobre todo para tratar la gota y otras enfermedades autoinflamatorias como el síndrome de Behçet.
El modelo TxGNN predice que podría ser efectiva para la **malaria por Plasmodium falciparum**,
pero hay **0 ensayos clínicos** y solo **6 publicaciones**, todas de laboratorio o indirectas, por lo que la evidencia es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota (según los datos farmacológicos; las autorizaciones de la AEMPS no incluyen texto de indicación) |
| Nueva Indicación Predicha | Malaria por Plasmodium falciparum |
| Puntaje de Predicción TxGNN | 99.60% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 8 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

El campo de mecanismo de acción del registro está vacío. Aun así, los datos farmacológicos indican que la colchicina se une a la tubulina (diana: tubulina beta clase I, *TUBB*) y altera los microtúbulos. Ese es el mecanismo conocido de su acción antiinflamatoria y antimitótica.

La relación con la malaria es solo hipotética. Plasmodium usa microtúbulos para dividirse y para invadir los glóbulos rojos, así que un compuesto que actúe sobre la tubulina podría tener efecto antiparasitario. Los estudios disponibles apoyan la idea de forma indirecta: en 1989 se vio que compuestos que se unen a proteínas del citoesqueleto inhiben *P. falciparum* in vitro. Esos estudios no probaron colchicina directamente.

Hay dos razones para ser cautos. Primero, el puntaje alto de TxGNN (99.60%) es una predicción basada en redes de conocimiento y no una prueba clínica. Segundo, la colchicina tiene un margen terapéutico muy estrecho y una toxicidad bien documentada, por lo que es dudoso que se alcancen concentraciones antiparasitarias en humanos sin toxicidad.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2655935](https://pubmed.ncbi.nlm.nih.gov/2655935/) | 1989 | In vitro | Cell Biol Int Rep | Nueve sustancias que se unen a tubulina y una que se une a actina se probaron contra *P. falciparum*. Las tubulinas del parásito parecen distintas de las de mamíferos. El compuesto más prometedor fue tubulozol-T, no la colchicina. (El registro [2670249](https://pubmed.ncbi.nlm.nih.gov/2670249/) es un duplicado.) |
| [2221861](https://pubmed.ncbi.nlm.nih.gov/2221861/) | 1990 | In vitro | Antimicrob Agents Chemother | Mecanismo de los tubulozoles, otra clase de compuestos: reducen la síntesis de proteínas del parásito. La colcemida, un análogo de la colchicina, tuvo un efecto similar sobre la síntesis de proteínas. |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro (células) | Mol Cell Biol | La expresión del gen *pfmdr1* del parásito en células de mamífero modifica la sensibilidad a fármacos, incluida la colchicina. Es un estudio de resistencia a fármacos, no de eficacia. |
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro | PLoS One | La curcumina, no la colchicina, altera los microtúbulos de *P. falciparum*. Apoya la idea de que los microtúbulos del parásito son una diana, pero no prueba nada sobre la colchicina. |
| [6362934](https://pubmed.ncbi.nlm.nih.gov/6362934/) | 1984 | Observacional (serología) | Clin Exp Immunol | Pacientes con malaria aguda presentan anticuerpos contra filamentos intermedios del citoesqueleto. No está relacionado con ningún fármaco. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 86658 | COLCHICINA TIOFARMA 1 MG COMPRIMIDOS | Comprimido |
| 33720 | COLCHICINA SEID 1 mg COMPRIMIDOS | Comprimido |
| 86430 | COLCAMEXX 0,5 MG COMPRIMIDOS EFG | Comprimido |
| 86659 | COLCHICINA TIOFARMA 0,5 MG COMPRIMIDOS | Comprimido |
| 78947 | COLCHICINA SEID 0,5 MG COMPRIMIDOS | Comprimido |

Se muestran 5 de las 8 autorizaciones. El registro no incluye el texto de indicación aprobada de ninguna de ellas.

## Consideraciones de Seguridad

- **Dianas farmacológicas registradas (7):** tubulina beta clase I (*TUBB*), receptores de glicina (subunidades α1, α2 y todos los subtipos), receptores del gusto amargo *TAS2R4* y *TAS2R46*, y *BRD4*. Son interacciones con dianas moleculares, no interacciones clínicas con otros medicamentos.
- **Toxicidad:** la literatura describe un margen terapéutico estrecho, sin una distinción clara entre dosis no tóxicas, tóxicas y letales. La intoxicación no intencionada es frecuente y suele tener mal pronóstico ([PMID 20586571](https://pubmed.ncbi.nlm.nih.gov/20586571/)). Esto es un obstáculo importante para cualquier uso antiparasitario.

Consultar el prospecto para el resto de la información de seguridad (advertencias, contraindicaciones e interacciones clínicas).

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en un puntaje del modelo y en estudios in vitro antiguos, casi todos con otros compuestos. No hay datos en animales ni en humanos, y el margen terapéutico estrecho de la colchicina hace dudosa la viabilidad de alcanzar concentraciones antipalúdicas seguras.

**Para avanzar se necesita:**
- Ensayos in vitro con colchicina sobre *P. falciparum* que determinen la CI50 y la comparen con las concentraciones plasmáticas alcanzables de forma segura.
- Datos de selectividad entre la tubulina del parásito y la humana, y modelos animales de malaria.
- El prospecto de la AEMPS, para cerrar el vacío de advertencias y contraindicaciones.
- Datos formales del mecanismo de acción (por ejemplo, desde DrugBank).

**Nota:** entre las otras predicciones del modelo, la fiebre mediterránea familiar (nivel L3, *Proceed with Guardrails*) tiene mucha más evidencia. Sin embargo, la colchicina ya es tratamiento de primera línea para esa enfermedad, así que probablemente no sea un reposicionamiento genuino, y habría que comprobarlo con la ficha técnica. La predicción de dermatofibrosarcoma protuberans (L5) no tiene ninguna evidencia.

*Este informe es solo para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

