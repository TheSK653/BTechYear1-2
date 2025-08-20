package java_functions;

public class Fun_Demo_2 {
	static int val = 100;             		//Global Variable: inside the class but outside the main method.
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello");
		int a=8;
		int b=7;
		System.out.println(val);
		System.out.println(Add(a,b));
		System.out.println(val);
		System.out.println("Bye");		
	}
	public static int Add(int a, int b) {
		int c = a+b;
		val = 80;
		Fun_Demo_2.val = Fun_Demo_2.val-5;		//to use local variable Use Class Name with dot(.) 
		//sub(c,a);
		return c + sub(c,a);
	}
	
	public static int sub(int a, int b) {
		return a-b;
	}
}
