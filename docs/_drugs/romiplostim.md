---
layout: default
title: Romiplostim
parent: Evidencia moderada (L3-L4)
nav_order: 474
evidence_level: L4
indication_count: 10
---

# Romiplostim
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

# Romiplostim: De Trombocitopenia Inmune (ITP) a Trastorno de Liberación Primaria de Plaquetas

## Resumen en Una Frase

Romiplostim es un agonista del receptor de la trombopoyetina (TPO), comercializado en España como Nplate. Los datos de AEMPS recibidos no incluyen el texto de la indicación aprobada; por el contexto de la evidencia, su uso se asocia a la trombocitopenia inmune (ITP).
El modelo TxGNN predice que podría ser efectivo para **trastorno de liberación primaria de plaquetas**, pero solo hay **1 ensayo clínico observacional indirecto** y **2 publicaciones** (una revisión y un estudio preclínico), sin evidencia directa.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos de AEMPS (texto de indicación vacío en las 4 autorizaciones); ITP inferida del contexto de la evidencia |
| Nueva Indicación Predicha | Trastorno de liberación primaria de plaquetas |
| Puntaje de Predicción TxGNN | 99.9998% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, romiplostim es un agonista del receptor de TPO que aumenta la producción de plaquetas. Su eficacia en trombocitopenias por déficit de producción o destrucción está documentada en los ensayos y la literatura del paquete de evidencia.

Sin embargo, el ajuste mecanístico con esta nueva indicación es débil. Un defecto de liberación (secreción) plaquetaria es un problema de **función** plaquetaria, y un fármaco que eleva el **recuento** de plaquetas no tiene un encaje claro. La puntuación tan alta del grafo probablemente refleja vecinos compartidos en la red de ITP y trombopoyesis, no una relación terapéutica directa.

Los datos disponibles refuerzan esta cautela. El único ensayo es un estudio observacional sobre factores de riesgo de trombosis en ITP y no prueba romiplostim en este trastorno. La literatura describe la megacariopoyesis en general y el efecto de autoanticuerpos sobre la formación de proplaquetas in vitro.

---

## Evidencia de Ensayos Clínicos

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT03820960](https://clinicaltrials.gov/study/NCT03820960) | N/A (observacional) | Completado | 10039 | Factores de riesgo de trombosis en trombocitopenia inmune. No evalúa romiplostim en un trastorno de liberación plaquetaria (relevancia: C) |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [23594368](https://pubmed.ncbi.nlm.nih.gov/23594368/) | 2013 | Revisión | British Journal of Haematology | Avances en megacariopoyesis y trombopoyesis: la TPO es el principal factor de crecimiento del linaje megacariocítico |
| [25682608](https://pubmed.ncbi.nlm.nih.gov/25682608/) | 2015 | Preclínico/mecanístico | Haematologica | En ITP, los autoanticuerpos antiplaquetarios inhiben in vitro la formación de proplaquetas por los megacariocitos y reducen la producción de plaquetas |

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 08497001 | NPLATE 250 microgramos polvo para solución inyectable | Polvo para solución inyectable |
| 08497005 | NPLATE 250 microgramos polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 08497007 | NPLATE 500 microgramos polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable |
| 08497002 | NPLATE 500 microgramos polvo para solución inyectable | Polvo para solución inyectable |

Titular: Amgen Europe B.V. El texto de indicación aprobada no figura en los datos recibidos.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay respaldo mecanístico ni clínico directo: romiplostim aumenta el recuento de plaquetas, pero este trastorno afecta a su función. La evidencia se limita a un estudio observacional indirecto y a literatura general (nivel L4).

**Para avanzar se necesita:**
- Texto de indicaciones, advertencias y contraindicaciones del prospecto de AEMPS
- Datos del mecanismo de acción desde DrugBank
- Estudios que evalúen romiplostim específicamente en defectos de liberación plaquetaria
- Revisar otras predicciones del mismo paquete con más respaldo, como "trastorno hemorrágico de tipo plaquetario" (nivel L2, decisión "Research Question"), que agrupa ensayos de romiplostim en trombocitopenias

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de su aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

