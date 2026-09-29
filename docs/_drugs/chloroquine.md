---
layout: default
title: Chloroquine
parent: Evidencia moderada (L3-L4)
nav_order: 121
evidence_level: L4
indication_count: 4
---

# Chloroquine
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **4** 
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

# Cloroquina: De Paludismo a Artritis Idiopática Juvenil Poliarticular con Factor Reumatoide Positivo

## Resumen en Una Frase

La cloroquina es un antipalúdico utilizado para prevenir y tratar la infección por *P. vivax*. La ficha de AEMPS incluida en los datos no trae texto de indicación.
El modelo TxGNN predice que podría ser eficaz en la **artritis idiopática juvenil poliarticular con factor reumatoide positivo**, pero hay **0 ensayos clínicos** y solo **2 publicaciones**, ambas indirectas, porque tratan de leflunomida y metotrexato.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Paludismo (según la información farmacológica; la autorización de AEMPS no incluye texto de indicación) |
| Nueva Indicación Predicha | Artritis idiopática juvenil poliarticular con factor reumatoide positivo |
| Puntaje de Predicción TxGNN | 99.41% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la información conocida, la cloroquina es un antipalúdico que también se usa fuera de indicación en enfermedades autoinmunes como la artritis reumatoide y el lupus eritematoso. Mecanísticamente podría ser aplicable a la artritis juvenil.

La hipótesis es que la cloroquina tiene actividad inmunomoduladora: inhibe la función lisosomal y la autofagia, y reduce la presentación de antígenos y la señalización de los receptores tipo Toll. Esto es plausible en la artritis autoinmune. No se puede verificar con los datos aportados, así que debe tomarse como hipótesis.

El puntaje de TxGNN (99.41%) es solo una predicción del modelo. Las dos publicaciones recuperadas no evalúan la cloroquina como tratamiento: una describe la experiencia con leflunomida y la otra un caso de nodulosis por metotrexato.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Cohorte | The Journal of Rheumatology | Experiencia prospectiva a largo plazo con leflunomida en artritis idiopática juvenil. No evalúa cloroquina (evidencia indirecta). |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Serie de casos | The Journal of Pediatrics | Dos pacientes con artritis reumatoide juvenil poliarticular con factor reumatoide positivo desarrollaron nodulosis acelerada durante el tratamiento con metotrexato. En uno, la adición de hidroxicloroquina detuvo la progresión. Es un dato anecdótico y con un fármaco relacionado, no con cloroquina. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 15797 | RESOCHIN 155 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA (Kern Pharma S.L.) | Comprimido recubierto | No consta texto de indicación en los datos disponibles |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo y en literatura indirecta. No hay ensayos clínicos ni estudios que evalúen la cloroquina en esta indicación. Faltan además los datos de seguridad de AEMPS y el mecanismo de acción, por lo que no se puede avanzar a una evaluación de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), que actualmente bloquea la evaluación de seguridad.
- Completar el mecanismo de acción desde DrugBank.
- Buscar evidencia directa de cloroquina o hidroxicloroquina en artritis idiopática juvenil. Un punto de partida es el metaanálisis de tres ensayos aleatorizados con hidroxicloroquina en artritis reumatoide juvenil (PMID 8235664), que aparece entre la literatura de la indicación relacionada.
- Evaluar la seguridad de la cloroquina en población pediátrica antes de plantear una pregunta de investigación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

