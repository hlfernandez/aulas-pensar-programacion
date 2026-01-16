# 🧠 Actividade: *Pensar como un programa — Conversor de unidades*

- **Duración:** 90 minutos
- **Nivel:** 1º Grao en Enxeñaría Informática / IA
- **Formato:** Aula para pensar (traballo cooperativo + pensamento visible)
- **Grupo:** ~15 estudantes (3–4 por grupo)
- **Produto da sesión:**
Deseño colectivo dun algoritmo e dunha arquitectura de solución para comparar tamaños expresados con unidades distintas.

---

## 🕐 Fase 1. Lanzamento do reto (10 min)

**Obxectivo:** poñer en xogo un problema real que require pensamento algorítmico.

O profesor lanza a seguinte pregunta: *sabedes que é un bit e a cantos bytes equivale? a cantos bytes corresponde un kylobyte? e  a cantos bytes corresponde un kibibyte?*

Tras comentar as equivalencias básicas aclaramos que traballaremos con *kibibytes*. Podemos aproveitar para explicar que significa mercar un disco de *1TB* (unidades do sistema internacional en base 10).

E lanzamos o reto, *como podemos deseñar un programa para determinar o resultado das seguintes comparacións entre unidades?*

```
1024B  ?  1KiB
1MiB   ?  1000KiB
1GiB   ?  1024MiB
```

---

## 🕑 Fase 2. Pensamento en grupo (15 min) — *Que pasos fai o programa?*

En grupos de 3–4, con papel grande ou pizarra vertical:

* Deben **describir os pasos** que seguiría o programa.
* Non se permite escribir código: só pasos, debuxos, caixas, frechas.

Guía mínima (se fai falta):

* Que datos de entrada ten o programa?
* Como se vai a especificar o resultado?
* Que información hai dentro dunha cadea como `1024MiB` e como a obtemos?
* Hai algo que teña que pasar sempre antes de comparar?

A idea é que emerxa o fluxo **extraer** (separar a cadea en valor e unidades), → **transformar** (a unha unidade común: bytes) → **comparar** (xa só queda comparar entre bytes).

---

## 🕒 Fase 3. Pensamento visible compartido (15 min)

Cada grupo expón o seu esquema e o profesor:

* recompila os pasos comúns,
* aliña vocabulario,
* fai visibles patróns repetidos.

No encerado acaba aparecendo algo como:

1. Separar número e unidade
2. Converter a unha unidade común
3. Comparar números

Pregunta clave:

> “Cal destes pasos podería cambiar sen tocar os demais?”

👉 Introduces **separación de responsabilidades** sen nomeala formalmente. Repásase o concepto de **abstracción**.

---

## 🕓 Fase 4. Estrutura e representación (20 min)

Agora o foco está no **deseño**, non no resultado.

### 🔧 Representación

Pregunta ao grupo:

> “Que tipo de datos manexa cada paso?”

O alumnado propón:

* string → `(int, string)`
* unidade → factor
* resultado → número

O docente pode escribir exemplos parciais:

```
"1024MiB" → (1024, "MiB")
```

### 🔁 Conversión

Pregunta detonante:

> “Como lle explicamos a un programa canto vale un MiB en bytes?”

As solucións emerxen:

* funcións separadas,
* táboa de equivalencias,
* constantes.

Aquí aparece **naturalmente** o dicionario como estrutura axeitada.

---

## 🕔 Fase 5. Debate de deseño (15 min) — *E cando isto medra?*

Plantexa un escenario evolutivo:

> “Mañá queremos engadir `TiB`, pasado `PiB`.
> Que solución escala mellor?”

Deixa que o grupo critique:

* moitos `if` / `match`,
* duplicación de código,
* cambios repartidos por todo o programa.

Pregunta sutil:

> “Que parte do sistema debería ‘saber’ canto vale unha unidade?”

👉 Isto prepara o terreo para POO sen impoñela.

---

## 🕕 Fase 6. Extensión conceptual (opcional) — *Deseño orientado a obxectos* (10–15 min)

Só se o grupo vai fluído.

No encerado, sen código:

* unha entidade `Unidad`
* método `a_bytes()`
* subclasses `KiB`, `MiB`, `GiB`
* unha factoría que recibe `"1024MiB"` e devolve un obxecto

Pregunta potente:

> “Que gañamos se agora podemos escribir `u1 < u2`?”

👉 Emerxe encapsulación, polimorfismo e sobrecarga de operadores.

---

## 🕖 Fase 7. Peche (5 min)

Peche explícito, verbalizado:

> “Hoxe non aprendemos unidades.
> Practicamos **como pensa un programa**:
>
> * separando tarefas,
> * normalizando datos,
> * e deseñando solucións que poden evolucionar.”

---

## 📦 Traballo para casa (coherente coa sesión)

Progresivo e aberto:

1. Implementar a solución básica funcional.
2. Refactorizar usando unha táboa de factores.
3. [Opcional] Versión POO con operadores de comparación.
4. [Extra] Xestión de erros e entradas inválidas.

---

## 🧭 Por que esta actividade encaixa en *aulas para pensar*

* Todo o razoamento é **social e visible**.
* Hai múltiples solucións correctas.
* O código aparece *despois*, como consecuencia do deseño.
* Traballa exactamente o tipo de pensamento que logo se necesita para:

  * índices,
  * estruturas de datos,
  * deseño de APIs.

---

Se queres, o seguinte paso lóxico sería:

* **alinhar esta actividade coa da sopa de letras e coa do índice** nunha progresión de 3 prácticas,
* ou preparar unha **rúbrica curta** para avaliar deseño, non só código.

Ti dirás.
