## 💡 Sesión: *Pensar como un programa — calcular medias*

**Duración:** 90 minutos
**Nivel:** 1º de Grao en Enxeñaría Informática / IA
**Tamaño de grupo:** 15 estudantes (3–4 por grupo)
**Enfoque:** *Aulas para pensar* — metacognición, colaboración e pensamento algorítmico básico

---

### 📌 **Nota para o profesor**

⚠️ **Contexto:** Esta actividade baséase no clásico **"Rainfall Problem"** (Soloway, 1986), un problema aparentemente sinxelo que revela moitas dificultades cognitivas fundamentais no pensamento algorítmico:
- Comprensión de **condicións de parada**
- Distinción entre **datos válidos e valores especiais** (sentinela)
- **Acumulación e contaxe** simultáneas
- Xestión de **casos extremos** (ningunha entrada válida)

**Como xestionalo:**
- **Non menosprezar a dificultade:** Aínda que parece trivial, múltiples estudos mostran que máis do 30% dos estudantes de primeiro curso ten dificultades.
- **Deixar que emerxan os erros:** Permitir que os grupos descubran por si mesmos problemas como "contar o 99999 na media" ou "dividir por cero".
- **Validar todas as aproximacións:** Haberá solucións moi diferentes; céntrate na xustificación do pensamento, non só na corrección.

Isto serve como **diagnóstico inicial** do pensamento algorítmico e como **base** para actividades máis complexas.

---

### 🎯 Obxectivos de aprendizaxe

| Dimensión     | Obxectivo                                                                      |
| ------------- | ------------------------------------------------------------------------------ |
| Cognitiva     | Identificar os elementos básicos dun algoritmo: entrada, proceso, saída.       |
| Metacognitiva | Recoñecer e verbalizar as propias dificultades ao descompoñer un problema.     |
| Técnica       | Distinguir entre valor sentinela e datos válidos; xestionar acumuladores.      |
| Social        | Comunicar o pensamento algorítmico de forma clara a outros.                    |

---

### 🧰 Materiais e preparación

* Follas **A3** en branco ou plantilla (ver abaixo).
* Rotuladores, celo para pegar nas paredes.
* **Tarxetas con números** (opcional): para simular entradas físicamente.
* Pizarra ou pantalla para resumo final.

#### 📋 **Enunciado orixinal (para proxectar ou imprimir)**

```
Write a program that will read in integers and output their average.
Stop reading when the value 99999 is input.
```

**Variante en galego:**

```
Escribe un programa que lea números enteiros e calcule a súa media.
Deixa de ler cando se introduza o valor 99999.
```

#### 📊 **Casos de proba recomendados**

| Caso | Entrada | Saída esperada | Propósito |
|------|---------|----------------|-----------|
| 1 | `10, 20, 30, 99999` | `20.0` | Caso básico |
| 2 | `5, 99999` | `5.0` | Un só valor |
| 3 | `99999` | `(sen datos válidos)` | Sentinela inmediato |
| 4 | `-10, -20, 99999` | `-15.0` | Números negativos |
| 5 | `0, 0, 0, 99999` | `0.0` | Ceros válidos |

💡 *A plantilla A3 ten 3 zonas:*

1. 🧩 **Pasos do algoritmo** (que fago primeiro? despois? cando paro?)
2. 🧠 **Decisións e dificultades** (que problemas atopei? como os resolvo?)
3. 💻 **Estrutura do código** (variables, condicións, bucles)

---

## 🕒 **Desenvolvemento da sesión (90 min)**

---

### 🔹 **Fase 1 – Activación e exploración do enunciado (10 min)**

**Obxectivo:** que o alumnado comprenda o problema e identifique os seus elementos.

Instrución:

> "Lede o enunciado. En parellas, identificade:
> - Que entra no programa?
> - Que sae?
> - Que significa 'average'?
> - Que ten de especial o 99999?"

**Preguntas para provocar pensamento:**

* Cantos números temos que ler? Sabémolo de antemán?
* O 99999 é un dato máis ou ten un significado especial?
* Que pasa se non hai números antes do 99999?

💭 O docente **anota na pizarra** as respostas e introduce o termo **"valor sentinela"** ou **"valor de parada"**.

---

### 🔹 **Fase 2 – Simulación manual en grupos (20 min)**

**Obxectivo:** experimentar o proceso paso a paso, manualmente.

Tarefa:
Cada grupo recibe un **caso de proba** (dos de arriba) en formato de tarxetas ou lista escrita.

Instrución:

> "Sen usar ordenador nin escribir código, procesade estes números como o faría o programa.
> Anotade no A3:
> - Que facedes con cada número?
> - Que valores gardades?
> - Cando parariades?
> - Como calculades a media?"

O docente circula e pregunta:

* "Cando vos dades conta de que chegou o 99999?"
* "Incluídes o 99999 na conta?"
* "Que valores estades gardando mentres lees?"
* "E se só vedes 99999 e máis nada?"

👉 Moitos grupos descubrirán problemas como:
- Esquecer contar cantos números levamos
- Incluír o sentinela por erro
- Non saber que facer sen datos válidos

---

### 🔹 **Fase 3 – Posta en común e identificación de patróns (15 min)**

**Obxectivo:** verbalizar o proceso e detectar elementos comúns.

Cada grupo comparte brevemente a súa estratexia (2 min cada grupo seleccionado).

O docente vai **extraendo patróns comúns** e escribíndoos na pizarra:

* Necesitamos **dúas variables**: suma e contador
* Temos un **bucle** que le números
* Hai unha **condición de parada** (cando chega 99999)
* **Despois do bucle**, dividimos suma/contador
* **Problema especial**: que pasa se contador = 0?

**Preguntas guía:**

> "Que diferenza hai entre 'ler un número' e 'procesalo'?"
> "Cantas cousas estades facendo dentro do bucle?"
> "A división faise dentro ou fóra do bucle?"

💥 Aquí emerxe naturalmente a estrutura de **acumuladores**, **bucle con sentinela** e **validación final**.

---

### 🔹 **Fase 4 – Construción do algoritmo en pseudocódigo (20 min)**

**Obxectivo:** formalizar o pensamento en pasos concretos.

Tarefa en grupos:

> "Agora escribide os pasos do algoritmo en linguaxe natural ou pseudocódigo.
> Non en Python, senón en frases como:
> - 'Inicializo a suma a 0'
> - 'Mentres o número sexa distinto de 99999...'
> - etc."

Guía na pizarra (exemplo de estrutura):

```
1. Inicializar suma = 0, contador = 0
2. Ler un número
3. Mentres o número ≠ 99999:
   a. Engadir o número á suma
   b. Incrementar o contador
   c. Ler outro número
4. Se contador > 0:
      Calcular media = suma / contador
      Mostrar media
   Senón:
      Mostrar mensaxe de erro
```

O docente circula para:
- Detectar se distinguen entre "ler" e "procesar"
- Ver se identifican a necesidade de ler **antes** e **dentro** do bucle
- Verificar se contemplan o caso sen datos válidos

---

### 🔹 **Fase 5 – Casos extremos e depuración (15 min)**

**Obxectivo:** anticipar problemas e desenvolver pensamento crítico.

O docente presenta **casos difíciles** na pizarra:

1. **Entrada:** `99999` (sentinela inmediato)
   - Que debería pasar?
   - O voso algoritmo xestiónaao ben?

2. **Entrada:** `0, 0, 0, 99999`
   - A media é 0? Como o diferenciades do caso sen datos?

3. **Entrada:** `-5, 5, 99999`
   - Funcionan os negativos?

4. **Entrada:** números moi grandes
   - Hai límites no noso sistema?

Cada grupo revisa o seu algoritmo e anota **que cambios** serían necesarios para cubrir estes casos.

**Pregunta clave:**

> "Un programa robusto ten que contemplar o inesperado.
> Que cousas non previstes ao principio?"

---

### 🔹 **Fase 6 – Da idea ao código: mapeo conceptual (7 min)**

**Obxectivo:** conectar a lóxica cos elementos de programación.

O docente fai un **mapeo colectivo** na pizarra:

| Concepto no algoritmo | En Python |
|-----------------------|-----------|
| "Inicializar suma a 0" | `suma = 0` |
| "Ler un número" | `numero = int(input())` |
| "Mentres o número ≠ 99999" | `while numero != 99999:` |
| "Engadir á suma" | `suma += numero` |
| "Se contador > 0" | `if contador > 0:` |
| "Mostrar" | `print(...)` |

👉 Isto **non é implementar aínda**, é só **traducir mentalmente** entre pensamento e sintaxe.

---

### 🔹 **Fase 7 – Preparación para casa (3 min)**

Tarefa individual:

1. Implementar o algoritmo en Python seguindo o pseudocódigo do grupo.
2. Probar cos 5 casos de proba da táboa inicial.
3. Reflexionar por escrito:

   > "Que foi o máis difícil ao pasar do pensamento ao código?
   > Que erro cometín que non previra no papel?"

**Reto opcional:** modificar o programa para que:
- Ignore valores negativos (como no problema orixinal "rainfall" clásico)
- Mostre tamén o máximo e mínimo
- Permita múltiples conxuntos de datos (reiniciar tras 99999)

---

### 🧾 **Peche (3 min)**

Breve reflexión colectiva:

> "Este problema aparenta ser sinxelo, pero escondia moitas decisións.
> Que vos sorprendeu?"

Resume na pizarra:

```
Entrada → Proceso → Saída
         ↓
    (Sentinela, acumuladores, casos extremos)
```

Mensaxe de peche:

> "Programar non é só escribir código.
> É **pensar con precisión** sobre cada paso."

---

## 🧩 **Plantilla A3 suxerida (para imprimir)**

```
┌───────────────────────────────────────────────┐
│   🧩 PASOS DO ALGORITMO                       │
│   (Que fago primeiro? Despois? Cando paro?)   │
│   ________________________________________    │
│                                               │
│   1.                                          │
│   2.                                          │
│   3.                                          │
│                                               │
├───────────────────────────────────────────────┤
│   🧠 DECISIÓNS E DIFICULTADES                 │
│   (Que problemas atopei? Como os resolvo?)    │
│   ________________________________________    │
│                                               │
│   • Sentinela:                                │
│   • Casos extremos:                           │
│   • Validacións:                              │
│                                               │
├───────────────────────────────────────────────┤
│   💻 ESTRUTURA DO CÓDIGO                      │
│   (Variables, condicións, bucles)             │
│   ________________________________________    │
│                                               │
│   Variables:                                  │
│   Bucle:                                      │
│   Condicións:                                 │
│                                               │
└───────────────────────────────────────────────┘
```

---

## 📚 **Contexto do Rainfall Problem clásico**

O **Rainfall Problem** foi introducido por Elliot Soloway en 1986 como ferramenta de investigación en educación de computación. O enunciado orixinal incluía máis restricións:

```
Design a program called RAINFALL that consumes a list of numbers 
representing daily rainfall amounts as entered by a user. 
Produce the average of the non-negative values in the list up to 
the first 999999 (a sentinel value).
```

**Dificultades documentadas** que aparecen nos estudantes:

1. **Problema do valor sentinela**: incluílo nos cálculos
2. **Problema dos negativos**: non filtrar valores inválidos
3. **Problema da división por cero**: non validar lista baleira
4. **Problema da orde das operacións**: calcular media antes de rematar de ler
5. **Problema da lectura**: confundir "ler antes do bucle" vs "ler no bucle"

Esta sesión traballa principalmente os puntos 1, 3 e 5, deixando o 2 como extensión opcional.

---

## 🔗 **Conexión coas outras actividades**

Esta actividade serve de **base conceptual** para:

- **Sopa de letras**: introduce bucles, condicións e validacións que alí se complexifican
- **Indexación de CSV**: os conceptos de lectura secuencial e procesamento aparecen aquí de forma máis sinxela

**Progresión didáctica recomendada:**

1. **Rainfall Problem** → conceptos básicos (bucles, acumuladores, sentinelas)
2. **Sopa de letras** → estruturas de datos, validacións complexas, aleatoriedade
3. **Indexación CSV** → eficiencia algorítmica, estruturas auxiliares (dicionarios)

---

## 🧩 **Notas didácticas**

* É unha actividade **diagnóstica e introductoria** excelente.
* Revela rapidamente o nivel de pensamento algorítmico do grupo.
* Permite traballar **conceptos fundamentais** sen sintaxe complexa.
* A frustración inicial (parece fácil pero non o é) é pedagoxicamente valiosa.
* **Non menosprezar o tempo necesario**: aínda que é un problema "pequeno", require pensamento profundo.

---

## 📖 **Lecturas complementarias (para o docente)**

- Soloway, E. (1986). "Learning to program = learning to construct mechanisms and explanations". *Communications of the ACM*, 29(9), 850-858.
- Fisler, K. (2014). "The Recurring Rainfall Problem". *ICER 2014*.
- Luxton-Reilly, A. (2016). "Learning to Program is Easy". *ITiCSE 2016*.
