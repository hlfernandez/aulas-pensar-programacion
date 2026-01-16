## 💡 Sesión: *Pensar como un programa — de decimal a binario*

**Duración:** 90 minutos
**Nivel:** 1º de Grao en Enxeñaría Informática / IA
**Tamaño de grupo:** 15 estudantes (3–4 por grupo)
**Enfoque:** *Aulas para pensar* — pensamento iterativo e recursivo, división e restos

---

### 📌 **Nota para o profesor**

⚠️ **Contexto didáctico:** Este problema serve como **ponte pedagóxica** entre o pensamento iterativo (bucles, acumuladores) e o pensamento recursivo (descomposición, caso base). A conversión decimal→binario mediante **divisións sucesivas por 2** ten unha estrutura que permite **dúas interpretacións naturais**:

1. **Iterativa (bucle)**: dividir repetidamente por 2, gardando os restos nun acumulador (string ou lista), ler ao revés
2. **Recursiva (descomposición)**: "binario(n) = binario(n÷2) + resto(n÷2)", con caso base n=0 ou n=1

**Como xestionalo:**
- **Deixar emerxer ambas estratexias**: algúns grupos pensarán en repetir divisións (bucle), outros en descompor o problema
- **Non impor unha única solución**: validar ambas como correctas e complementarias
- **Facilitar o descubrimento da recursión**: cando emerxa a idea de "converter n÷2 e engadir o resto", nomala como "pensamento recursivo"
- **Conectar con exemplos previos**: se xa fixeron rainfall (iterativo) e contar setes (recursivo), este exercicio consolida ambos

Esta actividade é ideal para:
- **Repasar bucles while** (versión iterativa)
- **Introducir recursión** de forma natural e visual
- **Traballar con división enteira e operador módulo** (// e %)
- **Comprender sistemas de numeración** (base 10 vs base 2)

---

### 🎯 Obxectivos de aprendizaxe

| Dimensión     | Obxectivo                                                                      |
| ------------- | ------------------------------------------------------------------------------ |
| Cognitiva     | Comprender o algoritmo de divisións sucesivas para cambiar de base.           |
| Metacognitiva | Reflexionar sobre dúas formas de abordar o mesmo problema (iterativa/recursiva).|
| Técnica       | Implementar conversións usando bucles while e usando recursión.                |
| Social        | Comparar estratexias e descubrir que o mesmo problema admite múltiples solucións.|

---

### 🧰 Materiais e preparación

* Follas **A3** en branco ou plantilla (ver abaixo).
* Tarxetas con **bits** (0 e 1) impresas para manipulación física.
* Rotuladores, celo para pegar nas paredes.
* Pizarra ou pantalla para táboa de conversións.
* Calculadora (permitida na fase de verificación).

#### 📋 **Problema inicial (para proxectar)**

```
🔢 PROBLEMA DO CONVERSOR BINARIO

Os ordenadores traballan con números binarios (só 0s e 1s).
Nós pensamos en números decimais (0 ao 9).

Como convertir un número decimal a binario?

Exemplos:
  • 5 en decimal  = ? en binario
  • 11 en decimal = ? en binario
  • 25 en decimal = ? en binario

Sabemos que:
  • 5 debería ser 101
  • 11 debería ser 1011
  
Pero... COMO chegamos a ese resultado paso a paso?
Que proceso segue o ordenador?
```

#### 📊 **Táboa de conversións esperadas**

| Decimal | Proceso de divisións | Binario |
|---------|---------------------|---------|
| 1 | 1 (xa é < 2) | 1 |
| 2 | 2÷2=1 resto 0, 1÷2=0 resto 1 | 10 |
| 3 | 3÷2=1 resto 1, 1÷2=0 resto 1 | 11 |
| 5 | 5÷2=2 r:1, 2÷2=1 r:0, 1÷2=0 r:1 | 101 |
| 11 | 11÷2=5 r:1, 5÷2=2 r:1, 2÷2=1 r:0, 1 | 1011 |
| 25 | ver proceso abaixo | 11001 |
| 42 | ... | 101010 |
| 100 | ... | 1100100 |

💡 *A plantilla A3 ten 3 zonas:*

1. 🧩 **Conversións manuais** (como o facemos paso a paso?)
2. 🧠 **Estratexias descubertas** (bucle de divisións? descomposición?)
3. 💻 **Do proceso ao algoritmo** (como o implementamos?)

---

## 🕒 **Desenvolvemento da sesión (90 min)**

---

### 🔹 **Fase 1 – Activación: como funcionan os números? (10 min)**

**Obxectivo:** conectar co sistema binario e activar o reto da conversión.

#### Parte A: Que sabemos do binario? (3 min)

Pregunta inicial:

> "Sabedes que 11 en decimal é 1011 en binario.
> Pero... como chegamos a ese resultado? Que proceso seguimos?"

Breve intercambio de ideas:
- Calculadora?
- Táboa de conversión?
- Algún algoritmo?

#### Parte B: O reto (7 min)

Tarefa individual:

> "Sen usar calculadora: intentade converter o número 5 a binario.
> Anotade TODO o que facedes, mesmo se non estades seguros."

O docente escribe no pizarrón as estratexias que emerxan:
- "Penso en potencias de 2: 4+1 → 101"
- "Provo coa táboa: 101 é 5"
- "Divido por 2 e miro os restos?"

👉 Algúns estudantes intuirán o método das divisións. Outros non. Ambas situacións son valiosas.

---

### 🔹 **Fase 2 – Descubrimento do algoritmo de divisións (20 min)**

**Obxectivo:** descubrir o método de divisións sucesivas por 2.

#### Tarefa 1: Conversión guiada de 11 a binario (10 min)

O docente propón na pizarra:

> "Imos converter 11 a binario PASO A PASO, seguindo este proceso:
> 
> Paso 1: Dividimos 11 ÷ 2 = ?
> Que nos dá? Cociente e resto?"

Execución colectiva (o docente vai anotando):

```
11 ÷ 2 = 5  resto 1   ← gardamos o 1
 5 ÷ 2 = 2  resto 1   ← gardamos o 1
 2 ÷ 2 = 1  resto 0   ← gardamos o 0
 1 ÷ 2 = 0  resto 1   ← gardamos o 1 e paramos (chegamos a 0)

Restos (de abaixo arriba): 1, 0, 1, 1
Resultado: 1011
```

**Preguntas provocadoras:**

* "Por que paramos cando chegamos a 0 (ou a 1)?"
* "Por que lemos os restos de abaixo arriba?"
* "Que representa cada resto?"

#### Tarefa 2: Conversión en grupos (10 min)

Cada grupo converte manualmente estes números:

> "Convertede a binario usando o método de divisións:
> - 5
> - 13
> - 25
> - 42"

Anotade:
- Cantas divisións fixestes?
- Donde gardades os restos?
- En que orde os lestes?

O docente circula e observa:
- Quen se confunde coa orde dos restos?
- Quen detecta que o número de divisións é aprox. log₂(n)?
- Quen propón formas de organizar o proceso?

---

### 🔹 **Fase 3 – Dúas estratexias de implementación (25 min)**

**Obxectivo:** descubrir que o mesmo proceso pode implementarse iterativa ou recursivamente.

#### Estratexia A: Bucle de divisións (iterativa) (12 min)

O docente pregunta:

> "Se queremos programar isto, que necesitamos?
> Como repetimos o proceso 'dividir por 2 e gardar resto'?"

Grupos traballan en pseudocódigo para 11:

```
número = 11
restos = []  (ou string baleira)

MENTRES número > 0:
    resto = número % 2
    gardar resto (ao principio da lista ou string)
    número = número ÷ 2

resultado = restos lidos ao revés (ou xa construídos ao revés)
```

**Cuestións que emerxen:**

1. **Orden de gardado dos restos:**
   - Opción A: gardar ao final e logo dar a volta
   - Opción B: gardar ao principio (prepending)

2. **Condición de parada:**
   - `mentres número > 0`
   - Que pasa con 0? (caso especial)

O docente escribe no pizarrón o patrón iterativo:

```
resultado = ""
mentres num > 0:
    resto = num % 2
    resultado = str(resto) + resultado  # prepend
    num = num // 2
```

👉 Isto é pensamento **iterativo** clásico: bucle while + acumulador.

#### Estratexia B: Descomposición recursiva (13 min)

O docente propón outro enfoque:

> "Observade este patrón:
> 
> Para converter 11 a binario:
>   11 é par ou impar? → impar → último díxito será 1
>   Resto do número: 11 ÷ 2 = 5
>   
>   binario(11) = binario(5) + '1'
> 
> Para converter 5:
>   5 é impar → último díxito será 1
>   5 ÷ 2 = 2
>   
>   binario(5) = binario(2) + '1'
> 
> Para converter 2:
>   2 é par → último díxito será 0
>   2 ÷ 2 = 1
>   
>   binario(2) = binario(1) + '0'
> 
> Para converter 1:
>   É o caso máis pequeno → '1'
> 
> Reconstruímos desde abaixo:
>   binario(1) = '1'
>   binario(2) = '1' + '0' = '10'
>   binario(5) = '10' + '1' = '101'
>   binario(11) = '101' + '1' = '1011'"
```

**Patrón observado:**

- O problema "grande" depende da solución do problema "pequeno" (n÷2)
- Hai un **caso base** (n=0 ou n=1)
- A solución constrúese "ao volver" da recursión

O docente pregunta:

> "Isto lémbranos algo? Lembra ao problema de contar setes?
> Estamos usando a solución dun problema máis pequeno para resolver o grande..."

👉 Alguén nomea: **pensamento recursivo**

**Comparación visual na pizarra:**

```
ITERATIVO:               RECURSIVO:
↓                        ↓
11 → dividir             binario(11) = binario(5) + "1"
5  → dividir                           ↓
2  → dividir             binario(5) = binario(2) + "1"
1  → parar                             ↓
                         binario(2) = binario(1) + "0"
↑                                      ↓
ler restos ao revés      binario(1) = "1"
```

---

### 🔹 **Fase 4 – Reflexión metacognitiva (12 min)**

**Obxectivo:** tomar conciencia das dúas formas de pensar.

O docente crea unha táboa comparativa na pizarra:

| Aspecto | Estratexia A (iterativa) | Estratexia B (recursiva) |
|---------|--------------------------|--------------------------|
| Estrutura | Bucle while | Chamada recursiva |
| Que facemos? | Dividir e gardar restos | Dividir e engadir ao resultado previo |
| Cando paramos? | Cando num = 0 | Caso base (num = 0 ou 1) |
| Orden de construción | Gardamos e lemos ao revés | Constrúese "ao volver" |
| Control | Explícito (bucle) | Implícito (pila de chamadas) |

Preguntas para reflexión en grupos:

> "Cal vos parece máis natural? Por que?
> Hai unha 'mellor' ca outra?
> En que situacións prefeririades cada unha?"

Posta en común (5 min):
- Algúns preferirán a iterativa (máis directa, máis controlable)
- Outros a recursiva (máis elegante, máis matemática)

👉 **Ambas son válidas**. O importante é comprender a diferenza de pensamento.

---

### 🔹 **Fase 5 – Da lóxica ao código (18 min)**

**Obxectivo:** implementar ambas versións en Python.

#### Versión iterativa (8 min)

O docente mostra o mapeo na pizarra:

| Concepto | En Python |
|----------|-----------|
| "mentres número > 0" | `while num > 0:` |
| "resto da división por 2" | `num % 2` |
| "división enteira por 2" | `num // 2` |
| "gardar ao principio" | `resultado = str(resto) + resultado` |
| "caso especial: 0" | `if num == 0: return "0"` |

Implementación guiada:

```python
def decimal_a_binario_iterativo(num):
    """
    Converte un número decimal a binario.
    Usa bucle while con divisións sucesivas.
    """
    # Caso especial
    if num == 0:
        return "0"
    
    binario = ""
    
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario  # prepend
        num = num // 2
    
    return binario
```

Variante con lista (máis eficiente):

```python
def decimal_a_binario_iterativo_v2(num):
    """Versión con lista (máis eficiente que concatenar strings)."""
    if num == 0:
        return "0"
    
    dixitos = []
    
    while num > 0:
        dixitos.append(str(num % 2))
        num = num // 2
    
    # Reversamos a lista e convertimos a string
    return ''.join(reversed(dixitos))
```

#### Versión recursiva (10 min)

O docente mostra a estrutura recursiva:

| Concepto | En Python |
|----------|-----------|
| "caso base: 0 ou 1" | `if num <= 1: return str(num)` |
| "dividir por 2" | `num // 2` |
| "resto da división" | `num % 2` |
| "chamar recursivamente" | `decimal_a_binario_recursivo(num // 2)` |
| "engadir resto ao final" | `... + str(num % 2)` |

Implementación guiada:

```python
def decimal_a_binario_recursivo(num):
    """
    Converte un número decimal a binario.
    Usa recursión: binario(n) = binario(n÷2) + resto(n%2)
    """
    # Caso base
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    
    # Caso recursivo
    # binario(n) = binario(n÷2) + díxito_resto
    return decimal_a_binario_recursivo(num // 2) + str(num % 2)
```

Versión alternativa (máis compacta):

```python
def decimal_a_binario_recursivo(num):
    """Versión compacta."""
    if num <= 1:
        return str(num)
    return decimal_a_binario_recursivo(num // 2) + str(num % 2)
```

**Exemplo de traza da recursión** (para 11):

```python
decimal_a_binario_recursivo(11)
  → decimal_a_binario_recursivo(5) + "1"
      → decimal_a_binario_recursivo(2) + "1"
          → decimal_a_binario_recursivo(1) + "0"
              → "1"
          ← "1" + "0" = "10"
      ← "10" + "1" = "101"
  ← "101" + "1" = "1011"
```

---

### 🔹 **Fase 6 – Probas e verificación (10 min)**

**Obxectivo:** validar ambas implementacións.

Execución colectiva:

```python
casos_proba = [0, 1, 2, 3, 5, 11, 25, 42, 100, 255]

print("Decimal | Iterativo  | Recursivo  | Python bin()")
print("--------|------------|------------|---------------")
for num in casos_proba:
    iter_result = decimal_a_binario_iterativo(num)
    rec_result = decimal_a_binario_recursivo(num)
    py_result = bin(num)[2:]  # quita o prefixo '0b'
    print(f"{num:>7} | {iter_result:>10} | {rec_result:>10} | {py_result:>13}")
```

Saída esperada:

```
Decimal | Iterativo  | Recursivo  | Python bin()
--------|------------|------------|---------------
      0 |          0 |          0 |             0
      1 |          1 |          1 |             1
      2 |         10 |         10 |            10
      3 |         11 |         11 |            11
      5 |        101 |        101 |           101
     11 |       1011 |       1011 |          1011
     25 |      11001 |      11001 |         11001
     42 |     101010 |     101010 |        101010
    100 |    1100100 |    1100100 |       1100100
    255 |   11111111 |   11111111 |      11111111
```

**Verificación manual** (na pizarra, para 11):

```
Iterativo:          Recursivo:
11 % 2 = 1          binario(11) = binario(5) + "1"
11 // 2 = 5           binario(5) = binario(2) + "1"
5 % 2 = 1               binario(2) = binario(1) + "0"
5 // 2 = 2                binario(1) = "1"
2 % 2 = 0             volta: "1" + "0" = "10"
2 // 2 = 1          volta: "10" + "1" = "101"
1 % 2 = 1         volta: "101" + "1" = "1011" ✓
1 // 2 = 0

restos: 1,1,0,1
ao revés: 1011 ✓
```

---

### 🔹 **Fase 7 – Extensións e problema inverso (10 min)**

**Obxectivo:** profundizar e conectar con outros problemas.

#### Reto 1: Binario a decimal

> "Agora ao revés: dado un número binario (como string), convertilo a decimal.
> Podes facelo de forma iterativa? E recursiva?"

Pista iterativa (na pizarra):

```python
def binario_a_decimal_iterativo(binario):
    resultado = 0
    for dixito in binario:
        resultado = resultado * 2 + int(dixito)
    return resultado
```

Pista recursiva:

```python
def binario_a_decimal_recursivo(binario):
    if len(binario) == 1:
        return int(binario)
    # Valor = primeiro_díxito × 2^n + resto
    return int(binario[0]) * (2 ** (len(binario)-1)) + \
           binario_a_decimal_recursivo(binario[1:])
```

#### Reto 2: Outras bases

> "Podes modificar o código para converter de decimal a calquera base (8, 16)?"

Exemplo (na pizarra):

```python
def decimal_a_base(num, base):
    """Converte decimal a calquera base (2-16)."""
    if num == 0:
        return "0"
    
    dixitos = "0123456789ABCDEF"
    resultado = ""
    
    while num > 0:
        resto = num % base
        resultado = dixitos[resto] + resultado
        num = num // base
    
    return resultado

# decimal_a_base(255, 16) → "FF"
# decimal_a_base(63, 8) → "77"
```

#### Reto 3: Versión recursiva con acumulador (tail recursion)

> "Investiga: podes facer unha versión recursiva que NON teña que esperar
> a 'volver' da recursión? (chamada recursión de cola ou tail recursion)"

```python
def decimal_a_binario_tail_rec(num, acum=""):
    """Recursión de cola (tail recursion)."""
    if num == 0:
        return acum if acum else "0"
    return decimal_a_binario_tail_rec(num // 2, str(num % 2) + acum)
```

---

### 🔹 **Fase 8 – Reflexión final (5 min)**

Preguntas para discutir:

> "Que versión (iterativa ou recursiva) vos pareceu máis intuitiva?
> Cal foi o momento 'aha!' durante a actividade?
> En que outros problemas vistes esta dobre natureza (iterativo/recursivo)?"

O docente resume na pizarra:

```
Mesmo problema, dúas formas de pensar:

ITERATIVA                    RECURSIVA
↓                            ↓
Procesar paso a paso         Descompor en caso máis pequeno
Bucle + acumulador           Caso base + caso recursivo
Control explícito            Estrutura auto-similar

Ambas válidas!
```

Mensaxe de peche:

> "Hoxe vimos como converter números decimais a binarios usando
> o **método de divisións sucesivas**.
> 
> Descubrimos que podemos implementar o mesmo proceso de **dúas formas**:
> - Con un bucle while (iterativo)
> - Con descomposición recursiva
> 
> Ambas son correctas e reflexan formas diferentes de pensar sobre o mesmo problema."

---

### 🧾 **Preparación para casa (listaxe na pizarra)**

Tarefa individual:

1. **Implementar** ambas versións (iterativa e recursiva) de decimal→binario.
2. **Verificar** que dan os mesmos resultados para varios casos.
3. **Implementar o problema inverso**: binario → decimal (ambas versións).
4. **Reto**: converter entre calquera base (2-16) e decimal.
5. **Reflexión escrita**:

   > "Que versión preferides? Por que?
   > Cando é máis útil pensar iterativamente? Cando recursivamente?
   > Que aprendín sobre o operador % e // ?"

**Reto avanzado:**

> "Investiga sobre 'recursión de cola' (tail recursion) e implementa
> unha versión de decimal_a_binario que use este patrón. Que vantaxes ten?"

---

## 🧩 **Plantilla A3 suxerida (para imprimir)**

```
┌───────────────────────────────────────────────┐
│   🧩 CONVERSIÓNS MANUAIS                      │
│   (Como o facemos paso a paso?)               │
│   ________________________________________    │
│                                               │
│   Decimal → Binario:                          │
│   5  →  ?     Como?                           │
│   11 →  ?     Que pasos seguimos?             │
│   25 →  ?                                     │
│                                               │
│   Método das divisións:                       │
│   11 ÷ 2 = ___ resto ___                      │
│   __ ÷ 2 = ___ resto ___                      │
│   __ ÷ 2 = ___ resto ___                      │
│   ...                                         │
│   Resultado: ______ (como lemos os restos?)  │
│                                               │
├───────────────────────────────────────────────┤
│   🧠 ESTRATEXIAS DESCUBERTAS                  │
│   (Podemos facelo de máis dunha forma?)       │
│   ________________________________________    │
│                                               │
│   Estratexia A (bucle):                       │
│   • Que repetimos?                            │
│   • Donde gardamos os restos?                 │
│   • Cando paramos?                            │
│   • Como obtemos o resultado final?           │
│                                               │
│   Estratexia B (recursiva):                   │
│   • Cal é o caso máis pequeno?                │
│   • Como descompoñemos?                       │
│   • Como se constrúe o resultado?             │
│                                               │
├───────────────────────────────────────────────┤
│   💻 DO PROCESO AO ALGORITMO                  │
│   (Como o implementamos en cada caso?)        │
│   ________________________________________    │
│                                               │
│   Versión iterativa (bucle while):            │
│   • Variables necesarias:                     │
│   • Condición do bucle:                       │
│   • Que facemos en cada iteración?            │
│   • Como construímos o resultado?             │
│                                               │
│   Versión recursiva:                          │
│   • Caso base:                                │
│   • Caso recursivo:                           │
│   • Como se combinan os resultados?           │
│                                               │
└───────────────────────────────────────────────┘
```

---

## 📊 **Análise matemática do problema (para o docente)**

### Algoritmo de divisións sucesivas

Para converter un número decimal N a binario:

**Proceso:**
1. Dividir N por 2, obtendo cociente Q e resto R
2. O resto R (0 ou 1) é un díxito binario
3. Repetir con Q ata que Q = 0
4. Os restos, lidos **ao revés**, forman o número binario

**Exemplo: 11 → binario**

```
11 ÷ 2 = 5  resto 1   ← díxito menos significativo
 5 ÷ 2 = 2  resto 1
 2 ÷ 2 = 1  resto 0
 1 ÷ 2 = 0  resto 1   ← díxito máis significativo

Restos ao revés: 1011
```

### Por que funciona?

Un número N pódese expresar como:

```
N = a_n × 2^n + a_{n-1} × 2^{n-1} + ... + a_1 × 2 + a_0
```

Ao dividir por 2:

```
N ÷ 2 = a_n × 2^{n-1} + ... + a_1  resto a_0
```

O resto é precisamente o díxito menos significativo (a_0).
O cociente contén o resto dos díxitos.

### Relación recursiva

Pódese expresar como:

```
binario(N) = binario(N ÷ 2) + str(N % 2)

Con caso base:
binario(0) = "0"
binario(1) = "1"
```

Ou de forma máis matemática:

```
f(n) = ""                      se n = 0
f(n) = "1"                     se n = 1
f(n) = f(⌊n/2⌋) + (n mod 2)    se n > 1
```

### Número de divisións

Para un número N, o número de divisións necesarias é:

```
⌊log₂(N)⌋ + 1
```

Exemplos:
- N = 11: ⌊log₂(11)⌋ + 1 = 3 + 1 = 4 divisións
- N = 100: ⌊log₂(100)⌋ + 1 = 6 + 1 = 7 divisións

Isto tamén é o **número de díxitos** en binario.

---

## 🔗 **Conexión coas outras actividades**

Esta actividade serve como **ponte** entre problemas iterativos e recursivos:

- **Rainfall**: iterativo puro (bucles + acumulador)
- **Sopa de letras**: lóxica de validación e estruturas
- **Conversor binario**: iterativo E recursivo ← PONTE
- **Contar setes**: recursivo avanzado (descomposición matemática)
- **Indexación CSV**: estruturas de datos e eficiencia

**Progresión didáctica recomendada:**

1. **Rainfall** → bucles, acumuladores, condicións
2. **Sopa de letras** → validacións, estruturas 2D
3. **Conversor binario** → divisións, iterativo + recursivo ← TRANSICIÓN
4. **Contar setes** → recursión avanzada con patróns
5. **Indexación CSV** → eficiencia, dicionarios

---

## 🧩 **Notas didácticas**

* É un problema **altamente motivador**: os estudantes de informática queren comprender como funcionan os números nos ordenadores.
* O método de **divisións sucesivas** é visual, concreto e fácil de seguir manualmente.
* A dobre natureza (iterativa/recursiva) é pedagoxicamente moi valiosa.
* **Non presentar a recursión como "mellor"**: simplemente como outra forma de pensar.
* Permite traballar **operadores % e //** de forma natural e con significado.
* O momento "aha!" cando ven que poden expresalo recursivamente é valioso.
* Conecta matemáticas (divisións, restos) e programación de forma orgánica.
* **Preparación para problemas máis complexos**: a recursión emerxe como estratexia de descomposición natural.
* O contraste entre "acumular ao principio" (prepend) vs "gardar e reverter" permite falar de eficiencia.

---

## 🎓 **Variantes e extensións**

### Variante 1: Binario a decimal (iterativo)

Procesar da esquerda á dereita, multiplicando por 2:

```python
def binario_a_decimal_iterativo(binario):
    resultado = 0
    for dixito in binario:
        resultado = resultado * 2 + int(dixito)
    return resultado
    
# Equivalente a ir construíndo:
# "101" → 0
#      → 0*2 + 1 = 1
#      → 1*2 + 0 = 2
#      → 2*2 + 1 = 5
```

### Variante 2: Binario a decimal (recursivo)

```python
def binario_a_decimal_recursivo(binario):
    if len(binario) == 1:
        return int(binario)
    # primeiro_díxito × 2^n + resto
    return int(binario[0]) * (2 ** (len(binario)-1)) + \
           binario_a_decimal_recursivo(binario[1:])
```

### Variante 3: Decimal a calquera base

```python
def decimal_a_base(num, base):
    """Converte un número decimal a calquera base (2-36)."""
    if num == 0:
        return "0"
    
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""
    
    while num > 0:
        resto = num % base
        resultado = digitos[resto] + resultado
        num = num // base
    
    return resultado

# Exemplos:
# decimal_a_base(11, 2) → "1011"
# decimal_a_base(255, 16) → "FF"
# decimal_a_base(63, 8) → "77"
```

### Variante 4: Versión recursiva de calquera base

```python
def decimal_a_base_recursivo(num, base):
    """Versión recursiva para calquera base."""
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if num < base:
        return digitos[num]
    
    return decimal_a_base_recursivo(num // base, base) + \
           digitos[num % base]
```

### Variante 5: Usando funcións integradas de Python

Mostrar que Python xa ten estas conversións:

```python
# Decimal a binario
bin(11)      # → "0b1011"
bin(11)[2:]  # → "1011" (sen prefixo)

# Binario a decimal
int("1011", 2)  # → 11

# Outras bases
hex(255)     # → "0xff"
oct(63)      # → "0o77"
int("FF", 16)  # → 255
int("77", 8)   # → 63
```

---

## 📖 **Lecturas complementarias (para o docente)**

- Knuth, D. (1997). "The Art of Computer Programming, Vol. 2: Seminumerical Algorithms" (sistemas de numeración e conversións de base).
- Concrete Mathematics (Graham, Knuth, Patashnik) - Capítulo 1: Recurrent Problems (relacións de recurrencia).
- Recursion in Computer Science: https://en.wikipedia.org/wiki/Recursion_(computer_science)
- Number Systems: https://en.wikipedia.org/wiki/Numeral_system
- Binary Number System: https://www.electronics-tutorials.ws/binary/bin_1.html

---

## 🎯 **Avaliación formativa**

### Criterios de observación durante a sesión:

| Indicador | Observación |
|-----------|-------------|
| Descobre o método de divisións | ¿Identifica que dividir por 2 funciona? |
| Comprende o papel dos restos | ¿Ve que os restos son os díxitos binarios? |
| Detecta a orde de lectura | ¿Entende por que se len ao revés? |
| Propón unha estratexia iterativa | ¿Usa bucle while correctamente? |
| Descobre a versión recursiva | ¿Ve a descomposición recursiva? |
| Comprende ambos enfoques | ¿Pode explicar as diferenzas? |
| Verifica os seus resultados | ¿Proba con varios casos? |

### Preguntas de avaliación final:

1. **Conceptual**: Explica por que o método de divisións sucesivas funciona para converter a binario.
2. **Procedemental**: Implementa ambas versións (iterativa e recursiva) correctamente.
3. **Metacognitiva**: Reflexiona sobre que enfoque lle resultou máis natural e por que.
4. **Transferencia**: Aplica o mesmo método para converter a outras bases (octal, hexadecimal).

---

## ✨ **Puntos clave para levar a casa**

1. **O mesmo problema pode resolverse de múltiples formas** (iterativa vs recursiva).
2. **O pensamento iterativo** procesa elemento a elemento acumulando resultado.
3. **O pensamento recursivo** descompón o problema en casos máis pequenos.
4. **Ambas estratexias son válidas** e complementarias.
5. **Os sistemas de numeración** teñen estrutura posicional (vale 2^i, 10^i, 16^i, etc.).
6. **A recursión emerge naturalmente** cando o problema ten estrutura auto-similar.

---

## ✨ **Puntos clave para levar a casa**

1. **O método de divisións sucesivas** por 2 converte decimal a binario.
2. **Os restos** (0 ou 1) son os díxitos binarios, lidos **ao revés**.
3. **O mesmo algoritmo pode implementarse de dúas formas**:
   - **Iterativa**: bucle while que vai dividindo e gardando restos
   - **Recursiva**: descomposición en casos máis pequenos
4. **Ambas estratexias son válidas** e complementarias.
5. **Os operadores % e //** son fundamentais para traballar con díxitos e bases.
6. **A recursión emerge naturalmente** cando vemos que binario(n) = binario(n÷2) + resto.
7. **O método xeneralízase** a calquera base (non só binario).

---

**Resumo visual final (na pizarra):**

```
    DECIMAL → BINARIO
         ↓
   Dividir por 2
   Gardar restos
   Ler ao revés
         ↓
    Dúas formas:
         ↓
    ┌────┴────┐
    ↓         ↓
ITERATIVA  RECURSIVA
(bucle while)  (descomposición)
    ↓         ↓
dividir      dividir
gardar       engadir
repetir      chamar
```

