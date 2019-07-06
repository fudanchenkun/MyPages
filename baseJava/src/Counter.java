import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Counter {
    private AtomicInteger atomicI = new AtomicInteger();
    private int i = 0;

    private void safeCount(){
        for (;;){
            int i = atomicI.get();
            boolean suc = atomicI.compareAndSet(i, ++i);
            if (suc)
                break;
        }
    }

    private void count(){
        i++;
    }


    public static void main(String[] args) {
        final Counter cas = new Counter();
        List<Thread> ts = new ArrayList<>(600);
        long start = System.currentTimeMillis();

        for (int x = 0; x < 100; x++) {
            Thread t = new Thread(new Runnable() {
                @Override
                public void run() {
                    for (int j = 0; j < 10000; j++) {
                        cas.count();
                        cas.safeCount();
                    }
                }
            });
            ts.add(t);
        }

        for(Thread t: ts)
            t.start();

        for (Thread t: ts){
            try{
                t.join();
            } catch (InterruptedException e){
                e.printStackTrace();
            }
        }

        System.out.println(cas.i);
        System.out.println(cas.atomicI.get());
        System.out.println(System.currentTimeMillis() - start);


    }
}
