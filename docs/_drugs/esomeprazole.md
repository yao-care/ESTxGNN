---
layout: default
title: Esomeprazole
parent: Evidencia moderada (L3-L4)
nav_order: 212
evidence_level: L4
indication_count: 3
---

# Esomeprazole
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

# Esomeprazol: De Trastornos Relacionados con el Ácido Gástrico a Reflujo Duodenogástrico

## Resumen en Una Frase

Esomeprazol es un inhibidor de la bomba de protones (IBP) utilizado para reducir la acidez gástrica en el reflujo gastroesofágico y otras causas de exceso de ácido en el estómago.
El modelo TxGNN predice que podría ser efectivo para **reflujo duodenogástrico**, pero actualmente hay **0 ensayos clínicos** y **1 publicación** (una revisión general sobre IBP, sin datos específicos de esta enfermedad) que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Exceso de ácido gástrico y enfermedad por reflujo gastroesofágico (según datos de farmacología; los textos de indicación de AEMPS están vacíos en el registro) |
| Nueva Indicación Predicha | Reflujo duodenogástrico |
| Puntaje de Predicción TxGNN | 99,53 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el registro de origen. Según la información farmacológica disponible, esomeprazol (el isómero S del omeprazol) actúa sobre la bomba de protones gástrica (H+/K+-ATPasa, gen *ATP4A*), reduce la secreción de ácido y se usa en enfermedades relacionadas con el ácido gástrico.

El reflujo duodenogástrico consiste en el retorno de contenido duodenal (bilis y secreciones pancreáticas) al estómago. Su causa de fondo es la incompetencia del píloro o alteraciones de la motilidad. Esomeprazol no actúa sobre esas causas. Solo podría aliviar síntomas cuando existe un componente mixto de reflujo ácido y biliar con gastritis.

Por ello, la relación mecanística es **indirecta**. El puntaje alto del modelo (0,995) no está respaldado por ningún ensayo clínico ni estudio específico de la enfermedad.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Revisión | European Journal of Clinical Pharmacology | Actualización sobre el uso clínico y la farmacocinética de los IBP: primera elección en úlcera péptica, infección por *H. pylori*, ERGE, lesiones por AINE y síndrome de Zollinger-Ellison. No trata el reflujo duodenogástrico. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 81148 | Esomeprazol Cipla 40 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente |
| 72702 | Esomeprazol Teva 40 mg cápsulas duras gastrorresistentes EFG | Cápsula dura gastrorresistente |
| 66038 | Nexium 40 mg polvo para solución inyectable y para perfusión | Polvo para solución inyectable y para perfusión |
| 63940 | Axiago 20 mg comprimidos gastrorresistentes | Comprimido gastrorresistente |
| 85415 | Esomeprazol Mylan Genéricos 40 mg comprimidos gastrorresistentes EFG | Comprimido gastrorresistente |

Se muestran 5 de las 20 autorizaciones vigentes. También existen formas de granulado para suspensión oral y cápsula gastrorresistente.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

Interacciones farmacológicas: el registro solo contiene el objetivo farmacológico del esomeprazol (*ATP4A*, la bomba de protones gástrica). No incluye interacciones con otros medicamentos.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (L4). No hay ensayos clínicos y la única publicación es una revisión general. El mecanismo es solo indirecto, ya que la supresión ácida no corrige el reflujo biliar.

**Para avanzar se necesita:**
- Estudios clínicos o series de casos de IBP en reflujo duodenogástrico o gastritis por reflujo biliar, con resultados sintomáticos y endoscópicos.
- Datos de indicación aprobada y de seguridad (advertencias y contraindicaciones) del prospecto de AEMPS.
- Datos del mecanismo de acción (MOA) desde DrugBank.
- Nota: la tercera indicación predicha, **úlcera duodenal** (L1, Proceed with Guardrails), tiene muchos ensayos de Fase 3 y RCT. Sin embargo, parece una indicación ya aprobada y no un reposicionamiento real. Debe verificarse contra la ficha técnica vigente antes de presentarla como hallazgo nuevo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

