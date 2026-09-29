---
layout: default
title: Enzalutamide
parent: Solo predicción del modelo (L5)
nav_order: 203
evidence_level: L5
indication_count: 7
---

# Enzalutamide
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

# Enzalutamida: De Cáncer de Próstata a Susceptibilidad al Cáncer de Próstata/Cerebral

## Resumen en Una Frase

Enzalutamida es un inhibidor del receptor de andrógenos, utilizado originalmente para el cáncer de próstata avanzado resistente a la castración.
El modelo TxGNN predice que podría ser efectivo para **susceptibilidad al cáncer de próstata/cerebral**, con una puntuación muy alta (99,71 %).
Sin embargo, actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción concreta.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Cáncer de próstata avanzado resistente a la castración (según la información farmacológica de DrugBank; las fichas de AEMPS del paquete no incluyen el texto de indicación) |
| Nueva Indicación Predicha | Susceptibilidad al cáncer de próstata/cerebral |
| Puntaje de Predicción TxGNN | 99,71 % |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 17 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Enzalutamida actúa sobre el receptor de andrógenos (gen *AR*). Bloquea la unión del ligando, la translocación al núcleo y la unión al ADN. Por eso frena el crecimiento de tumores que dependen de andrógenos. El paquete de datos no incluye una descripción detallada del mecanismo de acción, así que esta explicación se basa en la información farmacológica disponible.

La puntuación alta probablemente refleja la fuerte conexión entre el receptor de andrógenos y el cáncer de próstata en el grafo de conocimiento. Hay que tener cuidado con la interpretación. "Susceptibilidad al cáncer de próstata/cerebral" es un fenotipo de predisposición, no una enfermedad tratable. Por eso es difícil traducir esta predicción en una indicación clínica concreta.

En resumen, el mecanismo es plausible para el componente de próstata, pero la predicción es solo del modelo. No se recuperó ningún ensayo ni publicación que la respalde.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

| Número de Autorización | Nombre del Producto | Forma Farmacéutica |
|---------|------|------|
| 89057 | Enzalutamida Sandoz 80 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 113846002 | Xtandi 40 mg comprimidos recubiertos con película | Comprimido recubierto con película |
| 89615 | Enzalutamida Accord 40 mg cápsulas blandas EFG | Cápsula blanda |
| 1241842002 | Enzalutamida Viatris 40 mg comprimidos recubiertos con película EFG | Comprimido recubierto con película |
| 113846001 | Xtandi 40 mg cápsulas blandas | Cápsula blanda |

Se muestran 5 de las 17 autorizaciones. Los datos recibidos no incluyen el texto de indicación aprobada.

## Citotoxicidad

| Item | Contenido |
|------|------|
| Clasificación de Citotoxicidad | Terapia dirigida hormonal (inhibidor del receptor de andrógenos); no es un citotóxico convencional |
| Riesgo de Mielosupresión, Emetogenicidad, Items de Monitoreo y Protección en Manejo | Consultar las advertencias y precauciones del prospecto |

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción tiene un puntaje alto (99,71 %), pero es solo del modelo (L5), sin ensayos ni literatura. Además, el término predicho es un fenotipo de susceptibilidad y no una enfermedad tratable.

Otras entradas de la misma lista, como "neoplasia benigna del sistema reproductor" y "cáncer de órgano reproductor masculino", corresponden en la práctica al cáncer de próstata. Es una indicación ya autorizada, con ensayos de Fase 3. Por tanto, no constituye reposicionamiento novedoso. Si el objetivo es evaluar una indicación nueva, conviene revisar las predicciones de rango 2, 4 y 7 (leiomioma, fibroma y tumor filoides benigno de próstata). Estas tampoco tienen evidencia hasta ahora.

**Para avanzar se necesita:**
- Redefinir la indicación objetivo con un término de enfermedad tratable, en lugar de un fenotipo de susceptibilidad
- Descargar y analizar el prospecto de AEMPS (advertencias y contraindicaciones)
- Obtener datos detallados del mecanismo de acción (MOA) desde DrugBank
- Búsqueda dirigida de ensayos y literatura específicos para la indicación objetivo elegida
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

