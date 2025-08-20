package java_LinkedList;

public class LinkedList_Client {
	
	public static void main(String[] args) throws Exception {
		LinkedList ll = new LinkedList();
		ll.addFirst(10);
		ll.addLast(20);
		ll.add_at_index(30, 1);
		System.out.println(ll.getFirst());
		System.out.println(ll.getLast());
		System.out.println(ll.get_at_index(1));
		ll.Display();
		ll.removeFirst();
		ll.Display();
		ll.removeLast();
		ll.Display();
	}
}
