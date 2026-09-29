---
layout: default
title: Degarelix
parent: Solo predicción del modelo (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Degarelix
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

# Degarelix: De Indicación Original No Registrada a Hipertricosis

## Resumen en Una Frase

Degarelix es un antagonista del receptor de GnRH que reduce la LH y la testosterona; el registro de AEMPS incluido en los datos no detalla su indicación original.
El modelo TxGNN predice que podría ser efectivo para **hipertricosis**, pero **no hay ensayos clínicos ni publicaciones** que respalden esta predicción.
Se trata de una predicción puramente computacional, con un vínculo mecanístico débil.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No disponible (los textos de indicación de las autorizaciones de AEMPS están vacíos) |
| Nueva Indicación Predicha | Hipertricosis |
| Puntaje de Predicción TxGNN | 99.99% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 2 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Degarelix es un antagonista del receptor de GnRH. Bloquea la señal hipofisaria que estimula la producción de LH y, por tanto, reduce la testosterona. Actualmente no se dispone de datos detallados del campo de mecanismo de acción en DrugBank; esta descripción procede del análisis mecanístico del propio Evidence Pack.

La lógica de la predicción sería que un descenso de andrógenos podría reducir el crecimiento excesivo de vello. Sin embargo, la mayoría de las hipertricosis no dependen de andrógenos, por lo que el vínculo es débil y no está respaldado por datos. El puntaje alto del modelo (99.99%) refleja conectividad en el grafo de conocimiento, no evidencia biológica ni clínica.

Otras predicciones de la lista tampoco tienen sustento:
- **Hipertricosis universal congénita de Ambras:** trastorno congénito no mediado por andrógenos.
- **Anomalías genéticas aisladas del tallo piloso:** defectos estructurales sin respuesta hormonal.
- **Pubertad precoz masculina familiar:** es la más cercana biológicamente, pero depende de mutaciones activadoras de LHCGR y es independiente de GnRH, así que un antagonista de GnRH no debería funcionar.
- **Pubertad precoz central:** es mecanísticamente plausible, pero los agonistas de GnRH son el tratamiento estándar y degarelix no tiene datos pediátricos. Queda solo como pregunta de investigación.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible para hipertricosis.

Las publicaciones recuperadas en el Evidence Pack corresponden a otra predicción (síndrome de malformación con componente dental o periodontal) y tratan de la periodontitis en general. Ninguna menciona degarelix ni antagonistas de GnRH, así que son coincidencias de palabras clave y no evidencia del fármaco.

---

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Fabricante |
|---------|------|------|-----------|
| 08504002 | FIRMAGON 120 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | Ferring Pharmaceuticals A/S |
| 08504001 | FIRMAGON 80 mg polvo y disolvente para solución inyectable | Polvo y disolvente para solución inyectable | Ferring Pharmaceuticals A/S |

El texto de indicación aprobada no figura en los datos de ambas autorizaciones.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

Como señal indirecta, el análisis de la predicción de urticaria alérgica indica que degarelix se asocia con reacciones en el lugar de inyección y, raramente, con hipersensibilidad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Todas las predicciones están en nivel L5 (solo modelo), sin ensayos ni literatura específica del fármaco. El mecanismo no respalda la hipertricosis, que en su mayoría no depende de andrógenos.

**Para avanzar se necesita:**
- Obtener del prospecto de AEMPS las advertencias, las contraindicaciones y la indicación aprobada.
- Completar los datos del mecanismo de acción desde DrugBank.
- Realizar una búsqueda dirigida en la literatura sobre degarelix o antagonistas de GnRH en hipertricosis, para comprobar si existe alguna evidencia.
- Si se quiere explorar la pubertad precoz central (única hipótesis mecanísticamente plausible), justificar una ventaja sobre los agonistas de GnRH y aportar datos de seguridad pediátrica.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

