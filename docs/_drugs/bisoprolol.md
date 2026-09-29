---
layout: default
title: Bisoprolol
parent: Solo predicción del modelo (L5)
nav_order: 78
evidence_level: L5
indication_count: 5
---

# Bisoprolol
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Bisoprolol: De Indicación Original No Registrada a Enfermedad Renal Hipertensiva Maligna

## Resumen en Una Frase

Bisoprolol es un betabloqueante con 20 autorizaciones en España, pero los datos recibidos no incluyen el texto de su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para la **enfermedad renal hipertensiva maligna**, con una puntuación muy alta (99,94 %).
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que la predicción no tiene respaldo independiente.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones están vacíos) |
| Nueva Indicación Predicha | Enfermedad renal hipertensiva maligna |
| Puntaje de Predicción TxGNN | 99,94 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 20 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, bisoprolol es un betabloqueante selectivo beta-1, por lo que reducir la presión arterial es plausible en principio. Sin embargo, esto es una inferencia por clase farmacológica y no proviene de los datos aportados.

La hipertensión maligna es una emergencia hipertensiva que se maneja con fármacos por vía parenteral. Nada en los datos respalda que un betabloqueante oral sea adecuado en este escenario. La única base de la predicción es la puntuación de TxGNN.

Otras predicciones del modelo siguen el mismo patrón, todas en nivel L5 y sin ensayos clínicos:

- **Hipertensión renovascular maligna** (99,94 %): el bloqueo beta-1 reduce la liberación de renina, lo que es biológicamente plausible, pero solo por inferencia de clase.
- **Hipertensión pulmonar por enfermedad pulmonar o hipoxia** (99,93 %): sin vínculo mecanístico específico. Los betabloqueantes podrían plantear un problema de seguridad en pacientes con enfermedad pulmonar e hipoxia.
- **Hipertensión pulmonar de mecanismo multifactorial poco claro** (99,93 %): sin datos que permitan construir una hipótesis.
- **Síndrome de Braddock** (99,91 %): sin ningún vínculo identificable.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para la enfermedad renal hipertensiva maligna.

Para la predicción de hipertensión pulmonar por hipoxia se recuperaron 20 artículos (se mostraron 10). Son revisiones y trabajos generales de biología de la hipoxia, y ninguno parece estudiar bisoprolol ni betabloqueantes en hipertensión pulmonar. No se consideran evidencia de apoyo.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 57543 | EURADAL 10 mg comprimidos recubiertos con película | Comprimido recubierto |
| 73633 | BISOPROLOL COR VIATRIS 5 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 85878 | BISOPROLOL ZENTIVA 7,5 MG comprimidos EFG | Comprimido |
| 90545 | BISOPROLOL STADAFARMA 1,25 MG comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 82243 | BISOPROLOL STADA 10 MG comprimidos EFG | Comprimido |

Se muestran 5 de las 20 autorizaciones. Los textos de indicación aprobada no figuran en los datos recibidos.

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el modelo (nivel L5), sin ensayos ni literatura específica. Además, la enfermedad predicha es una emergencia que se trata por vía parenteral y no hay datos que respalden un betabloqueante oral.

**Para avanzar se necesita:**
- Obtener el prospecto de la AEMPS con advertencias y contraindicaciones, un dato bloqueante para el cribado de seguridad.
- Completar los datos del mecanismo de acción desde DrugBank.
- Recuperar la indicación aprobada de las autorizaciones españolas para definir la indicación original.
- Buscar literatura o ensayos específicos de bisoprolol o betabloqueantes en hipertensión maligna y renovascular.
- Evaluar la compatibilidad de vía de administración, hoy pendiente, dado que la hipertensión maligna requiere terapia parenteral.
- Revisar la seguridad de los betabloqueantes en pacientes con enfermedad pulmonar e hipoxia antes de considerar las predicciones de hipertensión pulmonar.

*Este informe es solo de referencia para investigación y no constituye consejo médico. Los candidatos de reposicionamiento requieren validación clínica antes de cualquier aplicación.*
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

