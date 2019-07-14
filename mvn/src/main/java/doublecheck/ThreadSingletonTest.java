package doublecheck;

import tools.SleepUnit;

import java.util.Random;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


public class ThreadSingletonTest implements Runnable {
    private static CountDownLatch c = new CountDownLatch(1000);

    @Override
    public void run() {
        Random random = new Random();
        UnsafeSingleton intance = UnsafeSingleton.getInstance();
        SleepUnit.SECOND.sleep(random.nextInt(10));
        String tmp = intance.nums;
        System.out.println(String.format("print run %s", Thread.currentThread().getName()));
        c.countDown();
    }

    public static void main(String[] args) throws Exception{
        ExecutorService pool = Executors.newFixedThreadPool(1000);
        long current = System.currentTimeMillis();
        for (int i = 0; i < 1000; i++) {
            pool.execute(new ThreadSingletonTest());
        }
        c.await();
        System.out.println(System.currentTimeMillis() - current);
        pool.shutdown();
    }
}
