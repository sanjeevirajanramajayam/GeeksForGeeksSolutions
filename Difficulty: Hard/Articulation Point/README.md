<h2><a href="https://www.geeksforgeeks.org/problems/articulation-point2616/1">Articulation Point</a></h2><h3>Difficulty Level : Difficulty: Hard</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p>Given an undirected graph with<strong> V</strong> vertices and <strong>E</strong> edges. The graph is represented as a 2D array <strong>edges[][]</strong>, where each element edges[i] = [u, v] indicates an undirected edge between vertices u and v. Return all the articulation points (or cut vertices) in the graph. An articulation point is a vertex whose removal, along with all its connected edges, increases the number of connected components in the graph.&nbsp;</p>
<ul>
<li>The given graph may be disconnected, i.e., it may consist of more than one connected component.&nbsp;</li>
<li>If no such point exists, return {-1}.</li>
</ul>
<p><span style="font-size: 14pt;"><strong>Examples :</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> V = 5, edges[][] = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/892595/Web/Other/blobid3_1744109134.png" alt="" width="277" height="151">
<strong>Output: </strong>[1, 4]
<strong>Explanation: </strong>Removing the vertex 1 or 4 will <span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; white-space: normal;">disconnects </span>the graph as-
<img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/892595/Web/Other/blobid4_1744109133.png" alt="" width="190" height="165">   </span><img style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;" src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/892595/Web/Other/blobid5_1744109133.png" alt="" width="191" height="163"></pre>
<pre><span style="font-size: 14pt;"><strong>Input:</strong> V = 4, edges[][] = [[0, 1], [0, 2]]
<strong>Output: </strong>[0]
<strong>Explanation: </strong>Removing the vertex 0 will increase the number of disconnected<span style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; white-space: normal; font-size: 14pt;">&nbsp;</span>components to 3.<span style="font-size: 14pt;">&nbsp;</span><span style="font-size: 14pt;">&nbsp;</span><br></span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ V, E ≤ 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Graph</code>&nbsp;<code>DFS</code>&nbsp;<code>BFS</code>&nbsp;