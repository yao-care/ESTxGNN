---
layout: default
title: Articaine
parent: Solo predicción del modelo (L5)
nav_order: 67
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Articaine: nueva indicación predicha, Gota (nivel de evidencia L5). Indicación original: No disponible en los datos compilados (los textos de indicación de la…"
monitor_inn: "articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma"]
---

# Articaine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Informe de evaluación farmacéutica

</div>

# Articaína: De Anestesia Local a Gota

## Resumen en Una Frase

Articaína es un anestésico local de tipo amida, comercializado en España en combinación con epinefrina (adrenalina) en solución inyectable.
El modelo TxGNN predice que podría ser efectivo para **gota**, pero no existen **ensayos clínicos** ni **publicaciones** que respalden esta dirección: se trata únicamente de una predicción computacional.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible en los datos compilados (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Gota |
| Puntaje de Predicción TxGNN | 99.58% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 12 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, articaína es un anestésico local de tipo amida que bloquea los canales de sodio dependientes de voltaje, y su uso establecido es la anestesia local (principalmente en odontología).

**No se identifica un vínculo mecanístico plausible** entre este mecanismo y la gota. Nada en los datos conecta el bloqueo de canales de sodio con el metabolismo del ácido úrico ni con la cascada inflamatoria de la gota (por ejemplo, NLRP3/IL-1β). El puntaje alto de TxGNN (99.58%) es una predicción computacional que, por sí sola, no constituye evidencia de eficacia; probablemente refleja similitudes de red en el grafo de conocimiento y no una justificación farmacológica definida.

Otras predicciones del modelo (exóstosis, asma alérgica, asma intrínseca) tampoco cuentan con respaldo mecanístico ni clínico. La similitud con la indicación original está pendiente de evaluación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para gota.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 68104 | Articaína/Epinefrina Dermogen 40 mg/ml + 5 µg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 61194 | Meganest 40 mg/ml + 10 µg/ml solución inyectable | Solución inyectable | No disponible |
| 59942 | Septanest con adrenalina 40 mg/ml + 10 µg/ml solución inyectable | Solución inyectable en cartucho | No disponible |
| 68103 | Articaína/Epinefrina Dermogen 40 mg/ml + 10 µg/ml solución inyectable EFG | Solución inyectable | No disponible |
| 89153 | Articaína/Epinefrina Normon 40 mg/ml + 5 µg/ml solución inyectable EFG | Solución inyectable | No disponible |

Se muestran 5 de las 12 autorizaciones vigentes.

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (TxGNN/PrimeKG, no proviene del texto del prospecto)**: hipertensión, enfermedad renal, enfermedad hepática, enfermedad de la vesícula biliar, diabetes mellitus y cetoacidosis diabética, enfermedad coronaria e infarto de miocardio, parada cardíaca súbita, enfermedad del sistema de conducción cardíaco, miocardiopatía dilatada, glaucoma de ángulo cerrado, miastenia gravis y enfermedades de la unión neuromuscular, deficiencia de butirilcolinesterasa, hipertiroidismo (enfermedad de Graves, tiroticosis), enfermedad de Parkinson y hemoglobinopatías.
- **Interacciones Farmacológicas** (10 identificadas):
  - **Mayor**: ácido nitroso.
  - **Moderada**: morfina liposomal, benzocaína tópica, lidocaína (oftálmica y tópica), oxibuprocaína oftálmica, cinchocaína tópica, tetracaína (oftálmica y tópica).
  - **Menor**: hialuronidasa.
- **Hipersensibilidad**: la literatura recuperada para asma alérgica trata de alergia a anestésicos locales, no de eficacia terapéutica, y apunta a una consideración de hipersensibilidad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para gota se basa solo en el modelo (nivel L5), sin ensayos clínicos, sin literatura y sin vínculo mecanístico plausible. Dado el perfil de un anestésico local con vasoconstrictor, no hay base actual para avanzar.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias y contraindicaciones), cuya ausencia bloquea el cribado de seguridad.
- Completar los datos del mecanismo de acción (por ejemplo, desde DrugBank).
- Definir una hipótesis mecanística concreta que conecte el bloqueo de canales de sodio con la fisiopatología de la gota, y respaldarla con estudios preclínicos.
- Evaluar la compatibilidad de vías de administración (las formulaciones actuales son inyectables de uso local/dental).
- Reevaluar la utilidad de otras predicciones solo si aparece evidencia independiente.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

