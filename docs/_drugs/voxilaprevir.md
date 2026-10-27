---
layout: default
title: Voxilaprevir
parent: Solo predicción del modelo (L5)
nav_order: 860
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Voxilaprevir: nueva indicación predicha, Infección por virus de la hepatitis B (nivel de evidencia L5). Indicación original: Infección crónica por el virus de la hepatitis C"
monitor_inn: "voxilaprevir"
predicted_indications: ["hepatitis B virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection", "Omsk hemorrhagic fever", "Kyasanur forest disease", "HIV infectious disease", "chronic hepatitis B virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome"]
---

# Voxilaprevir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
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

## Voxilaprevir: De Infección por Virus de la Hepatitis C a Infección por Virus de la Hepatitis B
{: .text-alpha }

## Resumen en Una Frase

Voxilaprevir es un inhibidor de la proteasa NS3/4A del virus de la hepatitis C (VHC), utilizado originalmente para tratar la infección crónica por VHC, y se comercializa en Espana dentro de la combinación Vosevi.
El modelo TxGNN predice que podría ser efectivo para **infección por virus de la hepatitis B**, pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Infección crónica por el virus de la hepatitis C |
| Nueva Indicación Predicha | Infección por virus de la hepatitis B |
| Puntaje de Predicción TxGNN | 99,84% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 1 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrados para este informe. Según la información conocida, voxilaprevir es un inhibidor de la proteasa NS3/4A del VHC que se administra en combinación con sofosbuvir y velpatasvir, y su eficacia en la hepatitis C está bien establecida.

La relación mecanística con la hepatitis B es débil. El VHB no codifica una proteasa de tipo NS3/4A; sus dianas clave son la polimerasa y la cápside/core. El puntaje elevado de TxGNN parece reflejar sobre todo asociaciones de grafo compartidas dentro de la categoría "hepatitis viral", y no una base farmacológica concreta.

Además, la necesidad terapéutica en hepatitis B ya está cubierta por los análogos de nucleós(t)idos. Por ello la predicción debe considerarse una hipótesis computacional sin respaldo experimental.

**Otras predicciones del modelo (todas con nivel L5, salvo VIH en L4, y decisión Hold):** hepatitis E (99,71%), hepatitis viral animal (99,70%), hepatitis A (99,70%), fiebre hemorrágica de Omsk (99,70%), enfermedad del bosque de Kyasanur (99,69%), infección por VIH (99,32%), hepatitis B crónica (99,21%), infección por virus de inmunodeficiencia simia (99,07%) e inmunodeficiencia adquirida felina (99,07%). Solo en los flavivirus (Omsk y Kyasanur) existe un vínculo especulativo, por la proteasa NS2B/NS3 distantemente homóloga a la del VHC; no hay datos que demuestren inhibición por voxilaprevir.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados para la hepatitis B.

*Nota:* para otras indicaciones predichas aparecen ensayos que son en realidad estudios de VHC (por ejemplo, NCT02185794, NCT02402452, NCT04695769 para hepatitis A; NCT03823911 para VIH). Se trata de evidencia indirecta, no evalúan voxilaprevir en esas enfermedades y no respaldan las nuevas indicaciones.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la hepatitis B.

*Nota:* la literatura asociada a la predicción de VIH (revisiones sobre antivirales de acción directa, estudios de retratamiento de VHC en pacientes coinfectados) trata del uso de voxilaprevir en VHC y no respalda una indicación anti-VIH.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 1171223001 | VOSEVI 400 MG/100 MG/100 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No disponible en los datos compilados (titular: Gilead Sciences Ireland Unlimited Company) |

---

## Consideraciones de Seguridad

- **Interacciones Farmacológicas:** se identificaron 19 interacciones. Las de gravedad **mayor** son:
  - Rosuvastatina
  - Edoxabán
  - Ciclosporina

  Las de gravedad **moderada** incluyen eluxadolina, ácido obeticólico, cobicistat, apixabán, eltrombopag, artesunato, afatinib, bosutinib, cobimetinib, etinilestradiol, idelalisib, lapatinib, lenvatinib, olaparib, pazopanib y teriflunomida.

Para advertencias y contraindicaciones, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se basa únicamente en el modelo (nivel L5), sin ensayos ni literatura, y el VHB no posee una diana mecanísticamente comparable a la proteasa NS3/4A. Además, existen tratamientos eficaces para la hepatitis B.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y evidencia preclínica (por ejemplo, ensayos in vitro de actividad anti-VHB)
- Revisión de advertencias y contraindicaciones del prospecto de la AEMPS
- Análisis de la relación de similitud con la indicación original y de la compatibilidad de vías de administración
- Evaluación del riesgo de interacciones mayores (rosuvastatina, edoxabán, ciclosporina) si se planteara un estudio
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

