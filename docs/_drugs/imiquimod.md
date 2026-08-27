---
layout: default
title: Imiquimod
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 10
---

# Imiquimod
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

# Imiquimod: De Queratosis Actinica a Neoplasia Pre-maligna

## Resumen en Una Frase

Imiquimod es un inmunomodulador topico (agonista TLR7), utilizado en otros mercados para el tratamiento de queratosis actinica, verrugas genitales externas y carcinoma basocelular superficial. El modelo TxGNN predice que podria ser efectivo para **Neoplasia Pre-maligna** (incluyendo CIN/VIN), con **19 ensayos clinicos** y **9 publicaciones** que actualmente respaldan esta direccion.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en registro de España (producto no comercializado); segun el contexto clinico de la evidencia, imiquimod tiene uso topico establecido en queratosis actinica, verrugas genitales externas y carcinoma basocelular superficial |
| Nueva Indicacion Predicha | Neoplasia Pre-maligna (pre-malignant neoplasm) |
| Puntaje de Prediccion TxGNN | 99.92% |
| Nivel de Evidencia | L1 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha tecnica de MOA (mecanismo de accion) formal en la fuente regulatoria (Data Gap de alta severidad). Sin embargo, la propia evidencia clinica recopilada describe el mecanismo: imiquimod es un agonista del receptor tipo Toll 7 (TLR7) que activa celulas dendriticas y macrofagos, induciendo citocinas como IFN-α y generando una respuesta inmune local antiviral y antitumoral.

Este mecanismo ya es la base farmacologica de usos topicos establecidos de imiquimod en lesiones cutaneas premalignas y asociadas a VPH (queratosis actinica, verrugas genitales, carcinoma basocelular superficial). La neoplasia pre-maligna predicha por TxGNN —que incluye entidades como la neoplasia intraepitelial cervical (CIN) y vulvar (VIN)— comparte el mismo sustrato biologico: lesiones epiteliales de bajo grado, muchas asociadas a VPH, susceptibles a destruccion mediada por inmunidad local.

Por ello, la extension de imiquimod a CIN/VIN no representa una hipotesis completamente nueva, sino una extrapolacion natural del mismo mecanismo dentro del mismo espectro de patologia epitelial premaligna, lo que explica el elevado nivel de evidencia (L1) alcanzado.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Fase 3 | Completado | 259 | Imiquimod como tratamiento neoadyuvante para reducir el tamano de excision quirurgica en lentigo maligno facial |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Fase 2 | Completado | 90 | ECA evaluando eficacia de imiquimod topico en lesiones intraepiteliales cervicales de alto grado |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Fase 2 | Completado | 5 | Estudio exploratorio de mecanismos inmunitarios y eficacia de imiquimod en VIN 2/3 y verrugas anogenitales |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Fase 3 | Terminado | 9 | ECA de imiquimod topico en CIN de alto grado; terminado prematuramente |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Fase 3 | Desconocido | 145 | Excision quirurgica vs. curetaje + imiquimod en carcinoma basocelular nodular |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Fase temprana 1 | Completado | 16 | Ensayo piloto de imiquimod neoadyuvante (agonista TLR7) en carcinoma escamoso oral en etapa temprana |
| [NCT03057340](https://clinicaltrials.gov/study/NCT03057340) | Fase 1 | Desconocido | 30 | Vacuna con antigeno DRibble en cancer de pulmon avanzado, con imiquimod como coadyuvante |
| [NCT01792505](https://clinicaltrials.gov/study/NCT01792505) | Fase 1 | Completado | 71 | Reseccion quirurgica + vacunacion con celulas dendriticas mas imiquimod en glioma maligno |
| [NCT03872947](https://clinicaltrials.gov/study/NCT03872947) | Fase 1b | Activo, no reclutando | 138 | TRK-950 combinado con multiples regimenes oncologicos, incluyendo crema de imiquimod, en tumores solidos avanzados |
| [NCT04072900](https://clinicaltrials.gov/study/NCT04072900) | Fase 1 | Desconocido | 30 | Vacuna personalizada de neoantigenos + anti-PD-1 en melanoma metastasico, con imiquimod como adyuvante |

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Revision (Cochrane) | Cochrane Database Syst Rev | Intervenciones para neoplasia intraepitelial del canal anal (AIN), condicion premaligna asociada a VPH |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Revision (Cochrane) | Cochrane Database Syst Rev | Tratamientos medicos para neoplasia intraepitelial vulvar (VIN) de alto grado |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Revision | Skin Therapy Lett | Manejo actual de la queratosis actinica, lesion cutanea premaligna |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Revision | Semin Cutan Med Surg | Estrategias topicas para cancer de piel no melanoma y lesiones precursoras, incluyendo imiquimod |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Revision | Int J Mol Sci | Tratamientos combinados con terapia fotodinamica para cancer de piel no melanoma |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinico | Urol Oncol | Farmacocinetica/farmacodinamia de agonistas TLR7 relacionados en modelo de rata |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Reporte de caso | Int J STD AIDS | VIN de alto grado tratado exitosamente con imiquimod 5% en paciente trasplantado renal |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Reporte de caso | Hautarzt | Porokeratosis actinica diseminada superficial con lesiones premalignas cutaneas concomitantes |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Reporte de caso | Int J STD AIDS | Papulosis bowenoide del pene tratada exitosamente con crema de imiquimod 5% |

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
El nivel de evidencia L1 se apoya en un ECA de Fase 3 completado (n=259) y un ECA de Fase 2 completado (n=90) dirigidos directamente a lesiones epiteliales premalignas, junto con una base mecanistica solida y precedente de uso topico de imiquimod en condiciones analogas. Sin embargo, persisten vacios bloqueantes de seguridad (advertencias, contraindicaciones e interacciones no disponibles) que impiden avanzar sin salvaguardas.

**Para avanzar se necesita:**
- Advertencias, contraindicaciones e interacciones farmacologicas (DG001, severidad Blocking — actualmente sin datos)
- Mecanismo de accion detallado via DrugBank (DG002, severidad High)
- Evaluacion de viabilidad regulatoria y comercial en España (actualmente no comercializado, 0 autorizaciones)
- Definicion de la subpoblacion objetivo especifica (CIN vs. VIN vs. AIN) para el diseno de un futuro ensayo confirmatorio
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

