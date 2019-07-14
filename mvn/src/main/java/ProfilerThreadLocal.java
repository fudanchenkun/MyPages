import tools.SleepUnit;

//
public class ProfilerThreadLocal {
    private static final ThreadLocal<Long> TIME_THREADLOCAL = new ThreadLocal<Long>(){
        protected Long initialValue(){
            return System.currentTimeMillis();
        }
    };

    public static final void begin(){
        TIME_THREADLOCAL.set(System.currentTimeMillis());
    }

    public static final Long end(){
        return System.currentTimeMillis() - TIME_THREADLOCAL.get();
    }

    public static void main(String[] args) {
        ProfilerThreadLocal.begin();
        SleepUnit.SECOND.sleep(2);
        System.out.println(ProfilerThreadLocal.end());
    }

}
