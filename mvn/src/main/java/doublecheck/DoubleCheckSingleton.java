package doublecheck;

public class DoubleCheckSingleton {
    private volatile static DoubleCheckSingleton instance; // 一定要是volatile的 否则jvm重排序引起问题

    public static DoubleCheckSingleton getInstance(){
        if(instance == null){
            synchronized (DoubleCheckSingleton.class) {
                if(instance == null) {
                    instance = new DoubleCheckSingleton();
                }
            }
        }
        return instance;
    }
}
