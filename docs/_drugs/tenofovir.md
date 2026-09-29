---
layout: default
title: Tenofovir
parent: Solo predicción del modelo (L5)
nav_order: 516
evidence_level: L5
indication_count: 3
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

# Tenofovir: De Antiviral contra el VIH/VHB a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Tenofovir es un antiviral inhibidor de la transcriptasa inversa, comercializado en España para infecciones virales como el VIH y la hepatitis B. Esta información de uso original proviene del conocimiento general del fármaco, porque los datos de AEMPS no incluyen el texto de indicación.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (SIDA felino, causado por el FIV)**.
Esta predicción cuenta con **2 publicaciones preclínicas en gatos** y **4 ensayos clínicos indirectos** (todos en VIH-1 humano, donde tenofovir es solo comparador o base del régimen).

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina |
| Puntaje de Predicción TxGNN | 99,96% |
| Nivel de Evidencia | L4 (estudios preclínicos) |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en DrugBank. Según la información conocida, tenofovir pertenece a la familia de los análogos nucleotídicos (PMPA/PMEA) que inhiben la transcriptasa inversa viral. Su eficacia contra el VIH está comprobada, y mecanísticamente podría ser aplicable a otros lentivirus.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus con una transcriptasa inversa que probablemente es susceptible a este tipo de fármacos. Causa en los gatos una disfunción inmunitaria progresiva similar a la del VIH en humanos.

El puntaje TxGNN muy alto (0,9996) probablemente refleja la cercanía del fármaco con los nodos del VIH en el grafo de conocimiento. Es una predicción computacional, y los datos animales solo la respaldan parcialmente.

**Aclaración importante:** se trata de una indicación veterinaria, por lo que **no aporta una nueva indicación en humanos**.

---

## Evidencia de Ensayos Clínicos

Los cuatro ensayos son estudios en VIH-1 humano en los que tenofovir no es el fármaco en evaluación. Constituyen evidencia indirecta, no datos en felinos.

| Número de Ensayo | Fase | Estado | Inscripción | Hallazgos Principales |
|---------|------|------|------|---------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Fase 3 | Completado | 844 | Dolutegravir + abacavir/lamivudina frente a Atripla (efavirenz/emtricitabina/tenofovir) en adultos con VIH-1 sin tratamiento previo; tenofovir es comparador |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Fase 4 | Completado | 145 | Darunavir potenciado + lamivudina frente a darunavir + emtricitabina/tenofovir o lamivudina/tenofovir en VIH-1 sin tratamiento previo; tenofovir es comparador |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Fase 3 | Completado | 828 | Dolutegravir frente a raltegravir con base de dos ITIAN (abacavir/lamivudina o tenofovir/emtricitabina) en VIH-1 |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Fase 2 | Completado | 208 | Selección de dosis de dolutegravir con abacavir/lamivudina o tenofovir/emtricitabina como base en VIH-1 |

---

## Evidencia de Literatura

| PMID | Año | Tipo | Revista | Hallazgos Principales |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Estudio preclínico en animales | Viruses | Evalúa la farmacocinética y los resultados clínicos de una terapia antirretroviral combinada (dolutegravir 2,5 mg/kg, tenofovir 20 mg/kg, emtricitabina 40 mg/kg) en gatos infectados con FIV |
| [24782459](https://pubmed.ncbi.nlm.nih.gov/24782459/) | 2015 | Estudio preclínico en animales | Journal of Feline Medicine and Surgery | Tratamiento de seis gatos con infección natural por FIV con PMPA (tenofovir); el artículo señala que otros antivirales humanos usados en gatos han causado efectos adversos graves |

---

## Información de Mercado en España

Hay 17 autorizaciones en total; se muestran las 5 principales. Todas son comprimidos de tenofovir disoproxilo 245 mg. También existe una forma en granulado. Los datos de AEMPS no incluyen el texto de indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 81917 | Tenofovir Disoproxilo Accord 245 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 82360 | Tenofovir Disoproxilo Glenmark 245 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 83226 | Tenofovir Disoproxilo Cipla 245 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 82554 | Tenofovir Disoproxilo Aristo 245 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 84647 | Tenofovir Disoproxilo Qilu 245 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La evidencia es únicamente preclínica (L4): dos estudios en gatos y ensayos humanos que solo sirven como evidencia indirecta. Además, es una indicación veterinaria que no añade una indicación humana nueva, y faltan los datos de seguridad de AEMPS, lo que impide avanzar al cribado de seguridad.

**Para avanzar se necesita:**
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones), un dato bloqueante.
- Obtener datos del mecanismo de acción desde DrugBank.
- Definir si el objetivo es una indicación veterinaria (estudios clínicos en gatos con FIV) o si se trata solo de una pregunta de investigación.
- Complementar con datos de seguridad en gatos: la literatura advierte de efectos adversos graves con antivirales humanos en esta especie.

**Otras predicciones del modelo (para referencia):**
- **Infección por virus de inmunodeficiencia simia (SIV):** puntaje 99,96%, nivel L4. Hay abundante literatura preclínica en macacos (profilaxis pre y postexposición con tenofovir y combinaciones) y ningún ensayo clínico, ya que el SIV es una infección de primates no humanos. Se interpreta como evidencia mecanística y traslacional, no como un candidato de reposicionamiento; su equivalente humano, el VIH, ya es una indicación aprobada. En el paquete de evidencia solo se recibieron 10 de las 20 publicaciones reportadas.
- **Trastorno del neurodesarrollo con marcha atáxica, ausencia del habla y reducción de sustancia blanca cortical:** puntaje 99,96%, nivel L5, decisión Hold. No hay vínculo mecanístico plausible, ni ensayos ni literatura. Probablemente es un artefacto del grafo de conocimiento.

*Este informe es solo para fines de investigación y no constituye consejo médico ni veterinario. Cualquier candidato de reposicionamiento requiere validación clínica.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

