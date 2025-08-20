package time_complexity_prob;
import java.util.*;
public class cursor {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while (n>0) {
            int cursor = 1;
            int move = 4;
            int x = sc.nextInt();
            for (int i=1000; i>=1;i*=0.1){
                int y=x/i;
                if (y==0){y=10;}
                x=x%i;
                int z=cursor-y;
                if (z<0){z=-z;}
                move+=z;
                cursor=y;
            }
            System.out.println(move);
            n--;
        }
        sc.close();
    }
}
