---
layout: default
title: Doxylamine
parent: Solo predicción del modelo (L5)
nav_order: 266
evidence_level: L5
indication_count: 4
---

# Doxylamine
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **4** 
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

# Doxilamina: De Rinitis Alérgica a Urticaria Alérgica

## Resumen en Una Frase

Doxilamina es un antihistamínico H1 de primera generación, cuyas indicaciones de partida en el grafo de conocimiento incluyen la rinitis alérgica, el resfriado común y la urticaria.
El modelo TxGNN predice que podría ser efectivo para **urticaria alérgica**, con un puntaje del 99.85%.
Actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección, por lo que se trata únicamente de una predicción del modelo.

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Rinitis alérgica (las autorizaciones de AEMPS no incluyen texto de indicación; se toma la primera indicación del grafo de conocimiento) |
| Nueva Indicación Predicha | Urticaria alérgica |
| Puntaje de Predicción TxGNN | 99.85% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en España | ✓ Comercializado |
| Número de Autorizaciones | 18 |
| Decisión Recomendada | Hold |

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, doxilamina es un antihistamínico H1 de primera generación con efectos anticolinérgicos y sedantes. Su eficacia en cuadros alérgicos de las vías respiratorias y de la piel figura entre sus indicaciones de partida, y mecanísticamente podría ser aplicable a la urticaria alérgica mediante el bloqueo H1 de la respuesta de habón y eritema mediada por histamina.

La urticaria ya aparece entre las indicaciones originales del fármaco, y la urticaria alérgica es un subtipo de ese cuadro. Por ello, esta predicción se parece más a una extensión cercana de una indicación existente que a un reposicionamiento genuino.

Las demás predicciones del modelo siguen la misma lógica, también con evidencia L5 y recomendación Hold:
- **Enfermedad de la cavidad nasal** (99.36%): categoría amplia que solapa con la rinitis alérgica, la rinitis vasomotora y el resfriado común.
- **Laringofaringitis aguda** (99.34%): relacionada con la faringitis y la nasofaringitis; el beneficio sería sintomático y el cuadro suele ser infeccioso.
- **Urticaria por frío** (99.26%): urticaria inducible mediada por histamina; en general se prefieren antihistamínicos de segunda generación por la sedación.

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

## Información de Mercado en España

Se muestran 5 de las 18 autorizaciones vigentes (todas de medicamentos con un único principio activo). Los datos compilados no incluyen el texto de la indicación aprobada.

| Número de Autorización | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 83322 | DOXIMAX 12,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 80704 | DOXILAMINA SANDOZ CARE 25 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 77281 | DOXILAMINA ESTEVE 12,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 60154 | DORMIDINA DOXILAMINA 12,5 mg comprimidos recubiertos con película | Comprimido recubierto con película | No disponible |
| 80761 | SOÑODOR DOXILAMINA 25 mg polvo oral | Polvo oral | No disponible |

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento** (no proceden del prospecto): hipertensión, insuficiencia y enfermedad hepática, pancreatitis, enfermedad de la vesícula biliar, úlcera péptica, diabetes mellitus y cetoacidosis diabética, hiperplasia benigna de próstata, obstrucción del cuello vesical, glaucoma de ángulo cerrado e hipertensión ocular, enfermedad coronaria, infarto de miocardio, aterosclerosis, taquicardia ventricular, hipertiroidismo (enfermedad de Graves, tirotoxicosis), hemoglobinopatía, abuso o dependencia de sustancias e intoxicación por paracetamol.
- **Interacciones farmacológicas**: se registraron 100 interacciones; entre las mostradas:
  - **Mayores**: cloruro de potasio y citrato de potasio.
  - **Moderadas**: anticolinérgicos (hioscina/escopolamina, atropina, glicopirronio, diciclomina, clidinio, propantelina, metescopolamina, mepenzolato), opioides y relacionados (morfina, opio, loperamida, eluxadolina), cannabinoides (dronabinol, nabilona) y metoclopramida. Es esperable un efecto aditivo sobre el sistema nervioso central y anticolinérgico.

Para las advertencias del prospecto, consultar el prospecto de AEMPS, ya que no se dispuso de ellas.

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
Las cuatro predicciones tienen un puntaje alto, pero no cuentan con ensayos clínicos ni literatura, es decir, nivel L5. Además, se solapan con indicaciones ya conocidas del fármaco, por lo que aportan poco valor de reposicionamiento. Además, falta la información del prospecto de AEMPS (advertencias y contraindicaciones), lo que impide avanzar a la evaluación de seguridad.

**Para avanzar se necesita:**
- Obtener y analizar el prospecto de AEMPS (advertencias, contraindicaciones y texto de las indicaciones aprobadas).
- Completar los datos del mecanismo de acción desde DrugBank.
- Revisar la literatura y los registros de ensayos sobre doxilamina en urticaria alérgica y urticaria por frío.
- Evaluar si las predicciones representan una indicación nueva o solo una extensión de las ya autorizadas.
- Valorar el perfil de seguridad (sedación, efectos anticolinérgicos y las contraindicaciones señaladas) frente a los antihistamínicos de segunda generación.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

