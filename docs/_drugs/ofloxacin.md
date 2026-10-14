---
layout: default
title: Ofloxacin
parent: Solo predicción del modelo (L5)
nav_order: 583
evidence_level: L5
indication_count: 10
---

# Ofloxacin
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

# Ofloxacino: De Infecciones Bacterianas a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Ofloxacino es una fluoroquinolona antibacteriana, utilizada originalmente para infecciones como la fiebre tifoidea, las infecciones urinarias, la bronquitis, la neumonía bacteriana y el carbunco.
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; se trata solo de una señal del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infecciones bacterianas (fiebre tifoidea, infecciones urinarias, bronquitis, neumonía bacteriana, carbunco, entre otras). El texto de indicación de las autorizaciones españolas no está disponible; se toma del grafo de conocimiento |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.91% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 9 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, ofloxacino pertenece a la clase de las fluoroquinolonas, que inhiben la ADN girasa y la topoisomerasa IV bacterianas, y su eficacia en infecciones bacterianas está establecida.

Sin embargo, el síndrome de hiperviscosidad policlonal es una afección hematológica ligada a proteínas e inmunoglobulinas, no a un patógeno. No se identifica un vínculo mecanístico plausible entre un antibacteriano y esta enfermedad. El puntaje alto de TxGNN refleja únicamente una predicción basada en el grafo de conocimiento, sin ensayos ni literatura que la sustenten.

Cabe señalar que otras predicciones de la lista tampoco muestran respaldo: hiperamilasemia, analbuminemia congénita y varias enfermedades hematológicas carecen de vínculo mecanístico. La única predicción biológicamente plausible es la **peste septicémica** (nivel L4), que sería una extensión del uso antibacteriano y no un reposicionamiento propiamente dicho. Se apoya en datos in vitro y modelos animales, sin ensayos en humanos.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 62560 | EXOCIN 3 MG/ML COLIRIO EN SOLUCION | Colirio en solución | No disponible |
| 82188 | FARMIFLOX 3 MG/ML COLIRIO EN SOLUCION | Colirio en solución | No disponible |
| 81022 | OFLOXACINO POS 3 MG/ML COLIRIO EN SOLUCION | Colirio en solución | No disponible |
| 59653 | OFLOVIR 200 mg COMPRIMIDOS RECUBIERTOS CON PELICULA | Comprimido recubierto | No disponible |
| 67741 | OFLOXACINO ALTAN 2 MG/ML SOLUCION PARA PERFUSION EFG | Solución para perfusión | No disponible |

Se muestran 5 de las 9 autorizaciones vigentes (todas de principio activo único).

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): síndrome de QT largo (incluido el familiar), torsades de pointes, epilepsia, insuficiencia hepática y renal, tendinitis, miastenia gravis, neuropatía periférica, rabdomiólisis, diabetes mellitus y cetoacidosis diabética, trombocitopenia, leucopenia, anemia, colitis por *Clostridium difficile*, entre otras.
- **Interacciones farmacológicas**: se identificaron 383 interacciones. Entre las de nivel **mayor** figuran hidrocortisona, triamcinolona, dexametasona, betametasona (corticoides; riesgo de tendinopatía), bupropión y clorpropamida. Entre las de nivel moderado figuran antidiabéticos (acarbosa, metformina, pioglitazona, alogliptina, canagliflozina, albiglutida), famotidina, loperamida, ácido acetilsalicílico, balsalazida, bisacodilo y suplementos de calcio y potasio.
- Un hallazgo relevante: las fluoroquinolonas se asocian a neuropatía periférica como efecto adverso, lo que va en contra de usarlas en la predicción de enfermedad hematológica asociada a neuropatía.

Consultar el prospecto para las advertencias y contraindicaciones oficiales, pues no están disponibles en los datos compilados.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción principal tiene nivel de evidencia L5: no hay ensayos, ni literatura, ni mecanismo plausible, y el puntaje alto de TxGNN no es suficiente por sí solo. Además, el perfil de seguridad es amplio y exigente.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y un vínculo mecanístico que justifique la hipótesis (hoy inexistente).
- Advertencias y contraindicaciones oficiales del prospecto de la AEMPS, y los textos de indicación aprobados.
- Estudios preclínicos o clínicos específicos en síndrome de hiperviscosidad policlonal; de lo contrario, considerar priorizar candidatas con más sustento, como la peste septicémica (L4, extensión del uso antibacteriano).
- Evaluación de compatibilidad de vía de administración y similitud con las indicaciones originales, hoy pendientes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

