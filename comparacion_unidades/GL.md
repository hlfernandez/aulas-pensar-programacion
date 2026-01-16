## Conversión de unidades

Esta proposta de tarefa ten como obxectivo que o alumnado acade o deseño dun programa para comparar tamaños de almacenamento expresados con unidades distintas.

A nivel de pensamento, a principal cuestión é como facer comparables as distintas unidades e o máis habitual é convertelas a unha unidade común na que facer as comparacións. A nivel técnico, o reto fundamental estará no procesamento de cadenas. Poden emerxer solucións máis orientadas á división do código en funcións ou outras que empregen mapas para almacenar as conversións de unidades básicas.

### Desenvolvemento da sesión

#### Fase 1: Activación e exploración do enunciado

- **Tempo estimado**: 5'

Comézase a sesión lanzando as seguintes pregunta ao alumnado, que estará de pé arredor do profesor: 
> Sabedes que é un bit e a cantos bytes equivale? A cantos bytes corresponde un kylobyte? E cantos bytes corresponde un kibibyte?

Tras comentar as equivalencias básicas aclaramos que traballaremos con *kibibytes*. Podemos aproveitar para explicar que significa mercar un disco de *1TB* (unidades do sistema internacional en base 10) e facer anotacións no taboleiro respecto ás convencións á hora de nomear as unidades. Como referencia:

- B: byte
- KB: 1000 bytes (sistema internacional, decimal)
- KiB: 1024 bytes (sistema binario)

Dividimos ao alumnado en grupos visiblemente aleatorios e lanzamos o reto, *como podemos deseñar un programa para determinar o resultado das seguintes comparacións entre unidades?*

```
1024B  ?  1KiB
1MiB   ?  1000KiB
1GiB   ?  1024MiB
```

#### Fase 2: Simulación manual

- **Tempo estimado**: 20'

O obxectivo é que o grupo identifique os pasos que debe seguir o programa para cada comparación, tratando de facer o proceso o máis explícito posible. Nesta fase non se permitirá escribir código, tan só pseudocódigo ou debuxos.

Ao observar como avanxan no pensamento, o profesorado pode ir facendo as seguintes preguntas para fomentar o pensamento:

- Que datos de entrada ten o programa?
- Como se vai a especificar o resultado? 
- Que información hai dentro dunha cadea como `1024MiB` e como a obtemos?
- Hai algo que teña que pasar sempre antes de comparar?

En xeral, nesta fase debería emerxer o fluxo de **extraer** (separar a cadea en valor e unidades), **transformar** (a unha unidade común ou dunha unidade á outra) e **comparar** (xa só queda comparar entre bytes para devolver -1, 0 ou 1, en función de se o primeiro é menor, se son iguais, ou se o segundo é maior).

#### Fase 3: Posta en común e identificación de patróns

- **Tempo estimado**: 15'

Nesta fase trátase de pór en común o proceso co obxectivo de verbalizalo e identificar elementos comúns.

Pode comezarse por convidar a cada grupo a compartir brevemente a súa estratexia (2'), de xeito que o docente vai **extraendo patróns comúns** e escribíndoos nun taboleiro libre. Deste xeito acaba aparecendo a estrutura comentada na fase anterior. Poden existir dúas variantes:

1. Converter ambos valores a unha unidade común (p. ex.: bytes).
2. Converter un valor ás unidades do outro de xeito que sexan comparables.

Nesta fase o docente fai fincapé na separación de responsabilidades así coma no concepto de **abstracción**.

#### Fase 4: Construción do algoritmo

- **Tempo estimado**: 15'

Nesta fase o docente indicará aos grupos que formalicen o pensamento en pasos concretos, é dicir, que produzan un algoritmo.

Este algoritmo poden facelo empregando linguaxe natural, pseudocódigo ou mesmo un diagrama de fluxo. O importante é que fagan explícito o progreso sen empregar inda unha linguaxe de programación. Farase fincapé na creación de subrutinas, de xeito que o programa principal manteña o foco na especificación de alto nivel.

Por exemplo:

```
SUBRUTINA extraer
  ENTRADA: cadea
  PROCESO:
    Separar cadea en valor_numérico e unidades
  SAÍDA: (valor_numérico, unidades)

SUBRUTINA converter_a_bytes
  ENTRADA: valor, unidades
  PROCESO:
    Buscar factor de conversión para unidades
    Calcular valor × factor
  SAÍDA: resultado_en_bytes

PROGRAMA comparar_unidades
  ENTRADA: cadea1, cadea2
  PROCESO:
    (v1, u1) ← extraer(cadea1)
    (v2, u2) ← extraer(cadea2)
    bytes1 ← converter_a_bytes(v1, u1)
    bytes2 ← converter_a_bytes(v2, u2)
    SE bytes1 < bytes2 ENTÓN
      resultado ← -1
    SE NON SE bytes1 = bytes2 ENTÓN
      resultado ← 0
    SE NON
      resultado ← 1
  SAÍDA: resultado
```

#### Fase 5: Deseño das funcións

- **Tempo estimado**: 15'

Nesta fase pedirase a cada grupo que identifique as funcións e os tipos de datos involucrados en cada un dos pasos do algoritmo obtido na fase 4. O obxectivo é que reflexionen sobre que funcións crearán, que parámetros de entrada e saída terán, e como as invocarán desde o programa xeral.

Ao ver como traballan, é preciso supervisar que reflexionan sobre:

- Representación: por exemplo, a conversión da cadea dos valores para separala en valor numérico e unidades pode facerse con tuplas.
- Conversión: a conversión pode facerse con funcións separadas ou empregando diccionarios.
- Resultado: ata agora pode que non se fixese explícito como se vai devolver o resultado, pero un booleano non é suficiente para devolver menor, igual ou maior, así que terán que codificalo dalgún xeito.

Por tanto, poden formularse preguntas coma:

- Como separamos a cadea nas dúas partes? É dicir: "1024MiB" → (1024, "MiB").
- Que tipo de datos manexa cada paso?
- Como imos codificar o resultado que se devolve?

#### Fase 6: Implementación e proba (individual)

- **Tempo estimado**: 40'

Transcorridas as fases anteriores, cun tempo estimado duns 70', esta fase consiste en pedirlle ao alumnado que faga unha implementación de xeito individual. Con sesións de laboratorio de 2 horas, sería posible deixarlles o resto de tempo da sesión para que fagan esta tarefa. Alternativamente, tamén é posible pedirlles que fagan esta parte como traballo autónomo fóra da aula.

#### Fase 7: Reflexión metacognitiva

- **Tempo estimado**: 10' (en grupo) ou individual (fóra da aula)

Esta fase de peche permite que o alumnado tome consciencia do seu propio proceso de aprendizaxe. O obxectivo é que o alumno poña de manifesto o aprendido non só sobre o problema en sí, senón tamén sobre **como pensa cando resolve problemas**, de xeito que sexa capaz de identificar os seus propios puntos fortes e áreas de mellora. Dependendo de se a implementación realízase en aula ou fóra dela, esta reflexión pode ser grupal ou individual.

Na aula, o docente reúne de novo aos grupos ou á clase completa para unha conversa guiada sobre o proceso completo. Algunhas preguntas clave:

- **Sobre o proceso de pensamento:**
  - "Que foi o máis difícil de pensar neste problema?"
  - "En que momento vos 'cadrou' o problema? Que foi o 'clic'?"
  - "Que descubristes que non sabías ao comezo?"

- **Sobre a brecha entre pensar e codificar:**
  - "Houbo diferenzas entre o que pensabades que funcionaría e o que realmente funcionou ao programar?"
  - "Que erros vos sorprenderon ao implementar?"
  - "Algo que vos parecía sinxelo resultou ser complicado? Por que?"

- **Sobre aprendizaxes transferibles:**
  - "Que estratexia ou idea deste problema poderiades usar noutros?"
  - "Se tivésedes que explicarlle a alguén a parte máis importante, cal sería?"

Se a implementación é realizada fóra da aula, podería facerse a reflexión anterior ao comezo da seguinte sesión ou ben pedirlles unha breve reflexión escrita (5-10 liñas) que acompañe ao código entregado, respondendo a 2-3 das preguntas anteriores. Isto axuda a consolidar o aprendido e proporciona información valiosa ao docente sobre as dificultades reais do alumnado.

### Posibles ampliacións

Pequenas ampliacións que se poderían facer:

- Analizar a robustez do programa (que pasa con valores como `'1024 MiB'` ou `'1024mib'`).
- Modificar o programa para soportar valores decimais (como 1.5GiB, 2.3MiB, etc.).
- Pedirlles que inclúan unidades do sistema internacional (KB, MB, GB, etc.).
- Pedirlles que escriban un pequeno programa en liña de comandos para converter valores dunha unidade a outra. Deste xeito poderán ver como reutilizar funcións para outras finalidades.
- Pedirlles que escriban un programa que lea un ficheiro cunha lista de unidades (unha por liña) e produzan a lista ordenada utilizando a función de comparación.
- Migrar o código ao paradigma de programación orientada a obxectos.