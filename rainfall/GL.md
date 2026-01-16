## O problema da choiva (calcular medias)

Esta proposta de tarefa baséase no clásico **"Rainfall Problem"** (Soloway, 1986) [@soloway1986learning], cuxo enunciado orixinal di:

> Design a program called RAINFALL that consumes a list of numbers representing daily rainfall amounts as entered by a user. Produce the average of the non-negative values in the list up to the first 999999 (a sentinel value).

Que podemos reformular como:

> Escribe un programa que lea números enteiros e calcule a súa media. Os números negativos introducidos deben ser ignorados. Deixa de ler cando se introduza o valor 99999.

Malia un problema aparentemente sinxelo, revela moitas dificultades cognitivas fundamentais no pensamento algorítmico:

- Comprensión de **condicións de parada** (bucles tipo *mentres*).
- Distinción entre **datos válidos e valores especiais** (uso de *sentinelas*).
- **Acumulación e contaxe** simultáneas.
- Xestión de **casos extremos** (como que ningunha entrada válida).

E de feito as investigacións indican que unha porcentaxe significativa do alumnado universitario de primeiro curso ten problemas con el. Por tanto, é unha tarefa de repaso ou diagnóstico ideal para estudantes que levan uns 3 ou 4 meses cursando materias de programación. No noso caso concreto, podería ser unha actividade final dunha materia de Programación I (ou mesmo de exame de laboratorio), ou unha actividade de diagnóstico ou toma de contacto inicial en Programación II.

Porén, ao contrario do que se podería pensar, tamén é unha tarefa na que poden xurdir distintas estratexias de resolución, habendo dúas grandes posibilidades: acumular os números nunha lista para procesar despois (calcular a media) ou ben ir acumulando os valores en dúas variables para facer o cálculo final.

### Desenvolvemento da sesión

#### Fase 1: Activación e exploración do enunciado

- **Tempo estimado**: 5'

Neste caso, o docente podería formar os grupos antes de pensar a tarefa e deixar que comecen a traballar inmediatamente tras presentar o enunciado do problema. O obxectivo, como é habitual, é que o alumnado comprenda o problema e identifique os seus elementos.

Algunhas preguntas para comezar a estimular o pensamento son:
- Cal é a entrada e saída do programa?
- Que ten de especial o 99999?
- Cantos números temos que ler? Sabémolo de antemán?

#### Fase 2: Simulación manual

- **Tempo estimado**: 20'

Proporciónanse os seguintes casos de proba e pídese que fagan unha simulación manual do que acontece en cada un:

| Caso | Entrada | Saída esperada | Propósito |
|------|---------|----------------|-----------|
| 1 | `10, 20, 30, 99999` | `20.0` | Caso básico |
| 2 | `5, 99999` | `5.0` | Un só valor |
| 3 | `99999` | `(sen datos válidos)` | Sentinela inmediato |
| 4 | `-10, -20, 99999` | `-15.0` | Números negativos |
| 5 | `0, 0, 0, 99999` | `0.0` | Ceros válidos |

O obxectivo é que empreguen a superficie vertical para simular o procesamento que deben facer de cada entrada. Sería posible pedirlles que anoten:

- Que fan con cada número?
- Que valores gardan?
- Cando teñen que parar?
- Como calculan a media?

E incluso dicirlles que no grupo unha persoa tome o rol de "cantar os números" (sería a entrada) e outro fai o procesamento (e por tanto fai anotacións no taboleiro).

Algúns erros esperables son que esquezan cantos números levan lidos, incluír o sentinela por erro ou non saber que facer se non teñen datos válidos. Sen dar solucións e deixando que pensen, o profesor segue circulando e pode lanzar preguntas como:

- "Cando vos dades conta de que chegou o 99999?"
- "Incluídes o 99999 na conta?"
- "Que valores estades gardando mentres lees?"
- "E se só vedes 99999 e máis nada?"

#### Fase 3: Posta en común e identificación de patróns

- **Tempo estimado**: 20'

Nesta fase trátase de pór en común o proceso co obxectivo de verbalizalo e identificar elementos comúns.

Pode comezarse por convidar a cada grupo a compartir brevemente a súa estratexia (2'), de xeito que o docente vai **extraendo patróns comúns** e escribíndoos nun taboleiro libre. 

Estes patróns serán que:

- Necesitamos **dúas variables**: suma e contador
- Temos un **bucle** que le números
- Hai unha **condición de parada** (cando chega 99999)
- **Despois do bucle**, dividimos suma/contador
- **Problema especial**: que pasa se contador = 0?

**Preguntas guía:**

- "Que diferenza hai entre 'ler un número' e 'procesalo'?"
- "Cantas cousas estades facendo dentro do bucle?"
- "A división faise dentro ou fóra do bucle?"

Neste punto, xa terán emerxido os conceptos de **acumuladores**, **bucle con sentinela** (*mentres*) e **validación final**.

#### Fase 4: Construción do algoritmo

- **Tempo estimado**: 15'

Nesta fase o docente indicará aos grupos que formalicen o pensamento en pasos concretos, é dicir, que produzan un algoritmo.

Este algoritmo poden facelo empregando linguaxe natural, pseudocódigo ou mesmo un diagrama de fluxo. O importante é que fagan explícito o progreso sen empregar inda unha linguaxe de programación.

Por exemplo:

```
SUBRUTINA ler_numero
  ENTRADA: ningúa
  PROCESO:
    Solicitar ao usuario que introduza un número
  SAÍDA: número

SUBRUTINA calcular_media
  ENTRADA: suma, contador
  PROCESO:
    SE contador > 0 ENTÓN
      media ← suma / contador
    SENÓ
      media ← 0 (ou mensaxe de erro)
  SAÍDA: media

PROGRAMA rainfall
  ENTRADA: ningúa (entrada interactiva)
  PROCESO:
    suma ← 0
    contador ← 0
    numero ← ler_numero()
    MENTRES numero ≠ 99999:
      SE numero ≥ 0 ENTÓN
        suma ← suma + numero
        contador ← contador + 1
      numero ← ler_numero()
    media ← calcular_media(suma, contador)
    Mostrar media
  SAÍDA: media
```

O docente circula polos grupos para:

- Detectar se distinguen entre "ler" e "procesar".
- Ver se identifican a necesidade de ler **antes** e **dentro** do bucle.
- Verificar se contemplan o caso sen datos válidos.

#### Fase 5: Casos extremos e depuración

- **Tempo estimado**: 10'

En caso de que se teñan esquecido dos casos de proba, o docente pode lembrar algúns casos extremos para que os repasen:

1. **Entrada:** `99999` (sentinela inmediato)
   - Que debería pasar?
   - O voso algoritmo xestiónaao ben?

2. **Entrada:** `0, 0, 0, 99999`
   - A media é 0? Como o diferenciades do caso sen datos?

3. **Entrada:** `-5, 5, 99999`
   - Funcionan os negativos?

4. **Entrada:** números moi grandes
   - Hai límites no noso sistema?

O obxectivo é que cada grupo revise o seu algoritmo e anote **que cambios** serían necesarios para cubrir estes casos.

As reflexións clave que deben facer son:

- Que un programa robusto ten que contemplar o inesperado.
- Que cousas non estaban previstas ao comezo?

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

- Escoller outro sentinela.
- Mostrar tamén o máximo e mínimo.
- Permitir múltiples conxuntos de datos (reiniciar tras 99999).
- Obter os datos dun ficheiro ou pasalos nunha lista ou array.
