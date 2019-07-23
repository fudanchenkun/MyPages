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
    }
}
