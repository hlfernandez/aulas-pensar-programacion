Aquí tes un **borrador inicial** dunha actividade completa deseñada “estilo aulas para pensar”, especificamente pensada para alumnado de **1º de grao en Enxeñaría Informática / IA**, e **situada didacticamente antes** da actividade de indexación (menos abstracta, máis visual, pero igualmente poderosa para traballar pensamento algorítmico, estrutura de datos, dependencia entre decisións e modularidade).

A actividade está pensada para unha **sesión de 90 minutos**, pero con marxe para adaptala a 60–120 min.
O nivel de dificultade é progresivo e deixa moito espazo para que emerxan solucións diferentes.

---

# 🧠 Actividade: *Pensar como un programa — Xerar unha sopa de letras*

**Duración:** 90 min
**Nivel:** 1º de Grao en Enxeñaría Informática / IA
**Tamaño do grupo:** 15 estudantes
**Producto final conceptual (non código):** deseño dun algoritmo, esquema modular de funcións, e reflexión sobre casos extremos.

> Obxectivo global:
> Que o alumnado **pense como un programa** para deseñar un algoritmo capaz de xerar unha sopa de letras consistente a partir dun conxunto de palabras e un tamaño dado. Que descubran pola súa conta restricións, dependencias lóxicas, estrutura dos datos e posibilidade de modularización.

---

# 🔹 Estrutura da sesión

## 🕐 Fase 1. Activación (10 min) — *Como faría isto un programa?*

**Material:** unha sopa de letras impresa nunha folla.

1. Amosar unha sopa de letras e preguntar:

   > “Como cres que se xera isto automaticamente?”
2. Recoller ideas rápidas:

   * coloco palabras en horizontal
   * en vertical
   * en diagonal
   * en calquera orde
   * palabra encima doutra: que pasa?
3. Lanzar pregunta clave:

   > “Que pasos concretos tería que seguir un programa? Onde poden aparecer os problemas?”

👉 Isto activa a observación e fai explícitos os retos sen falar aínda de código.

---

## 🕑 Fase 2. Exploración individual (10 min) — *Debuxa o que pensas que fai o programa*

Cada estudante:

1. Debuxa nun papel **unha grella pequena** (p.ex. 6×6).
2. Tenta **colocar dúas ou tres palabras** manualmente.
3. Anota que decisións tivo que tomar:

   * escoller celda inicial
   * escoller dirección
   * comprobar se cabe
   * comprobar se non choca con outra palabra
   * como encher os ocos baleiros
4. Identificar que parte lle resultou máis costosa.

👉 O obxectivo é que experimenten manualmente o proceso exacto que logo terá que executar un algoritmo.

---

## 🕒 Fase 3. Discusión en pequenos grupos (15 min) — *Descompoñer o problema*

Cada grupo (3–4 persoas) comparte as súas ideas e constrúe unha primeira lista de pasos.

Guía de preguntas (para circular polos grupos):

* “Como decidides a posición inicial dunha palabra?”
* “Permitides solapamentos ou non? En que condicións?”
* “O programa debe reintentar? Canto?”
* “E se a palabra non cabe nunca? Como o detectariades?”
* “Como encher os ocos baleiros?”

Ao final, o grupo elabora un **primeiro borrador dun algoritmo** de máximo 8–10 pasos.

---

## 🕓 Fase 4. Reto guiado (20 min) — *Facemos emerxer as decisións e a estrutura dos datos*

Agora preguntas máis técnicas para elevar o nivel:

### 🔧 1. Representación de datos

> “Como representaría un programa a grella? E as palabras?”

As respostas que deberían emerxer:

* grella → lista de listas, matriz 2D, array
* palabras → lista de strings
* posición → tupla (fila, columna)
* dirección → offsets (dx, dy)

---

### 🧭 2. Estratexia para colocar palabras

Lanza preguntas que revelen a necesidade de comprobacións:

* “Que fai o programa se a palabra sobresae polo bordo?”
* “E se choca con outras palabras xa colocadas?”
* “Cando se considera que unha posición é válida?”

Isto leva ao alumnado a inventar estas funcións (conceptualmente):

* `cabe_en(grelha, palabra, pos, direccion)`
* `encaixa_con_existente(grelha, palabra, pos, direccion)`
* `colocar_palabra(...)`

---

### 🎲 3. Comportamento non determinista

> “O programa ten que elixir unha posición e unha dirección… como escolle?”

Aquí aparecerán dúas liñas:

* estratexias deterministas: buscar sistematicamente
* estratexias aleatorias: proba aleatoria ata que encaixe

Logo pregúntase:

> “E se tras 100 intentos non encaixa? Que se fai?”

👉 Introduces a noción de *fallo controlado* e *backtracking*, pero sen chamalo.

---

## 🕔 Fase 5. Deseño modular (15 min) — *De pasos a funcións*

Cada grupo debe transformar o seu algoritmo en **módulos/funccións** sen escribir código.

Guía (apúntase na pizarra):

* `crear_grelha(n, m)`
* `colocar_todas_as_palabras(lista_palabras)`
* `colocar_1_palabra(...)`
* `probar_posicion(...)`
* `encher_baleiros(...)`
* `imprimir_grelha(...)`

A pregunta clave:

> “Cal destas funcións poderías implementar ti mesmo en casa sen cambiar o resto?”

👉 Isto é modularidade real e pensamento computacional.

---

## 🕕 Fase 6. Extensión opcional (10 min) — *Parámetros extra e complexidade*

Agora que teñen un sistema, pregunta:

* “Como cambiaría o algoritmo se permitimos diagonais?”
* “E palabras do revés?”
* “Canto tempo calculades que tarda un algoritmo que proba aleatoriamente ata conseguir encaixar todo?”
* “Pódese quedar atrapado nun bucle?”
* “É máis eficiente colocar primeiro as palabras longas?”

Isto activa a reflexión sobre complexidade e heurísticas de optimización.

---

## 🕖 Fase 7. Peche (5 min)

* Cada grupo comparte **unha idea clave** que descubriu.
* O docente pecha coa frase marco:

  > “Hoxe non programamos unha sopa de letras.
  > **Pensamos como a pensa un programa**.”

---

# 📦 Resultado final esperado (para casa)

Cada estudante implementa (nunha ou varias sesións posteriores):

1. Representación da grella.
2. Función para colocar palabras horizontal e verticalmente.
3. Comprobación de colisións e bordes.
4. Relleno final con letras aleatorias.
5. [Opcional] diagonais, palabras ao revés, heurísticas.

---

## 🧩 Notas didácticas

* Esta actividade **constrúe pensamento algorítmico** antes de traballar estruturas como dicionarios ou índices.
* É altamente visual, física e divertida → funciona moi ben antes de pasar a problemas máis abstractos.
* Permite ver **como emerxe a noción de restrición, comprobación, ciclo e función** de forma natural.
* Encadea moi ben coa actividade do índice (a seguinte): ambas tratan de

  * analizar un problema,
  * descompoñelo,
  * identificar dependencias,
  * e deseñar unha solución modular.

---

Se queres, podo preparar:

* **unha versión imprimible A4** para docentes (guión da sesión),
* **unha ficha para o alumnado**,
* ou **exemplos de sopas de letras pequenas** para usar como material manipulable.
