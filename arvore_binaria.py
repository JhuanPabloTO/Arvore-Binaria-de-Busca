
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        #cria o nó que vai ser inserido na árvore
        newNode = Node(data)
       
        #verifica se árvore esta vazia e caso sim insere na raiz
        if (self.isEmpty()):
            self.root = newNode
            return
        
        #insere recursivamente na arvore
        self.insertRecursive(self.root, newNode)
        
    def insertRecursive(self, currentNode, newNode):
        #verificar se o novo nó sera inserido na esquerda
        if newNode.data < currentNode.data:
            #Filho do nó visitado é nulo (vai ser inserido nesta posicao)
            if currentNode.left is None:
                currentNode.left = newNode
            else:
                self.insertRecursive(currentNode.left, newNode)
                
       #verificar se o novo nó sera inserido a direita
        else:
            if currentNode.right is None:
                currentNode.right = newNode
            else:
                self.insertRecursive(currentNode.right, newNode)
  
    #retorna verdadeiro se árvore vazia(root = none) ou árvore com pelo menos
    #1 elemento (retorna isEmpty = false)    
    def isEmpty(self):
        return self.root == None
    
    #imprime os nós da arvore em pre-ordem (raiz, esquerda, direita)
    def printPreOrdem(self, no):
        if no != None:
            print(no.data)
            self.printPreOrdem(no.left)
            self.printPreOrdem(no.right)
    
    
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(15)

print("Pre-ordem:")
tree.printPreOrdem(tree.root)