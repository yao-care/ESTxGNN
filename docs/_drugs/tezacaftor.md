---
layout: default
title: Tezacaftor
parent: Solo predicción del modelo (L5)
nav_order: 788
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
description: "Tezacaftor: nueva indicación predicha, Infección por VIH (nivel de evidencia L5). Indicación original: Fibrosis quística"
monitor_inn: "tezacaftor"
predicted_indications: ["HIV infectious disease", "leprosy", "multiple endocrine neoplasia"]
---

# Tezacaftor
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

## Tezacaftor: De Fibrosis Quística a Infección por VIH
{: .text-alpha }

## Resumen en Una Frase

Tezacaftor es un corrector de la proteína CFTR, originalmente utilizado para el tratamiento de la fibrosis quística, tanto en combinación con ivacaftor (Symkevi) como en terapias triples (Kaftrio, Alyftrek).
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección; se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Fibrosis quística |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 0,9924 |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | Comercializado (autorizaciones comercializadas: 8 de 8) |
| Número de Autorizaciones | 8 (comercializadas: 8) |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Según la sección «Mechanism of Action» de la información de prescripción aprobada por la FDA de EE. UU. (Prescribing Information) para vanzacaftor, tezacaftor, and deutivacaftor (combinación que contiene Tezacaftor) (traducción no oficial): «Vanzacaftor y tezacaftor se unen a distintos sitios de la proteína CFTR y tienen un efecto aditivo al facilitar el procesamiento celular y el tráfico de determinadas formas mutantes de CFTR (incluida F508del- CFTR), lo que aumenta la cantidad de proteína CFTR que llega a la superficie celular en comparación con cualquiera de las dos moléculas por separado. El efecto combinado de vanzacaftor, tezacaftor y deutivacaftor es un aumento de la cantidad y la función de CFTR en la superficie celular, lo que da lugar a un aumento de la actividad de CFTR, medida tanto por el transporte de cloruro mediado por CFTR in vitro como por el cloruro en el sudor en pacientes con FQ.» Texto original en inglés: "Vanzacaftor and tezacaftor bind to different sites on the CFTR protein and have an additive effect in facilitating the cellular processing and trafficking of select mutant forms of CFTR (including F508del- CFTR) to increase the amount of CFTR protein delivered to the cell surface compared to either molecule alone. The combined effect of vanzacaftor, tezacaftor and deutivacaftor is increased quantity and function of CFTR at the cell surface, resulting in increased CFTR activity as measured both by CFTR-mediated chloride transport in vitro and by sweat chloride in patients with CF." ([DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20), versión del 2026-08-26; consultado el 2026-11-19). Según el conocimiento farmacológico general, tezacaftor es un corrector de CFTR: mejora el plegamiento de la proteína CFTR y su transporte a la superficie celular. Su eficacia en fibrosis quística, en pacientes con determinadas mutaciones del gen CFTR, es conocida.

No se identifica un vínculo mecanístico plausible con el VIH. Tezacaftor no tiene actividad antiviral conocida ni una conexión evidente con la patogénesis del VIH. El puntaje elevado (0,9924) proviene del modelo TxGNN (aprendizaje profundo) y puede reflejar similitudes que el modelo aprendió entre enfermedades relacionadas, no evidencia biológica; no hay ensayos clínicos ni literatura que lo corroboren.

Cualquier hipótesis tendría que evaluarse primero in vitro. Por ello, esta predicción debe considerarse exploratoria y de baja confianza mecanística.

**Otras predicciones del modelo** (también con nivel de evidencia L5, sin ensayos ni literatura, y recomendación Hold):

| Posición | Nueva indicación | Puntaje TxGNN | Comentario |
|------|------|------|------|
| 2 | Lepra | 0,9914 | Sin actividad conocida frente a *Mycobacterium leprae* ni sobre vías inmunes específicas de la lepra |
| 3 | Neoplasia endocrina múltiple | 0,9906 | Enfermedad por mutaciones germinales (p. ej., MEN1, RET) sin relación conocida con la acción correctora de CFTR |

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 1181306001 | Symkevi 100 mg/150 mg | Comprimido recubierto con película |
| 1181306002 | Symkevi 50 mg/75 mg | Comprimido recubierto con película |
| 1201468001 | Kaftrio 75 mg/50 mg/100 mg | Comprimido recubierto con película |
| 1201468002 | Kaftrio 37,5 mg/25 mg/50 mg | Comprimido recubierto con película |
| 1201468003 | Kaftrio 60 mg/40 mg/80 mg | Granulado en sobre |

Se muestran 5 de las 8 autorizaciones vigentes (todas del titular Vertex Pharmaceuticals (Ireland) Limited); las restantes corresponden a Kaftrio 75 mg/50 mg/100 mg granulado y a Alyftrek (50/20/4 mg y 125/50/10 mg). El texto de indicación aprobada no figura en los datos compilados para este informe.

## Consideraciones de Seguridad

- **Interacciones farmacológicas**: la consulta se completó y solo registra una interacción de tipo farmacológico con la diana CFTR, que corresponde a su mecanismo de acción y no a una interacción clínica relevante con otros fármacos.

No se dispone de advertencias ni contraindicaciones del prospecto. Consultar el prospecto para información de seguridad completa.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para VIH se basa únicamente en el modelo (nivel L5), sin ensayos clínicos, literatura ni vínculo mecanístico plausible entre la corrección de CFTR y la infección por VIH.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y una hipótesis mecanística explícita que conecte tezacaftor con la biología del VIH
- Estudios in vitro de actividad antiviral o de modulación de la respuesta del huésped
- Revisión de la ficha técnica de la AEMPS (advertencias y contraindicaciones) antes de cualquier evaluación de seguridad
- Evaluación de compatibilidad de vía de administración y similitud con la indicación original, hoy pendientes

<!-- review:begin log -->

## Registro de revisión

A continuación, el registro de verificación de esta página. La frase que indicaba que no había datos sobre el mecanismo de acción se sustituyó por un extracto de la información de prescripción oficial citada (con traducción no oficial); las predicciones del modelo, los niveles de evidencia y las conclusiones no se reescribieron.

| Fecha de revisión | Elemento | Acción | Fuente |
|------|------|------|------|
| 2026-11-19 | Frase «no se dispone de datos del mecanismo de acción» sustituida por un extracto de la ficha técnica de EE. UU. | Frase sobre la falta de datos del mecanismo de acción sustituida por un extracto con fuente | [DailyMed: Alyftrek (vanzacaftor, tezacaftor, and deutivacaftor) prescribing information, Vertex Pharmaceuticals Incorporated](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7e635909-c6fd-4f0d-ae77-cdff03653a20) |

<!-- review:end log -->

## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

