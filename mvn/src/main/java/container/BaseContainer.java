package container;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class BaseContainer<T> {
    private Map<String, T> map = new HashMap<>();
    private Set<T> set = new TreeSet<>();

}
