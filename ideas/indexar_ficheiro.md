
## 💡 Sesión: *Pensar como un programa — de ler a indexar*

**Duración:** 90 minutos
**Nivel:** 1º de Grao en Enxeñaría Informática / IA
**Tamaño de grupo:** 15 estudantes (3–4 por grupo)
**Enfoque:** *Aulas para pensar* — metacognición, colaboración e deseño de sistemas

---

### 📌 **Nota para o profesor**

⚠️ **Importante:** O CSV proporcionado está **ordenado por ID**. É posible que algún grupo detecte esta característica e propoña explotala (por exemplo, parando a busca cando o ID sexa maior que o buscado, ou incluso suxerindo unha busca binaria).

**Como xestionalo:**
- **Validar e reforzar:** Se xurde, valóraa positivamente como observación aguda.
- **Non profundizar aínda:** Explica que é unha boa idea, pero que de momento centrarémonos no contraste entre busca secuencial completa e acceso por índice (dicionario).
- **Apuntar para o futuro:** Podes mencionar que a ordenación é outra forma de estruturar datos que se verá máis adiante no curso.

Isto pode servir para **diferenciar** e conectar con estudantes máis avanzados, sen desviar o obxectivo principal da sesión.

---

### 🎯 Obxectivos de aprendizaxe

| Dimensión     | Obxectivo                                                               |
| ------------- | ----------------------------------------------------------------------- |
| Cognitiva     | Comprender a diferenza entre lectura secuencial e acceso indexado.      |
| Metacognitiva | Reflexionar sobre o proceso de pensamento e resolución de problemas.    |
| Técnica       | Relacionar o deseño dun algoritmo co seu custo temporal (O(n) vs O(1)). |
| Social        | Explicar e compartir estratexias de resolución en grupo.                |

---

### 🧰 Materiais e preparación

* Un **CSV impreso** (20–30 liñas, 5–6 columnas): ver exemplo completo abaixo.
* Follas **A3** en branco ou plantilla (ver abaixo).
* Rotuladores, celo para pegar nas paredes.
* Pizarra ou pantalla para resumo final.

#### 📄 **CSV de exemplo (imprimir para cada grupo)**

```csv
id,nome,idade,cidade,nota
101,Ana Silva,19,Vigo,8.5
102,Carlos Méndez,20,A Coruña,7.2
103,Lucía Fernández,18,Santiago,9.1
104,Marcos López,21,Ourense,6.8
105,Sara Rodríguez,19,Pontevedra,8.0
106,Diego Rama,20,Ferrol,7.5
107,Marta González,19,Lugo,8.8
108,Pablo Núñez,18,Vigo,6.5
109,Carmen Vidal,21,Santiago,9.0
110,Raúl Campos,19,A Coruña,7.8
111,Laura Prado,20,Pontevedra,8.3
112,Javier Torres,18,Ourense,7.0
113,Elena Varela,19,Vigo,9.2
114,Miguel Castro,21,Santiago,6.9
115,Noa Pérez,20,A Coruña,8.6
116,David Iglesias,19,Ferrol,7.4
117,Sofía Ríos,18,Lugo,8.1
118,Adrián Suárez,20,Vigo,7.7
119,Claudia Martín,19,Pontevedra,9.3
120,Bruno Soto,21,Santiago,6.6
121,Iria Blanco,18,A Coruña,8.9
122,Daniel Regueiro,20,Ourense,7.3
123,Andrea Moure,19,Vigo,8.4
124,Sergio Lima,21,Ferrol,7.1
125,Patricia Vázquez,20,Santiago,9.4
```

**IDs recomendados para buscar durante a actividade:**
- **103** (Lucía Fernández) — ao principio da lista
- **115** (Noa Pérez) — no medio
- **125** (Patricia Vázquez) — ao final
- **130** — ID inexistente (para provocar reflexión sobre condicións de parada)

💡 *A plantilla A3 ten 3 zonas:*

1. 🧩 **Etapas do proceso** (ler, buscar, indexar, etc.)
2. 🧠 **Ideias e decisións** (como o fixemos, que custo ten)
3. 💻 **Funcións en código** (nome, entrada, saída)

---

## 🕒 **Desenvolvemento da sesión (90 min)**

---

### 🔹 **Fase 1 – Activación e contexto (10 min)**

**Obxectivo:** situar o reto e activar o pensamento computacional.

Instrución:

> “Este CSV é unha pequena base de datos.
> O voso obxectivo é atopar a información dun estudante dado o seu *ID*, lendo o ficheiro liña a liña.”

**Preguntas para provocar pensamento:**

* Que significa “buscar rapidamente”?
* Como o fariades se o CSV tivese 10.000 liñas?
* Que pasos seguiría un programa? E unha persoa?

💭 O docente **anota ideas clave** na pizarra: *ler, comparar, gardar, repetir...*

---

### 🔹 **Fase 2 – Exploración guiada (25 min)**

**Obxectivo:** facer emerxer estratexias de lectura e acceso.

Tarefa:
Cada grupo debe atopar 3–4 IDs concretos no CSV.

Instrución:

> “Non podedes escribir código nin usar ordenador.
> Anotade no A3 como o facedes, que pasos seguides e que dificultades aparecen.”

O docente circula e pregunta:

* “Como sabedes que xa mirastes todo?”
* “Que vos faría máis rápido?”
* “Que patrón seguistes?”

👉 Emerxe a noción de lectura secuencial e o custo **O(n)** de buscar liña a liña.

---

### 🔹 **Fase 3 – Reflexión metacognitiva (15 min)**

**Obxectivo:** tomar conciencia do proceso e verbalizalo.

Cada grupo presenta brevemente o seu método (2–3 min).
O docente escribe na pizarra as categorías que aparecen:

* lectura liña a liña
* busca visual
* marcas ou mini-índices manuais
* comparacións, revisións, etc.

**Preguntas guía:**

> “Cantas operacións fixestes ata atopar o último?”
> “Poderíades facelo máis rápido se gardásedes algo?”

💥 Aquí introdúcese naturalmente a idea de **crear un índice** e o salto conceptual cara ao acceso **O(1)**.

---

### 🔹 **Fase 4 – Mini-exposición e deseño do índice (15 min)**

**Obxectivo:** conectar o proceso manual coa noción de complexidade e estrutura de datos.

Explicación interactiva (5–7 min):

* Ler fila a fila → tempo proporcional a n → **O(n)**.
* Crear un dicionario `{id: posición}` → acceso directo → **O(1)**.
* Trade-off: máis tempo ao principio, menos nas buscas.

**💡 Metáfora do índice:**

> "Pensade nun **índice dun libro**: podedes ir páxina por páxina ata atopar o tema que buscades (O(n)), ou ben consultar o índice alfabético ao final, que vos di directamente en que páxina está (O(1)).
>
> O mesmo pasa cun **directorio telefónico** ordenado por apelidos: se coñecedes o apelido, buscades directamente na letra correspondente; se non, terías que mirar páxina por páxina.
>
> No noso caso, o 'índice' é un dicionario que garda: `{ID → posición na lista}`, para que logo podamos saltar directamente a esa liña."

Tarefa curta en grupo (8 min):

> "Como poderiades crear un sistema que garde as posicións dos rexistros para acceder directamente por ID?"

Cada grupo esboza no A3 **a súa idea de índice ou estrutura auxiliar.**

---

### 🔹 **Fase 5 – Workflow global e mapeo a código (20 min)**

**Obxectivo:** consolidar o sistema global e preparar a implementación.

#### 🧩 Paso 1: debuxar o workflow (10 min)

> “Debuxade o voso proceso completo: dende que abrimos o CSV ata que devolvemos o resultado.”

Incluír:

* Etapas ou bloques
* Frechas de fluxo
* Condicións ou repeticións

#### 💻 Paso 2: mapeo a funcións (5–7 min)

> “Imaginade que cada bloque é unha función: que nome tería? que recibe? que devolve?”

Exemplo:

* `ler_csv(ruta) → lista_de_liñas`
* `crear_indice(lista) → dict_id_a_posicion`
* `buscar_por_id(id, indice) → liña`

#### 🧠 Paso 3: preparación para casa (3 min)

Tarefa individual:

1. Implementar en Python dúas versións:

   * Busca secuencial (O(n))
   * Busca con índice (O(1))
2. Comparar tempos con `timeit`.
3. Reflexionar:

   > “Que aprendín sobre o meu xeito de pensar e organizar o problema?”

---

### 🧾 **Peche (5 min)**

Breve posta en común colectiva:

> “Que aprendemos sobre como pensamos? Que nos fixo máis eficientes?”

Resume na pizarra:

```
Ler → Procesar → Indexar → Acceder
O(n)        vs.         O(1)
```

---

## 🧩 **Plantilla A3 suxerida (para imprimir)**

```
┌───────────────────────────────────────────────┐
│   🧩 ETAPAS DO PROCESO                        │
│   (Qué fixemos, en que orde, que decisións)   │
│   ________________________________________    │
│                                               │
│                                               │
│                                               │
├───────────────────────────────────────────────┤
│   🧠 IDEAS E REFLEXIÓNS                       │
│   (Como melloramos? que problema resolvimos?) │
│   ________________________________________    │
│                                               │
│                                               │
│                                               │
├───────────────────────────────────────────────┤
│   💻 POSIBLES FUNCIÓNS EN CÓDIGO              │
│   (nome, entrada, saída, relacións)           │
│   ________________________________________    │
│                                               │
│                                               │
│                                               │
└───────────────────────────────────────────────┘
```
