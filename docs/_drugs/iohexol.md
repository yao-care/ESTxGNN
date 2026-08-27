---
layout: default
title: Iohexol
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 2
---

# Iohexol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Iohexol: De Agente de Contraste Radiologico a Insomnio

## Resumen en Una Frase

Iohexol es un agente de contraste yodado no ionico, utilizado en radiologia diagnostica (mielografia, angiografia, tomografia computarizada) sin actividad farmacologica sistemica conocida. El modelo TxGNN predice con puntuaciones muy altas una posible utilidad en **insomnio** (99.87%) y, en segundo lugar, en **ansiedad** (99.25%), pero **no existe ningun ensayo clinico ni publicacion que respalde un uso terapeutico real** en ninguna de las dos indicaciones — toda la evidencia disponible corresponde al uso del propio agente de contraste en contextos diagnosticos no relacionados.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Agente de contraste radiologico (mielografia, TC, angiografia) — sin uso farmacologico sistemico |
| Nueva Indicacion Predicha | Insomnio |
| Puntaje de Prediccion TxGNN | 99.87% |
| Nivel de Evidencia | L5 |
| Estado de Mercado | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

*Nota: existe una segunda indicacion predicha por el mismo modelo, **ansiedad** (score 99.25%, tambien L5/Hold), detallada mas abajo por su relevancia adicional.*

---

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion (MOA) farmacodinamico de iohexol. Segun la informacion disponible, iohexol es un agente de contraste yodado no ionico utilizado exclusivamente con fines de diagnostico por imagen, sin actividad conocida sobre dianas del sistema nervioso central (GABA, serotonina u otras) relacionadas con el sueno o la ansiedad.

No se identifica una relacion mecanistica plausible entre el uso original de iohexol (diagnostico por imagen) y las indicaciones predichas (insomnio, ansiedad). La puntuacion elevada de TxGNN probablemente refleja una asociacion indirecta dentro del grafo de conocimiento — por ejemplo, pacientes sometidos a pruebas de imagen con iohexol que tambien presentan diagnosticos de insomnio o ansiedad por otras causas, sin relacion causal ni terapeutica real.

La revision de los ensayos y publicaciones asociadas a la indicacion de ansiedad confirma esta hipotesis: en todos los casos, iohexol aparece unicamente como herramienta diagnostica (p. ej., medicion de tasa de filtracion glomerular) y nunca como intervencion terapeutica. La conclusion del equipo de evaluacion es que ambas predicciones representan muy probablemente **ruido del modelo (falso positivo)**.

---

## Evidencia de Ensayos Clinicos

### Insomnio (Rank 1)
Actualmente no hay ensayos clinicos relacionados registrados.

### Ansiedad (Rank 2)

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01053130](https://clinicaltrials.gov/study/NCT01053130) | N/A | Completado | 16 | Cirugia bariatrica y preservacion de funcion renal en ERC estadios 3-4; iohexol usado solo como marcador de filtracion glomerular, sin relacion con ansiedad |
| [NCT01629537](https://clinicaltrials.gov/study/NCT01629537) | Fase 2 | Completado | 41 | Bloqueo del ganglio estrellado para TEPT; sin vinculo con iohexol como tratamiento de ansiedad |
| [NCT02864706](https://clinicaltrials.gov/study/NCT02864706) | Fase 4 | Completado | 95 | Seguimiento a largo plazo de everolimus en trasplante cardiaco; sin relacion con ansiedad |
| [NCT03736005](https://clinicaltrials.gov/study/NCT03736005) | N/A | Completado | 40 | Perdida de masa muscular y disfuncion renal tras enfermedad critica; iohexol como marcador de funcion renal, no terapeutico |
| [NCT05428631](https://clinicaltrials.gov/study/NCT05428631) | N/A | Reclutando | 10 | Evaluacion del dispositivo CardioMEMS en sindrome cardiorrenal; sin relacion con ansiedad |
| [NCT00634920](https://clinicaltrials.gov/study/NCT00634920) | Fase 4 | Completado | 204 | Conversion a everolimus en trasplante renal de novo; sin relacion con ansiedad |

**Ninguno de estos ensayos evalua iohexol como tratamiento de la ansiedad**; su presencia se debe a su uso como marcador diagnostico de funcion renal (aclaramiento/GFR) en poblaciones con comorbilidades diversas.

---

## Evidencia de Literatura

### Insomnio (Rank 1)
Actualmente no hay literatura relacionada disponible.

### Ansiedad (Rank 2)

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [2352635](https://pubmed.ncbi.nlm.nih.gov/2352635/) | 1990 | Cohorte | Neuroradiology | Efectos secundarios de mielografia lumbar con iohexol; la ansiedad se menciona como sintoma mental transitorio post-procedimiento, no como indicacion tratada |
| [8883531](https://pubmed.ncbi.nlm.nih.gov/8883531/) | 1996 | ECA | Academic Radiology | Comparacion de iodixanol vs iohexol en flebografia de extremidades; no aborda ansiedad |
| [2125805](https://pubmed.ncbi.nlm.nih.gov/2125805/) | 1990 | Cohorte | Acta Neurochirurgica | Monitorizacion Doppler transcraneal en angiografia cerebral; sin relacion con ansiedad |
| [39861464](https://pubmed.ncbi.nlm.nih.gov/39861464/) | 2025 | Revision | Nutrients | Actividad fisica y nutricion en onco-nefrologia; menciona reduccion de ansiedad como beneficio general de la actividad fisica, no de iohexol |
| [16034655](https://pubmed.ncbi.nlm.nih.gov/16034655/) | 2005 | Cohorte | Cardiovasc Intervent Radiol | Colocacion de filtro de vena cava en ancianos; la ansiedad del paciente se menciona como factor logistico, no como resultado tratado |
| [25690708](https://pubmed.ncbi.nlm.nih.gov/25690708/) | 2015 | Cohorte | La Radiologia Medica | Hernia hiatal incidental en TC con enema de agua; menciona ansiedad diagnostica derivada de hallazgos incidentales, no relacionada con tratamiento farmacologico |

**Ninguna de estas publicaciones estudia iohexol como tratamiento de la ansiedad**; las menciones de "ansiedad" son incidentales (sintoma peri-procedimiento o del paciente durante pruebas de imagen).

---

## Informacion de Mercado

Iohexol **no esta actualmente comercializado**: no se registran autorizaciones de comercializacion en los datos disponibles (0 licencias).

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Ambas indicaciones predichas (insomnio, ansiedad) presentan nivel de evidencia L5 — puntuacion alta del modelo TxGNN sin ningun ensayo clinico ni literatura que respalde un efecto terapeutico real. La revision manual de toda la evidencia disponible para ansiedad confirma que se trata de asociaciones indirectas (iohexol como marcador diagnostico, no como tratamiento), lo que sugiere que ambas predicciones son muy probablemente ruido del modelo (falso positivo) mas que una senal biologica plausible.

**Para avanzar se necesita:**
- Advertencias y contraindicaciones oficiales del TFDA (brecha bloqueante DG001) para poder completar la evaluacion de seguridad S1
- Datos del mecanismo de accion (MOA) de iohexol (brecha DG002) para confirmar o descartar definitivamente cualquier plausibilidad mecanistica
- Dado el perfil de evidencia actual, no se recomienda invertir mas recursos en esta direccion salvo que aparezcan nuevos datos mecanisticos o clinicos que la respalden
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

