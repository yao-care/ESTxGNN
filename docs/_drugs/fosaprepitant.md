---
layout: default
title: Fosaprepitant
parent: Solo predicción del modelo (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Fosaprepitant
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

# Fosaprepitant: De Indicación Original No Especificada a Síndrome Nefrogénico de Antidiuresis Inapropiada

## Resumen en Una Frase

Fosaprepitant es un profármaco de aprepitant, un antagonista del receptor NK1, comercializado en España en perfusión intravenosa. En los datos compilados para este informe no consta el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome nefrogénico de antidiuresis inapropiada (NSIAD)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Síndrome nefrogénico de antidiuresis inapropiada |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 6 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados. Según la información conocida, fosaprepitant es un profármaco de aprepitant, un antagonista del receptor de neuroquinina 1 (NK1) que bloquea la señalización de la sustancia P.

El NSIAD se debe a mutaciones con ganancia de función en el receptor V2 de la vasopresina (AVPR2). **No se ha establecido un vínculo mecanístico directo**: el antagonismo de NK1 no tiene un papel conocido en la señalización del receptor V2. El elevado puntaje de TxGNN es únicamente una predicción basada en el grafo de conocimiento y debe interpretarse con cautela.

Otras predicciones del modelo (neumocistosis, lepra, meningitis criptocócica, síndromes de neoplasia endocrina múltiple, absceso intracraneal, malaria por *P. falciparum*, equinococosis, hiperargininemia) tampoco cuentan con ensayos ni literatura. La excepción es la retinitis, con un estudio preclínico indirecto (nivel L4, ver más abajo).

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para esta indicación.

*Nota:* para la segunda indicación mejor puntuada con algún respaldo, la retinitis (puntaje TxGNN 99.68%), existe un estudio preclínico en ratones (PMID [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/), 2021, *Ocular Immunology and Inflammation*). En él, fosaprepitant bloqueó la expresión de NK1 inducida por radiación UVR-B en tejidos oculares. Es evidencia indirecta (lesión ocular por UV, no retinitis) y se clasifica como L4.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 88344 | Fosaprepitant Tarbis 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible |
| 07437003 | Ivemend 150 mg polvo para solución para perfusión | Polvo para solución para perfusión | No disponible |
| 86382 | Fosaprepitant Hikma 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible |
| 83380 | Fosaprepitant Accord 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible |
| 88054 | Fosaprepitant Tecnigen 150 mg polvo para solución para perfusión EFG | Polvo para solución para perfusión | No disponible |

Se muestran 5 de las 6 autorizaciones vigentes (la sexta es Fosaprepitant Zentiva, nº 84452).

---

## Consideraciones de Seguridad

- **Contraindicaciones (grafo de conocimiento):** el grafo de conocimiento TxGNN señala insuficiencia hepática como enfermedad asociada a contraindicación. No proviene del texto del prospecto.
- **Interacciones Farmacológicas:** se identificaron 100 interacciones en total. Entre las principales mostradas:
  - **Mayores:** eliglustat, naloxegol.
  - **Moderadas:** corticoides (hidrocortisona, betametasona, budesonida, dexametasona, triamcinolona), claritromicina, cimetidina, rabeprazol, lansoprazol, miconazol, dronabinol, alosetrón, pioglitazona, saxagliptina, glimepirida, nateglinida y naldemedina.

Para advertencias y contraindicaciones oficiales, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para NSIAD se basa solo en el modelo (nivel L5), sin ensayos ni literatura, y el mecanismo conocido (antagonismo de NK1) no se relaciona con el defecto del receptor V2. No hay base para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas), actualmente un vacío bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, vía DrugBank).
- Establecer una hipótesis mecanística plausible entre NK1 y la señalización de AVPR2 y evaluarla en estudios preclínicos.
- Valorar si otra indicación predicha con algún respaldo preclínico (retinitis) merece priorización como pregunta de investigación.
- Revisar las interacciones mayores (eliglustat, naloxegol) y la contraindicación en insuficiencia hepática en cualquier plan futuro.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

