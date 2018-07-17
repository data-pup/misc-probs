struct BTree<T>
where
    T: Clone + Copy,
{
    value: Option<T>,
    left: Option<Box<BTree<T>>>,
    right: Option<Box<BTree<T>>>,
}

impl<T> BTree<T>
where
    T: Clone + Copy,
{
    fn new() -> Self {
        Self {
            value: None,
            left: None,
            right: None,
        }
    }

    fn value(&self) -> Option<&T> {
        self.value.as_ref()
    }

    fn push(&mut self, value: T) {
        if self.value.is_none() {
            self.value = Some(value);
        } else if self.left.is_none() {
            let mut new_node = BTree::new();
            new_node.push(value);
            self.left = Some(Box::new(new_node));
        } else if self.right.is_none() {
            let mut new_node = BTree::new();
            new_node.push(value);
            self.right = Some(Box::new(new_node));
        } else {
            unimplemented!();
        }
    }

    fn get(&self, value: T) -> Option<&BTree<T>> {
        if self.value.is_none() {
            return None;
        } else if let res @ Some(_) = self.left.as_ref().and_then(|l| l.get(value)) {
            res
        } else if let res @ Some(_) = self.right.as_ref().and_then(|l| l.get(value)) {
            res
        } else {
            None
        }
    }

    fn get_mut(&mut self, value: T) -> Option<&mut BTree<T>> {
        if self.value.is_none() {
            return None;
        } else if let res @ Some(_) = self.left.as_mut().and_then(|l| l.get_mut(value)) {
            res
        } else if let res @ Some(_) = self.right.as_mut().and_then(|l| l.get_mut(value)) {
            res
        } else {
            None
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn build_empty_tree() {
        let tree: BTree<u32> = BTree::new();
    }

    #[test]
    fn add_single_value() {
        let mut tree: BTree<u32> = BTree::new();
        let val = 1;
        tree.push(val);
        assert_eq!(tree.value(), Some(&val));
    }

    #[test]
    fn create_test_tree() {
        let mut tree: BTree<u32> = BTree::new();
        tree.push(5);
        tree.push(4);
        tree.push(8);

        let mut curr = tree.get_mut(4);
        curr.unwrap().push(11);

        // curr = tree.get_mut(11);
        // curr.push(7);
        // curr.push(2);

        // curr = tree.get_mut(8);
        // curr.push(13);
        // curr.push(4);

        // curr = tree.get_mut(4);
        // curr.push(5);
        // curr.push(1);
    }
}
