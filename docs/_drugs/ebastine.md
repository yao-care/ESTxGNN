---
layout: default
title: Ebastine
parent: Solo predicción del modelo (L5)
nav_order: 190
evidence_level: L5
indication_count: 2
---

# Ebastine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **2** 
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

# Ebastina: De Antihistamínico H1 a Enfermedad de las Arterias Coronarias

## Resumen en Una Frase

Ebastina es un antihistamínico H1 comercializado en España. Los datos disponibles no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectiva para **enfermedad de las arterias coronarias** (y, en segundo lugar, **isquemia miocárdica**).
Actualmente no hay **ningún ensayo clínico** y solo **1 publicación** (un estudio computacional) respalda esta dirección.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No registrada en los datos de AEMPS (ebastina es un antihistamínico H1) |
| Nueva Indicación Predicha | Enfermedad de las arterias coronarias |
| Puntaje de Predicción TxGNN | 99,18% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, ebastina es un antihistamínico H1, pero no existe un mecanismo establecido que vincule el bloqueo H1 con un beneficio en la enfermedad coronaria.

El único vínculo identificado es indirecto. Un estudio computacional sobre la enzima CYP2J2, presente en tejido cardiovascular y que metaboliza ebastina, describe una interacción metabólica. CYP2J2 produce ácidos epoxieicosatrienoicos (EET), que se estudian en cardioprotección. Por eso la unión de ebastina a CYP2J2 podría alterar la señalización de los EET, pero se desconoce en qué dirección, si beneficiosa o perjudicial.

La predicción es, por tanto, una hipótesis del grafo de conocimiento y no un hallazgo terapéutico. La segunda indicación predicha, **isquemia miocárdica** (puntaje 99,10%), se apoya en la misma publicación, por lo que ambas evidencias no son independientes.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | Estudio in silico | Proteins | Modelado por homología, dinámica molecular y acoplamiento (docking) de ligandos en CYP2J2 humano. No incluye resultados de isquemia ni datos de eficacia o seguridad en pacientes o modelos cardíacos. |

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 78558 | Ebastina Ratiopharm 10 mg comprimidos bucodispersables EFG | Comprimido bucodispersable |
| 68663 | Alastina 20 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 67663 | Ebastina Tarbis 10 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 80256 | Ebastina Flas Stada 10 mg comprimidos bucodispersables EFG | Comprimido bucodispersable |
| 74992 | Ebastina Teva-Ratiopharm 20 mg comprimidos bucodispersables EFG | Comprimido bucodispersable |

Se muestran 5 de las 20 autorizaciones. Los datos no incluyen el texto de indicación aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa solo en el modelo TxGNN y en un único estudio computacional que describe una interacción metabólica, no un efecto terapéutico. No hay ensayos clínicos, no hay un mecanismo plausible establecido y la dirección del efecto es desconocida.

**Para avanzar se necesita:**
- Prospecto de AEMPS (advertencias y contraindicaciones), que es un bloqueo para el cribado de seguridad
- Datos del mecanismo de acción (por ejemplo, desde DrugBank)
- Estudios preclínicos que muestren el efecto de ebastina sobre la vía CYP2J2/EET en tejido cardiovascular y su dirección
- Texto de la indicación aprobada para analizar la relación con la indicación original
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

