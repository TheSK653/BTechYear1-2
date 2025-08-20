package java_Stack_Basic;
import java.util.Stack;
public class stack_add_last {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<Integer> st = new Stack<>();
		st.push(3);//add
		st.push(1);//add
		st.push(5);//add
		st.push(6);//add
		st.push(2);//add
		System.out.println(st.peek());
		System.out.println(st);
		Add_Last(st,6);
		System.out.println(st);
	}

	public static void Add_Last(Stack<Integer> st, int item) {
		// TODO Auto-generated method stub
		if(st.isEmpty()) {
			st.push(item);
			return;
		}
		int x=st.pop();
		Add_Last(st, item);
		st.push(x);
		
	}

}
