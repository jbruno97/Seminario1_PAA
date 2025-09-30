from collections import deque

def bfs(graph, s, t, parent):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    queue = deque()
    
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        for v in range(num_nodes):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                
                if v == t: 
                    return True # Caminho aumentante encontrado
    
    return False # Não há mais caminhos disponíveis

def edmonds_karp(graph, s, t):
    num_nodes = len(graph)
    parent = [-1] * num_nodes
    residual_graph = [row[:] for row in graph] 
    max_flow = 0
    
    while bfs(residual_graph, s, t, parent):
        
        path_flow = float("Inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = u
            
        max_flow += path_flow
        
        v = t
        while v != s:
            u = parent[v]
            
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            
            v = u
            
    return max_flow

# --- Definição da Instância do Problema (Data Center 7 Nós) ---

node_labels = {
    0: 's', 1: 'R1', 2: 'R2', 3: 'P1', 4: 'P2', 5: 'P3', 6: 't'
}
source = 0  # Fonte
sink = 6    # Sumidouro

# Matriz de Capacidades (7x7)
# Índices: 0=s, 1=R1, 2=R2, 3=P1, 4=P2, 5=P3, 6=t
capacities = [
    [0, 15, 15, 0, 0, 0, 0],  # s
    [0, 0, 0, 8, 7, 0, 0],   # R1
    [0, 0, 0, 0, 5, 10, 0],  # R2
    [0, 0, 0, 0, 0, 0, 8],   # P1
    [0, 0, 0, 0, 0, 0, 12],  # P2
    [0, 0, 0, 0, 0, 0, 10],  # P3
    [0, 0, 0, 0, 0, 0, 0]    # t
]

# --- Execução e Apresentação da Solução ---

fluxo_maximo_resultado = edmonds_karp(capacities, source, sink)

print(f"Instância do Problema (7 Nós):")
print("Nós: s=0, R1=1, R2=2, P1=3, P2=4, P3=5, t=6")
print("--- Arestas e Capacidades ---")
for i, row in enumerate(capacities):
    for j, cap in enumerate(row):
        if cap > 0:
            print(f"Aresta {node_labels[i]} -> {node_labels[j]} | Capacidade: {cap}")

print("\n--- Solução do Algoritmo Edmonds-Karp ---")
print(f"O Fluxo Máximo que o Data Center pode processar é: {fluxo_maximo_resultado}")