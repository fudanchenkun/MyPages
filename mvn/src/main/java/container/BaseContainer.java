package container;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class BaseContainer<T> {
    private Map<String, T> map = new HashMap<>();
    private Set<T> set = new TreeSet<>();
    private String string = new String();
    private StringBuffer stringBuffer = new StringBuffer();
    private StringBuilder stringBuilder = new StringBuilder();


    public static void main(String[] args) {
        Integer i1 = Integer.valueOf(10);
        Integer i2= Integer.valueOf(10);
        System.out.println(i1==i2);
        System.out.println(i1.equals(i2));

        Integer i3 = new Integer(10);
        Integer i4= new Integer(10);
        System.out.println(i3==i4);
        System.out.println(i3.equals(i4));


        String num = "jiada";
        num.length();
        System.out.println(num.length());

        char c = '1';
        int n = 1;
        char copy = (char)n;

        char[] ca = new char[]{'1', '2', '3'};

        System.out.println(String.valueOf(ca));
        System.out.println((char)48);


        Map<String, Integer> map = new HashMap<>(){
            {
                put("I", 1);
                put("IV", 3);
                put("IX", 8);
                put("V", 5);
                put("X", 10);
                put("XL", 30);
                put("XC", 80);
                put("L", 50);
                put("C", 100);
                put("CD", 300);
                put("CM", 800);
                put("D", 500);
                put("M", 1000);
            }
        };
        System.out.println(Integer.MAX_VALUE);
        int[] t = new int[]{1,2,3};


    }
}
