import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String b="";
		for (int i = 0; i <a.length() ; i++) {
			char ca=a.charAt(i);
			if(ca>=97){
				b+=Character.toUpperCase(ca);
			}
			else{
				b+=Character.toLowerCase(ca);
			}
		}
		System.out.println(b);
    }
}