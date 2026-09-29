---
layout: default
title: Ciclesonide
parent: Solo predicción del modelo (L5)
nav_order: 125
evidence_level: L5
indication_count: 6
---

# Ciclesonide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **6** 
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

# Ciclesonida: De Asma Persistente a Eccema Atópico

## Resumen en Una Frase

Ciclesonida es un corticosteroide inhalado que se usa para tratar enfermedades inflamatorias y obstructivas de las vías respiratorias, como el asma persistente. El modelo TxGNN predice que podría ser efectivo para **eccema atópico**, pero **no hay ensayos clínicos ni publicaciones** específicos de ciclesonida que respalden esta dirección. La predicción se basa solo en el modelo y en el efecto de clase de los corticosteroides.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Asma persistente (según la farmacología del ligando; las autorizaciones españolas no incluyen texto de indicación) |
| Nueva Indicación Predicha | Eccema atópico |
| Puntaje de Predicción TxGNN | 99.96% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Ciclesonida es un agonista del receptor de glucocorticoides (NR3C1). Es un profármaco inhalado: las esterasas del pulmón lo convierten en su metabolito activo, desisobutirilciclesonida. Este metabolito tiene mucha más afinidad por el receptor que el fármaco original (IC50 de 1,75 nM frente a 210 nM). La activación del receptor produce un efecto antiinflamatorio e inmunosupresor amplio.

Los corticosteroides son una clase establecida para el eccema atópico, y de ahí viene el puntaje alto del modelo. Es una predicción a nivel de clase dentro del grafo de conocimiento, no un hallazgo específico de ciclesonida. Además, el término "dermatitis atópica" (puntaje 99.73%) es sinónimo de "eccema atópico" y debe fusionarse con él para no contar la señal dos veces.

Hay una limitación importante. No está establecido si ciclesonida se activa en la piel, cuánta exposición dérmica alcanzaría ni qué vía o dosis serían adecuadas (tópica o sistémica). Se diseñó como profármaco para activarse en el pulmón, por lo que su comportamiento en piel es incierto.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 70372 | ALVESCO 160 microgramos/INHALACIÓN solución para inhalación en envase a presión (Covis Pharma Europe B.V.) | Solución para inhalación en envase a presión |
| 05-0019 | ALVESCO 160 microgramos/INHALACIÓN solución para inhalación en envase a presión (Takeda GmbH) | Solución para inhalación en envase a presión |

Los registros no incluyen texto de indicación aprobada. Solo existe la presentación inhalada, sin formulación tópica.

---

## Consideraciones de Seguridad

- **Señal de sensibilización cruzada**: un informe de caso (PMID 22957490, 2012) describe una dermatitis alérgica sistémica causada por budesonida inhalada, con reactividad cruzada en pruebas de parche con ciclesonida. No es evidencia de eficacia. Indica que un corticosteroide puede causar dermatitis y que existe posible sensibilización cruzada, algo relevante para cualquier uso dermatológico.

Para el resto de la información de seguridad, consultar el prospecto.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción es de nivel L5: solo el modelo, sin ensayos ni literatura de ciclesonida en eccema atópico. El puntaje alto refleja el efecto de clase de los corticosteroides, y la vía de administración para piel no está validada. Existen alternativas corticosteroides ya establecidas y optimizadas para uso cutáneo.

**Para avanzar se necesita:**
- Confirmar las indicaciones aprobadas y la información de seguridad en la ficha técnica de la AEMPS.
- Revisar si ciclesonida se activa en la piel y qué exposición dérmica alcanzaría.
- Buscar estudios preclínicos o clínicos de ciclesonida en dermatitis atópica.
- Definir la vía y la formulación viables (tópica frente a sistémica).
- Evaluar el riesgo de sensibilización cruzada entre corticosteroides.

**Otras predicciones del modelo (no seleccionadas como principal):** bronquitis y dermatitis de contacto tienen solo evidencia indirecta (una guía de EPOC y un informe de caso de seguridad, respectivamente). "Sensibilización a metacrilato de 2-hidroxietilo" y "rasgos de susceptibilidad al asma" no son indicaciones tratables. Esta última probablemente refleja el uso ya conocido del fármaco en asma.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

