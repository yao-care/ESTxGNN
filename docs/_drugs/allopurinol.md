---
layout: default
title: Allopurinol
parent: Evidencia moderada (L3-L4)
nav_order: 39
evidence_level: L4
indication_count: 10
---

# Allopurinol
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **10** 
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

# Alopurinol: De Gota a Porfiria Hepática

## Resumen en Una Frase

Alopurinol es un inhibidor de la xantina oxidasa, utilizado originalmente para el tratamiento de la gota y la hiperuricemia.
El modelo TxGNN predice que podría ser efectivo para **porfiria hepática**,
pero actualmente no hay ensayos clínicos y solo **2 publicaciones** indirectas (una hipótesis y un estudio en ratas), por lo que la evidencia es muy limitada.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Gota (según las indicaciones originales del grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Porfiria hepática |
| Puntaje de Predicción TxGNN | 99,95 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, alopurinol inhibe la xantina deshidrogenasa/oxidasa (gen *XDH*), enzima que genera ácido úrico; su eficacia en gota, hiperuricemia y nefropatía aguda por uratos está establecida.

La relación con la porfiria hepática es **indirecta y especulativa**. Las dos publicaciones recuperadas tratan sobre la regulación de la 5-aminolevulinato sintasa (ALAS) y el metabolismo del hemo: una hipótesis sobre el uso de triptófano o inhibidores de la utilización del hemo, y un estudio en rata sobre carbamazepina, que exacerba las porfirias. Ninguna evalúa alopurinol como tratamiento. En la literatura antigua se ha descrito que alopurinol puede afectar el metabolismo hepático del hemo en modelos animales, pero no existen datos clínicos en humanos que respalden un beneficio.

Además, la dirección del efecto es incierta: alopurinol se ha discutido como un posible agente que perturba el hemo o es porfirinogénico, por lo que podría empeorar la enfermedad. El puntaje alto de TxGNN es solo una predicción computacional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hipótesis/Revisión | Medical Hypotheses | Propone el control metabólico de la ALAS hepática mediante triptófano o inhibidores de la utilización del hemo por la triptófano 2,3-dioxigenasa como terapia de las porfirias hepáticas agudas; no evalúa alopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Estudio animal (rata) | Biochemical Pharmacology | Carbamazepina a dosis muy bajas actúa como exacerbador de porfirias al alterar el metabolismo del hemo hepático |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 81288 | Alopurinol Bluefish 300 mg comprimidos EFG | Comprimido | No disponible |
| 63478 | Alopurinol Cinfa 300 mg comprimidos EFG | Comprimido | No disponible |
| 69156 | Alopurinol Teva 100 mg comprimidos EFG | Comprimido | No disponible |
| 56360 | Zyloric 300 mg comprimidos | Comprimido | No disponible |
| 43775 | Zyloric 100 mg comprimidos | Comprimido | No disponible |

Se muestran 5 de las 20 autorizaciones vigentes (todas de principio activo único, ninguna cancelada).

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del texto del prospecto): enfermedad hepática, enfermedad de la vesícula biliar, insuficiencia renal, vasculitis por hipersensibilidad, angeítis leucocitoclástica cutánea, vasculitis cutánea alérgica y enfermedad antimembrana basal glomerular.
- **Interacciones farmacológicas**: la consulta no identificó interacciones con otros fármacos; únicamente se registra su diana farmacológica, la xantina deshidrogenasa (XDH).
- **Aspectos específicos de esta indicación**: la enfermedad hepática figura entre las contraindicaciones del grafo, y la porfiria hepática es una enfermedad del hígado en la que alopurinol podría ser porfirinogénico. Esto exige especial cautela.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en un puntaje computacional y en dos publicaciones indirectas, sin ensayos clínicos ni datos en humanos, y existe riesgo de que el efecto sea contrario al deseado. Otras predicciones del modelo (p. ej., hipertensión portal, síndrome hepatopulmonar, miopatías inflamatorias) carecen de toda evidencia (L5) y tampoco justifican avanzar.

**Para avanzar se necesita:**
- Datos detallados del mecanismo de acción (MOA).
- Estudios preclínicos que evalúen directamente el efecto de alopurinol sobre la ALAS y el metabolismo del hemo, incluido su potencial porfirinogénico.
- Revisión de las advertencias y contraindicaciones del prospecto de la AEMPS.
- Una evaluación de seguridad específica para pacientes con enfermedad hepática antes de considerar cualquier estudio clínico.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

