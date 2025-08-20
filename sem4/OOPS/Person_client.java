package OOPS;

public class Person_client {
	
	public static void main(String[] args) {// throws Exception {
		// TODO Auto-generated method stub
		System.out.println("Hey");
		Person p = new Person("kunal", 28);
		Person p1 = new Person("Ankita", 128);
		System.out.println(p.getAge());
		System.out.println(p.getName());
//		p.age = 99;
		p1.setAge(-18);
		System.out.println(p1.getAge());
		System.out.println("Bye");
	}
}
