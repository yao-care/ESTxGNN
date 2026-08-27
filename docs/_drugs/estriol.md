---
layout: default
title: Estriol
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 1
---

# Estriol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Usando el Evidence Pack proporcionado, genero el informe siguiendo el formato especificado. Aviso metodológico: `taiwan_regulatory.licenses` está vacío (fármaco no comercializado) y `original_moa` es un vacío de datos, por lo que esos campos se completan con el uso farmacológico generalmente reconocido de estriol, siguiendo la regla de fallback del prompt (nunca se muestra el literal "[Data Gap]").

---

# Estriol: De Terapia Hormonal en Sintomas de Menopausia a Amenorrea

## Resumen en Una Frase

Estriol es un estrogeno natural de baja potencia, utilizado historicamente en terapia hormonal para sintomas de menopausia y atrofia urogenital.
El modelo TxGNN predice que podria ser efectivo para **Amenorrea**,
con **3 ensayos clinicos** y **13 publicaciones** que actualmente respaldan esta direccion, aunque con relevancia limitada.

## Resumen Rapido

| Item | Contenido |
|------|------|
| Indicacion Original | No disponible formalmente (farmaco no comercializado en Espana); uso reconocido internacionalmente: sintomas de menopausia / atrofia urogenital |
| Nueva Indicacion Predicha | Amenorrea |
| Puntaje de Prediccion TxGNN | 99.18% |
| Nivel de Evidencia | L3 (estudios observacionales / revision) |
| Estado de Mercado en Espana | ✗ No comercializado |
| Numero de Autorizaciones | 0 |
| Decision Recomendada | Hold |

## Por que es Razonable esta Prediccion?

Actualmente no se dispone de datos detallados sobre el mecanismo de accion procedentes de fuentes estructuradas (DrugBank). Segun la informacion farmacologica conocida, estriol es un estrogeno de baja potencia, historicamente empleado en terapia hormonal sustitutiva para aliviar sintomas relacionados con el hipoestrogenismo (menopausia, atrofia vulvovaginal); su perfil de eficacia en ese uso esta bien establecido, aunque no consta un texto de indicacion aprobada en las fuentes consultadas para este informe.

Mecanisticamente, estriol podria modular el eje hipotalamo-hipofisis-gonadas (eje HPG) mediante retroalimentacion negativa, regulando la secrecion de hormona luteinizante (LH) en pacientes con amenorrea hipotalamica funcional (FHA), y favoreciendo asi la recuperacion del ciclo menstrual. Sin embargo, este mecanismo se emplea principalmente en terapia hormonal a dosis bajas para aliviar sintomas de hipoestrogenismo (como la perdida osea), y no como tratamiento causal directo de la amenorrea (p. ej., disfuncion hipotalamica o insuficiencia ovarica prematura).

La evidencia actual se basa sobre todo en observaciones clinicas mecanisticas de pequena escala y articulos de revision, y carece de ensayos clinicos aleatorizados y bien disenados que confirmen su eficacia y seguridad especificamente para esta indicacion.

## Evidencia de Ensayos Clinicos

| Numero de Ensayo | Fase | Estado | Inscripcion | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT04487392](https://clinicaltrials.gov/study/NCT04487392) | Fase 2 | Retirado | 0 | Fotobiomodulacion para atrofia vulvovaginal postmenopausica; ensayo retirado sin datos. Relevancia baja para amenorrea (grado C). |
| [NCT04090957](https://clinicaltrials.gov/study/NCT04090957) | Fase 3 | Completado | 1015 | Estetrol (E4) para sintomas vasomotores moderados-severos en mujeres postmenopausicas; no evalua amenorrea directamente. Relevancia baja (grado C). |
| [NCT04209543](https://clinicaltrials.gov/study/NCT04209543) | Fase 3 | Completado | 1570 | Estetrol (E4) para sintomas vasomotores, con componente de seguridad endometrial; relevancia indirecta para amenorrea (grado C). |

**Nota:** Ninguno de los ensayos identificados evalua directamente estriol en pacientes con amenorrea; los tres fueron clasificados con relevancia baja (grado C).

## Evidencia de Literatura

| PMID | Ano | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [22137494](https://pubmed.ncbi.nlm.nih.gov/22137494/) | 2012 | Estudio de cohorte | Fertility and Sterility | La administracion de estriol modula la secrecion de hormona luteinizante (LH) en mujeres con amenorrea hipotalamica funcional (FHA), sugiriendo un efecto neuroendocrino directo. |
| [37371858](https://pubmed.ncbi.nlm.nih.gov/37371858/) | 2023 | Revision | Biomedicines | Estrogenos en dosis bajas como moduladores neuroendocrinos en la FHA, con un posible mecanismo de retroalimentacion positiva sobre el eje GnRH-LH/FSH. |
| [16526238](https://pubmed.ncbi.nlm.nih.gov/16526238/) | 2005 | Estudio de cohorte | Medicinski pregled | Efectos de estro-progestagenos sobre el perfil lipidico y hormonal en mujeres con insuficiencia ovarica primaria prematura (amenorrea hipergonadotropica). |
| [2949864](https://pubmed.ncbi.nlm.nih.gov/2949864/) | 1986 | Observacional | Zhong xi yi jie he za zhi | Relacion entre la "deficiencia renal" (medicina tradicional china) y cambios en la funcion gonadal en mujeres con amenorrea y oligomenorrea (resumen no disponible). |
| [4102186](https://pubmed.ncbi.nlm.nih.gov/4102186/) | 1971 | Reporte de caso | Lancet | Hallazgos endocrinologicos en dos pacientes con insuficiencia ovarica prematura, causa de amenorrea hipergonadotropica (resumen no disponible). |
| [14194444](https://pubmed.ncbi.nlm.nih.gov/14194444/) | 1964 | No clasificado | J Obstet Gynaecol Br Commonw | Ensayo clinico de gonadotropinas humanas en pacientes con amenorrea secundaria idiopatica (resumen no disponible). |
| [5935707](https://pubmed.ncbi.nlm.nih.gov/5935707/) | 1966 | Serie de casos | American Journal of Obstetrics and Gynecology | Manifestaciones ginecologicas y endocrinas prolongadas tras acetato de medroxiprogesterona durante el embarazo (resumen no disponible). |
| [4254759](https://pubmed.ncbi.nlm.nih.gov/4254759/) | 1971 | Reporte de caso/Revision | British Journal of Psychiatry | Revision sobre anorexia nerviosa, condicion frecuentemente asociada a amenorrea hipotalamica funcional (resumen no disponible). |
| [13931724](https://pubmed.ncbi.nlm.nih.gov/13931724/) | 1963 | No clasificado | J Clin Endocrinol Metab | Mecanismo de accion de compuestos anti-ovulatorios, relevante para la modulacion estrogenica del eje HPG (resumen no disponible). |
| [7026111](https://pubmed.ncbi.nlm.nih.gov/7026111/) | 1981 | Revision | Clinical Obstetrics and Gynecology | Revision sobre neoplasia y anticoncepcion hormonal; relevancia indirecta como contexto de seguridad de terapias estrogenicas (resumen no disponible). |

## Consideraciones de Seguridad

No se dispone de datos de advertencias, contraindicaciones ni interacciones farmacologicas (DDI) en las fuentes consultadas para este candidato. Dado que el medicamento no esta actualmente comercializado en Espana y falta el analisis del prospecto/ficha tecnica de la agencia reguladora, se recomienda consultar el prospecto oficial en cuanto este disponible antes de cualquier uso clinico.

## Conclusion y Proximos Pasos

**Decision: Hold**

**Justificacion:**
La prediccion de TxGNN tiene un puntaje alto (99.18%) y existe una base mecanistica plausible (modulacion del eje HPG en amenorrea hipotalamica funcional), respaldada por dos estudios de cohorte y una revision reciente. Sin embargo, ningun ensayo clinico identificado evalua directamente esta indicacion (los tres disponibles fueron calificados de relevancia baja), el nivel de evidencia global es L3, y falta informacion de seguridad critica (advertencias, contraindicaciones, DDI) ademas de que el farmaco no esta comercializado en Espana. Esta combinacion no permite avanzar mas alla de la etapa de pregunta de investigacion.

**Para avanzar se necesita:**
- Obtener el prospecto/ficha tecnica oficial y datos de seguridad (advertencias, contraindicaciones, interacciones)
- Confirmar el mecanismo de accion mediante fuentes estructuradas (DrugBank u otra base validada)
- Disenar o identificar un ensayo clinico especifico de estriol en poblacion con amenorrea hipotalamica funcional
- Evaluar la via regulatoria para eventual comercializacion en Espana
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

