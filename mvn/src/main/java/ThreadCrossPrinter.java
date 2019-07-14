import tools.SleepUnit;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;

public class ThreadCrossPrinter {
    static int count = 0;  // 静态内部内要调用的变量也应该是静态的
    static Object lock = new Object();
    private static boolean over = false;

    static AtomicInteger atomicCount = new AtomicInteger(0);
    static AtomicBoolean atomicOver = new AtomicBoolean(false);

    public static void main(String[] args) {
        char[] s1 = "abcefdfasdfasdfasdfsa".toCharArray();
        char[] s2 = "123456789fdasddfdasdfasdfasdfas".toCharArray();

//        Thread printabc = new Thread(new AtomicPrinter(s1), s1.toString());
//        Thread print123 = new Thread(new AtomicPrinter(s2), s2.toString());

        Thread printabc = new Thread(new Printer(s1), "print chars");
        printabc.start();
//
        Thread print123 = new Thread(new Printer(s2), "print nums");
        print123.start();
    }

    static class Printer implements Runnable {
        private char[] s;
        Printer(char[] s) {
        this.s = s;
        }
        public void run() {
            while (true){
                synchronized (lock) { // java任何一个对象都可以是一个锁，有notify、wait等方法
                    int tmp = count/2;
                    try{
                        System.out.println(s[tmp]);
                        SleepUnit.SECOND.sleep(2);
                        if (over)
                            count += 2;
                        else
                            count++;
                        lock.notify();
                        if (tmp == (s.length - 1)){
                            over = true;
                            break;
                        }
                        if(!over)
                            lock.wait(); // wait需要捕获InterruptedException异常
                    } catch (InterruptedException e){

                    }
                }
            }
        }
    }

    static class AtomicPrinter implements Runnable{
        int index = 0; // 记录打印位置
        int lastCount = -1; // 记录atomicCount在该线程上一次的值
        char[] s;

        AtomicPrinter(char[] s){
            this.s = s;
        }

        public void run() {
            while (true){
                if(index == s.length){
                    atomicOver.set(true);
                    break;
                }
                if (!atomicOver.get()){  // 循环等待实现通信机制
                    while (lastCount == atomicCount.get()){
                        try {
                            TimeUnit.MILLISECONDS.sleep(10);
                        }catch (Exception e){

                        }
                    }
                }

                System.out.println(s[index]);
                lastCount = atomicCount.incrementAndGet();
                index ++;

            }
        }
    }
}