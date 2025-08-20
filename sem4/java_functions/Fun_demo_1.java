//public: Access Modifiers for JVM (Java Virtual Machine)
//main:   method name
//void:   This method has no return value
//static: 
//Methods are used to perform certain actions
//parameters: they are specified after the method name in parenthesis() 

package java_functions;
 
public class Fun_demo_1{
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello");
		int a=8;
		int b=7;
		Add(a,b);
		System.out.println("Bye");		
	}
	public static void Add(int a, int b) {
		int c = a+b;
		sub(c,a);
		System.out.println(c);
	}
	
	public static void sub(int a, int b) {
		int c=a-b;
		System.out.println(c);
	}

	
	

}
