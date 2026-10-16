---
layout: default
title: Procaine
parent: Solo predicción del modelo (L5)
nav_order: 664
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Procaine: nueva indicación predicha, Metahemoglobinemia (nivel de evidencia L5). Indicación original: No disponible en las autorizaciones de la AEMPS (el texto de indicaci…"
monitor_inn: "procaine"
predicted_indications: ["methemoglobinemia", "methemoglobinemia, alpha type", "Tourette syndrome", "anaphylaxis", "methemoglobin reductase deficiency", "hyperthyroidism", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis"]
---

# Procaine
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

# Procaína: De Anestésico Local a Metahemoglobinemia (predicción con dirección adversa)

## Resumen en Una Frase

La procaína es un anestésico local de tipo éster, comercializado en España en solución inyectable (y como componente de una asociación con penicilina). Los datos compilados no incluyen el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **metahemoglobinemia**, pero la literatura disponible (**5 publicaciones**, sin ensayos clínicos) indica que la procaína **provoca** esta condición, por lo que la predicción refleja una asociación adversa y no terapéutica.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en las autorizaciones de la AEMPS (el texto de indicación está vacío). Uso conocido: anestesia local |
| Nueva Indicación Predicha | Metahemoglobinemia |
| Puntaje de Predicción TxGNN | 99,50% |
| Nivel de Evidencia | L4 (solo estudios preclínicos, casos clínicos y de mecanismo; sin ensayos clínicos) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 3 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, la procaína es un anestésico local que bloquea canales de sodio. Las bases farmacológicas también la relacionan con los receptores de rianodina RyR1 y RyR2, aunque sin datos de bioactividad que confirmen un objetivo principal.

**La predicción no parece razonable en sentido terapéutico.** La literatura describe que la procaína (y otros anestésicos locales como la lidocaína) **causa** metahemoglobinemia, principalmente por metabolitos de amina aromática con capacidad oxidante (como el ácido para-aminobenzoico). La puntuación alta de TxGNN refleja una asociación fármaco-enfermedad en el grafo de conocimiento, pero con dirección adversa. No hay evidencia de que la procaína trate la metahemoglobinemia.

Otras predicciones del modelo siguen el mismo patrón: metahemoglobinemia tipo alfa y déficit de metahemoglobina reductasa (donde la procaína empeoraría el cuadro). Las predicciones con cierta plausibilidad analgésica local son fibromialgia y tendinitis. La tendinitis es la que cuenta con más respaldo relativo (nivel L3).

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [5529388](https://pubmed.ncbi.nlm.nih.gov/5529388/) | 1970 | Reporte de caso | Acta physiologica latino americana | Metahemoglobinemia causada por procaína intravenosa |
| [14246695](https://pubmed.ncbi.nlm.nih.gov/14246695/) | 1965 | Reporte de caso | Lancet | Metahemoglobinemia tras el uso de lidocaína |
| [3691245](https://pubmed.ncbi.nlm.nih.gov/3691245/) | 1987 | Estudio observacional clínico | Zhonghua Wai Ke Za Zhi | Efecto de la anestesia con procaína intravenosa sobre los niveles de metahemoglobina |
| [6705717](https://pubmed.ncbi.nlm.nih.gov/6705717/) | 1984 | Revisión | Drugs | Uso racional de anestésicos locales |
| [5644303](https://pubmed.ncbi.nlm.nih.gov/5644303/) | 1968 | Estudio farmacocinético | Am J Obstet Gynecol | Paso de procaína y ácido para-aminobenzoico a través de la placenta humana |

Ninguna de estas publicaciones respalda un efecto terapéutico de la procaína en la metahemoglobinemia.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 37923 | PROCAINA SERRA 10 MG/ML SOLUCION INYECTABLE | Solución inyectable | No disponible |
| 37925 | PROCAINA SERRA 20 MG/ML SOLUCION INYECTABLE | Solución inyectable | No disponible |
| 38676 | BENZETACIL 6.3.3. | Polvo y disolvente para suspensión inyectable | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no proceden del prospecto):** síndrome de QT largo (incluida la forma familiar), torsades de pointes, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, trombocitopenia, lupus eritematoso sistémico, deficiencia de potasio, trastornos hipotensivos, colitis por *Clostridium difficile*, miastenia gravis y enfermedad de la unión neuromuscular, deficiencia de butirilcolinesterasa, enfermedad cardiovascular, bloqueo auriculoventricular, agranulocitosis y neutropenia (incluidas formas congénitas).
- **Interacciones farmacológicas (17 registros):**
  - Mayor: ácido nitroso (Major).
  - Moderadas: sulfasalazina y otros anestésicos locales (lidocaína, benzocaína, cocaína, tetracaína, oxibuprocaína, cinchocaína).
  - Menores: laronidasa, hialuronidasa, doxorrubicina (incluida la liposomal).
  - Dianas farmacológicas: RyR1 y RyR2.
- **Riesgos señalados en la literatura:** metahemoglobinemia, reacciones alérgicas y seudoalérgicas (anafilaxia, síndrome de Hoigné, dermatitis de contacto).

Consultar el prospecto para las advertencias y contraindicaciones oficiales, que no figuran en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal (metahemoglobinemia) tiene dirección adversa: la procaína la induce, no la trata. No hay ensayos clínicos y el nivel de evidencia es L4. Entre las predicciones secundarias, la tendinitis (L3) y la fibromialgia son candidatas a pregunta de investigación por su plausibilidad como analgesia local.

**Para avanzar se necesita:**
- Descartar formalmente la metahemoglobinemia como indicación y registrarla como señal de seguridad.
- Obtener y analizar el prospecto de la AEMPS (indicaciones, advertencias y contraindicaciones).
- Obtener datos del mecanismo de acción desde DrugBank.
- Evaluar con mayor profundidad la tendinitis (estudio de terapia neural de 2022) y la fibromialgia mediante revisión sistemática y ensayos controlados modernos.
- Evaluar la compatibilidad de vía de administración y el riesgo cardiovascular y hematológico en las poblaciones de interés.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

