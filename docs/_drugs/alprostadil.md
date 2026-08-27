---
layout: default
title: Alprostadil
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Alprostadil
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

# Alprostadil: De Cardiopatía Congénita Ductus-Dependiente a Malformación Aórtica

## Resumen en Una Frase

Alprostadil (prostaglandina E1) es un fármaco cuyo uso clínico histórico, descrito extensamente en la literatura incluida en este informe, es mantener la permeabilidad del ductus arterioso en neonatos con cardiopatías congénitas ductus-dependientes. El modelo TxGNN predice que también podría ser relevante para **Malformación Aórtica**, con **2 ensayos clínicos** y **20 publicaciones** que actualmente respaldan esta dirección, aunque en gran parte se trata de práctica clínica ya establecida (uso puente pre-quirúrgico) más que de un estudio dirigido específicamente a esta indicación.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible como dato formal (fármaco no comercializado en España, sin ficha técnica localizada). Según la literatura del pack: mantenimiento de la permeabilidad del ductus arterioso en cardiopatías congénitas ductus-dependientes |
| Nueva Indicación Predicha | Malformación Aórtica (aortic malformation) |
| Puntaje de Predicción TxGNN | 99.98% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | ✗ No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Proceed with Guardrails |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en las fuentes estructuradas consultadas (DrugBank). Según la información recogida en la literatura del pack, alprostadil es la forma sintética de la prostaglandina E1 (PGE1), con efecto vasodilatador sobre el músculo liso, particularmente del ductus arterioso; este efecto ha revolucionado desde finales de los años 70 el manejo de cardiopatías congénitas que dependen de la permeabilidad ductal para mantener el flujo pulmonar o sistémico.

Las malformaciones aórticas congénitas (arco aórtico interrumpido, coartación aórtica, atresia/estenosis aórtica crítica) frecuentemente cursan con fisiología ductus-dependiente: el flujo sistémico distal a la obstrucción depende de un ductus arterioso permeable. Por ello, mantener dicha permeabilidad con alprostadil mientras se prepara la corrección quirúrgica es, mecanísticamente, una extensión directa y ya practicada de su acción farmacológica, más que una indicación completamente nueva.

Esto explica por qué el modelo TxGNN asigna una puntuación muy alta a esta asociación: la literatura muestra un solapamiento sustancial entre "cardiopatía congénita ductus-dependiente" (uso histórico) y "malformación aórtica" (indicación predicha), incluyendo múltiples series de casos y un ensayo clínico de fase 1 evaluando directamente el efecto de alprostadil en el flujo tras cirugía paliativa de cardiopatía univentricular.

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04054115](https://clinicaltrials.gov/study/NCT04054115) | Fase 1 | Terminado | 10 | Efectos agudos de alprostadil sobre el flujo cerebral y pulmonar tras la conexión cavopulmonar bidireccional (segunda etapa de paliación univentricular); evalúa si PGE1 aumenta el flujo pulmonar/cerebral post-quirúrgico |
| [NCT02042092](https://clinicaltrials.gov/study/NCT02042092) | No aplica | Completado | 39 | Comparación de ecografía Doppler color vs. angio-RM en vasculitis sistémica de grandes vasos (incluye aorta); estudio diagnóstico, no evalúa tratamiento con alprostadil |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [26686446](https://pubmed.ncbi.nlm.nih.gov/26686446/) | 2015 | Revisión | Semin Thorac Cardiovasc Surg | La introducción de PGE1 revolucionó el manejo del arco aórtico interrumpido; reparación neonatal en una etapa es el abordaje preferido |
| [32184038](https://pubmed.ncbi.nlm.nih.gov/32184038/) | 2020 | Serie de casos | Asian J Surg | Resultados de reparación quirúrgica escalonada en lactantes con arco aórtico interrumpido |
| [25647388](https://pubmed.ncbi.nlm.nih.gov/25647388/) | 2014 | Revisión | Cardiol Young | Manejo preoperatorio del neonato con estenosis valvular aórtica crítica, incluyendo estabilización con PGE1 |
| [16368373](https://pubmed.ncbi.nlm.nih.gov/16368373/) | 2006 | Serie de casos | Ann Thorac Surg | Valvotomía aórtica transventricular cerrada para estenosis aórtica crítica en neonatos: resultados, factores de riesgo y reoperaciones |
| [31010402](https://pubmed.ncbi.nlm.nih.gov/31010402/) | 2020 | Reporte de caso / revisión | World J Pediatr Congenit Heart Surg | Infusión de prostaglandina en neonato con coartación aórtica grave y ductus cerrado; revisión de la literatura sobre el papel de PGE1 en la coartación incluso sin ductus permeable |
| [9750448](https://pubmed.ncbi.nlm.nih.gov/9750448/) | 1998 | Reporte de caso | Nihon Kyobu Geka Gakkai Zasshi | Reparación exitosa de estenosis aórtica crítica con coartación el primer día de vida |
| [7201134](https://pubmed.ncbi.nlm.nih.gov/7201134/) | 1982 | Serie de casos | Pediatr Cardiol | Infusión de PGE1 en recién nacidos con ventrículo izquierdo hipoplásico y atresia aórtica |
| [6537955](https://pubmed.ncbi.nlm.nih.gov/6537955/) | 1984 | Cohorte | J Am Coll Cardiol | Terapia prolongada con PGE1 en 17 neonatos con cardiopatías congénitas, incluyendo coartación aórtica |
| [26118445](https://pubmed.ncbi.nlm.nih.gov/26118445/) | 2015 | Reporte de caso | Can J Cardiol | Arco aórtico derecho detectado prenatalmente con ductus arterioso bilateral y arterias pulmonares no confluentes |
| [19080093](https://pubmed.ncbi.nlm.nih.gov/19080093/) | 2008 | Estudio clínico | Zhonghua Yi Xue Za Zhi | Efectos de alprostadil y ulinastatina sobre la respuesta inflamatoria y lesión pulmonar tras circulación extracorpórea en cardiopatías congénitas pediátricas |

## Consideraciones de Seguridad

Los campos estructurados de advertencias principales, contraindicaciones e interacciones farmacológicas no están disponibles en las fuentes consultadas (ficha técnica/TFDA no localizada; alprostadil no está comercializado en España, por lo que no existe prospecto local). Esto corresponde a una brecha de datos de severidad "Blocking" para la evaluación de seguridad (DG001).

De forma complementaria, la literatura incluida en este informe describe efectos adversos conocidos asociados al uso prolongado de PGE1 en neonatos: apnea, fiebre, rubefacción, diarrea, irritabilidad; y en uso prolongado, hiperplasia antral con estenosis pilórica hipertrófica y obstrucción de la salida gástrica, necrosis grasa subcutánea e hiperostosis cortical (PMID 23521358, PMID 25263728, PMID 30347623 sobre riesgo de enterocolitis necrotizante con alimentación enteral). Esta información procede de reportes de casos y no sustituye a una ficha técnica oficial.

## Conclusión y Próximos Pasos

**Decisión: Proceed with Guardrails**

**Justificación:**
El uso de alprostadil en fisiología ductus-dependiente asociada a malformaciones aórticas (arco interrumpido, coartación, atresia/estenosis aórtica crítica) está respaldado por décadas de práctica clínica documentada en series de casos, un estudio de cohorte y un ensayo clínico de fase 1 dirigido específicamente a evaluar su efecto hemodinámico post-quirúrgico. Sin embargo, no existe un ensayo de fase 2/3 diseñado específicamente para "malformación aórtica" como indicación formal, y persisten brechas críticas de datos regulatorios y de seguridad.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha técnica de alprostadil (TFDA o AEMPS) para completar la evaluación de seguridad S1 (brecha bloqueante DG001)
- Completar los datos de mecanismo de acción vía API de DrugBank (DG002)
- Clasificar la relevancia clínica ("relevance grade") de los 2 ensayos y 20 publicaciones, actualmente marcados como "pending"
- Confirmar la vía regulatoria aplicable dado que el fármaco no está comercializado en España (uso extranjero/importación)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

