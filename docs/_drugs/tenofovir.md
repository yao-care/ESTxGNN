---
layout: default
title: Tenofovir
parent: Solo predicción del modelo (L5)
nav_order: 775
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tenofovir: nueva indicación predicha, Síndrome de inmunodeficiencia adquirida felina (nivel de evidencia L5). Indicación original: Infección crónica por el virus de la hepatitis B…"
---

# Tenofovir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **3** 
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

# Tenofovir: De Hepatitis B Crónica e Infección por VIH a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Tenofovir es un inhibidor nucleotídico de la transcriptasa inversa, originalmente utilizado para el tratamiento de la infección crónica por el virus de la hepatitis B, la infección por VIH y el SIDA.
El modelo TxGNN predice que podría ser efectivo para **síndrome de inmunodeficiencia adquirida felina**, con **0 ensayos clínicos** y **2 publicaciones** preclínicas en animales que respaldan esta dirección. Se trata de una indicación veterinaria, no de una nueva indicación en humanos.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis B, infección por VIH y SIDA (según el grafo de conocimiento; los textos de indicación de las autorizaciones españolas no están disponibles) |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L4 (solo estudios preclínicos en animales; la clasificación interna de los datos indica L3) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en los datos compilados para este informe. Según la información conocida, tenofovir es un análogo nucleotídico que, tras su activación intracelular a tenofovir difosfato, inhibe la transcriptasa inversa viral. Su eficacia en VIH y hepatitis B está establecida.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus con una transcriptasa inversa homóloga a la del VIH-1, por lo que el mecanismo original podría trasladarse. Hay un estudio en gatos infectados con FIV tratados con el compuesto original PMPA (tenofovir) y otro de 2023 con terapia antirretroviral combinada.

Cabe señalar que el puntaje TxGNN, muy alto, refleja en gran medida la similitud con el VIH, que ya es una indicación aprobada. La enfermedad es veterinaria y no hay ensayos clínicos en humanos, por lo que el hallazgo no es directamente aplicable al reposicionamiento en medicina humana.

Las otras predicciones del modelo tienen un puntaje casi idéntico: simian immunodeficiency virus infection (modelo animal del VIH, con 20 publicaciones, mayormente estudios en macacos de profilaxis pre y postexposición) y un trastorno del neurodesarrollo raro sin ninguna evidencia ni vínculo mecanístico (nivel L5, Hold). Esto sugiere un poder discriminativo limitado del puntaje.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclínico in vivo | Viruses | Evaluó la farmacocinética y los resultados clínicos de una terapia antirretroviral combinada (dolutegravir, tenofovir y emtricitabina) en gatos infectados con FIV, que carecen de una terapia definitiva |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Preclínico in vivo | J Feline Med Surg | Tratamiento antiviral con PMPA (tenofovir) en gatos infectados naturalmente con FIV; los antivirales humanos usados experimentalmente se han asociado a efectos adversos graves |

## Información de Mercado en España

Se listan 5 de las 17 autorizaciones vigentes (todas de principio activo único). Los textos de indicación aprobada no están disponibles en los datos compilados.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 01200001 | VIREAD 245 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 101200004 | Viread 123 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 101200003 | Viread 33 mg/g gránulos | Granulado | No disponible |
| 81917 | Tenofovir disoproxilo Accord 245 mg EFG | Comprimido recubierto con película | No disponible |
| 80476 | Tenofovir disoproxilo Teva 245 mg EFG | Comprimido recubierto con película | No disponible |

## Consideraciones de Seguridad

- **Enfermedades asociadas a contraindicación o precaución en el grafo de conocimiento** (no proceden del prospecto): insuficiencia hepática, enfermedad hepática, enfermedad renal, síndrome de Fanconi, hipofosfatemia, osteomalacia, raquitismo, acidosis láctica, hígado graso y esteatohepatitis no alcohólica, hipertrigliceridemia, síndrome de QT largo y torsade de pointes, epilepsia, hepatitis C, entre otras.
- No se dispone de datos de interacciones farmacológicas en los datos compilados.
- Consultar el prospecto para la información oficial de advertencias y contraindicaciones.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La única evidencia disponible son dos estudios preclínicos en gatos, sin ensayos clínicos, y la indicación es veterinaria, por lo que no constituye un reposicionamiento en humanos. El puntaje TxGNN alto refleja sobre todo la similitud con el VIH, ya aprobado.

**Para avanzar se necesita:**
- Decidir si el interés es veterinario o humano; en este último caso, la predicción no aporta una nueva indicación.
- Obtener advertencias y contraindicaciones del prospecto de AEMPS (hueco de datos bloqueante para el cribado de seguridad).
- Obtener datos del mecanismo de acción desde DrugBank.
- Disponer de estudios controlados en gatos (tamaño muestral, controles) y evaluar la seguridad renal y ósea en esa especie.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

