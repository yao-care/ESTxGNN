---
layout: default
title: Deferasirox
parent: Evidencia moderada (L3-L4)
nav_order: 162
evidence_level: L4
indication_count: 5
---

# Deferasirox
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **5** 
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

# Deferasirox: De Quelante de Hierro (Sobrecarga de Hierro) a Infección por VIH

## Resumen en Una Frase

Deferasirox es un quelante de hierro comercializado en España en varias presentaciones genéricas. Los datos de AEMPS recibidos no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **infección por VIH**, pero solo hay **0 ensayos clínicos** y **2 publicaciones**, ninguna con datos clínicos en VIH.
Además, la evidencia preclínica disponible sugiere que la quelación de hierro podría ser contraproducente.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS recibidos (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Infección por VIH |
| Puntaje de Predicción TxGNN | 99,40 % |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, deferasirox se utiliza como quelante de hierro (tratamiento de la sobrecarga de hierro, por ejemplo en talasemia). Esta clasificación proviene del contexto de la literatura recuperada y no de un texto de indicación aprobado en los datos recibidos. Su relación mecanística con el VIH es solo indirecta.

La única pista mecanística proviene de un estudio preclínico (PMID 34550543). Según ese estudio, el hierro en los endolisosomas **restringe** la transactivación del LTR del VIH-1 mediada por Tat, al aumentar la oligomerización de Tat y la expresión de β-catenina. Si esto es correcto, quelar hierro con deferasirox podría debilitar esa restricción natural y favorecer la replicación viral. La dirección del efecto es, por tanto, incierta o incluso adversa.

El puntaje TxGNN es muy alto (99,40 %), pero es una predicción del modelo basada en el grafo de conocimiento. No está respaldada por datos clínicos.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclínico / mecanístico in vitro | J Neurovirol | El hierro endolisosomal restringe la transactivación del LTR del VIH-1 mediada por Tat, al aumentar la oligomerización de Tat y la expresión de β-catenina. |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Revisión (resumen de nuevos fármacos) | J Am Pharm Assoc | Resumen general de nuevos fármacos, incluido deferasirox. No es específico de VIH. |

---

## Información de Mercado en España

Se muestran 5 de las 20 autorizaciones. Los datos recibidos no incluyen el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 84909 | Deferasirox Stada 180 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Laboratorio Stada S.L. |
| 86261 | Deferasirox Aurovitas 90 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Aurovitas Spain, S.A.U. |
| 86337 | Deferasirox Alembic 360 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Alembic Pharmaceuticals Europe Limited |
| 89130 | Deferasirox Sun 360 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Sun Pharmaceutical Industries (Europe) B.V. |
| 1191412002 | Deferasirox Accord 90 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película | Accord Healthcare S.L.U. |

También existe la forma de comprimido dispersable entre las presentaciones registradas.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas registradas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos y la única evidencia es un estudio preclínico cuyo sentido apunta a un posible efecto adverso de la quelación de hierro sobre el VIH. El puntaje TxGNN por sí solo no basta para avanzar.

**Para avanzar se necesita:**
- Obtener el prospecto de AEMPS para confirmar la indicación original, las advertencias y las contraindicaciones (actualmente falta información de seguridad).
- Obtener los datos del mecanismo de acción desde DrugBank.
- Realizar estudios in vitro de deferasirox en modelos de replicación del VIH para aclarar si el efecto es beneficioso o perjudicial.
- Solo si esos estudios son favorables, evaluar estudios clínicos exploratorios con monitorización de carga viral.

**Otras predicciones del modelo (para referencia):**
- **Hepatitis C crónica:** L4, "Research Question". El vínculo es indirecto, a través de la sobrecarga de hierro. Cualquier beneficio vendría de tratar la sobrecarga de hierro comórbida, no de una acción antiviral.
- **Trastorno del neurodesarrollo con marcha atáxica, dermatofibrosarcoma protuberans e hiperlipidemia familiar combinada (término obsoleto):** L5, "Hold". No hay ensayos ni literatura. El término de hiperlipidemia debe actualizarse en la ontología antes de evaluarlo.

*Estos resultados son solo de referencia para investigación y no constituyen consejo médico. Cualquier candidato de reposicionamiento requiere validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

