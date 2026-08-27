---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 150
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

Usando la estructura de la plantilla, con dos adaptaciones justificadas por los propios datos: (1) el paquete es explícitamente "multi" e incluye 3 indicaciones predichas con evidencia real en literatura para las indicaciones #2 y #3 — omitirlas habría descartado la información más relevante del pack; (2) `original_indications` y `original_moa` están vacíos, así que la "indicación original" se toma del propio texto de `repurposing_rationale` (que identifica el fármaco como agente de contraste), no de una suposición.

---

# Iodixanol: De Agente de Contraste (TC) a Osteoarthritis Susceptibility (predicción sin evidencia)

## Resumen en Una Frase

Iodixanol es un agente de contraste yodado no iónico utilizado en tomografía computarizada, sin indicación terapéutica registrada ni datos de MOA disponibles.
El modelo TxGNN predice que podría ser efectivo para **Osteoarthritis Susceptibility** (puntaje 99.16%),
pero actualmente **no existe ningún ensayo clínico ni publicación** que respalde directamente esta indicación; las dos predicciones relacionadas (osteoartritis, artritis reumatoide) solo cuentan con literatura de imagenología/casos clínicos que no aborda un uso terapéutico.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Agente de contraste (TC) — no se dispone de indicacion terapeutica ni de licencias registradas |
| Nueva Indicacion Predicha | Osteoarthritis Susceptibility |
| Puntaje de Prediccion TxGNN | 99.16% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion. Segun la informacion disponible en el propio Evidence Pack, iodixanol es un agente de contraste yodado no ionico (radiocontrast agent) usado en TC, sin indicacion terapeutica ni MOA farmacologico documentado — es decir, no es un farmaco de tratamiento sino una herramienta diagnostica.

Las tres indicaciones predichas por TxGNN (osteoarthritis susceptibility, osteoarthritis, rheumatoid arthritis) comparten un patron: la literatura disponible no describe a iodixanol tratando estas enfermedades, sino **utilizandolo como herramienta de imagen** en estudios de cartilago articular (micro-CT, nanoparticle diffusion imaging, modelos de elementos finitos), o bien describe reacciones alergicas al contraste en pacientes que ya tenian artritis reumatoide. El puntaje alto de TxGNN (>99%) probablemente refleja la co-ocurrencia frecuente de "agente de contraste" y "enfermedad articular" en la literatura biomedica, no una senal terapeutica real.

Para la indicacion de mayor rango (osteoarthritis susceptibility) no existe ningun ensayo clinico ni publicacion en absoluto — es una prediccion puramente algoritmica sin ningun tipo de evidencia indirecta.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados para ninguna de las tres indicaciones predichas (osteoarthritis susceptibility, osteoarthritis, rheumatoid arthritis).

## Evidencia de Literatura

### Osteoarthritis Susceptibility (rank 1, indicacion principal)

Actualmente no hay literatura relacionada disponible.

### Osteoarthritis (rank 2)

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [40155520](https://pubmed.ncbi.nlm.nih.gov/40155520/) | 2025 | Imagenologia/Metodos | Annals of Biomedical Engineering | Uso de contraste dual (nanoparticula + molecular) en TC de conteo de fotones para evaluar salud del cartilago articular |
| [39012563](https://pubmed.ncbi.nlm.nih.gov/39012563/) | 2024 | Imagenologia/Metodos | Annals of Biomedical Engineering | Imagen de difusion de nanoparticulas por TC y modelo de elementos finitos para evaluar funcion del cartilago |
| [30145230](https://pubmed.ncbi.nlm.nih.gov/30145230/) | 2018 | Ciencia Basica (ex vivo) | Osteoarthritis and Cartilage | Rigidez del cartilago condilar mandibular en caballos segun edad |
| [28518064](https://pubmed.ncbi.nlm.nih.gov/28518064/) | 2017 | Ciencia Basica (modelo FE) | J Vis Exp | Protocolo experimental y de elementos finitos para transporte de solutos neutros/cargados en cartilago articular |
| [28063646](https://pubmed.ncbi.nlm.nih.gov/28063646/) | 2017 | Ciencia Basica (modelo FE) | J Biomechanics | Transporte de solutos en la interfaz cartilago-hueso subcondral usando iodixanol como trazador de difusion en TC |
| [30374787](https://pubmed.ncbi.nlm.nih.gov/30374787/) | 2018 | In vitro | J Experimental Orthopaedics | Los agentes de contraste yodados no afectan la funcion plaquetaria de PRP en fase temprana in vitro |
| [27793406](https://pubmed.ncbi.nlm.nih.gov/27793406/) | 2016 | Ciencia Basica (modelo FE) | J Biomechanics | Transporte de solutos neutros en la interfaz osteocondral mediante TC y modelado biphasic-solute |

*Nota: todos estos estudios usan iodixanol como herramienta de imagen/trazador para investigar el cartilago, no como tratamiento de la osteoartritis.*

### Rheumatoid Arthritis (rank 3)

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [36628042](https://pubmed.ncbi.nlm.nih.gov/36628042/) | 2022 | Reporte de caso | Cureus | Desensibilizacion exitosa al contraste iohexol en paciente con amiloidosis secundaria a artritis reumatoide; describe manejo de reaccion alergica al contraste, no tratamiento de la AR |

## Informacion de Mercado en Espana

Iodixanol no esta comercializado en Espana (0 autorizaciones registradas en los datos disponibles).

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad. (No hay datos de advertencias, contraindicaciones ni interacciones farmacologicas en el Evidence Pack; la busqueda en TFDA sobre alertas/contraindicaciones esta marcada como bloqueante y pendiente de resolucion.)

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Las tres direcciones predichas por TxGNN carecen de evidencia terapeutica real: la indicacion de mayor puntaje (osteoarthritis susceptibility) no tiene ningun ensayo ni publicacion, y las otras dos solo cuentan con literatura donde iodixanol aparece como herramienta de imagen o como causante de alergia al contraste, no como tratamiento. Dado que iodixanol es un agente de contraste diagnostico sin indicacion terapeutica de base, la plausibilidad mecanistica de reposicionamiento es baja.

**Para avanzar se necesita:**
- Resolver el data gap bloqueante (DG001): obtener el prospecto/advertencias TFDA para poder pasar a la evaluacion de seguridad S1
- Resolver el data gap de alta prioridad (DG002): datos de MOA via DrugBank API para evaluar plausibilidad mecanistica
- Confirmar si existe alguna hipotesis farmacologica (no solo de imagen) que vincule iodixanol con modulacion de la enfermedad articular, antes de invertir en busqueda adicional de evidencia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

