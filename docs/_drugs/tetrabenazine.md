---
layout: default
title: Tetrabenazine
parent: Solo predicción del modelo (L5)
nav_order: 523
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazina: De Trastornos Hipercinéticos (Corea de Huntington) a Enfermedad Renal Poliquística Tipo 3 con o sin Enfermedad Hepática Poliquística

## Resumen en Una Frase

La tetrabenazina se utiliza principalmente para el tratamiento sintomático de trastornos hipercinéticos, como la corea de la enfermedad de Huntington, el síndrome de Tourette y la discinesia tardía.
El modelo TxGNN predice que podría ser efectiva para la **enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística**, pero **no hay ensayos clínicos** y las **20 publicaciones** encontradas tratan la enfermedad en general, sin evaluar la tetrabenazina.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Trastornos hipercinéticos (corea de Huntington, síndrome de Tourette, discinesia tardía). Los registros de AEMPS no incluyen el texto de indicación, por lo que se toma de la ficha farmacológica. |
| Nueva Indicación Predicha | Enfermedad renal poliquística tipo 3 con o sin enfermedad hepática poliquística |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 4 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

La tetrabenazina es un inhibidor reversible del transportador vesicular de monoaminas 2 (VMAT2, gen SLC18A2). También tiene como diana el VMAT1 (SLC18A1). Al inhibir el VMAT2, agota las monoaminas presinápticas, y por eso reduce los movimientos involuntarios en la corea.

**Esta predicción no tiene un vínculo mecanístico plausible.** La enfermedad predicha depende de la vía de la policistina y los cilios, y de genes de procesamiento en el retículo endoplasmático (como *PRKCSH*, *SEC63* y *GANAB*). La inhibición del VMAT2 no actúa sobre esas vías. El puntaje alto de TxGNN (0.999) parece un artefacto del grafo de conocimiento y no refleja un mecanismo real.

Las otras nueve predicciones del modelo, todas de nivel L5, tampoco muestran un mecanismo plausible. La única con algún registro clínico (malformación torácica) se basa en un ensayo de marcha en enfermedad de Huntington, sin relación con la indicación predicha.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Ninguna de las publicaciones evalúa la tetrabenazina. Todas describen la enfermedad, su genética o su manejo general. No hay ECA.

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guía | J Hepatol | Guía de la EASL sobre el diagnóstico y manejo de las enfermedades quísticas hepáticas, incluida la enfermedad hepática poliquística |
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Guía | Am J Gastroenterol | Guía del ACG sobre lesiones hepáticas focales, incluidos los quistes hepáticos y la enfermedad hepática poliquística |
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Revisión | Lancet | Revisión de la poliquistosis renal autosómica dominante como enfermedad sistémica, con quistes hepáticos y otras complicaciones extrarrenales |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Revisión | Clin Liver Dis | La enfermedad hepática poliquística es la manifestación extrarrenal más frecuente; se menciona tolvaptán para frenar el deterioro renal |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Revisión | J Am Soc Nephrol | Solapamiento genético entre la poliquistosis renal y la hepática; ocho genes asociados (*PKD1*, *PKD2*, *PRKCSH*, *SEC63*, *LRP5*, *ALG8*, *SEC61B*, *GANAB*) |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Revisión | Adv Kidney Dis Health | Espectro genético de las enfermedades poliquísticas renales y hepáticas; el defecto de los cilios primarios es central en la patogenia |
| [36047551](https://pubmed.ncbi.nlm.nih.gov/36047551/) | 2022 | Revisión | Rev Med Suisse | Descripción de la enfermedad hepática poliquística en adultos; las formas sintomáticas afectan sobre todo a mujeres |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Investigación básica | J Clin Invest | Los genes de la enfermedad hepática poliquística aislada definen efectores de la función de la policistina-1 |
| [28973524](https://pubmed.ncbi.nlm.nih.gov/28973524/) | 2017 | Investigación básica | Hum Mol Genet | La pérdida de genes de quistes hepáticos en colangiocitos inhibe la formación de cilios y la señalización Wnt |
| [40842155](https://pubmed.ncbi.nlm.nih.gov/40842155/) | 2025 | Preclínico | Mol Ther | La edición de bases in vivo reduce los quistes hepáticos en un modelo de poliquistosis renal autosómica dominante |

---

## Información de Mercado en España

Los registros de AEMPS no incluyen el texto de la indicación aprobada, por eso la tabla no tiene esa columna.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Titular |
|---------|------|------|-----------|
| 84164 | Tetrabenazina Aristo 25 mg comprimidos EFG | Comprimido | Aristo Pharma GmbH |
| 82080 | Tetrabenazina Sun 25 mg comprimidos EFG | Comprimido | Sun Pharmaceutical Industries (Europe) B.V. |
| 70142 | Nitoman 25 mg comprimidos | Comprimido | Bausch Health Ireland Limited |
| 72730 | Tetmodis 25 mg comprimidos EFG | Comprimido | Walter Ritter GmbH & Co. KG |

---

## Consideraciones de Seguridad

Consultar el prospecto para informacion de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5): no hay ensayos clínicos ni estudios con tetrabenazina en esta enfermedad. Además, la inhibición del VMAT2 no tiene relación con la biología de la enfermedad, por lo que el puntaje de 99.90% parece un artefacto del grafo de conocimiento.

**Para avanzar se necesita:**
- Un vínculo mecanístico plausible entre la inhibición del VMAT2 y la vía de la policistina y los cilios, o evidencia preclínica que lo respalde
- Descargar y analizar la ficha técnica de AEMPS para completar el perfil de advertencias y contraindicaciones
- Revisar las indicaciones aprobadas en España, que no figuran en los registros actuales
- Considerar otras indicaciones predichas solo si aparece evidencia real; hoy todas están en nivel L5
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

