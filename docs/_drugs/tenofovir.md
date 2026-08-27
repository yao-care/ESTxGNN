---
layout: default
title: Tenofovir
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 3
---

# Tenofovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Tenofovir: De Infección por VIH a Síndrome de Inmunodeficiencia Adquirida Felina (FIV)

## Resumen en Una Frase

Tenofovir es un inhibidor nucleotídico de la transcriptasa inversa empleado originalmente como componente base de la terapia antirretroviral combinada contra el VIH-1 en humanos. El modelo TxGNN predice que podría ser efectivo para el **Síndrome de Inmunodeficiencia Adquirida Felina (FIV)**, con **4 ensayos clínicos** (todos realizados en contexto de VIH humano, sin relación directa con gatos) y **2 publicaciones** específicas sobre FIV felina que respaldan el vínculo mecanístico.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección por VIH-1 (inferida del contexto de los ensayos clínicos aportados; el paquete de evidencia no registra una indicación original explícita) |
| Nueva Indicación Predicha | Síndrome de Inmunodeficiencia Adquirida Felina (FIV) |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L3 |
| Estado de Mercado en España | No comercializado |
| Número de Autorizaciones | 0 |
| Decisión Recomendada | Hold |

## Por qué es Razonable esta Predicción?

No se dispone de datos detallados del mecanismo de acción en DrugBank para este informe (brecha de datos identificada, severidad Alta). Según la evidencia disponible en los propios ensayos clínicos, Tenofovir es un análogo nucleotídico (profármaco PMPA/tenofovir disoproxil fumarato) que actúa como inhibidor de la transcriptasa inversa, utilizado como componente base de regímenes antirretrovirales combinados frente al VIH-1 (ensayos NCT01263015, NCT02770508, NCT01227824, NCT00951015).

El fundamento del reposicionamiento hacia FIV es la homología estructural entre el VIH y el Virus de Inmunodeficiencia Felina: ambos pertenecen al género *Lentivirus* y comparten una transcriptasa inversa muy conservada. Esto explica que Tenofovir muestre actividad antiviral directa frente a FIV en gatos infectados de forma natural (Taffin et al., 2015) y en modelos de inmunofenotipo felino (Kim et al., 2023). No se trata, por tanto, de un mecanismo nuevo, sino de la extensión de una actividad antiviral de clase ya conocida a otra especie huésped con un virus lentiviral homólogo.

Cabe señalar que el candidato de rango 2 del mismo paquete de evidencia (infección por SIV/SHIV en macacos) refuerza esta lógica: numerosos estudios en primates no humanos confirman que Tenofovir/TAF bloquea la infección por lentivirus homólogos por vía vaginal y rectal, con un mecanismo idéntico al de su indicación humana ya aprobada de profilaxis pre-exposición (PrEP).

## Evidencia de Ensayos Clínicos

*Nota: los 4 ensayos registrados para esta indicación fueron realizados en pacientes humanos con VIH-1, no en gatos con FIV. Se listan porque documentan el uso de tenofovir dentro de regímenes de referencia (p. ej. Atripla), pero su relevancia directa para el reposicionamiento a FIV es baja (grado C).*

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Completado | 844 | Dolutegravir (GSK1349572) + ABC/3TC vs. Atripla (que contiene tenofovir disoproxil fumarato) en VIH-1 naive |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Completado | 145 | Darunavir/ritonavir + lamivudina vs. combinaciones con tenofovir/emtricitabina en VIH-1 naive |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Completado | 828 | Dolutegravir vs. raltegravir, ambos con tenofovir/emtricitabina de base, en VIH-1 naive |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Completado | 208 | Selección de dosis de dolutegravir combinado con ABC/3TC o tenofovir/emtricitabina en VIH-1 naive |

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Cohorte/Revisión (inmunofenotipo) | Viruses | Terapia antirretroviral combinada (dolutegravir + tenofovir + emtricitabina) evaluada en gatos con FIV: farmacocinética y desenlaces clínicos |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Estudio animal (antiviral in vivo) | J Feline Med Surg | Tratamiento de gatos infectados naturalmente con FIV usando PMPA (tenofovir), sin desarrollo de efectos adversos graves reportados |

## Información de Mercado en España

Tenofovir figura como **no comercializado** en el paquete de evidencia (0 autorizaciones registradas). No hay licencias que listar en esta sección.

## Consideraciones de Seguridad

Consulte el prospecto para información de seguridad. Adicionalmente, existe una brecha de datos **bloqueante** sobre las advertencias y contraindicaciones oficiales (TFDA) de tenofovir, lo que actualmente impide completar la evaluación de seguridad de la etapa S1.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La indicación con mayor puntaje TxGNN (FIV) corresponde a una enfermedad felina, no humana; la evidencia clínica disponible procede exclusivamente de ensayos de VIH humano sin relación directa con gatos, y la literatura específica en FIV es de nivel observacional/preclínico veterinario (L3). A esto se suma una brecha de datos bloqueante sobre advertencias/contraindicaciones oficiales que impide cerrar la evaluación de seguridad S1. Los otros dos candidatos del mismo paquete (SIV en macacos, L3/Hold; trastorno del neurodesarrollo, L5/sin evidencia real) tampoco justifican avanzar en este momento.

**Para avanzar se necesita:**
- Resolver la brecha bloqueante sobre advertencias/contraindicaciones oficiales (TFDA) antes de progresar a evaluación de seguridad S1
- Obtener el mecanismo de acción detallado vía DrugBank
- Clarificar si el objetivo del reposicionamiento es una aplicación veterinaria (FIV en gatos) o su traducción a una indicación humana equivalente, dado que el candidato principal no es una enfermedad humana
- Evaluar la viabilidad regulatoria y comercial, considerando que el fármaco no está actualmente comercializado en España
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

