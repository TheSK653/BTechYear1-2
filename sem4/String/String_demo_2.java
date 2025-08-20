package String;

public class String_demo_2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//string + string = string
		//string + integer = string
		//integer + integer = integer 
		String s1 = "hello"+10+20+"world";
		String s2 = "hello"+(10+20)+"world";
		String s3 = 10+20+"hello"+"world";
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(s3);
	}

}
