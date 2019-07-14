package doublecheck;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class UnsafeSingleton{
    private static UnsafeSingleton instance;
    private Map<String, Long> map;
    final String nums = "num";

    UnsafeSingleton(){
        map = new HashMap<>();
        for (long i = 0; i < 10000000; i++) {
            map.put(String.format("num %s", i), i);
        }
        System.out.println("init finished!");
    }

    public static synchronized UnsafeSingleton getInstance(){
//        if(instance == null){
//            synchronized (UnsafeSingleton.class){
                if(instance == null)
                    instance = new UnsafeSingleton();
//            }
//        }

        return instance;
    }

}
