import java.util.HashMap;
import java.util.concurrent.ConcurrentHashMap;

public class Join {


    public static void main(String[] args) {
        Thread previous = Thread.currentThread();
        for (int i = 0; i < 10; i++) {
            Thread thread = new Thread(new Domino(previous), String.valueOf(i+1));
            thread.start();
            previous = thread;
        }
    }


    static class Domino implements Runnable{
        private Thread previous;
        Domino(Thread previous){
            this.previous = previous;
        }

        public void run() {
            try {
                previous.join();
            } catch (InterruptedException e){

            }

            System.out.println(Thread.currentThread().getName() + " terminate.");
        }
    }

}
