---
layout: default
title: Diflunisal
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Diflunisal
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

# Diflunisal: De Antiinflamatorio no Esteroideo (AINE) a Espondilitis Anquilosante

> **Nota metodologica:** Este Evidence Pack contiene 10 indicaciones candidatas. La de mayor puntaje TxGNN (rango #1, "acromesomelic dysplasia, Hunter-Thompson type") esta senalada por el propio analisis mecanistico como probable falso positivo por agrupamiento fenotipico de enfermedades oseas, sin ningun ensayo clinico ni literatura de respaldo (L5, Hold). Este informe se centra en cambio en la **Espondilitis Anquilosante** (rango #5), la unica candidata con evidencia clinica real y nivel L2.

## Resumen en Una Frase

Diflunisal es un antiinflamatorio no esteroideo (AINE) derivado del acido salicilico. El modelo TxGNN predice que podria ser efectivo para **Espondilitis Anquilosante**, respaldado por **1 ensayo clinico controlado aleatorizado (1986)** y **7 publicaciones** en total, aunque actualmente el farmaco no esta comercializado en Espana.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible en los datos suministrados (Diflunisal no esta comercializado en Espana; sin licencias ni indicacion aprobada registrada) |
| Nueva Indicacion Predicha | Espondilitis Anquilosante |
| Puntaje de Prediccion TxGNN | 99.98% |
| Nivel de Evidencia | L2 |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Proceed with Guardrails |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de una ficha tecnica detallada del mecanismo de accion de diflunisal en los datos suministrados. Segun la informacion recogida en la evidencia de respaldo, diflunisal es un AINE derivado del acido salicilico cuyo mecanismo conocido es la inhibicion de las enzimas COX-1/COX-2, reduciendo la sintesis de prostaglandinas y con ello el dolor y la inflamacion.

La espondilitis anquilosante (EA) es una espondiloartropatia inflamatoria cronica cuyo tratamiento de primera linea son precisamente los AINEs. La extension de diflunisal a esta indicacion no es una inferencia cruzada entre categorias de enfermedad distantes, sino una extension dentro de la misma clase farmacologica ya establecida (los AINEs se usan de forma rutinaria en EA).

Esto se confirma con evidencia directa: un ensayo clinico aleatorizado doble ciego de 1986 comparo diflunisal frente a fenilbutazona en 38 pacientes varones con EA activa, mostrando eficacia comparable, con un efecto analgesico inicial mas rapido y pronunciado con diflunisal. Estudios de seguimiento del mismo grupo de investigadores documentaron ademas el impacto del tratamiento sobre marcadores de actividad de enfermedad (IgA serica) y funcion pulmonar en esta poblacion.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados (busquedas en ClinicalTrials.gov e ICTRP para diflunisal + espondilitis anquilosante devolvieron 0 resultados).

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [3524970](https://pubmed.ncbi.nlm.nih.gov/3524970/) | 1986 | ECA | Clinical rheumatology | Ensayo doble ciego aleatorizado (12 sem + extension abierta 36 sem) en 38 varones con EA: diflunisal 500 mg 2x/dia vs. fenilbutazona 200 mg 2x/dia; ambos eficaces, diflunisal con inicio analgesico mas rapido |
| [4062389](https://pubmed.ncbi.nlm.nih.gov/4062389/) | 1985 | Cohorte | Annals of the rheumatic diseases | Estudio prospectivo de 48 semanas en 38 pacientes con EA activa (diflunisal o fenilbutazona): IgA serica correlaciono con expansion toracica e indice de flexion lumbar |
| [3546687](https://pubmed.ncbi.nlm.nih.gov/3546687/) | 1986 | Cohorte | The Journal of rheumatology | 33 varones con EA activa, diseno doble ciego (diflunisal vs. fenilbutazona, 12 sem + extension 36 sem): evaluo funcion pulmonar (capacidad vital) segun actividad de enfermedad y tratamiento |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Revision | Clinical pharmacy | Revision de diclofenaco sodico (otro AINE) como referencia de clase: farmacologia, eficacia y uso en enfermedad reumatica |
| [6772422](https://pubmed.ncbi.nlm.nih.gov/6772422/) | 1980 | Revision | Drugs | Revision de diclofenaco sodico en enfermedades reumaticas, incluyendo espondilitis anquilosante, como evidencia de clase AINE |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Revision | Drugs | Revision de naproxeno (AINE) en enfermedad reumatica; evidencia de clase, no especifica de diflunisal |
| [3539573](https://pubmed.ncbi.nlm.nih.gov/3539573/) | 1986 | Revision | Drugs | Revision de pirprofeno (AINE) como alternativa terapeutica en espondilitis anquilosante y trastornos musculoesqueleticos |

*Nota: los 4 ultimos articulos son revisiones sobre otros AINEs (diclofenaco, naproxeno, pirprofeno) usados como evidencia de clase farmacologica en EA, no ensayos de diflunisal.*

## Informacion de Mercado en Espana

Diflunisal no esta actualmente comercializado en Espana (0 autorizaciones registradas en los datos disponibles; sin fichas de producto que listar).

## Consideraciones de Seguridad

No se dispone de datos de seguridad especificos (advertencias, contraindicaciones e interacciones aparecen sin informacion en las fuentes consultadas, y no existe ficha tecnica AEMPS al no estar comercializado en Espana). Consultar el prospecto/ficha tecnica internacional del producto antes de cualquier uso.

## Conclusion y Proximos Pasos

**Decision: Proceed with Guardrails**

**Justificacion:**
Existe un ensayo clinico controlado aleatorizado (1986) que muestra eficacia de diflunisal en espondilitis anquilosante frente a un comparador activo, respaldado por dos estudios observacionales adicionales del mismo grupo y por evidencia de clase (otros AINEs ya usados en EA). Sin embargo, la evidencia es antigua (anos 80), diflunisal no esta comercializado en Espana, y faltan datos criticos de seguridad y mecanismo de accion — por lo que no se recomienda avanzar sin salvaguardas adicionales.

**Para avanzar se necesita:**
- Ficha tecnica/prospecto oficial con advertencias y contraindicaciones (actualmente gap bloqueante, DG001)
- Mecanismo de accion detallado via DrugBank API (actualmente gap de alta prioridad, DG002)
- Evaluacion de la via de registro o importacion, dado que el farmaco no esta comercializado en Espana
- Busqueda actualizada de ensayos clinicos recientes (la evidencia disponible data de hace ~40 anos)
- Perfil de interacciones farmacologicas (DDI), actualmente sin resultados ("not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

