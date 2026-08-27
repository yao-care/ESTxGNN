---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 3
---

# Cobicistat
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

# Cobicistat: De Potenciador Farmacocinetico en VIH a Infeccion por Virus de Inmunodeficiencia de Simios

## Resumen en Una Frase

Cobicistat no es un antirretroviral por si mismo, sino un inhibidor de CYP3A4/P-gp utilizado como potenciador farmacocinetico (PK booster) junto con otros antirretrovirales (atazanavir, darunavir, elvitegravir) en el tratamiento del VIH. El modelo TxGNN predice como direccion principal la **infeccion por virus de inmunodeficiencia de simios (SIV)**, con un score de **99.92%**, pero actualmente **no existen ensayos clinicos ni publicaciones** que respalden esta prediccion.

---

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | Sin indicacion propia aprobada; usado como potenciador farmacocinetico junto a antirretrovirales en VIH |
| Nueva Indicacion Predicha | Infeccion por virus de inmunodeficiencia de simios (SIV) |
| Puntaje de Prediccion TxGNN | 99.92% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

---

## Por que es Razonable esta Prediccion?

No se dispone de datos estructurados sobre el mecanismo de accion (campo `original_moa` marcado como vacio). Sin embargo, la informacion recopilada en el analisis de esta candidatura indica que Cobicistat actua como inhibidor de CYP3A4/P-gp, potenciando las concentraciones plasmaticas de otros antirretrovirales sin poseer actividad antiviral directa propia. No tiene, por tanto, una "indicacion original" en el sentido clasico, sino un rol de coadyuvante farmacocinetico dentro de regimenes contra el VIH.

El VIH y el SIV pertenecen ambos a la familia de los lentivirus, por lo que existe una proximidad conceptual entre ambas infecciones. Sin embargo, esta cercania es unicamente taxonomica/de grafo de conocimiento: dado que Cobicistat carece de actividad antiviral intrinseca, su utilidad en SIV solo podria plantearse como coadyuvante de otro antirretroviral en un regimen combinado, nunca como monoterapia.

En consecuencia, la señal de TxGNN probablemente refleja la cercania de nodos relacionados con VIH en el grafo farmaco-enfermedad, mas que una relacion mecanistica directa y verificable. La ausencia total de ensayos clinicos, literatura y datos preclinicos para esta indicacion refuerza que se trata de una hipotesis exploratoria, no de una senal validada.

---

## Evidencia de Ensayos Clinicos

Actualmente no hay ensayos clinicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Informacion de Mercado en España

Cobicistat no esta comercializado en España (0 autorizaciones registradas).

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

> Nota: el analisis identifico un vacio de datos de severidad **Bloqueante** (DG001 — advertencias/contraindicaciones de AEMPS/prospecto), que impide actualmente avanzar a la fase de evaluacion inicial de seguridad (S1).

---

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La evidencia disponible corresponde unicamente a la prediccion del modelo (L5), sin ningun ensayo clinico, publicacion ni dato preclinico de respaldo. Ademas, falta informacion de seguridad basica (advertencias y contraindicaciones), lo cual bloquea el avance a la fase de evaluacion de seguridad. El propio razonamiento mecanistico generado indica que Cobicistat carece de actividad antiviral directa, lo que debilita aun mas la plausibilidad de esta indicacion como monoterapia.

**Para avanzar se necesita:**
- Datos de seguridad de AEMPS/prospecto (advertencias, contraindicaciones e interacciones)
- Mecanismo de accion (MOA) confirmado via DrugBank u otra fuente estructurada
- Evidencia preclinica o clinica real (no solo prediccion de modelo) que vincule Cobicistat con infecciones por lentivirus en modelos animales
- Aclarar si la aplicacion propuesta seria como monoterapia o como coadyuvante junto a un antiviral activo

> Nota adicional: el mismo pipeline predijo otras dos indicaciones para Cobicistat — "feline acquired immunodeficiency syndrome" (score 99.92%) y un trastorno neurodesarrollo raro (score 99.91%) — ambas tambien en L5, sin evidencia real y con relacion mecanistica nula o cuestionable. La consistencia de score alto sin soporte real en las tres indicaciones sugiere posible ruido del grafo de conocimiento para este farmaco, mas que una senal robusta de reposicionamiento.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

