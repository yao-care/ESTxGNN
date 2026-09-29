---
layout: default
title: Acyclovir
parent: Solo predicción del modelo (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Aciclovir: De Infecciones por Herpesvirus a Queratoconjuntivitis Epitelial Punteada

## Resumen en Una Frase

Aciclovir es un antivirico nucleosidico que se utiliza habitualmente contra infecciones por virus herpes (uso general conocido; las fichas de AEMPS recuperadas no incluyen el texto de indicacion).
El modelo TxGNN predice que podria ser efectivo para la **queratoconjuntivitis epitelial punteada**,
pero **no hay ensayos clinicos** y solo hay **2 publicaciones**, ninguna de las cuales evalua aciclovir. Por ahora es una prediccion sin respaldo real.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No consta en las fichas de AEMPS recuperadas (uso general conocido: infecciones por herpesvirus) |
| Nueva Indicacion Predicha | Queratoconjuntivitis epitelial punteada |
| Puntaje de Prediccion TxGNN | 99.67% (posicion 5810) |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Espana | ✓ Comercializado |
| Numero de Autorizaciones | 20 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion en el Evidence Pack. Segun la informacion conocida, aciclovir es un analogo de guanosina que se activa gracias a la timidina quinasa viral. Por eso su actividad se limita a virus que poseen esa enzima, como los herpesvirus.

La queratoconjuntivitis epitelial punteada suele ser de origen adenoviral, y el adenovirus no tiene timidina quinasa. Por tanto, se espera poca o ninguna actividad de aciclovir, y el fundamento mecanistico es **debil**.

La prediccion parece reflejar asociaciones en el grafo de conocimiento (enfermedades oculares virales) y no un mecanismo demostrado. Solo tendria sentido si algunos casos tuvieran etiologia herpetica, lo que aun habria que confirmar.

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Serie de casos | Indian J Pathol Microbiol | Caracteristicas de la queratoconjuntivitis microsporidial en una cohorte del este de la India. No evalua aciclovir |
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Observacional | Am J Ophthalmol | Lipidosis corneal inducida por farmacos en dos pacientes con SIDA. No evalua aciclovir |

Ninguno de los dos trabajos respalda el uso de aciclovir en esta indicacion.

## Informacion de Mercado en Espana

| Numero de Autorizacion | Nombre del Producto | Forma Farmaceutica |
|---------|------|------|
| 63759 | ACICLOVIR VIATRIS 200 MG COMPRIMIDOS EFG | Comprimido |
| 62686 | ACICLOVIR SANDOZ 800 MG COMPRIMIDOS EFG | Comprimido |
| 62736 | ACICLOVIR KERN PHARMA 200 mg COMPRIMIDOS DISPERSABLES EFG | Comprimido dispersable |
| 62740 | ACICLOVIR PENSA 200 mg COMPRIMIDOS DISPERSABLES EFG | Comprimido dispersable |
| 85741 | HERVAX 250 MG POLVO PARA SOLUCION PARA PERFUSION EFG | Polvo para solucion para perfusion |

Entre las 20 autorizaciones tambien hay formas como pomada oftalmica, crema, comprimido recubierto y suspension oral. Los datos recuperados no incluyen el texto de la indicacion aprobada.

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
Es una prediccion pura del modelo (L5) sin ensayos clinicos ni literatura que evalue aciclovir, y con un mecanismo poco plausible para una enfermedad frecuentemente adenoviral.

**Para avanzar se necesita:**
- Confirmar si existe una subpoblacion con etiologia herpetica y una razon clinica para el uso de aciclovir.
- Datos del mecanismo de accion (MOA) y del prospecto de AEMPS (advertencias y contraindicaciones).
- Estudios preclinicos o clinicos que evaluen aciclovir en esta indicacion.

**Nota:** en el mismo Evidence Pack, la segunda prediccion (verruga comun, L2) tiene mas respaldo. Incluye un ECA de Fase 2/3 (NCT06261684, PMID 40889709) con aciclovir intralesional, y conviene evaluarla por separado. Esa evidencia corresponde a la via intralesional, no a la oral comercializada.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

