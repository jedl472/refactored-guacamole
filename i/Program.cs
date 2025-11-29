using System;

namespace graph_utility {
  internal class Program {
    class Node {
      public int value;
      public int uloha_db;
      public int distanceFromOrigin;

      public Node? predecessor;
    }

    class Graph {
      public Dictionary<int, List<int>> edges = new Dictionary<int, List<int>>(); // list of node values connected by 
      public List<Node> adjacement_nodes(Node originNode) { 

      }
    }

    class LIFO {
      public List<Node> queue;

      public void add(Node node) {
        queue.Add(node);
      }
      public Node removeElement() { 
        Node node = queue[0];
        queue.RemoveAt(0);

        return node; 
      }
    }

    class BFS {
      Graph graph;
      List<Node> explored;
      LIFO queue;
      int target_value;

      void step() {
        foreach (Node node in graph.adjacement_nodes(queue.removeElement()))
        {
          if(node.value == target_value) {
            backtrack();
          } else {
            queue.add(node);
          }
        }
      }

      void backtrack() {}
    }


    static void Main(string[] args) {
       Graph graph = new Graph();
      
      

       int pocetUzivatelu = Int32.Parse(Console.ReadLine());
       string hrany = Console.ReadLine();

       foreach(string hrana in hrany.Split(' ')) {
         int[] dvojice = new int[] { Int32.Parse(hrana.Split('-')[0]), Int32.Parse(hrana.Split('-')[1]) };

         if(graph.edges.ContainsKey(dvojice[0])) {
           graph.edges[dvojice[0]].Add(dvojice[1]);
         } else {
           graph.edges.Add(dvojice[0], new List<int> { dvojice[1] });
         }

         if(graph.edges.ContainsKey(dvojice[1])) {
           graph.edges[dvojice[1]].Add(dvojice[0]);
         } else {
           graph.edges.Add(dvojice[1], new List<int> { dvojice[0] });
         }
      
      }


      // printing out the graph dict
      foreach (var kvp in graph.edges)
      {
        Console.WriteLine($"{kvp.Key}: {string.Join(", ", kvp.Value)}");
      }

  }
}
