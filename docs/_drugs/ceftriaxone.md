---
layout: default
title: Ceftriaxone
parent: Evidencia moderada (L3-L4)
nav_order: 111
evidence_level: L4
indication_count: 7
---

# Ceftriaxone
{: .fs-9 }

Nivel de evidencia: **L4** | Indicaciones predichas: **7** 
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

# Ceftriaxona: De Indicación Original No Registrada a Hiperamilasemia

## Resumen en Una Frase

Ceftriaxona es un antibiótico betalactámico (cefalosporina de tercera generación). Los datos de AEMPS disponibles no incluyen el texto de su indicación original.
El modelo TxGNN predice que podría ser efectivo para **Hiperamilasemia**,
pero solo hay **0 ensayos clínicos** y **3 publicaciones** de relevancia indirecta, por lo que la evidencia real es muy débil.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Hiperamilasemia |
| Puntaje de Predicción TxGNN | 99.39% |
| Nivel de Evidencia | L4 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el Evidence Pack. Según la información conocida, ceftriaxona es un betalactámico que inhibe las proteínas de unión a penicilina (PBP) bacterianas, y su uso antibacteriano está establecido.

Sin embargo, no existe un mecanismo directo que relacione ceftriaxona con la reducción de la amilasa. La hiperamilasemia es un hallazgo de laboratorio, no una enfermedad tratable en sí misma. Cualquier señal sería indirecta, por ejemplo la prevención de complicaciones infecciosas tras procedimientos biliares o pancreáticos.

El puntaje TxGNN (0.994) es muy alto, pero **no está respaldado por datos clínicos**. Debe interpretarse como una hipótesis del modelo, no como una señal de eficacia.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Estudio clínico (diseño no determinable) | Bratislavske lekarske listy | Compara 30 pacientes con ceftriaxona profiláctica (1 g) tras esfinterotomía endoscópica papilar con 30 sin antibiótico. Las bacterias biliares (*Pseudomonas aeruginosa*, *E. coli*) eran sensibles a ceftriaxona. El resumen disponible está truncado y no permite confirmar el resultado sobre la amilasa. |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Observacional (no específico de ceftriaxona) | Southern Medical Journal | En 38 pacientes con hemorragia intracraneal, 25 tenían lipasa elevada y 17 también amilasa elevada, sin pancreatitis. No evalúa ceftriaxona. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Reporte de caso | Revista Española de Enfermedades Digestivas | Síndrome de Weil (leptospirosis) con hemorragia digestiva alta por úlcera gástrica. Es un caso aislado sin valor de eficacia. |

## Información de Mercado en España

Se listan 5 de las 20 autorizaciones. Los textos de indicación aprobada están vacíos en los datos recibidos, por lo que se omite esa columna.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 83903 | CEFTRIAXONA QILU 1 G POLVO PARA SOLUCION INYECTABLE Y PARA PERFUSION EFG | Polvo para solución inyectable y para perfusión |
| 63251 | CEFTRIAXONA LDP TORLAN 500 MG POLVO Y DISOLVENTE PARA SOLUCION INYECTABLE INTRAVENOSA EFG | Polvo y disolvente para solución inyectable |
| 88920 | CEFTRIAXONA KALCEKS 1 G POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN | Polvo para solución inyectable y para perfusión |
| 64950 | CEFTRIAXONA SALA 2 G POLVO PARA SOLUCIÓN INYECTABLE Y PARA PERFUSIÓN EFG | Polvo para solución para perfusión |
| 62635 | CEFTRIAXONA NORMON 1000 MG POLVO Y DISOLVENTE PARA SOLUCIÓN INYECTABLE Y PARA PERFUSION EFG | Polvo y disolvente para solución inyectable |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
No hay ensayos clínicos ni mecanismo plausible para hiperamilasemia, que es un hallazgo de laboratorio y no una enfermedad tratable. Las tres publicaciones son indirectas o anecdóticas, y el alto puntaje de TxGNN no compensa esa falta de respaldo.

**Para avanzar se necesita:**
- Descargar y analizar la ficha técnica de AEMPS (advertencias, contraindicaciones e indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Definir si existe una enfermedad clínica concreta asociada a la hiperamilasemia (por ejemplo, complicaciones infecciosas tras procedimientos biliares o pancreáticos) que pueda ser el verdadero objetivo terapéutico.
- Como referencia, en el mismo Evidence Pack la predicción de otitis media infecciosa (rango 4) tiene nivel L2 y decisión "Proceed with Guardrails". Probablemente ya es un uso antibacteriano establecido y no un reposicionamiento genuino, por lo que conviene evaluarla por separado.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

