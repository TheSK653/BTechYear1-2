	package String;

public class String_Builder_Demo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StringBuilder sb = new StringBuilder();
		System.out.println(sb.capacity());
		sb.append("jhkfss");
		sb.append(true);
		sb.append(7);
		sb.append('s');
		System.out.println(sb);
		System.out.println(sb.length());
		System.out.println(sb.charAt(2));
		System.out.println(sb.reverse());
		System.out.println(sb.delete(0, 4));
		String s = sb.toString();
		String str = "kjbvddklfvnklndfvk";
		sb.append(str);
	}

}
