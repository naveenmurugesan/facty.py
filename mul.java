import java.io.*;
import java.utill.*;
public class multiple
{
public static void main(String args[])
{
int i,n,m;
Scanner s=new Scanner(System.in);
n=s.nextInt();
for(i=1;i<=5;i++)
{
m=i*n;
System.out.println(n+"*"+i+"="+m);
}
}
}
