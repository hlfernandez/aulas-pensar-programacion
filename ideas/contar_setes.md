## 💡 Sesión: *Pensar como un programa — contar díxitos recurrentes*

**Duración:** 90 minutos
**Nivel:** 1º de Grao en Enxeñaría Informática / IA
**Tamaño de grupo:** 15 estudantes (3–4 por grupo)
**Enfoque:** *Aulas para pensar* — descubrimento de patróns, pensamento recursivo e optimización

---

### 📌 **Nota para o profesor**

⚠️ **Contexto:** Este problema aparenta ser unha simple tarefa de contaxe, pero escondia **múltiples capas de complexidade**:

1. **Primeira aproximación (brute force)**: contar un por un todos os números → O(n log n)
2. **Descubrimento de patróns**: observar regularidades ao incrementar a orde de magnitude
3. **Salto conceptual**: descompor o problema en bloques → pensamento recursivo
4. **Solución elegante**: recursión que aproveita a estrutura decimal → O(log n)

**Como xestionalo:**
- **Deixar tempo para exploración manual**: a frustración inicial de contar manualmente é pedagoxicamente valiosa
- **Non anticipar a recursión**: deixar que emerxa naturalmente do descubrimento de patróns
- **Valorar múltiples estratexias**: haberá solucións iterativas, recursivas, matemáticas puras
- **Conectar con casos reais**: fabricantes de azulexos, optimización de recursos, etc.

Esta actividade é ideal para introducir **pensamento recursivo** de forma visual e concreta, antes de pasar a casos máis abstractos (torres de Hanoi, travesías en árbores, etc.).

---

### 🎯 Obxectivos de aprendizaxe

| Dimensión     | Obxectivo                                                                      |
| ------------- | ------------------------------------------------------------------------------ |
| Cognitiva     | Descubrir patróns en secuencias numéricas e xenerar hipóteses.                 |
| Metacognitiva | Reflexionar sobre como cambiar de estratexia ao detectar ineficiencias.        |
| Técnica       | Comprender a estrutura recursiva dun problema e a súa implementación.          |
| Social        | Construír coñecemento colectivamente a través da comparación de patróns.       |

---

### 🧰 Materiais e preparación

* Follas **A3** en branco ou plantilla (ver abaixo).
* Rotuladores, celo para pegar nas paredes.
* **Tarxetas con números do 1 ao 100** (opcional, para manipulación física).
* Calculadora (permitida na fase de verificación).
* Pizarra ou pantalla para táboa de patróns.

#### 📋 **Problema inicial (para proxectar)**

```
🏠 PROBLEMA DOS AZULEXOS

Unha empresa fabrica azulexos co díxito "7" para numerar casas.

Se queremos numerar casas do 1 ao 10, cantos azulexos co "7" necesitamos?
  → Números que conteñen 7: {7}
  → Total de "7"s: 1

Se queremos numerar do 1 ao 100, cantos azulexos co "7" necesitamos?

Se queremos numerar do 1 ao 1000? E ao 10.000?

Podes descubrir un patrón xeral?
```

#### 📊 **Táboa de resultados esperados**

| Rango | Nº de "7"s | Observación |
|-------|-----------|-------------|
| 1–10 | 1 | Só o 7 |
| 1–100 | 20 | 7, 17, 27, ..., 70-79, ..., 97 |
| 1–1.000 | 300 | Patrón emerge |
| 1–10.000 | 4.000 | 10× o anterior + corrección |
| 1–100.000 | 50.000 | Secuencia clara |

💡 *A plantilla A3 ten 3 zonas:*

1. 🧩 **Contaxe e estratexia** (como contamos? que patróns vemos?)
2. 🧠 **Hipóteses sobre o patrón** (que relación hai entre 1-10, 1-100, 1-1000?)
3. 💻 **Do patrón ao algoritmo** (como o implementariamos?)

---

## 🕒 **Desenvolvemento da sesión (90 min)**

---

### 🔹 **Fase 1 – Activación: contar manualmente (15 min)**

**Obxectivo:** experimentar a dificultade da conta bruta e activar a busca de patróns.

#### Parte A: Caso pequeno (5 min)

Instrución individual:

> "Conta cantos díxitos '7' hai do 1 ao 10."

Resposta rápida: **1** (só no número 7).

#### Parte B: Caso medio (10 min)

Tarefa en grupos:

> "Agora contade cantos '7' hai do 1 ao 100.
> Anotade **como** o facedes: que estratexia seguides?"

O docente circula e observa estratexias:
- Quen conta un por un (7, 17, 27, 37...)
- Quen agrupa por decenas
- Quen identifica casos especiais (70-79)

**Preguntas provocadoras:**

* "Hai algún grupo de números onde apareza máis o 7?"
* "Podedes agrupar de algunha forma para non contar un por un?"
* "Canto tempo vos levou? E se fose ata 1.000?"

👉 Emerxe a noción de que **contar brutamente non escala**.

---

### 🔹 **Fase 2 – Descubrimento do patrón (20 min)**

**Obxectivo:** construír unha táboa de datos e buscar regularidades.

O docente escribe na pizarra:

```
Rango       | Nº de "7"s | Como se relacionan?
------------|------------|--------------------
1–10        | 1          |
1–100       | 20         | = 20 × ?
1–1.000     | ?          | 
1–10.000    | ?          |
```

#### Tarefa 1: Verificar 1–100 (5 min)

Grupos verifican o resultado de 20 de diferentes formas:
- **Unidades**: 7, 17, 27, 37, 47, 57, 67, 77, 87, 97 → 10 veces
- **Decenas**: 70, 71, 72, ..., 79 → 10 veces (pero o 77 xa se contou)

Corrección colectiva na pizarra.

#### Tarefa 2: Predición para 1–1.000 (8 min)

> "Sen contar un por un, podedes **predecir** cantos '7' haberá do 1 ao 1.000?"

Grupos traballan con hipóteses:
- "Será 10 veces máis que 1-100?" → 200
- "Pero tamén están os 700-799..." → +100
- "Total: 300"

#### Tarefa 3: Buscar a relación (7 min)

> "Que relación matemática hai entre estos resultados?
> 
> - 1→10: **1**
> - 1→100: **20**
> - 1→1000: **300**
>
> Podedes expresala como unha fórmula?"

Grupos tentan atopar patróns:
- 1, 20, 300 → multiplicación por algo?
- Relación coa orde de magnitude?

💥 Aquí emerxe a idea de **descompoñer por bloques de potencias de 10**.

---

### 🔹 **Fase 3 – Reflexión metacognitiva (10 min)**

**Obxectivo:** tomar conciencia do cambio de estratexia.

Preguntas para discutir en grupos:

> "Cal foi a vosa primeira estratexia? Funcionou para todos os casos?
> Cando vos destes conta de que precisabades outro enfoque?
> Que vos fixo cambiar de idea?"

Posta en común (3-4 grupos comparten brevemente).

O docente resume na pizarra:

```
Estratexia bruta (contar 1 por 1)
         ↓
   Non escala → frustración
         ↓
   Busca de patróns
         ↓
   Descomposición en bloques
```

👉 Isto é **pensamento algorítmico real**: recoñecer cando unha solución non funciona e buscar outra.

---

### 🔹 **Fase 4 – Construción da lóxica recursiva (25 min)**

**Obxectivo:** descubrir a estrutura recursiva do problema.

#### Paso 1: Descomposición visual (10 min)

O docente presenta na pizarra a idea de **bloques**:

```
Do 1 ao 100:
  - Bloque 1-10:   contén N "7"s
  - Bloque 11-20:  contén N "7"s
  - Bloque 21-30:  contén N "7"s
  ...
  - Bloque 71-80:  contén N+10 "7"s (polo 7 na decena)
  ...
  
Total = 10 bloques × (contido de cada bloque) + extra do 70-79
```

Pregunta clave:

> "Que contén cada bloque de 10 números?
> É o mesmo problema pero **máis pequeno**?"

👉 Isto introduce a noción de **recursión sen nomala aínda**.

#### Paso 2: Formalización do patrón (8 min)

Grupos traballan en responder:

> "Para contar os '7' de 1 a 1.000, podedes usar o resultado de 1 a 100?"

Guía na pizarra:

```
contar_setes(1000) = ?

Descompoñemos en bloques de 100:
  - 0-99:   contar_setes(100) → 20
  - 100-199: contar_setes(100) → 20
  - ...
  - 700-799: contar_setes(100) + 100 extra → 120
  - ...

Total = 10 × contar_setes(100) + 100
      = 10 × 20 + 100
      = 300
```

#### Paso 3: Caso base e caso recursivo (7 min)

O docente pregunta:

> "E se quiséramos unha fórmula xeral para calquera número?
> Cal sería o caso máis pequeno? (caso base)
> Como expresaríamos o resto? (caso recursivo)"

Grupos esbocen en pseudocódigo:

```
función contar_setes(num):
  
  CASO BASE:
    se num < 10:
      devolver 1 se num >= 7, senón 0
  
  CASO RECURSIVO:
    tamaño_bloque = num / 10
    total = 10 × contar_setes(tamaño_bloque) + tamaño_bloque
    devolver total
```

---

### 🔹 **Fase 5 – Da lóxica ao código (12 min)**

**Obxectivo:** traducir o pensamento a Python.

O docente mostra o mapeo na pizarra:

| Concepto | En Python |
|----------|-----------|
| "se num < 10" | `if num < 10:` |
| "devolver 1 se num >= 7" | `return 1 if num >= 7 else 0` |
| "tamaño_bloque = num / 10" | `tam_bloq = num // 10` |
| "10 × contar_setes(...)" | `10 * contar_setes(tam_bloq)` |
| "chamar a función dende si mesma" | Recursión! |

#### Implementación guiada (8 min)

Grupos intentan escribir o código completo:

```python
def contar_setes(num):
    # Caso base
    if num < 10:
        return 1 if num >= 7 else 0
    
    # Caso recursivo
    tam_bloq = num // 10
    total = 10 * contar_setes(tam_bloq) + tam_bloq
    return total
```

#### Probas (4 min)

Execución colectiva:

```python
for i in range(1, 8):
    num = int("1" + "0" * i)
    print(f"{num:>10} => {int(contar_setes(num))}")
```

Saída esperada:

```
        10 => 1
       100 => 20
      1000 => 300
     10000 => 4000
    100000 => 50000
   1000000 => 600000
  10000000 => 7000000
```

---

### 🔹 **Fase 6 – Extensións e reflexión final (5 min)**

**Obxectivo:** consolidar o aprendido e abrir novas preguntas.

Preguntas para reflexión:

* "Por que a recursión funciona aquí?"
* "Que outros problemas poderían ter esta estrutura?"
* "Cal é a complexidade da solución recursiva vs contar un por un?"

O docente introduce:

> "Contar un por un: **O(n log n)** (n números, log n díxitos cada un)
> Solución recursiva: **O(log n)** (só procesamos as potencias de 10)"

---

### 🔹 **Fase 7 – Preparación para casa (3 min)**

Tarefa individual:

1. **Implementar** a función recursiva en Python.
2. **Verificar** os resultados para 10, 100, 1000, 10000.
3. **Extensión A**: Modificar para contar calquera díxito (non só o 7).
4. **Extensión B**: Resolver para rangos arbitrarios (p.ex., do 50 ao 250).
5. **Reflexión escrita**:

   > "Que parte do proceso de pensamento foi máis difícil?
   > Como identificaches que a recursión era unha boa estratexia?"

**Reto avanzado:**

> "Podes resolver o problema **sen recursión**, usando só matemáticas?
> (Pista: pensa en canto '7' aparece en cada posición: unidades, decenas, centenas...)"

---

### 🧾 **Peche (5 min)**

Mensaxe de peche:

> "Hoxe vimos como un problema de contaxe aparentemente sinxelo
> escondia unha **estrutura recursiva elegante**.
> 
> A recursión non é só unha técnica de programación:
> é unha forma de **pensar en problemas que se repiten a si mesmos a diferente escala**."

Resume na pizarra:

```
Problema grande
    ↓
Descomponer en bloques
    ↓
Cada bloque = mesmo problema máis pequeno
    ↓
Recursión
```

---

## 🧩 **Plantilla A3 suxerida (para imprimir)**

```
┌───────────────────────────────────────────────┐
│   🧩 CONTAXE E ESTRATEXIA                     │
│   (Como contamos? Que números teñen 7?)       │
│   ________________________________________    │
│                                               │
│   1-10:    [  ]  "7"s                         │
│   1-100:   [  ]  "7"s → como contei?          │
│                                               │
│   Grupos especiais:                           │
│   • Unidades con 7:                           │
│   • Decenas con 7:                            │
│                                               │
├───────────────────────────────────────────────┤
│   🧠 HIPÓTESES SOBRE O PATRÓN                 │
│   (Que relación hai entre 10, 100, 1000?)     │
│   ________________________________________    │
│                                               │
│   1→10:    1                                  │
│   1→100:   20    = 10 × ____ + ____           │
│   1→1000:  ___   = 10 × ____ + ____           │
│                                               │
│   Patrón xeral:                               │
│                                               │
├───────────────────────────────────────────────┤
│   💻 DO PATRÓN AO ALGORITMO                   │
│   (Como o implementamos?)                     │
│   ________________________________________    │
│                                               │
│   Caso base (máis pequeno):                   │
│                                               │
│   Caso recursivo (como descompoñer):          │
│                                               │
│   Estructura:                                 │
│   • Variables necesarias:                     │
│   • Operacións:                               │
│   • Chamada recursiva:                        │
│                                               │
└───────────────────────────────────────────────┘
```

---

## 📊 **Análise matemática do problema (para o docente)**

### Demostración do patrón

Para un número da forma **10^k** (10, 100, 1000, ...):

1. **Aparicións nas unidades**: cada 10 números aparece un 7 na posición de unidades
   - De 0 a 10^k hai 10^(k-1) veces

2. **Aparicións nas decenas**: cada 100 números aparece un bloque 70-79
   - De 0 a 10^k hai 10^(k-1) veces, 10 números cada vez = 10 × 10^(k-1)

3. **Aparicións nas centenas, etc.**: segue o mesmo patrón

**Fórmula xeral**: para contar díxitos '7' de 1 a 10^k:

```
f(10^k) = k × 10^(k-1)
```

Verificación:
- f(10^1) = 1 × 10^0 = 1 ✓
- f(10^2) = 2 × 10^1 = 20 ✓
- f(10^3) = 3 × 10^2 = 300 ✓
- f(10^4) = 4 × 10^3 = 4000 ✓

### Relación recursiva

```
f(10^k) = 10 × f(10^(k-1)) + 10^(k-1)
```

Ou en forma xenérica para un número n:

```
f(n) = 10 × f(n/10) + n/10     (se n >= 10)
f(n) = 1 se n >= 7, senón 0     (se n < 10)
```

---

## 🔗 **Conexión coas outras actividades**

Esta actividade introduce **recursión** de forma concreta e visual:

- **Rainfall**: bucles e acumuladores (iterativo)
- **Sopa de letras**: backtracking implícito (case recursivo)
- **Contar setes**: recursión pura e explícita ← NOVA
- **Indexación CSV**: estruturas de datos e eficiencia

**Progresión didáctica recomendada:**

1. **Rainfall** → bucles, condicións, acumuladores
2. **Sopa de letras** → validacións, estruturas 2D
3. **Contar setes** → recursión, patróns matemáticos ← aquí
4. **Indexación CSV** → eficiencia, dicionarios

---

## 🧩 **Notas didácticas**

* É un problema **altamente motivador**: real, visual, con sorpresa matemática.
* A transición de "contar manualmente" a "descubrir o patrón" é poderosa.
* **Non anticipar a recursión**: deixar que emerxa como solución natural.
* Permite traballar **diferentes niveis de abstracción** no mesmo problema.
* Conecta matemáticas, lóxica e programación de forma orgánica.
* O momento "aha!" cando ven que 1→1000 usa o resultado de 1→100 é moi valioso.

---

## 🎓 **Variantes e extensións**

### Variante 1: Contar outros díxitos

Modificar a función para contar calquera díxito (parámetro adicional):

```python
def contar_dixito(num, dixito):
    if num < 10:
        return 1 if num >= dixito else 0
    
    tam_bloq = num // 10
    total = 10 * contar_dixito(tam_bloq, dixito) + tam_bloq
    return total
```

### Variante 2: Rangos arbitrarios

Contar díxitos entre dous números calquera:

```python
def contar_setes_rango(inicio, fin):
    return contar_setes(fin) - contar_setes(inicio - 1)
```

### Variante 3: Solución iterativa

Desafío: resolver sen recursión usando bucles:

```python
def contar_setes_iterativo(num):
    total = 0
    potencia = 1
    
    while potencia <= num:
        cifras_superiores = num // (potencia * 10)
        cifra_actual = (num // potencia) % 10
        cifras_inferiores = num % potencia
        
        # Contar aparicións do 7 nesta posición
        if cifra_actual > 7:
            total += (cifras_superiores + 1) * potencia
        elif cifra_actual == 7:
            total += cifras_superiores * potencia + cifras_inferiores + 1
        else:
            total += cifras_superiores * potencia
        
        potencia *= 10
    
    return total
```

---

## 📖 **Lecturas complementarias (para o docente)**

- Knuth, D. (1997). "The Art of Computer Programming, Vol. 1: Fundamental Algorithms" (sección sobre recursión).
- Roberts, E. (2006). "Thinking Recursively" - introducción pedagóxica á recursión.
- Problema similar: "Number of 1 Bits" (LeetCode), "Digit DP" (técnicas de programación dinámica sobre díxitos).
