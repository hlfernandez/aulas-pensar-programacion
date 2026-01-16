Exactamente 💯 — **é unha idea excelente** e encaixa perfectamente co espírito da sesión “aulas para pensar”.
Facendo que o ficheiro CSV estea **ordenado por ID**, introduces de forma implícita unha propiedade estrutural que algunhas mentes curiosas detectarán e **explotarán espontaneamente**.

Déixoche unha análise detallada de por que isto funciona tan ben, e como podes aproveitalo didacticamente 👇

---

## 💡 Por que ordenar o CSV favorece a aparición da busca binaria

1. **Permite estratexias diversas e comparables.**

   * Co ficheiro desordenado, todas as solucións acaban sendo *forzosamente lineais*.
   * Co ficheiro ordenado, hai **punto de partida común**, pero **varias rutas posibles**:

     * seguir lendo liña a liña,
     * facer saltos (p. ex. “vou á metade do ficheiro”),
     * ou propoñer un índice auxiliar.
       → Tes diversidade de solucións e polo tanto **materia prima para o debate colectivo**.

2. **Crea a condición lóxica necesaria para que emerxa a busca binaria.**
   Sen orde non hai lóxica de “maior/menor”; coa orde, é natural que alguén diga:

   > “Podemos comezar polo medio e ver se o ID é maior ou menor.”
   > Ese *clic mental* é exactamente o tipo de pensamento algorítmico que buscas provocar.

3. **Introduce o concepto de propiedade dos datos.**
   Podes lanzar unha pregunta metacognitiva:

   > “Que características teñen os datos que fan posible esta mellora?”
   > → Isto leva ao concepto de *supostos previos* (precondicións) dun algoritmo, un paso fundamental no razoamento formal.

4. **Permite medir o impacto da estrutura na complexidade.**
   Ao final, cando compares estratexias, o alumnado pode:

   * identificar *lineal* vs *logarítmica* vs *constante*,
   * e razonar sobre *custo vs preparación (indexación)*.

---

## 🧭 Como integrar isto na sesión

Na **Fase 4 (Reto guiado)** podes facer un pequeno *twist*:

> Dilles que o ficheiro `alumnos.csv` xa está ordenado por `id`.
> Non digas por que nin que fagan coa orde — só menciona o feito.

A partir de aí:

* deixa que exploren libremente;
* apunta as estratexias que vaian xurdindo na pizarra;
* e **anima a defender por que pensan que o seu método sería máis rápido**.

💬 Se aparece a idea da busca binaria, felicita o razoamento, e **documenta o proceso** (pódese comparar despois cunha implementación real).

---

## 🧩 Variante práctica (por se queres prolongar o exercicio)

Podes mesmo facer que haxa **dúas versións do CSV**:

* unha desordenada (`alumnos_raw.csv`);
* outra ordenada (`alumnos_sorted.csv`).

E formular o reto así:

> “Probad o voso método con ambos ficheiros. Que observades?”

→ Isto reforza a noción de que **a estrutura dos datos condiciona o algoritmo posible**, algo que encaixa perfectamente no pensamento computacional de primeiro curso.

---

Se queres, podo actualizarche o **plan da sesión de 90’** co ficheiro ordenado e as indicacións adaptadas para que esa emerxencia da busca binaria ocorra de forma natural (sen módulo opcional separado). ¿Queres que o reformule así?
