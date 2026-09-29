---
layout: default
title: Dupilumab
parent: Evidencia moderada (L3-L4)
nav_order: 187
evidence_level: L4
indication_count: 10
---

# Dupilumab
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

# Dupilumab: De Indicación Original No Disponible a Bronquitis

## Resumen en Una Frase

Dupilumab es un anticuerpo monoclonal comercializado en España (4 autorizaciones, Sanofi Winthrop Industrie). Los datos recibidos no incluyen su indicación original.
El modelo TxGNN predice que podría ser efectivo para **bronquitis**, pero solo hay **1 ensayo clínico** (en una enfermedad distinta, la rinosinusitis crónica) y **6 publicaciones** de enfermedades vecinas (asma, EPOC). Ninguna evalúa directamente la bronquitis.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (los textos de indicación están vacíos) |
| Nueva Indicación Predicha | Bronquitis |
| Puntaje de Predicción TxGNN | 99.92% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Dupilumab bloquea el receptor IL-4Rα, con lo que inhibe la señalización de IL-4 e IL-13, dos citocinas centrales de la inflamación tipo 2. Los datos no incluyen una descripción detallada del mecanismo de acción en DrugBank, pero este bloqueo está bien caracterizado en la literatura recibida.

Este mecanismo es plausible en enfermedades eosinofílicas de la vía aérea, como el asma, la EPOC con fenotipo tipo 2 y la bronquitis plástica eosinofílica pediátrica. Por eso el modelo relaciona el fármaco con la bronquitis.

Hay que ser prudente. Ningún ensayo de los datos tiene la bronquitis como objetivo. La evidencia procede de enfermedades adyacentes (asma y EPOC), y por eso el nivel de evidencia es L4 y no superior.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04362501](https://clinicaltrials.gov/study/NCT04362501) | Fase 2 | Completado | 33 | Ensayo aleatorizado, doble ciego y controlado con placebo de dupilumab en rinosinusitis crónica sin pólipos nasales. Es una enfermedad distinta: solo aporta apoyo indirecto de la vía aérea superior tipo 2 y no da datos de eficacia en bronquitis. |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [30273510](https://pubmed.ncbi.nlm.nih.gov/30273510/) | 2019 | Revisión sistemática/Metaanálisis | J Asthma | Metaanálisis de ECA que compara dupilumab con placebo en asma no controlada (seguridad y eficacia). |
| [34597534](https://pubmed.ncbi.nlm.nih.gov/34597534/) | 2022 | Extensión abierta (asma) | Lancet Respir Med | Seguridad y eficacia a largo plazo de dupilumab en asma moderada-grave más allá de 1 año (TRAVERSE). |
| [39904363](https://pubmed.ncbi.nlm.nih.gov/39904363/) | 2025 | Revisión | Tuberc Respir Dis | Revisión de terapias farmacológicas para prevenir exacerbaciones de EPOC, incluidos agentes novedosos. |
| [32428511](https://pubmed.ncbi.nlm.nih.gov/32428511/) | 2020 | Cohorte | Chest | Efecto de biológicos anti-T2 sobre la ventilación pulmonar medida por RM en asma dependiente de prednisona. |
| [38488768](https://pubmed.ncbi.nlm.nih.gov/38488768/) | 2024 | Revisión | Pediatr Pulmonol | Terapias novedosas para la bronquitis plástica eosinofílica pediátrica (sin resumen disponible). |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Revisión | Expert Opin Pharmacother | Manejo del asma asociada a enfermedades de la vía aérea inducidas por el tabaco, incluida la bronquitis crónica. |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171229018 | DUPIXENT 300 MG solución inyectable en pluma precargada | Solución inyectable | No disponible |
| 1171229014 | DUPIXENT 200 MG solución inyectable en pluma precargada | Solución inyectable | No disponible |
| 1171229006 | DUPIXENT 300 MG solución inyectable en jeringa precargada | Solución inyectable | No disponible |
| 1171229010 | DUPIXENT 200 MG solución inyectable en jeringa precargada | Solución inyectable | No disponible |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción de TxGNN es muy alta (99.92%), pero no hay ensayos ni literatura que evalúen dupilumab en bronquitis. La evidencia solo procede de asma, EPOC y rinosinusitis, así que el nivel es L4.

**Para avanzar se necesita:**
- Definir el subtipo de bronquitis objetivo (por ejemplo, eosinofílica o tipo 2, frente a la bronquitis crónica general).
- Evidencia clínica directa en ese subtipo.
- Obtener del prospecto de AEMPS las advertencias y contraindicaciones, y las indicaciones aprobadas en España.
- Confirmar el mecanismo de acción en DrugBank.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

