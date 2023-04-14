<h3>PROBLEM STATEMENT: Distância das vilas</h3>
---
<p>O mapa do Minecraft é composto de blocos cúbicos em uma relação de igualdade com o sistema métrico, assim, cada aresta dos blocos tem 1 metro. Dessa forma, é possível identificar localidades por triplas de coordenadas X, Y, Z, na qual X representa a longitude, Y representa a elevação em blocos e Z representa a latitude.</p>
<p>Para simplificar a comunicação, é comum se referir a localidades apenas no plano da superfície do mapa, utilizando apenas as coordenadas X e Z, referindo-se ao ponto no X e Z informados e no Y do ponto da superfície.</p>
<p>Para definir distâncias entre duas localidades é utilizada a fórmula de distância euclidiana, na qual o Y das duas coordenadas pode ser omitido para definir apenas a distância nas duas dimensões. A fórmula de distância euclidiana é:</p>
- D² = (X1 - X2)² + (Z1 - Z2)²
<br/><br/>
<p>Para entregar os ferros para as vilas, Tantan precisaria saber quais as distâncias da sua localidade para cada vila, podendo se programar em suas viagens. Nas anotações de Tantan, as vilas estavam associadas as seguintes coordenadas:</p>
- Hogsmeade (X: 34, Y: 110, Z: 220)
<br/>
- Kakariko (X: 0, Y: 64, Z: 0)
<br/>
- Solitude (X: 140, Y: 200, Z: 456)
<br/><br/>
<p>Sua tarefa é, baseado nas coordenadas atuais de Tantan, listar as distâncias para cada uma das vilas.</p>
<h6>Input</h6>
---
<br/>
- X (número inteiro)
- Z (número inteiro)
<br/><br/>
<p>As duas linhas da entrada são compostas por números inteiros X e Z, que indica a coordenada atual de Steve, sem o Y, que pode ser abstraído como informado na descrição.</p>
<p>Obs: Você deve considerar que a entrada é amigável, ou seja, sempre estará dentro do formato descrito.</p>
<h6>Output</h6>
---
<br/>
- Distancia para Hogsmeade: H (número de ponto flutuante)
<br/>
- Distancia para Kakariko: K (número de ponto flutuante)
<br/>
- Distancia para Solitude: S (número de ponto flutuante)
<br/><br/>
<p>As linhas de saída são compostas por um texto seguido, seguido pela distância da coordenada atual de Tantan para a vila correspondente.</p>
<p>Obs: A distância deve ser aproximada em duas casas decimais.</p>