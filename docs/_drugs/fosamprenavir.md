---
layout: default
title: Fosamprenavir
parent: Solo predicción del modelo (L5)
nav_order: 244
evidence_level: L5
indication_count: 7
---

# Fosamprenavir
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **7** 
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

# Fosamprenavir: De Infección por VIH-1 (inferida por clase terapéutica) a Síndrome de Inmunodeficiencia Adquirida Felina

## Resumen en Una Frase

Fosamprenavir es un profármaco de amprenavir, un inhibidor de la proteasa del VIH-1. Está comercializado en España como Telzir, aunque el registro disponible no incluye el texto de la indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para el **síndrome de inmunodeficiencia adquirida felina (FIV)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección. Es una hipótesis basada solo en la predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No consta en el registro de autorizaciones. Por su clase farmacológica se infiere infección por VIH-1 |
| Nueva Indicación Predicha | Síndrome de inmunodeficiencia adquirida felina (enfermedad veterinaria) |
| Puntaje de Predicción TxGNN | 99.88% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en el paquete de evidencia. Según la clase conocida, fosamprenavir es un profármaco de amprenavir, un inhibidor de la proteasa del VIH-1. Este mecanismo es propio de su clase y no procede de los datos suministrados. Esta enzima es necesaria para que el virus madure y produzca partículas infecciosas.

El virus de la inmunodeficiencia felina (FIV) es un lentivirus, como el VIH, y tiene su propia proteasa. Por eso existe una justificación mecanística a nivel de clase. Sin embargo, la proteasa del FIV tiene una especificidad de sustrato e inhibidores distinta de la del VIH-1, así que cabe esperar una actividad de amprenavir más débil. El vínculo es plausible pero no está verificado, y al tratarse de una enfermedad veterinaria, su relevancia para el reposicionamiento en humanos es limitada.

La segunda predicción del modelo, la infección por el virus de la inmunodeficiencia de simios (SIV), tiene exactamente el mismo puntaje. El SIV es un patógeno de modelos en primates no humanos y está muy emparentado con el VIH. Es probable que la predicción refleje la cercanía con el VIH en el grafo de conocimiento y no una indicación nueva. Las demás predicciones (un trastorno del neurodesarrollo y varias enfermedades mamarias benignas de tipo fibroquístico) no tienen un vínculo mecanístico identificable. Probablemente son artefactos del grafo, y las entradas mamarias parecen un mismo grupo redundante.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 04282002 | TELZIR 50 MG/ML SUSPENSIÓN ORAL | Suspensión oral | No especificada en el registro |
| 04282001 | TELZIR 700 MG COMPRIMIDOS RECUBIERTOS CON PELÍCULA | Comprimido recubierto con película | No especificada en el registro |

Ambas autorizaciones pertenecen a Viiv Healthcare B.V.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción solo tiene respaldo del modelo (L5): no hay ensayos ni literatura, y la enfermedad es veterinaria, con relevancia limitada para humanos. La actividad de amprenavir sobre la proteasa del FIV es probablemente débil. Las predicciones restantes (SIV y enfermedades mamarias benignas) no aportan una indicación nueva ni tienen sustento mecanístico.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS (advertencias, contraindicaciones e indicación aprobada), que es un vacío bloqueante para el cribado de seguridad
- Consultar en DrugBank el mecanismo de acción detallado
- Buscar estudios in vitro o preclínicos de amprenavir frente a la proteasa del FIV
- Definir si el interés está en medicina veterinaria o en modelos animales, ya que esta línea no tiene aplicación humana directa
- Evaluar la compatibilidad de vías de administración, hoy pendiente
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

