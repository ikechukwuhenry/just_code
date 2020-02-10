#include <bits/stdc++.h>

namespace treap
{

/**
 * basic chinable storage unit.
 *
 *
 * @tparam T the type of data stored in the treap
 */
template <typename T>
class Node {
	public:
		//constructor
		Node();
		Node(T _value);
		//member variables
		T value;
		double priority;
		std::shared_ptr<Node<T>> left = nullptr;
		std::shared_ptr<Node<T>> right = nullptr;
	private:
		double uniform();
};

/**
 * Standard Treap implementation with log(h) lookup.
 * where: h is the height of the tree
 *
 * The ADT contains the following methods:
 * - insert: insert a new node into the tree
 * - delete: deletes the given node from the tree
 * - search: search the given node into the tree
 * - successor: search the successor of the give node in the tree
 * - min: returns the min of the tree
 * - max: returns the max of the tree
 *
 * @tparam T the type of data stored in the bst
 */
template<typename T>
class Treap {
	private:
		std::shared_ptr<Node<T>> root = nullptr;
	public:
		Treap();
		Treap(const std::vector<T>& _data);
	public:
		void insert(const T& key);
		std::shared_ptr<Node<T>> search(const T& key);
		std::shared_ptr<Node<T>> successor(const T& key);
		std::shared_ptr<Node<T>> min();
		std::shared_ptr<Node<T>> max();
		void erase(const T& key);
		void traverse();
	private:
		void insert(const T& key, std::shared_ptr<Node<T>> node);
		std::shared_ptr<Node<T>> search(const T& key, std::shared_ptr<Node<T>> node);
		std::shared_ptr<Node<T>> successor(const T& key,
										   std::shared_ptr<Node<T>> node,
										   std::shared_ptr<Node<T>> ancestor=nullptr);
		void rotate_left(std::shared_ptr<Node<T>> node);
		void rotate_right(std::shared_ptr<Node<T>> node);
		void erase(const T& key,
				   std::shared_ptr<Node<T>> node,
				   std::shared_ptr<Node<T>> father=nullptr);
		void traverse(std::shared_ptr<Node<T>> node, int level = 0);
};

} // namespace Node


