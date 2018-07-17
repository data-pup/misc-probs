use std::collections::HashMap;

type NodeId = u32;

struct Node<T> {
    value: T,
    id: NodeId,
}

struct BTree<T> {
    nodes: HashMap<NodeId, Node<T>>,
    edges: HashMap<NodeId, (NodeId, NodeId)>,
    root: Option<NodeId>,
}

impl<T> BTree<T> {
    fn new() -> Self {
        Self {
            nodes: HashMap::new(),
            edges: HashMap::new(),
            root: None,
        }
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
