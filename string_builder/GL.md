## Construír un StringBuilder: Encapsulación e eficiencia

Esta proposta de tarefa ten como obxectivo que o alumnado acade o deseño dunha clase `StringBuilder` que permita construír cadeas de texto de forma eficiente mediante programación orientada a obxectos.

A nivel de pensamento computacional, o reto principal é comprender **por que a concatenación repetida de cadeas é ineficiente** (cando as cadeas non son mutables) e como unha estrutura de datos mutable interna (unha lista) pode resolver este problema. A nivel técnico, traballarase a **encapsulación** (ocultando a representación interna), o **deseño de APIs** (definindo unha interface clara e útil) e a distinción entre **inmutabilidade e mutabilidade**.

En linguaxes coma C++ pode ser un exercicio de menos interese xa que os obxectos da clase `std::string` son mutables e por tanto a concatenación soe ser eficiente (dependerá de reservas/reallocs), pero en linguaxes coma Java ou Python, nos que as cadeas non son mutables, ten sentido. De feito en Java xa existe dita clase `StringBuilder` mentres que en Python o patrón idiomático é usar listas con `join`. 

Implementar unha clase propia para proporcionar esta funcionalidade é un bo exercicio didáctico para comprender conceptos fundamentais de POO e eficiencia algorítmica, especialmente adecuado para un curso de programación onde xa se ten base de estructuras de datos e estase a introducir a orientación a obxectos.

### Desenvolvemento da sesión

#### Fase 1: Activación e exploración do problema

- **Tempo estimado**: 10'

O docente comeza a sesión reunindo ao alumnado de pé e lanzando unha pregunta que os faga reflexionar:

> *Cantos de vós concatenastes cadeas con `+` nas vosas prácticas? Sabedes cantas operacións se realizan internamente cando facedes isto 10, 100 ou 1000 veces?"*

Tras escoitar algunhas respostas, o docente presenta o problema de eficiencia mediante un exemplo no taboleiro:

```python
resultado = ""
for i in range(1000):
    resultado = resultado + "palabra "
```

A modo de repaso, a pregunta clave é: *Por que este código é ineficiente?*

O docente involucra ao alumnado a participar nun debate, a modo de repaso, para recordar que:

- As cadenas en Python son **inmutables**
- Cada `+` crea unha **nova cadea**, copiando todo o contido anterior
- Con 100 ou 1000 iteracións, estamos copiando moitísimas veces os mesmos datos (custo `O(n²)` en tempo e en copias de memoria; pode obviarse a complexidade se inda non se viu ou aproveitar a actividade para introducila)

Entre todos os presentes debe chegarse á solución idiomática en Python:

```python
partes = []
for i in range(1000):
    partes.append("palabra ")
resultado = "".join(partes)
```

E formula o reto: *E se queremos encapsular este patrón nunha clase reutilizable? Nesta tarefa trátase de crear o noso propio `StringBuilder`!*

Divídese ao alumnado en grupos aleatorios e preséntase o obxectivo: deseñar unha clase que permita construír cadeas eficientemente mediante unha API limpa.

#### Fase 2: Exploración do concepto e requisitos

- **Tempo estimado**: 15'

Neste caso o docente debe orientar ao alumnado cara un deseño da clase, é dicir, que identifiquen os seguintes aspectos:
- Que datos debe almacenar internamente a clase?
- Como debe ser esa estrutura de datos (mutable/inmutable)?
- Que métodos públicos precisa a clase?
- Que fai o construtor?
- Cantas veces se xunta todo en unha cadea final?

Incluso pode pedirse que identifiquen a maneira de usar a súa clase `StringBuilder` antes de implementala (como se faría en TDD e como se fai habitualmente cando se pensa en POO), por exemplo:

```python
sb = StringBuilder()
sb.append("Ola")
sb.append(" ")
sb.append("mundo")
cadea = sb.build()  # "Ola mundo"
```

#### Fase 3: Posta en común e deseño da interface

- **Tempo estimado**: 20'

Os grupos comparten as súas conclusións iniciais e o docente vai consolidando no taboleiro os **elementos consensuados**. Por exemplo, en canto á **estrutura interna:**
- Unha lista privada que almacena as partes.
- Esta lista **non debe ser accesible** dende fóra (encapsulación; en Python soe usarse o prefixo `_` xa que non existe control da visibilidade dos atributos).

De xeito que pode chegarse á seguinte **interface pública mínima:**
```python
class StringBuilder:
    def __init__(self): ...           # Inicializa a lista interna baleira
    def append(self, texto): ...      # Engade texto á lista
    def build(self): ...              # Xunta todo e devolve a cadea final
```

Pode aproveitarse esta fase para debatir co alumnado sobre algunhas decisións de deseño:

1. **Por que `build()` e non simplemente `__str__()`?**
  - Deixa clara a intención de construír a cadea final.
  - Separar responsabilidades: construción vs representación.

2. **Debe `append()` devolver algo?**
  - Pode ser que non.
  - Pode ser que si, que devolva `self` para permitir encadeamento (*method chaining*).

3. **Que pasa se chamamos `build()` múltiples veces?**
   - Debe funcionar: cada vez xunta de novo a lista.

Neste punto o docente pode repasar os conceptos de **TAD** (Tipo Abstracto de Datos) e **encapsulación**: o usuario da clase (cliente) non precisa saber que por dentro hai unha lista, só precisa coñecer a **interface pública** coa que interactuar.

#### Fase 4: Simulación manual e casos de proba

- **Tempo estimado**: 15'

Os grupos deben simular manualmente que acontece internamente coa lista en distintos casos de uso. Nesta fase pedirase ao alumnado que constrúa unha serie de exemplos cos seus resultados esperados, de forma que simulen no taboleiro vertical a evolución da lista interna e o que devolve `build()` en cada paso.

O obxectivo é que entendan como as chamadas aos métodos `append()` modifican o estado interno mentres que `build()` percorre a lista para producir un resultado.

#### Fase 5: Implementación dos casos de proba (individual ou en parellas)

- **Tempo estimado**: 15'

Antes de implementar a clase en si, nesta fase pedirase ao alumnado que escriba o código correspondente as clases anteriores. Isto, sen dicirllo de entrada, é unha aproximación ao *Test Driven Development* (TDD), en que escriben o código das probas antes do código real. Por tanto, deberán pensar nunha maneira de comprobar automáticamente que a clase devolve o que se espera. Nesta fase poderán traballar de maneira individual ou incluso en parellas.

O docente supervisará que o alumnado:
- É capaz de crear instancias da clase e empregalas.
- Ten un conxunto de casos de proba e resultados esperados (fase 4).
- Comeza a intuír como probar sistemáticamente os seus programas.

Antes de pasar á seguinte fase, ao alumnado máis avanzado pode pedírselle que automatice as probas cunha función reutilizable do estilo: `test_string_builder(input_values, expected_result)`.

#### Fase 6: Implementación da clase `StringBuilder` (individual ou en parellas)

- **Tempo estimado**: 45'

Nesta fase, cada persoa implementa individualmente ou en parellas a clase `StringBuilder` en Python seguindo o deseño acordado de xeito que funcionen os tests anteriores.

O docente supervisa que:
- Distinguen entre atributos privados e métodos públicos.
- Comprenden o retorno de `self` en `append()` en caso de que escollesen ese diseño.
- Identifican correctamente os parámetros de entrada/saída.

#### Fase 7: Reflexión metacognitiva

- **Tempo estimado**: 10' (en grupo) ou individual (fóra da aula)

Esta fase de peche permite que o alumnado tome consciencia do seu propio proceso de aprendizaxe. O obxectivo é que o alumno poña de manifesto o aprendido non só sobre o problema en sí, senón tamén sobre **como pensa cando resolve problemas**, de xeito que sexa capaz de identificar os seus propios puntos fortes e áreas de mellora.

Na aula, o docente reúne de novo aos grupos ou á clase completa para unha conversa guiada sobre o proceso completo. Algunhas preguntas clave:

- **Sobre encapsulación e abstracción:**
  - "Por que era importante que a lista interna fose privada?"
  - "Que gaña o usuario da clase ao non ter que preocuparse da lista?"
  - "Como afecta o deseño da interface á facilidade de uso?"

- **Sobre eficiencia:**
  - "Por que é máis eficiente este enfoque que concatenar con `+`?"
  - "En que momento se fai realmente o traballo 'caro' (xuntar as cadeas)?"
  - "Que relación hai entre mutabilidade e eficiencia neste caso?"

- **Sobre deseño de clases:**
  - "Que decisións de deseño foron máis difíciles de tomar?"
  - "Por que devolver `self` en `append()` mellora a usabilidade?"
  - "Como decidistes que métodos debían ser públicos e cales non?"

- **Sobre contexto e práctica real:**
  - "Por que non se usa `StringBuilder` en Python real?"
  - "En que linguaxes (Java, C#, etc.) si que se usa?"
  - "Que aprendestes deste exercicio que poidedes aplicar a outras clases?"

Se a implementación é realizada fóra da aula, podería facerse a reflexión anterior ao comezo da seguinte sesión ou ben pedirlles unha breve reflexión escrita (5-10 liñas) que acompañe ao código entregado, respondendo a 2-3 das preguntas anteriores. Isto axuda a consolidar o aprendido e proporciona información valiosa ao docente sobre as dificultades reais do alumnado.

### Posibles ampliacións

Este exercicio ten potencial para ampliacións:

**Ampliacións técnicas:**
- Implementar métodos adicionais: `clear()`, `is_empty()` ou `size()`.
- Engadir parámetros ao construtor: valores iniciais, prefixo, sufixo, separador, etc.
- Sobrecarga de operadores Python: `__len__()`, `__str__()`, `__repr__()`, `__eq__()`
- Permitir eliminar contido: `remove_last()`, `remove_at(index)`
- Implementar iterador para percorrer as partes sen construír a cadea

**Ampliacións de análise:**
- Medir experimentalmente a diferenza de rendemento entre concatenación con `+` e `StringBuilder` con 1000, 10000 e 100000 iteracións
- Analizar a complexidade algorítmica: O(n²) vs O(n)
